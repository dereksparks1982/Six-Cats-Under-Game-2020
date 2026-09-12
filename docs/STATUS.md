# Preservation status

## Preservation snapshot: captured

The original Six Cats Under release has now been preserved from the live Team Bean Loop itch.io release page.

### Browser release

- itch.io HTML5 upload ID: `2267583`
- Original Unity WebGL payload committed under `offline-web/`
- Original `index.html` preserved
- Original `Build/UnityLoader.js` preserved
- Original `Build/web.json` preserved
- Original data, WASM code, WASM framework, and background image preserved
- SHA-256 manifest committed
- Source URL map committed
- Local HTTP launcher included

The preserved `web.json` identifies the release as **Six Cats Under 1.0**, by **Team Bean Loop**, built with **Unity 2019.2.6f1**.

### Native releases

The three native downloads that were publicly available from the original itch.io page have also been archived under `native-builds/`:

- Windows — upload `2267563`
- Linux — upload `2267557`
- macOS — upload `2267627`

All three downloads passed `unzip -t` before being committed. Their SHA-256 hashes are recorded in `native-builds/MANIFEST.sha256`, and their original itch upload IDs/source endpoints are recorded in `native-builds/SOURCE-MAP.tsv`.

## Integrity records

The repository now contains independent SHA-256 manifests for both the browser release and native ZIP archives.

This means a future copy can be checked against the preservation snapshot even if the original itch.io release is no longer available.

## About `offline-web/FAILED-URLS.txt`

The capture crawler also recorded several 404 candidates discovered while scanning strings inside the minified Unity loader. Those candidate module paths are not part of the release files referenced by the preserved `index.html` and `web.json`.

The required Unity release payload is present:

- `Build/UnityLoader.js`
- `Build/web.json`
- `Build/web.data.unityweb`
- `Build/web.wasm.code.unityweb`
- `Build/web.wasm.framework.unityweb`
- `Build/web.jpg`

The 404 list is retained as capture evidence rather than silently discarded.

## Remaining work

The core preservation objective is complete: the original browser release and all three native public downloads are now stored in the repository with provenance and hashes.

Useful follow-up work includes compatibility testing on current browsers/Linux, documenting native executable contents, and preserving any additional original screenshots, release-page metadata, development notes, or creator material that adds historical context without altering the original game files.

## Preservation principle

The Roomz and other partially lost web games demonstrate why this work is being done before Six Cats Under disappears. Original files remain clearly separated from preservation tooling and later compatibility work, and original creator credit is retained throughout the repository.
