# Sources and provenance

## Original release

**Six Cats Under** by Team Bean Loop / Mosu

Original itch.io page:

`https://teambeanloop.itch.io/six-cats-under`

itch.io game ID:

`646263`

The release page identifies the game as a Unity title with HTML5, Windows, macOS and Linux versions.

The live original page and public release files were inspected and captured on **2026-09-12**.

## Original browser build

The deployed HTML5 game is embedded from itch.io's classic HTML host. The preserved upload identifier is:

`2267583`

Known original entry point:

`https://html-classic.itch.zone/html/2267583/index.html?v=1591301667`

The upload ID and loader path are independently corroborated by a Mozilla Bugzilla report concerning the game. The report records requests to:

`/html/2267583/Build/UnityLoader.js`

That makes upload `2267583` a strong independently documented identifier for the original deployed Unity WebGL build.

The original build metadata preserved in `offline-web/Build/web.json` identifies:

- Company: `Team Bean Loop`
- Product: `Six Cats Under`
- Product version: `1.0`
- Unity version: `2019.2.6f1`

## Original native downloads

The public itch.io release page exposed the following native downloads and upload identifiers:

| Platform | Original filename | itch upload ID |
| --- | --- | ---: |
| Windows | `Six Cats Under - Windows.zip` | `2267563` |
| Linux | `Six Cats Under - Linux.zip` | `2267557` |
| macOS | `Six Cats Under.app.zip` | `2267627` |

The public itch file endpoint for each upload returned the signed itch CDN location used to retrieve the original archive. The exact source endpoint mapping is retained in `native-builds/SOURCE-MAP.tsv`.

All three ZIP archives were tested successfully with `unzip -t` before being committed.

## Third-party corroboration

Historical/current game portal pages embedding the title have also used the same itch.io upload `2267583` entry point. These are useful corroborating references, but the preservation snapshot in this repository was taken from the original Team Bean Loop itch.io release rather than from a third-party mirror.

## Integrity records

Browser release:

- `offline-web/MANIFEST.sha256` — SHA-256 for every captured original browser file.
- `offline-web/SOURCE-MAP.tsv` — local path, original URL, byte size and reported content type.

Native releases:

- `native-builds/MANIFEST.sha256` — SHA-256 for the Windows, Linux and macOS ZIP archives.
- `native-builds/SOURCE-MAP.tsv` — original filenames, itch upload IDs and source endpoints.

These records make it possible to distinguish the preserved original release from future compatibility patches, launcher changes, or reconstructed material.
