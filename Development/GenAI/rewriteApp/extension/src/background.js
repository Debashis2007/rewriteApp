// Service Worker for handling background tasks
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'rewrite') {
    // Handle rewrite request from content script
    handleRewrite(request.text, request.tone, request.action).then(sendResponse);
    return true; // Will respond asynchronously
  }
});

async function handleRewrite(text, tone, action) {
  try {
    const response = await fetch('http://localhost:8000/rewrite', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text,
        tone,
        action,
      }),
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    return { error: error.message };
  }
}
