# Six Cats Under — Preservation Project

A preservation and offline-play project for **Six Cats Under**, the 2020 point-and-click puzzle game by Team Bean Loop / Mosu.

## Why this repository exists

The goal of this repository is to preserve the original released game in a form that can still be played locally if the hosted web version eventually disappears.

This kind of preservation matters because web games can vanish surprisingly fast when a hosting service shuts down, a domain expires, browser technology changes, or original developer files are lost. Projects such as **The Roomz** show how much harder recovery becomes after that happens: surviving game files, forum posts, mirrors, documentation, and dependencies can end up scattered across old archives or disappear entirely.

By preserving **Six Cats Under while the original release is still available**, we can keep untouched copies of the actual released files, record exactly where they came from, hash them for later verification, retain the original credits, and provide a local way to run the game without depending on the original host.

This is a preservation repository. It is **not** a claim of authorship and it is not presented as an original DKLab game.

## Preservation snapshot

The original public release has now been captured in four forms:

- **HTML5 / Unity WebGL** — itch.io upload `2267583`
- **Windows ZIP** — itch.io upload `2267563`
- **Linux ZIP** — itch.io upload `2267557`
- **macOS ZIP** — itch.io upload `2267627`

The itch.io game ID is `646263`.

The preserved Unity browser build identifies itself as:

- Product: **Six Cats Under**
- Company: **Team Bean Loop**
- Version: **1.0**
- Unity: **2019.2.6f1**

## What is preserved

### Original browser release

`offline-web/` contains the captured original Unity WebGL release, including:

- `index.html`
- `Build/UnityLoader.js`
- `Build/web.json`
- `Build/web.data.unityweb`
- `Build/web.wasm.code.unityweb`
- `Build/web.wasm.framework.unityweb`
- `Build/web.jpg`
- `MANIFEST.sha256`
- `SOURCE-MAP.tsv`

The source build was captured from the original deployed itch.io HTML5 upload. The required files referenced by the original `index.html` and `web.json` are preserved locally.

### Original native releases

`native-builds/` contains untouched copies of the publicly downloadable native releases:

- `Six Cats Under - Windows.zip`
- `Six Cats Under - Linux.zip`
- `Six Cats Under.app.zip`
- `MANIFEST.sha256`
- `SOURCE-MAP.tsv`

Each ZIP was tested as a valid archive before being committed.

## Play offline

For the preserved browser release on Linux:

```bash
bash play.sh
```

The launcher starts a local HTTP server for the preserved Unity build and opens it in the default browser. The actual Unity game payload is served from this repository rather than downloaded from itch.io at play time.

You can also use the preserved native ZIP for your operating system directly from `native-builds/`.

## Verify the preserved files

Browser build:

```bash
cd offline-web
sha256sum -c MANIFEST.sha256
```

Native releases:

```bash
cd native-builds
sha256sum -c MANIFEST.sha256
```

## Re-capture tooling

The repository also contains tooling that can reproduce the browser capture while the original hosted release remains online:

```bash
bash tools/capture_official_web.sh
```

The capture tool follows the original Unity WebGL page, downloads the same-build dependencies, and generates SHA-256 and source manifests.

## Repository layout

```text
Six-Cats-Under-Game-2020/
├── README.md
├── play.sh
├── offline-web/          # preserved original HTML5 / Unity WebGL release
├── native-builds/        # preserved Windows, Linux and macOS releases
├── docs/
│   ├── SOURCES.md
│   ├── STATUS.md
│   └── WEB-CAPTURE.md
├── tools/
│   ├── capture_official_web.sh
│   ├── capture_web.py
│   └── serve.py
└── .github/workflows/    # reproducible capture / archival jobs
```

## Original credits

Six Cats Under was made as a game jam project. The original itch.io page credits:

- Miles Äijälä / @qwertyprophecy
- Robin Swift / @SwiftSketches
- Tomas Beržinskas
- Alex Martin

Original game authorship remains with its creators.

## Preservation rule

Keep original files untouched wherever possible. Compatibility fixes, launchers, documentation, reconstructed material, or later experiments should remain clearly separated from the preserved originals so there is never any confusion about what came from the 2020 release and what was added later for preservation or compatibility.
