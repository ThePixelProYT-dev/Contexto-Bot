#!/bin/bash
echo "=== Kontexto Bot Uninstaller (Linux/macOS) ==="

# Prüfen ob python3 verfügbar
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed!"
    exit 1
fi

# Deinstalliere alle Pakete aus packages.txt
while read -r pkg; do
    if [[ "$pkg" != "" && "$pkg" != \#* ]]; then
        pip3 uninstall -y "$pkg"
    fi
done < packages.txt

echo "Done. All packages from packages.txt have been uninstalled."
