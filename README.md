# 🧠 Kontexto Bot (Auto-Typing Tool)

A cross-platform Python tool that automatically types and submits words on [contexto.me](https://contexto.me). It supports a GUI, multiple modes, word skipping, and automatic language detection.



## 📦 Requirements

- Python 3.8 or higher
- Internet connection (for online wordlist)
- `tkinter` (GUI support – usually included with Python)



## 🔧 Installation

Choose **one of two installation methods** depending on your system:

### 🪟 Windows

#### Option 1: With virtual environment (recommended)

1. Double-click `install_venv.bat`  
2. It will:
   - Create a virtual environment
   - Install dependencies from `packages.txt`
   - Launch `contexto_bot.py`

#### Option 2: Without virtual environment (simpler)

1. Double-click `install_simple.bat`  
2. It installs the packages globally (with `--user`) and launches the bot directly



### 🐧 Linux / macOS

#### Option 1: With virtual environment (recommended)

```bash
chmod +x install_venv.sh
./install_venv.sh
````

#### Option 2: Without virtual environment (simpler)

```bash
chmod +x install_simple.sh
./install_simple.sh
```

> 💡 If you get errors related to `tkinter`, run:

```bash
sudo apt install python3-tk
```



## 📁 Files

| File                 | Description                                    |
| -- | - |
| `contexto_bot.py`    | Main Python script with GUI                    |
| `packages.txt`       | List of required Python packages               |
| `install_venv.bat`   | Windows installer with virtual environment     |
| `install_simple.bat` | Windows installer without venv                 |
| `install_venv.sh`    | Linux/macOS installer with virtual environment |
| `install_simple.sh`  | Linux/macOS installer without venv             |



## 🖥️ Features

* Automatic word typing and submission
* Mode toggle: `Standard` / `Better Tip`
* Better Tip = List of common categories from: [puzzlesbay.com/contexto-words](https://puzzlesbay.com/contexto-words/)
* Optional skipping of predefined start words
* Automatic GUI language detection (English/German)
* Clean interface with Start / Stop / Mode switch / Status label



## ⌨️ Controls

* `▶️ Start`: Begin word typing
* `⏹️ Stop`: Immediately stop typing
* `Mode`: Toggle between `Standard` and `Better Tip`
* `Skip Start Words`: If you've already entered them manually



## 🌐 Word Sources

* **START\_WORDS**: Fixed category-based English words (e.g. "Object", "Animal")
* **ONLINE LIST**: 20,000+ real English words fetched from GitHub



# 🇩🇪 Kontexto Bot (Auto-Tipp-Tool)

Ein plattformübergreifendes Python-Tool, das automatisch Wörter auf [contexto.me](https://contexto.me) eingibt und abschickt. Es bietet eine grafische Oberfläche, zwei Modi, Startwort-Überspringung und automatische Sprachumschaltung (Deutsch/Englisch).



## 📦 Voraussetzungen

* Python 3.8 oder höher
* Internetverbindung (für die Online-Wortliste)
* `tkinter` (meist bereits in Python enthalten)



## 🔧 Installation

Wähle **eine der zwei Installationsmethoden** je nach System:

### 🪟 Windows

#### Option 1: Mit virtueller Umgebung (empfohlen)

1. Doppelklick auf `install_venv.bat`
2. Das Skript:

   * erstellt ein virtuelles Environment
   * installiert alle Abhängigkeiten aus `packages.txt`
   * startet `contexto_bot.py`

#### Option 2: Ohne virtuelle Umgebung (einfacher)

1. Doppelklick auf `install_simple.bat`
2. Das Skript installiert die Pakete global (mit `--user`) und startet direkt den Bot



### 🐧 Linux / macOS

#### Option 1: Mit virtueller Umgebung (empfohlen)

```bash
chmod +x install_venv.sh
./install_venv.sh
```

#### Option 2: Ohne virtuelle Umgebung (einfacher)

```bash
chmod +x install_simple.sh
./install_simple.sh
```

> 💡 Falls `tkinter`-Fehler auftreten:

```bash
sudo apt install python3-tk
```



## 📁 Dateien

| Datei                | Beschreibung                                  |
| -- |  |
| `contexto_bot.py`    | Hauptskript mit GUI                           |
| `packages.txt`       | pip-Abhängigkeiten                            |
| `install_venv.bat`   | Windows-Installer mit virtueller Umgebung     |
| `install_simple.bat` | Windows-Installer ohne virtuelle Umgebung     |
| `install_venv.sh`    | Linux/macOS-Installer mit virtueller Umgebung |
| `install_simple.sh`  | Linux/macOS-Installer ohne virtuelle Umgebung |



## 🖥️ Funktionen

* Automatisches Eingeben und Absenden von Wörtern
* Umschaltbarer Modus: `Standard` / `Better Tip`
* Better Tip = Liste von häufigen Kategorien: [puzzlesbay.com/contexto-words](https://puzzlesbay.com/contexto-words/)
* Optionales Überspringen der Startwörter
* Sprache der GUI wird automatisch erkannt
* Übersichtliche Oberfläche mit Steuerung und Statusanzeige



## ⌨️ Steuerung

* `▶️ Start`: Startet die automatische Eingabe
* `⏹️ Stop`: Stoppt den Prozess sofort
* `Modus`: Wechselt zwischen `Standard` und `Better Tip`
* `Startwörter überspringen`: Falls du sie schon manuell eingegeben hast



## 🌐 Wortquellen

* **START\_WORDS**: Feste Kategorien (z. B. „Object“, „Animal“)
* **ONLINE LIST**: 20.000+ echte englische Wörter von GitHub (automatisch geladen)