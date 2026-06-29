import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

appointments = []  # [patient_id, name, age, problem, time]


def is_valid_id(value):
    return str(value).strip().isdigit()


def is_valid_time(value):
    parts = str(value).strip().upper().split()
    if len(parts) == 2 and parts[0].isdigit() and parts[1] in ("AM", "PM"):
        return 1 <= int(parts[0]) <= 12
    return False


class Handler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass  # silence terminal logs

    def _json(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/appointments":
            self._json(200, [
                {"id": a[0], "name": a[1], "age": a[2], "problem": a[3], "time": a[4]}
                for a in appointments
            ])

        elif self.path.startswith("/search?id="):
            sid = self.path.split("=", 1)[1]
            if not sid.isdigit():
                self._json(400, {"error": "ID must be number"})
                return
            found = next((a for a in appointments if a[0] == int(sid)), None)
            if found:
                self._json(200, {"id": found[0], "name": found[1],
                                 "age": found[2], "problem": found[3], "time": found[4]})
            else:
                self._json(404, {"error": "Not Found"})
        else:
            self._json(404, {"error": "Not found"})

    def do_POST(self):
        if self.path == "/appointments":
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length).decode())

            if not is_valid_id(data.get("id", "")):
                self._json(400, {"error": "ID must be number"})
                return
            if not is_valid_time(data.get("time", "")):
                self._json(400, {"error": "Enter valid time (10 AM / 2 PM)"})
                return
            for f in ["name", "age", "problem"]:
                if not str(data.get(f, "")).strip():
                    self._json(400, {"error": f"{f.capitalize()} cannot be empty"})
                    return

            appointments.append([
                int(data["id"]),
                data["name"].strip(),
                str(data["age"]).strip(),
                data["problem"].strip(),
                data["time"].strip().upper()
            ])
            self._json(201, {"message": "Appointment Added Successfully"})
        else:
            self._json(404, {"error": "Not found"})


if __name__ == "__main__":
    server = HTTPServer(("localhost", 5000), Handler)
    print("=" * 47)
    print("   Clinic Booking Server is RUNNING")
    print("   URL  :  http://127.0.0.1:5000")
    print("   Next :  open Frontend.html")
    print("   Stop :  Ctrl+C")
    print("=" * 47)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n   Server stopped.")
