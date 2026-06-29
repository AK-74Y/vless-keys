#!/usr/bin/env python3
"""
VLESS Key Grabber
Скачивает все свежие ключи с tiagorrg.github.io/vless-checker
и сохраняет их в текстовый файл для v2rayNG.
"""

import urllib.request
import json
import os
from datetime import datetime

# URL файла с ключами
KEYS_JSON_URL = "https://tiagorrg.github.io/vless-checker/keys.json"
OUTPUT_FILE = "vless_keys.txt"


def fetch_keys():
    print(f"[*] Загружаю ключи с {KEYS_JSON_URL} ...")
    try:
        with urllib.request.urlopen(KEYS_JSON_URL, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"[!] Ошибка загрузки: {e}")
        return []

    keys = []

    # Структура: {"normal": {"Baltic": [...], "Finland": [...], ...}, "whitelist": {...}}
    for section_name, section in data.items():
        if not isinstance(section, dict):
            continue
        for country, entries in section.items():
            if not isinstance(entries, list):
                continue
            for entry in entries:
                key = None
                if isinstance(entry, str):
                    key = entry.strip()
                elif isinstance(entry, dict):
                    # Поля могут называться "key", "vless", "uri", "config"
                    for field in ("key", "vless", "uri", "config", "link"):
                        if field in entry:
                            key = str(entry[field]).strip()
                            break
                if key and key.startswith("vless://"):
                    keys.append(key)

    return keys


def save_keys(keys):
    if not keys:
        print("[!] Ключей не найдено.")
        return

    # Убираем дубликаты, сохраняем порядок
    seen = set()
    unique = []
    for k in keys:
        if k not in seen:
            seen.add(k)
            unique.append(k)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# VLESS keys — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"# Источник: {KEYS_JSON_URL}\n")
        f.write(f"# Всего ключей: {len(unique)}\n\n")
        f.write("\n".join(unique))
        f.write("\n")

    print(f"[+] Сохранено {len(unique)} уникальных ключей → {os.path.abspath(OUTPUT_FILE)}")


if __name__ == "__main__":
    keys = fetch_keys()
    save_keys(keys)
    print("\n[i] Готово! Открой vless_keys.txt и импортируй ключи в v2rayNG:")
    print("    v2rayNG → ⋮ → Import config from clipboard (по одному)")
    print("    или используй 'Batch import' если поддерживается вашей версией.")
