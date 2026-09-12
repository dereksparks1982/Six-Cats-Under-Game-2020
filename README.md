# Six Cats Under — Preservation Project

A preservation and offline-play project for **Six Cats Under**, the 2020 point-and-click puzzle game by Team Bean Loop / Mosu.

The goal of this repository is to preserve the original released game in a form that can still be played locally if the hosted web version eventually disappears.

## Current status

- Original itch.io release identified and still live.
- Original HTML5 upload identified: itch.io upload **2267583**.
- Original embedded build endpoint identified as:
  `https://html-classic.itch.zone/html/2267583/index.html?v=1591301667`
- Official Windows, Linux and macOS downloads are still listed on the developer's itch.io page.
- Offline capture and launcher tooling is included here.

## Capture the original web build

On Linux:

```bash
./tools/capture_official_web.sh
```

The capture tool follows the original Unity WebGL page, discovers same-build dependencies, downloads them into `offline-web/`, and generates SHA-256 and source manifests.

## Play offline

After a successful capture:

```bash
./play.sh
```

The launcher serves the preserved Unity build over localhost and opens it in the default browser. Unity WebGL builds should be served over HTTP rather than opened directly with `file://`.

## Repository layout

```text
Six-Cats-Under-Game-2020/
├── README.md
├── play.sh
├── docs/
│   ├── SOURCES.md
│   └── STATUS.md
├── tools/
│   ├── capture_official_web.sh
│   ├── capture_web.py
│   └── serve.py
└── offline-web/
```

## Original credits

Six Cats Under was made as a game jam project. The original itch.io page credits:

- Miles Äijälä / @qwertyprophecy
- Robin Swift / @SwiftSketches
- Tomas Beržinskas
- Alex Martin

This preservation repository is not the original development repository and does not claim authorship of the game.

## Preservation rule

Keep original files untouched wherever possible. Any compatibility patches or reconstructed material should live separately and be clearly labeled so the preserved release can always be distinguished from later work.
