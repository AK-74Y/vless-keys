# VLESS Key Grabber

Собирает актуальные VLESS-ключи из открытых источников и сохраняет их в один файл для импорта в v2rayNG.

## Файлы

### 🌐 `index.html`
Веб-версия. Открой файл в браузере, нажми **«Обновить»** — ключи подтянутся сразу из 4 источников (3 списка igareck + keys.json от tiagorrg), покажутся по отдельности для каждого источника. Кнопка **«Скачать всё»** сохранит общий файл `vless_keys.txt`.

### 🐍 `vless_keys_grabber.py`
Простая версия скрипта. Берёт ключи из **одного источника**:
- `tiagorrg/vless-checker/keys.json`

Быстрее, проще, меньше ключей на выходе.

```bash
python vless_keys_grabber.py
```

### 🐍 `vless_keys_grabber_v2.py`
Расширенная версия. Берёт ключи из **трёх источников**:
- `igareck/vpn-configs-for-russia` — BLACK_VLESS_RUS.txt
- `igareck/vpn-configs-for-russia` — BLACK_VLESS_RUS_mobile.txt
- `igareck/vpn-configs-for-russia` — WHITE-CIDR-RU-checked.txt

Больше ключей, дольше работает (три запроса вместо одного).

```bash
python vless_keys_grabber_v2.py
```

## Какой вариант выбрать

| | v1 | v2 |
|---|---|---|
| Источников | 1 | 3 |
| Скорость | быстрее | медленнее |
| Количество ключей | меньше | больше |

Оба скрипта убирают дубликаты и сохраняют результат в `vless_keys.txt`.

## Импорт в v2rayNG

1. Открой `vless_keys.txt`
2. v2rayNG → меню (⋮) → **Import config from file** — выбери файл
   или **Import config from clipboard** — по одному ключу

---
Только для личного использования.
