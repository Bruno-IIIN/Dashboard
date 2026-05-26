import json
import os


HISTORY_FILE = 'history.json'


def save_history(item):
    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            history = json.load(f)

    history.append(item)

    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4)
