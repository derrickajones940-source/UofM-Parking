import json
import os
import threading
import urllib.request
from http.server import HTTPServer

import app


def test_parking_request_stores_and_returns_data(tmp_path):
    database_path = tmp_path / "test_parking.db"
    app.DB_PATH = str(database_path)

    app.initialize_database()

    server = HTTPServer(("localhost", 0), app.ParkingHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()

    try:
        url = f"http://localhost:{server.server_port}/parking"

        request_data = json.dumps(
            {
                "name": "Student Lot",
                "total_spaces": 100,
                "available_spaces": 15,
            }
        ).encode("utf-8")

        request = urllib.request.Request(
            url,
            data=request_data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urllib.request.urlopen(request) as response:
            assert response.status == 201
            created = json.loads(response.read().decode("utf-8"))

        lot_id = created["id"]

        with urllib.request.urlopen(f"{url}/{lot_id}") as response:
            assert response.status == 200
            parking_lot = json.loads(response.read().decode("utf-8"))

        assert parking_lot["name"] == "Student Lot"
        assert parking_lot["total_spaces"] == 100
        assert parking_lot["available_spaces"] == 15
        assert parking_lot["status"] == "Getting Full"

    finally:
        server.shutdown()
        thread.join()
        server.server_close()
