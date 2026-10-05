import json
import os
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from parking import get_parking_status


DB_PATH = os.environ.get("PARKING_DB", "parking.db")


def initialize_database():
    connection = sqlite3.connect(DB_PATH)
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS parking_lots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            total_spaces INTEGER NOT NULL,
            available_spaces INTEGER NOT NULL,
            status TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


def create_parking_lot(name, total_spaces, available_spaces):
    status = get_parking_status(available_spaces, total_spaces)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.execute(
        """
        INSERT INTO parking_lots
        (name, total_spaces, available_spaces, status)
        VALUES (?, ?, ?, ?)
        """,
        (name, total_spaces, available_spaces, status),
    )
    lot_id = cursor.lastrowid
    connection.commit()
    connection.close()

    return lot_id


def get_parking_lot(lot_id):
    connection = sqlite3.connect(DB_PATH)
    row = connection.execute(
        """
        SELECT id, name, total_spaces, available_spaces, status
        FROM parking_lots
        WHERE id = ?
        """,
        (lot_id,),
    ).fetchone()
    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "total_spaces": row[2],
        "available_spaces": row[3],
        "status": row[4],
    }


class ParkingHandler(BaseHTTPRequestHandler):

    def send_json(self, status_code, data):
        response = json.dumps(data).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_POST(self):
        if self.path != "/parking":
            self.send_json(404, {"error": "Not found"})
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)

            name = data["name"]
            total_spaces = int(data["total_spaces"])
            available_spaces = int(data["available_spaces"])

            if total_spaces <= 0:
                raise ValueError("total_spaces must be greater than zero")

            if available_spaces < 0 or available_spaces > total_spaces:
                raise ValueError(
                    "available_spaces must be between 0 and total_spaces"
                )

            lot_id = create_parking_lot(
                name,
                total_spaces,
                available_spaces,
            )

            self.send_json(
                201,
                {
                    "id": lot_id,
                    "message": "Parking lot created",
                },
            )

        except (KeyError, ValueError, json.JSONDecodeError) as error:
            self.send_json(400, {"error": str(error)})

    def do_GET(self):
        path = urlparse(self.path).path

        if not path.startswith("/parking/"):
            self.send_json(404, {"error": "Not found"})
            return

        try:
            lot_id = int(path.split("/")[-1])
        except ValueError:
            self.send_json(400, {"error": "Invalid parking lot ID"})
            return

        parking_lot = get_parking_lot(lot_id)

        if parking_lot is None:
            self.send_json(404, {"error": "Parking lot not found"})
            return

        self.send_json(200, parking_lot)


def run_server():
    initialize_database()

    server = HTTPServer(("localhost", 8000), ParkingHandler)

    print("Parking app running at http://localhost:8000")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    run_server()
