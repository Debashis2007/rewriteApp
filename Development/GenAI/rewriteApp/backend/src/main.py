"""FastAPI application for text rewriting."""

import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import logging

from src.config import settings
from src.rewriter import TextRewriter, Tone, RewriteAction, get_rewriter


# Configure logging
logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Rewrite Professional API",
    description="Text rewriting service with tone control",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models
class RewriteRequest(BaseModel):
    """Request model for text rewriting."""
    text: str
    tone: Tone = Tone.FORMAL
    action: RewriteAction = RewriteAction.REWRITE
    context: Optional[str] = None


class RewriteResponse(BaseModel):
    """Response model for text rewriting."""
    original: str
    rewritten: str
    tone: Tone
    action: RewriteAction
    analysis: dict


class AnalysisResponse(BaseModel):
    """Response model for text analysis."""
    word_count: int
    char_count: int
    sentence_count: int
    avg_word_length: float
    tone_detected: str


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "rewrite-professional-api"}


@app.post("/rewrite", response_model=RewriteResponse)
async def rewrite_text(request: RewriteRequest):
    """
    Rewrite text with specified tone and action.

    - **text**: Text to rewrite (required)
    - **tone**: formal, friendly, or assertive (default: formal)
    - **action**: rewrite, shorten, or strengthen (default: rewrite)
    - **context**: Optional context for rewriting
    """
    try:
        if not request.text or not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        if len(request.text) > 5000:
            raise HTTPException(status_code=400, detail="Text exceeds maximum length of 5000 characters")

        rewriter = get_rewriter()

        # Perform rewriting
        rewritten = await rewriter.rewrite(
            text=request.text,
            tone=request.tone,
            action=request.action,
            context=request.context,
        )

        # Analyze both original and rewritten
        analysis = await rewriter.analyze(request.text)

        logger.info(f"Successfully rewrote text with tone={request.tone}, action={request.action}")

        return RewriteResponse(
            original=request.text,
            rewritten=rewritten,
            tone=request.tone,
            action=request.action,
            analysis=analysis,
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error rewriting text: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(request: RewriteRequest):
    """
    Analyze text and provide metrics.

    Returns:
    - Word count
    - Character count
    - Sentence count
    - Average word length
    - Detected tone
    """
    try:
        if not request.text or not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        rewriter = get_rewriter()
        analysis = await rewriter.analyze(request.text)

        logger.info("Successfully analyzed text")

        return AnalysisResponse(**analysis)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error analyzing text: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@app.get("/tones")
async def get_tones():
    """Get available tone options."""
    return {"tones": [tone.value for tone in Tone]}


@app.get("/actions")
async def get_actions():
    """Get available action options."""
    return {"actions": [action.value for action in RewriteAction]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))


# Serve React frontend (must be last — after all API routes)
FRONTEND_DIST = Path(__file__).parent.parent.parent / "frontend" / "dist"
if FRONTEND_DIST.exists():
    app.mount("/assets", StaticFiles(directory=str(FRONTEND_DIST / "assets")), name="assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa(full_path: str):
        index = FRONTEND_DIST / "index.html"
        return FileResponse(str(index))
