#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "==> Creating Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "==> Installing Python dependencies..."
pip install -r requirements.txt

echo "==> Installing Playwright Chromium browser (needed for NotebookLM auth)..."
if ! playwright install chromium; then
  echo ""
  echo "WARNING: Playwright Chromium download failed (may be blocked in this environment)."
  echo "Please run 'playwright install chromium' manually on your local machine."
fi

echo ""
echo "============================================="
echo "  Setup complete!"
echo "============================================="
echo ""
echo "NEXT STEP: Authenticate with NotebookLM."
echo "Open a separate terminal and run:"
echo ""
echo "  cd $SCRIPT_DIR && source .venv/bin/activate && notebooklm login"
echo ""
echo "This will open a browser window for Google OAuth."
echo "============================================="
