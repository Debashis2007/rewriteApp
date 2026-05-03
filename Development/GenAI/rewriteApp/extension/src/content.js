// Content script injected on all pages
// This allows users to right-click and rewrite selected text

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'getSelectedText') {
    sendResponse({ text: window.getSelection().toString() });
  }
});

// Create context menu when extension loads
chrome.runtime.sendMessage({ action: 'createContextMenu' });
