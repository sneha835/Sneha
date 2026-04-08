@echo off
call .venv\Scripts\activate.bat
set /p PRODUCT="Enter product name: "
python scripts\dpap_research.py --product "%PRODUCT%" --output report
pause
