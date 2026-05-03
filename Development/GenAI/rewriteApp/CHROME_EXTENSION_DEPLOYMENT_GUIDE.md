# Chrome Extension Deployment Guide

This guide explains how to:

1. Install the extension locally in Chrome (developer mode)
2. Point it to the Railway app URL
3. Package it as a ZIP
4. Publish it to the Chrome Web Store

---

## 1) Prerequisites

- Chrome browser
- Project cloned locally
- Railway app deployed at:
  - `https://rewriteapp-production.up.railway.app`

---

## 2) Configure API URL (Production)

Open:

- `extension/src/popup.js`

Make sure the value is:

```javascript
const API_BASE_URL = 'https://rewriteapp-production.up.railway.app';
```

---

## 3) Install Locally in Chrome (Load Unpacked)

1. Open Chrome and go to:
   - `chrome://extensions`
2. Enable **Developer mode** (top-right)
3. Click **Load unpacked**
4. Select folder:
   - `rewriteApp/extension`
5. Pin the extension from the puzzle icon (optional)

If you change code, click **Reload** on the extension card.

---

## 4) Create ZIP Package for Store Upload

From project root (`rewriteApp`):

```bash
rm -f extension-chrome.zip
zip -r extension-chrome.zip extension/ -x "*.DS_Store"
```

Output file:

- `extension-chrome.zip`

---

## 5) Publish to Chrome Web Store

1. Open Developer Dashboard:
   - `https://chrome.google.com/webstore/devconsole`
2. Click **Add new item**
3. Upload:
   - `extension-chrome.zip`
4. Fill listing details:
   - Name
   - Short description
   - Full description
   - Screenshots
   - Category
5. Complete compliance forms:
   - Single purpose
   - Permissions justification
   - Host permissions justification
   - Privacy policy URL (required if data is sent to backend)
6. Choose visibility:
   - Public / Unlisted / Private
7. Submit for review

---

## 6) Permissions Used

Current permissions in `extension/manifest.json`:

- `activeTab`
- `scripting`
- `storage`

Host permissions:

- `http://localhost:8000/*` (local development)
- `https://*.railway.app/*` (production)

---

## 7) Update Workflow (After First Publish)

For each update:

1. Increase `version` in `extension/manifest.json`
2. Recreate ZIP package
3. Upload new ZIP in Developer Dashboard
4. Submit updated version

---

## 8) Troubleshooting

### A) "Manifest file is missing or unreadable"
- Confirm `extension/manifest.json` exists
- Ensure JSON is valid and `manifest_version` is `3`

### B) API requests fail from extension
- Verify Railway URL in `extension/src/popup.js`
- Confirm Railway endpoint is up:
  - `https://rewriteapp-production.up.railway.app/health`

### C) CORS or permission issues
- Ensure backend CORS allows extension origin/requests
- Ensure `host_permissions` includes the target API domain

---

## 9) Useful Links

- Railway app: `https://rewriteapp-production.up.railway.app`
- Health endpoint: `https://rewriteapp-production.up.railway.app/health`
- API docs: `https://rewriteapp-production.up.railway.app/docs`
- Chrome Extension dashboard: `https://chrome.google.com/webstore/devconsole`
