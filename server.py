#!/usr/bin/env python3
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

SRC = [
    "https://api.adsb.lol/v2/point/{a}/{o}/25",
    "https://api.airplanes.live/v2/point/{a}/{o}/25",
    "https://opendata.adsb.fi/api/v2/lat/{a}/lon/{o}/dist/25",
]


class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        u = urlparse(self.path)
        if u.path != "/api":
            return super().do_GET()
        q = parse_qs(u.query)
        try:
            a, o = float(q["lat"][0]), float(q["lon"][0])
        except Exception:
            return self.send_error(400, "lat/lon no válidos")
        for s in SRC:
            try:
                req = urllib.request.Request(
                    s.format(a=a, o=o), headers={"User-Agent": "radar-local/1.0"}
                )
                data = urllib.request.urlopen(req, timeout=8).read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
                return
            except Exception as e:
                print("fallo", s, e)
        self.send_error(502, "ninguna fuente respondió")


if __name__ == "__main__":
    print("Abre http://localhost:8000/radar.html  (Ctrl+C para parar)")
    ThreadingHTTPServer(("127.0.0.1", 8000), H).serve_forever()
