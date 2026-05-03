// Configuration
const API_BASE_URL = 'http://localhost:8000'; // Change in production

// Get DOM elements
const inputText = document.getElementById('inputText');
const tone = document.getElementById('tone');
const action = document.getElementById('action');
const rewriteBtn = document.getElementById('rewriteBtn');
const clearBtn = document.getElementById('clearBtn');
const copyBtn = document.getElementById('copyBtn');
const output = document.getElementById('output');
const outputText = document.getElementById('outputText');
const loading = document.getElementById('loading');
const message = document.getElementById('message');

// Load saved values
chrome.storage.local.get(['tone', 'action'], (result) => {
  if (result.tone) tone.value = result.tone;
  if (result.action) action.value = result.action;
});

// Save preferences
tone.addEventListener('change', () => {
  chrome.storage.local.set({ tone: tone.value });
});

action.addEventListener('change', () => {
  chrome.storage.local.set({ action: action.value });
});

// Rewrite handler
rewriteBtn.addEventListener('click', async () => {
  const text = inputText.value.trim();

  if (!text) {
    showMessage('Please enter text to rewrite', 'error');
    return;
  }

  if (text.length > 5000) {
    showMessage('Text exceeds 5000 characters', 'error');
    return;
  }

  loading.style.display = 'block';
  output.style.display = 'none';
  message.innerHTML = '';

  try {
    const response = await fetch(`${API_BASE_URL}/rewrite`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text,
        tone: tone.value,
        action: action.value,
      }),
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    const data = await response.json();
    outputText.textContent = data.rewritten;
    output.style.display = 'block';
    showMessage('Text rewritten successfully!', 'success');
  } catch (error) {
    showMessage(`Error: ${error.message}`, 'error');
  } finally {
    loading.style.display = 'none';
  }
});

// Copy handler
copyBtn.addEventListener('click', () => {
  navigator.clipboard.writeText(outputText.textContent);
  showMessage('Copied to clipboard!', 'success');
});

// Clear handler
clearBtn.addEventListener('click', () => {
  inputText.value = '';
  outputText.textContent = '';
  output.style.display = 'none';
  message.innerHTML = '';
});

// Helper function to show messages
function showMessage(text, type) {
  message.textContent = text;
  message.className = type;
  setTimeout(() => {
    message.innerHTML = '';
  }, 3000);
}
