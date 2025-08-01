#!/bin/bash
echo "=== Kontexto Bot Installer (Linux/macOS, with venv) ==="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed!"
    exit 1
fi

# venv erstellen
python3 -m venv venv
source venv/bin/activate

# pip & Pakete
pip install --upgrade pip
pip install -r packages.txt

# Start
echo "Starting contexto_bot.py..."
python contexto_bot.py
