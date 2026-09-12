#!/usr/bin/env python3
import argparse
import functools
import http.server
import mimetypes
import socketserver

mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("application/octet-stream", ".unityweb")
mimetypes.add_type("application/octet-stream", ".data")
mimetypes.add_type("application/javascript", ".js")


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--directory", default="offline-web")
    ap.add_argument("--port", type=int, default=8765)
    args = ap.parse_args()

    handler = functools.partial(Handler, directory=args.directory)
    with socketserver.TCPServer(("127.0.0.1", args.port), handler) as httpd:
        print(f"Serving Six Cats Under at http://127.0.0.1:{args.port}/")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
