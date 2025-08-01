@echo off
echo === Kontexto Bot Uninstaller (Windows) ===

REM Prüfe Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed!
    pause
    exit /b
)

REM Deinstalliere alle Pakete aus packages.txt
for /f %%p in (packages.txt) do (
    pip uninstall -y %%p
)

echo Done. All packages from packages.txt have been uninstalled.
pause
