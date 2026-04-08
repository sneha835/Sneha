@echo off
echo =============================================
echo   BabyOrgano Research System - Windows Setup
echo =============================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Download from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during install.
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
python -m venv .venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment.
    pause
    exit /b 1
)

echo [2/4] Activating virtual environment...
call .venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
pip install yt-dlp pytrends requests beautifulsoup4 praw lxml
if errorlevel 1 (
    echo WARNING: Some packages may have failed. Continuing...
)

echo [4/4] Verifying installation...
python -c "import yt_dlp; import pytrends; import requests; import bs4; print('All packages OK')"
if errorlevel 1 (
    echo WARNING: Some packages missing. Try running: pip install yt-dlp pytrends requests beautifulsoup4 praw lxml
)

echo.
echo =============================================
echo   Setup complete!
echo =============================================
echo.
echo To run a report, open Command Prompt and type:
echo.
echo   cd %CD%
echo   .venv\Scripts\activate
echo   python scripts\dpap_research.py --product "YOUR PRODUCT" --output report
echo.
echo Or for quick access, just double-click run_report.bat
echo =============================================
pause
