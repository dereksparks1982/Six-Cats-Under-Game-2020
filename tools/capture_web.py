#!/usr/bin/env python3
import argparse
import hashlib
import html.parser
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import deque

UA = "Mozilla/5.0 (Six-Cats-Under-Preservation/1.0)"
TEXT_EXTS = {".html", ".htm", ".js", ".json", ".css", ".txt"}
ASSET_EXTS = {
    ".html", ".htm", ".js", ".json", ".css", ".png", ".jpg", ".jpeg",
    ".gif", ".svg", ".ico", ".wasm", ".data", ".unityweb", ".mem",
    ".webgl", ".wav", ".ogg", ".mp3", ".txt"
}
QUOTED_RESOURCE = re.compile(
    r"['\"]([^'\"?#]+\.(?:html?|js|json|css|png|jpe?g|gif|svg|ico|wasm|data|unityweb|mem|webgl|wav|ogg|mp3|txt)(?:\?[^'\"]*)?)['\"]",
    re.I,
)


class LinkParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key.lower() in {"src", "href"} and value:
                self.links.append(value)


def request_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read(), resp.headers.get_content_type()


def iter_json_strings(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from iter_json_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_json_strings(item)
    elif isinstance(value, str):
        yield value


def clean_url(url):
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((p.scheme, p.netloc, p.path, p.query, ""))


def local_path_for(url, root_prefix, output):
    p = urllib.parse.urlsplit(url)
    rel = p.path[len(root_prefix):].lstrip("/")
    if not rel or rel.endswith("/"):
        rel += "index.html"
    return pathlib.Path(output) / urllib.parse.unquote(rel)


def candidate_urls(text, source_url):
    found = set()

    parser = LinkParser()
    if "<" in text and ">" in text:
        try:
            parser.feed(text)
            found.update(parser.links)
        except Exception:
            pass

    found.update(m.group(1) for m in QUOTED_RESOURCE.finditer(text))

    try:
        obj = json.loads(text)
        for value in iter_json_strings(obj):
            suffix = pathlib.PurePosixPath(urllib.parse.urlsplit(value).path).suffix.lower()
            if suffix in ASSET_EXTS:
                found.add(value)
    except Exception:
        pass

    for value in found:
        value = value.strip()
        if not value or value.startswith(("data:", "blob:", "javascript:", "mailto:")):
            continue
        yield urllib.parse.urljoin(source_url, value)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description="Capture the original Six Cats Under Unity WebGL build.")
    ap.add_argument("--url", required=True)
    ap.add_argument("--output", default="offline-web")
    args = ap.parse_args()

    start = clean_url(args.url)
    p = urllib.parse.urlsplit(start)
    root_prefix = "/html/2267583/"
    allowed_host = p.netloc

    output = pathlib.Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    queue = deque([start])
    seen = set()
    source_map = []
    failures = []

    while queue:
        url = clean_url(queue.popleft())
        if url in seen:
            continue
        seen.add(url)

        up = urllib.parse.urlsplit(url)
        if up.netloc != allowed_host or not up.path.startswith(root_prefix):
            continue

        dest = local_path_for(url, root_prefix, output)
        try:
            data, content_type = request_bytes(url)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            failures.append((url, str(exc)))
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        source_map.append((dest.relative_to(output).as_posix(), url, len(data), content_type))
        print(f"saved {dest} ({len(data):,} bytes)")

        suffix = dest.suffix.lower()
        if suffix in TEXT_EXTS or content_type.startswith("text/") or content_type in {"application/json", "application/javascript"}:
            text = data.decode("utf-8", errors="replace")
            for candidate in candidate_urls(text, url):
                cp = urllib.parse.urlsplit(candidate)
                if cp.netloc == allowed_host and cp.path.startswith(root_prefix):
                    queue.append(candidate)

                # Unity build configs occasionally use root-relative-looking paths
                # inside scripts. Trying the upload root too catches those safely.
                raw_path = urllib.parse.urlsplit(candidate).path
                if "/Build/Build/" in raw_path:
                    repaired = candidate.replace("/Build/Build/", "/Build/")
                    queue.append(repaired)

    # Known loader location documented by the original deployed build.
    loader = urllib.parse.urljoin(start, "Build/UnityLoader.js")
    if clean_url(loader) not in seen:
        queue.append(loader)

    # If the loader was added late, process it and anything it reveals.
    while queue:
        url = clean_url(queue.popleft())
        if url in seen:
            continue
        seen.add(url)
        up = urllib.parse.urlsplit(url)
        if up.netloc != allowed_host or not up.path.startswith(root_prefix):
            continue
        dest = local_path_for(url, root_prefix, output)
        try:
            data, content_type = request_bytes(url)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            failures.append((url, str(exc)))
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        source_map.append((dest.relative_to(output).as_posix(), url, len(data), content_type))
        print(f"saved {dest} ({len(data):,} bytes)")
        if dest.suffix.lower() in TEXT_EXTS or content_type.startswith("text/"):
            text = data.decode("utf-8", errors="replace")
            for candidate in candidate_urls(text, url):
                cp = urllib.parse.urlsplit(candidate)
                if cp.netloc == allowed_host and cp.path.startswith(root_prefix):
                    queue.append(candidate)

    files = sorted(p for p in output.rglob("*") if p.is_file() and p.name not in {"MANIFEST.sha256", "SOURCE-MAP.tsv", "FAILED-URLS.txt"})
    with open(output / "MANIFEST.sha256", "w", encoding="utf-8") as f:
        for path in files:
            f.write(f"{sha256(path)}  {path.relative_to(output).as_posix()}\n")

    with open(output / "SOURCE-MAP.tsv", "w", encoding="utf-8") as f:
        f.write("path\tsource_url\tbytes\tcontent_type\n")
        for row in source_map:
            f.write("\t".join(map(str, row)) + "\n")

    if failures:
        with open(output / "FAILED-URLS.txt", "w", encoding="utf-8") as f:
            for url, error in failures:
                f.write(f"{url}\t{error}\n")

    index = output / "index.html"
    if not index.exists():
        print("ERROR: index.html was not captured", file=sys.stderr)
        return 2

    print(f"\nCaptured {len(files)} files into {output}")
    print(f"SHA-256 manifest: {output / 'MANIFEST.sha256'}")
    if failures:
        print(f"Non-fatal fetch failures: {len(failures)} (see FAILED-URLS.txt)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
