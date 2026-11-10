# Poster

Barevné A4 plakáty série „Ananas&Bananas“ (appky z olin.now) k zalaminování.

- `posters/artifact/` — interaktivní editor plakátů (`template.html`) + skripty. Výstup: barevné PDF.
- `posters/build.py` + `poster.json` — dávkový build PDF přes Playwright.
- `posters/harvest.py` — stáhne názvy, popisy, ikony a screenshoty z olin.now do `posters/assets/`.

## Použití
```
cd posters
python3 -m venv .venv && .venv/bin/pip install playwright "qrcode[pil]" jinja2 pypdf
.venv/bin/playwright install chromium
.venv/bin/python harvest.py                 # stáhne assets/ a harvest.json
.venv/bin/python artifact/build_data.py     # zabalí obrázky do artifact/data.json
python3 artifact/build.py                   # složí artifact/plakatovna.html (editor)
.venv/bin/python build.py                   # PDF podle poster.json
```
