# POSTER_PLAN.md — Barevné plakáty do kavárny (série „Ananas&Bananas“)

Handoff pro Director session. Cíl: nahradit černobílý list se dvěma QR sérií barevných A4 plakátů k zalaminování, které ukazují **co appky dělají** (název + krátký popis + signifikantní screenshot), říkají **zdarma, bez reklam, bez sledování**, a vedou lidi do obchodů i na olin.now. Volba stylu/layoutu: viz konfigurátor (artefakt „Plakáty Ananas&Bananas“) — zvolená konfigurace se vloží do sekce 0.

---

## 0. Zvolená konfigurace (vyplnit z konfigurátoru)

```
Styl:          ___ (Tropical Tech / Neon Arcade / Pastel Kids / Papír & tisk)
Hustota:       ___ appek na stránku (4 doporučeno, 6 pro „přehledové“ listy)
Sada stránek:  ___ (Minimal 3 / Kategorie 7–8 / Kompletní 10–12)
Formát:        A4 na výšku, 300 dpi, okraje 10 mm, matná laminace
Jazyk:         CZ (EN podtitul u názvů appek, kde dává smysl)
```

## 1. Zjištění, ze kterých plán vychází

- olin.now má **41 projektů**, každý s vlastní stránkou (`olin.now/<slug>.html`) a **už hotovými screenshoty** (SwypeKids: 5 desktop + 14 mobilních). → Screenshoty se nejdřív *sklidí* z olin.now, fotí se jen chybějící/slabé.
- V obchodech je **publikováno jen ~5–6 appek** (obě platformy: SwypeKids, MirrorBooth; jen App Store: Kirian, StreamPoetry, Lexify, Puff — kvůli closed-test limitu na Play). Zbytek je web / desktop download (GitHub) / „chystáme“. → Plakáty musí rozlišit **„Nainstaluj teď“** (store QR) od **„Podívej se na olin.now“** (web QR). Jinak lidé naskenují a nic nenajdou.
- **Google Play QR dnes vede na vyhledávání `ol1n`** – to není spolehlivé (vývojářské jméno org účtu je jiné než „Ol1n“, vyhledávání vrací cizí appky). → Nahradit přímou URL vývojářské stránky z Play Console (`play.google.com/store/apps/dev?id=<číslo>`), totéž pro Apple (`apps.apple.com/developer/id<číslo>`).
- olin.now dnes nikde nemá souhrnnou větu „zdarma · bez reklam · bez sledování“ ani Ol1n Pass. Plakát to bude říkat → sjednotit i na webu (jedna věta v patičce + na landing page), aby QR vedl na stránku, která to potvrzuje.
- Ol1n Pass zatím není v obchodech (PASS_PLAN.md). → Stránka „Pass“ se tiskne až po spuštění; do té doby místo ní list „Všechno zdarma“ (viz 4.3).

## 2. Struktura série (co je na kterém listu)

Každý list = samostatný A4 na výšku, funguje i sám o sobě (kavárna si může pověsit jen některé). Všechny mají stejnou hlavičku (logo A&B vlevo nahoře, název kategorie), stejnou patičku (věta o zdarma/bez sledování + 1 velký QR + malé TikTok/YouTube).

| # | List | Obsah | QR v patičce |
|---|------|-------|--------------|
| 1 | **Obálka** „První český AI slop“ | Logo, claim, 3 věty co to je (jeden člověk, Praha, 40+ appek, vše bez reklam a sledování), 2 velké oficiální badge + QR App Store / Google Play, QR olin.now | App Store, Google Play, olin.now |
| 2 | **Teď v obchodech** | 4–6 publikovaných appek s **oficiálními store badge** u každé karty | App Store + Google Play (dev stránky) |
| 3 | **Pro děti a rodiče** | SwypeKids, Lexify, Šachové království, Hajánek, Pohádkomat, Mutants, Automatka, Papánek | olin.now/#deti |
| 4 | **Hry** | Kirian, Puff, Kačeny, Kittens, ImmunoRun, DoodlebugsRevival, DoggioWars, RattleRamp, Fotball Simulator, Archion | olin.now/#hry |
| 5 | **Kreativita & AI** | Ol1nLLM, MirrorBooth, Restyler, HandWrittenStickers, TsumikiMangaBot, MemeShorts, Toonfork, UGC Factory, StreamPoetry, Kindlify | olin.now/#ai |
| 6 | **Hudba & párty** | DJfy, PartyCockpit, Elfton Player, AudioScanner | olin.now/#hudba |
| 7 | **Každodenní pomocníci** | Tlumočník, Běhánek, Been Here, The Pill, BestBet, AlienMatch | olin.now/#pomocnici |
| 8 | **Pro firmy** (jen v Kompletní sadě) | PMTracker, TerraReality, Předávka | olin.now/business |
| 9 | **Ol1n Pass** / „Všechno zdarma“ | Pitch (viz 4.3) | Pass landing / olin.now |

Sady: **Minimal** = 1, 2, 9 (3 listy, stačí na první kolo — kavárna chce něco rychle). **Kategorie** = 1–7 + 9 (8 listů). **Kompletní** = vše (9 listů; kategorie s >6 appkami se dělí na 2 listy → 10–12).

Doporučení: **vytisknout Minimal hned** (do kavárny do týdne), sadu Kategorie dodat ve druhém kole až budou screenshoty.

## 3. Layout listu (A4 210×297, okraje 10 mm)

```
┌──────────────────────────────────────────┐
│ [logo A&B]   NÁZEV KATEGORIE        [■]  │  hlavička 28 mm; vpravo barevný štítek kategorie
│ jednořádkový podtitul kategorie          │
├──────────────────────────────────────────┤
│ ┌──────────────┐  ┌──────────────┐       │
│ │ [screenshot] │  │ [screenshot] │       │  karta: telefon 50×108 mm (poměr 9:19.5)
│ │   Název      │  │   Název      │       │  název 18 pt, popis 10,5 pt max 2 řádky
│ │   popis      │  │   popis      │       │  štítky: iOS / Android / Mac / Win / Web
│ └──────────────┘  └──────────────┘       │
│ ┌──────────────┐  ┌──────────────┐       │  hustota 4 = 2×2 (čitelné z 1 m)
│ │              │  │              │       │  hustota 6 = 2×3 (telefon 40×87 mm)
│ └──────────────┘  └──────────────┘       │
├──────────────────────────────────────────┤
│ Zdarma · bez reklam · bez sledování  [QR]│  patička 40 mm; QR 32 mm + popisek
│ olin.now                 [TikTok][YT]    │  malé QR 18 mm
└──────────────────────────────────────────┘
```

Pravidla:
- **Jeden screenshot na appku** – ten, který ukáže „aha“ moment (viz tabulka v 5). Ne úvodní obrazovka, ne menu.
- Screenshot v rámečku telefonu (jednoduchý zaoblený obdélník s notch, ne kresba konkrétního iPhonu).
- Popis = **1 věta, co uživatel dělá** („Dítě přejíždí prstem po obrázcích a skládá slova.“), ne feature list.
- Oficiální badge App Store / Google Play **jen u appek, které tam jsou** (min. výška 10 mm, Apple pravidla: nezkracovat, volný prostor 1/4 výšky badge okolo). Soubory: `badges/apple_badge.svg` (máme), `badges/google_badge.*` (stáhnout z Partner Marketing Hub / play.google.com/intl/cs/badges).
- QR: min. 32 mm, korekce H, tichá zóna 4 moduly, **testovat po laminaci** (lesklá fólie odráží — proto matná).
- Text min. 9 pt, kontrast ≥ 4.5:1 (kavárna = horší světlo).

## 4. Texty

### 4.1 Patička (na každém listu)
> **Zdarma. Bez reklam. Bez sledování.** Appky dělá jeden člověk v Praze s pomocí AI. Platíš jen za rozšíření, které chceš — a vždy víš dopředu za co.

### 4.2 Obálka
> **První český AI slop**
> 40+ aplikací pro děti, hráče, tvůrce i firmy. Všechny bez reklam a bez sledování. Naskenuj a vyber si.

### 4.3 List 9 — dvě varianty
- **Před spuštěním Passu („Všechno zdarma“)**: „Každá appka je zdarma v plné základní verzi. Placené jsou jen balíčky navíc (skiny, jazyky, hlasy). Nikdy reklama, nikdy prodej dat.“ + 3 příklady „co je zdarma / co je v balíčku“.
- **Po spuštění Passu**: „**Ol1n Pass — jednou zaplatíš, odemkneš všechno. Navždy.** Všechny balíčky ve všech appkách, včetně těch, které teprve vzniknou. 49 $ / ~1 100 Kč.“ + QR na pass landing + 3 argumenty (bez předplatného, bez reklam, podporuješ nezávislého vývojáře).

## 5. Screenshoty — co sklidit, co nafotit

Pořadí: (a) stáhnout `olin.now/<slug>.html` galerie → složka `assets/<slug>/`; (b) vybrat 1 „signature“ screen; (c) chybí-li nebo je slabý → spustit appku a nafotit podle sloupce „Co ukázat“.

Technické: iPhone 15 Pro simulátor (1179×2556) nebo Pixel 8 (1080×2400), **světlý režim, 100 % baterie, 9:41**, bez notifikací, CZ lokalizace. PNG. Pro děti a hry klidně reálný prst/kurzor v záběru.

| Appka | Kategorie | Co ukázat (signature screen) | Zdroj |
|-------|-----------|------------------------------|-------|
| SwypeKids | Děti | prst táhne po obrázkové klávesnici, slovo se skládá | olin.now (14 ks) – vybrat |
| Lexify | Děti | karta s obrázkem + slovo ve 3 jazycích | olin.now |
| Šachové království | Děti | bitevní animace figurek v pohádkovém stylu | nafotit |
| Hajánek | Děti | noční obrazovka s mořem + „táta vypráví“ | nafotit |
| Pohádkomat | Děti | roztočený glóbus + nápověda vypravěči | nafotit |
| Mutants / Kittens | Děti / Hry | sestavený mutant / karta bomby | nafotit (jsou-li hratelné) |
| Kirian | Hry | hustá vertikální střelba s bossem | olin.now |
| Puff | Hry | neonový mrak těsně před výbuchem | olin.now |
| Kačeny | Hry | 8 nábojů, kačeny shora, skin | nafotit |
| MirrorBooth | AI | symetrická tvář vedle originálu (vlastní obličej!) | olin.now |
| Restyler | AI | před/po: vousy + brýle | nafotit |
| HandWrittenStickers | AI | rukopis → samolepka v chatu | olin.now |
| Ol1nLLM | AI | chat s rolí Knihovník + studio obrázků | olin.now |
| Toonfork | AI | vertikální komiks s animovaným panelem | nafotit |
| DJfy | Hudba | party mód – hosté hlasují z telefonů | nafotit |
| PartyCockpit | Hudba | velká obrazovka s fotkami hostů | nafotit (TV záběr) |
| Tlumočník | Pomocníci | telefon mezi dvěma lidmi, dvě bubliny CZ/EN | nafotit |
| Běhánek | Pomocníci | běžecká obrazovka s hlasovým pacerem | nafotit |
| The Pill | Pomocníci | „jak to říct jinak“ před odesláním | nafotit |
| PMTracker / TerraReality / Předávka | Firmy | ověření polohy / mapa pronájmů / kuchyňský display | olin.now / nafotit |

Pro „chystáme“ appky bez buildu: místo screenshotu **ilustrace z L40S** ve stylu listu + štítek „Brzy“.

## 6. Vizuální styl a L40S

Layout zůstává v kódu (HTML/CSS → PDF přes Playwright, už v stacku). L40S (T-Mobile sandbox, FLUX.1-dev / SDXL) se použije na **tři věci**, ne na celé plakáty:
1. **Pozadí kategorie** – jemná textura/ilustrace v rohu hlavičky (ananas + obvodový had v barvě kategorie), 2480×700 px, 1 na kategorii.
2. **Ilustrace „Brzy“** pro appky bez screenshotu, 1179×2556 px, stejný styl.
3. **Style-sheet** – 1 referenční obrázek na zvolený styl, aby všechny generace držely paletu.

Prompt-kostra (doplní se podle zvoleného stylu z konfigurátoru):
`flat vector illustration, pineapple wrapped by a circuit-board snake, {palette}, {category motif}, clean background, poster header art, no text`
Negativ: `text, watermark, logo, photo, 3d render`. Generovat 8 variant, vybrat ručně, nikdy netisknout text z generátoru.

Barvy/fonty jsou v konfigurátoru jako CSS tokeny — po volbě je zkopírovat do `posters/theme.css`.

## 7. Atribuce QR (napojení na ANALYTICS_PLAN)

Každý QR vede přes krátký odkaz na olin.now, aby se dalo měřit, kolik instalací kavárna přinesla:
- `olin.now/go/cafe-ios` → App Store dev stránka s `?pt=<provider>&ct=cafe&mt=8`
- `olin.now/go/cafe-android` → Play dev stránka s `&referrer=utm_source%3Dcafe%26utm_medium%3Dposter`
- `olin.now/go/cafe-web` → `olin.now/?src=cafe`
Pro každé další místo (U Chřestýše, škola) jiný suffix → jiný tisk patičky, zbytek listu stejný.

## 8. Tisk a laminace

- Export PDF/X-ish: A4, 300 dpi, RGB je OK (kavárenská tiskárna / copy centrum), **bez spadávky** (laminace nechá 3–5 mm průhledný okraj; okraje 10 mm počítají s tím).
- Papír 160–200 g matný; laminace **matná 125 µm** (lesklá odráží světlo přes QR).
- Před tiskem série: 1 zkušební list, naskenovat všechny QR z 1 m a 2 m pod kavárenským světlem.
- Připravit i **A5 verzi obálky** (stolní stojánek) – stejný HTML, jiný `@page`.

## 9. Implementace (repo `posters/`)

```
posters/
  apps.json          # slug, name, desc, category, platforms, store URLs, screenshot, badge flags
  theme.css          # tokeny ze zvoleného stylu
  templates/         # cover.html, category.html, pass.html (Jinja/plain HTML)
  assets/<slug>/     # screenshoty (sklizené + nafocené), l40s/ ilustrace
  badges/            # apple_badge.svg, google_badge.svg
  build.py           # render HTML → PDF (Playwright), 1 PDF na list + sloučený
  qr.py              # generování QR s atribucí (qrcode, korekce H)
```

Kroky:
1. `apps.json` naplnit z olin.now (scrape 41 stránek: název, popis, platformy, store linky, galerie). Ručně doplnit `signature_shot` a `store_status`.
2. Ověřit v App Store Connect / Play Console **přesné URL vývojářských stránek** a seznam skutečně publikovaných appek; opravit QR z aktuálního listu.
3. Sklizeň screenshotů → review → seznam k nafocení → nafotit (sekce 5).
4. Téma z konfigurátoru → `theme.css`; L40S: hlavičkové ilustrace (sekce 6).
5. Šablony + build; nejdřív **Minimal (3 listy)** → zkušební tisk → laminace → do kavárny.
6. Sada Kategorie (druhé kolo). Patičkové varianty pro další místa (sekce 7).
7. Na olin.now přidat větu zdarma/bez sledování a kotvy `#deti #hry #ai #hudba #pomocnici`, aby QR z kategorií vedly na správné místo.

## 10. Otevřené otázky

- Které appky jsou dnes **opravdu** live na obou obchodech (a pod jakým vývojářským jménem)? Určuje list 2.
- Ol1n Pass: tisknout variantu „Všechno zdarma“ hned, Pass až po launchi? (plán předpokládá ano)
- Chce kavárna i **anglickou** verzi? (turisté – Minimal sada v EN je +3 listy, texty jsou krátké)
- Kolik kusů: 1 sada do kavárny + záloha; další místa dostanou patičku s vlastním QR suffixem.
