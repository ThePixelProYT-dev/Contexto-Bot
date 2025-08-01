@echo off
echo === Kontexto Bot Installer (Windows, with venv) ===

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed!
    pause
    exit /b
)

REM venv anlegen & aktivieren
python -m venv venv
call venv\Scripts\activate

pip install --upgrade pip
pip install -r packages.txt

echo Starting contexto_bot.py...
python contexto_bot.py
pause
