#!/bin/bash
echo "=== Kontexto Bot Installer (Linux/macOS, global pip) ==="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed!"
    exit 1
fi

# Pip direkt (lokal)
pip3 install --user --upgrade pip
pip3 install --user -r packages.txt

# Start
echo "Starting contexto_bot.py..."
python3 contexto_bot.py
