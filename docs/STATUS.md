# Preservation status

## Confirmed

- The original Six Cats Under itch.io release is still online.
- The original release lists HTML5, Windows, Linux, and macOS builds.
- The deployed HTML5 build uses itch.io upload ID `2267583`.
- The original browser entry point is known.
- Mozilla's historical WebGL bug report independently records the same upload ID and `Build/UnityLoader.js` path.
- Local capture tooling, a local HTTP server, and an offline launcher are present in this repository.

## Not yet vendored

The original Unity WebGL payload itself has not yet been committed to this repository. The capture script is designed to pull the original deployed files from itch.io and record their hashes and source URLs.

The official downloadable Linux, Windows, and macOS ZIP files are also not yet vendored.

## Next preservation step

Run the capture tool from a machine with normal internet access:

```bash
bash tools/capture_official_web.sh
```

Then verify the resulting build locally:

```bash
bash play.sh
```

Once verified, the untouched `offline-web/` payload and generated manifests can be committed as the preserved browser release.

## Secondary hunt

Public mirrors and GitHub repositories found so far mostly embed the same itch.io browser build rather than hosting an independent copy. They are useful corroboration, but they do not currently replace the original payload.
