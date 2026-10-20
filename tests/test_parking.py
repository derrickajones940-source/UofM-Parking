from parking import get_parking_status, get_lot_status_from_storage

# --- Unit Tests (Assert behavior of core logic) ---
def test_parking_lot_is_available():
    assert get_parking_status(50, 100) == "Available"

def test_parking_lot_is_getting_full():
    # Tests the exact boundary condition (<= 20%)
    assert get_parking_status(20, 100) == "Getting Full"

def test_parking_lot_is_full():
    assert get_parking_status(0, 100) == "Full"

# --- Acceptance Test (Exercises real storage-to-edge boundary) ---
def test_acceptance_end_to_end_lot_status():
    response = get_lot_status_from_storage("lot_a")
    assert response["lot_id"] == "lot_a"
    assert response["status"] == "Available"
    assert response["available_spaces"] == 50
    assert "total_spaces" in response
