# Chrome Extension - Rewrite Professional

## Installation

### Development Mode
1. Open `chrome://extensions/`
2. Enable "Developer mode" (top right)
3. Click "Load unpacked"
4. Select the `extension/` directory

### Production Release
- Upload to [Chrome Web Store](https://chrome.google.com/webstore)

## Features

- **Popup Interface**: Click extension icon to open rewriting panel
- **Tone Control**: Choose formal, friendly, or assertive tone
- **Actions**: Rewrite, shorten, or strengthen text
- **Clipboard Integration**: Copy rewritten text with one click
- **Settings Storage**: Preferences saved locally

## Configuration

Edit `src/popup.js` to change API endpoint:

```javascript
const API_BASE_URL = 'http://localhost:8000'; // Change this for production
```

## API Requirements

Ensure backend is running at the configured URL:

```bash
python -m uvicorn src.main:app --reload
```
