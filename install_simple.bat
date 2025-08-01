@echo off
echo === Kontexto Bot Installer (Windows, global pip) ===

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed!
    pause
    exit /b
)

pip install --user --upgrade pip
pip install --user -r packages.txt

echo Starting contexto_bot.py...
python contexto_bot.py
pause
