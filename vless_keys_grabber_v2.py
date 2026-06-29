#!/usr/bin/env python3
"""
VLESS Key Grabber — все ключи без фильтрации
Источник: igareck/vpn-configs-for-russia (тот же что использует tiagorrg/vless-checker)
Сохраняет все ключи в vless_keys.txt для v2rayNG.
"""

import urllib.request
import os
from datetime import datetime

SOURCES = [
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-CIDR-RU-checked.txt",
]

OUTPUT_FILE = "vless_keys.txt"


def fetch(url):
    print(f"[*] Загружаю: {url.split('/')[-1]} ...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            lines = resp.read().decode("utf-8").splitlines()
        keys = [l.strip() for l in lines if l.strip().startswith("vless://")]
        print(f"    → найдено {len(keys)} ключей")
        return keys
    except Exception as e:
        print(f"    [!] Ошибка: {e}")
        return []


def main():
    all_keys = []
    for url in SOURCES:
        all_keys.extend(fetch(url))

    # Убираем дубликаты, сохраняем порядок
    seen = set()
    unique = []
    for k in all_keys:
        if k not in seen:
            seen.add(k)
            unique.append(k)

    if not unique:
        print("\n[!] Ключей не найдено. Проверьте подключение к интернету.")
        return

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(unique) + "\n")

    print(f"\n[+] Сохранено {len(unique)} уникальных ключей → {os.path.abspath(OUTPUT_FILE)}")
    print("\n[i] Импорт в v2rayNG:")
    print("    Меню (⋮) → Import config from file → выбери vless_keys.txt")
    print("    или копируй ключи по одному через 'Import from clipboard'")


if __name__ == "__main__":
    main()
