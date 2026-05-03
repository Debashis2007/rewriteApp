"""Text rewriting engine with LLM integration."""

from enum import Enum
from typing import Optional
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

from src.config import settings


class Tone(str, Enum):
    """Tone options for rewriting."""
    FORMAL = "formal"
    FRIENDLY = "friendly"
    ASSERTIVE = "assertive"


class RewriteAction(str, Enum):
    """Action to perform on text."""
    REWRITE = "rewrite"
    SHORTEN = "shorten"
    STRENGTHEN = "strengthen"


class TextRewriter:
    """Handles text rewriting using LLM."""

    def __init__(self):
        self.llm_provider = settings.llm_provider
        self.llm_client = None

    async def _get_llm_client(self):
        """Lazy initialize LLM client."""
        if self.llm_client is None:
            if self.llm_provider == "openai":
                try:
                    from openai import AsyncOpenAI
                    self.llm_client = AsyncOpenAI(api_key=settings.openai_api_key)
                except ImportError:
                    raise ImportError("openai package required: pip install openai")
            elif self.llm_provider == "anthropic":
                try:
                    from anthropic import AsyncAnthropic
                    self.llm_client = AsyncAnthropic(api_key=settings.anthropic_api_key)
                except ImportError:
                    raise ImportError("anthropic package required: pip install anthropic")
            elif self.llm_provider == "ollama":
                try:
                    import aiohttp
                    self.llm_client = aiohttp.ClientSession()
                except ImportError:
                    raise ImportError("aiohttp package required: pip install aiohttp")
            else:
                raise ValueError(f"Unknown LLM provider: {self.llm_provider}")
        return self.llm_client

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def rewrite(
        self,
        text: str,
        tone: Tone = Tone.FORMAL,
        action: RewriteAction = RewriteAction.REWRITE,
        context: Optional[str] = None,
    ) -> str:
        """Rewrite text with specified tone and action."""
        client = await self._get_llm_client()

        # Build prompt based on action and tone
        action_guidance = {
            RewriteAction.REWRITE: f"Rewrite the following text in a {tone} tone.",
            RewriteAction.SHORTEN: f"Shorten the following text while keeping the meaning. Use a {tone} tone.",
            RewriteAction.STRENGTHEN: f"Make the following text more impactful and persuasive. Use a {tone} tone.",
        }

        prompt = action_guidance.get(action, f"Rewrite the following text in a {tone} tone.")

        if context:
            prompt += f"\n\nContext: {context}"

        prompt += f"\n\nOriginal text:\n{text}\n\nRewritten text:"

        try:
            if self.llm_provider == "openai":
                response = await client.chat.completions.create(
                    model=settings.openai_model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=2000,
                )
                return response.choices[0].message.content.strip()

            elif self.llm_provider == "anthropic":
                response = await client.messages.create(
                    model=settings.anthropic_model,
                    max_tokens=2000,
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.content[0].text.strip()

            elif self.llm_provider == "ollama":
                async with client.post(
                    f"{settings.ollama_base_url}/api/generate",
                    json={
                        "model": settings.ollama_model,
                        "prompt": prompt,
                        "stream": False,
                        "temperature": 0.7,
                    },
                ) as response:
                    data = await response.json()
                    result = data.get("response", "").strip()
                    if result:
                        return result

            raise ValueError(f"Unknown provider: {self.llm_provider}")
        except Exception:
            return self._fallback_rewrite(text=text, tone=tone, action=action)

    def _fallback_rewrite(self, text: str, tone: Tone, action: RewriteAction) -> str:
        """Fallback rewrite logic when external LLM is unavailable."""
        cleaned = " ".join(text.split())

        if action == RewriteAction.SHORTEN:
            words = cleaned.split()
            cleaned = " ".join(words[: max(8, len(words) // 2)])

        if action == RewriteAction.STRENGTHEN:
            if not cleaned.endswith("!"):
                cleaned = f"{cleaned}!"

        if tone == Tone.FORMAL:
            return f"{cleaned} Please let me know if you need any additional clarification."
        if tone == Tone.FRIENDLY:
            return f"{cleaned} Happy to help!"
        if tone == Tone.ASSERTIVE:
            return f"{cleaned} This should be acted on promptly."

        return cleaned

    async def analyze(self, text: str) -> dict:
        """Analyze text and provide metrics."""
        words = len(text.split())
        chars = len(text)
        sentences = text.count(".") + text.count("!") + text.count("?")
        avg_word_length = chars / words if words > 0 else 0

        return {
            "word_count": words,
            "char_count": chars,
            "sentence_count": max(sentences, 1),
            "avg_word_length": round(avg_word_length, 2),
            "tone_detected": self._detect_tone(text),
        }

    def _detect_tone(self, text: str) -> str:
        """Simple heuristic tone detection."""
        formal_words = ["hereby", "furthermore", "consequently", "therefore"]
        friendly_words = ["hey", "thanks", "cheers", "cool", "awesome"]
        assertive_words = ["must", "definitely", "absolutely", "certainly", "strongly"]

        text_lower = text.lower()
        formal_count = sum(1 for word in formal_words if word in text_lower)
        friendly_count = sum(1 for word in friendly_words if word in text_lower)
        assertive_count = sum(1 for word in assertive_words if word in text_lower)

        if formal_count > friendly_count and formal_count > assertive_count:
            return "formal"
        elif friendly_count > assertive_count:
            return "friendly"
        elif assertive_count > 0:
            return "assertive"
        return "neutral"


# Global rewriter instance
_rewriter_instance = None


def get_rewriter() -> TextRewriter:
    """Get or create rewriter instance."""
    global _rewriter_instance
    if _rewriter_instance is None:
        _rewriter_instance = TextRewriter()
    return _rewriter_instance
