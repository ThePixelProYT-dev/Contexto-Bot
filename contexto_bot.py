import tkinter as tk
import pyautogui
import time
import threading
import requests
import random
import locale

# === Sprache (autoerkennung) ===
lang_code = locale.getdefaultlocale()[0]
lang = "de" if lang_code and lang_code.startswith("de") else "en"

# === Übersetzungen ===
T = {
    "de": {
        "title": "Kontexto Bot",
        "start": "▶️ Start",
        "stop": "⏹️ Stop",
        "mode": "Modus",
        "standard": "Standard",
        "better_tip": "Better Tip",
        "status_ready": "Bereit",
        "status_running": "Läuft...",
        "status_stopped": "Gestoppt",
        "status_done": "Fertig",
        "skip_startwords": "Startwörter überspringen",
        "skip_startwords_on": "✔️ Startwörter überspringen"
    },
    "en": {
        "title": "Kontexto Bot",
        "start": "▶️ Start",
        "stop": "⏹️ Stop",
        "mode": "Mode",
        "standard": "Standard",
        "better_tip": "Better Tip",
        "status_ready": "Ready",
        "status_running": "Running...",
        "status_stopped": "Stopped",
        "status_done": "Done",
        "skip_startwords": "Skip Start Words",
        "skip_startwords_on": "✔️ Skip Start Words"
    }
}[lang]

# === Konfiguration ===
START_WORDS = [
    "Object", "Animal", "Event", "Emotion", "Activity", "Material", "Food", "Technology"
]

PUZZLESBAY_WORDS = [
    "Place", "Feeling", "Device", "Thing", "Idea", "Country", "Plant", "Profession", "City", "Clothing",
    "Instrument", "Furniture", "Occupation", "Vehicle", "Tool", "Natural", "Structure", "Liquid",
    "Body", "Part", "Color", "Shape", "Building", "Container", "Element", "Energy", "Entertainment",
    "Language", "Metal", "Mineral", "Planet", "Star", "Stone", "Substance", "Toy", "Weapon", "Weather",
    "Weaponry", "Reptile", "Bird", "Mammal", "Fish", "Bug", "Insect", "Fruit", "Vegetable", "Meat",
    "Beverage", "Dairy", "Condiment", "Grain", "Nutrient", "Gadget", "Appliance", "Machine", "Electronic",
    "Cloth", "Fabric", "Accessory", "Jewelry", "Cosmetic", "Sport", "Game", "Hobby", "Utensil",
    "Currency", "Symbol", "Sign", "Gesture", "Sound", "Light", "Vibration", "Scent", "Flavor",
    "Sensation", "Action", "Movement", "Act", "Dance", "Performance", "Show", "Festival", "Holiday",
    "Celebration", "Ceremony", "Tradition", "Custom", "Religion", "Myth", "Legend", "Story", "Tale",
    "Fable", "Novel", "Book", "Movie", "Film", "Song", "Music", "Tune", "Melody", "Rhythm"
]

WORD_DELAY = 1.0
START_DELAY = 0.5
running = False
use_better_tip = False
skip_startwords = False

def load_words_online():
    url = "https://gist.githubusercontent.com/eyturner/3d56f6a194f411af9f29df4c9d4a4e6e/raw/63b6dbaf2719392cb2c55eb07a6b1d4e758cc16d/20k.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        words = [line.strip() for line in response.text.splitlines() if line.strip().isalpha()]
        random.shuffle(words)
        return words
    except Exception as e:
        print(f"[ERROR] Wörter konnten nicht geladen werden: {e}")
        return []

def clear_previous_word(word):
    pyautogui.press("backspace", presses=len(word))

def word_typing_thread():
    global running
    time.sleep(START_DELAY)
    wordlist = PUZZLESBAY_WORDS if use_better_tip else load_words_online()
    all_words = wordlist if skip_startwords else START_WORDS + wordlist

    for word in all_words:
        if not running:
            break
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(WORD_DELAY)
        clear_previous_word(word)

    running = False
    status_label.config(text=T["status_done"], fg="green")

def start_typing():
    global running
    if running:
        return
    running = True
    status_label.config(text=T["status_running"], fg="blue")
    threading.Thread(target=word_typing_thread, daemon=True).start()

def stop_typing():
    global running
    running = False
    status_label.config(text=T["status_stopped"], fg="red")

def toggle_mode():
    global use_better_tip
    use_better_tip = not use_better_tip
    mode_button.config(text=f"{T['mode']}: {T['better_tip'] if use_better_tip else T['standard']}")

def toggle_skip_startwords():
    global skip_startwords
    skip_startwords = not skip_startwords
    skip_button.config(
        text=T["skip_startwords_on"] if skip_startwords else T["skip_startwords"]
    )

# === GUI ===
root = tk.Tk()
root.title(T["title"])

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Button(frame, text=T["start"], width=25, command=start_typing).pack(pady=5)
tk.Button(frame, text=T["stop"], width=25, command=stop_typing).pack(pady=5)

mode_button = tk.Button(frame, text=f"{T['mode']}: {T['standard']}", width=25, command=toggle_mode)
mode_button.pack(pady=5)

skip_button = tk.Button(frame, text=T["skip_startwords"], width=25, command=toggle_skip_startwords)
skip_button.pack(pady=5)

status_label = tk.Label(frame, text=T["status_ready"], fg="green")
status_label.pack(pady=10)

root.mainloop()
