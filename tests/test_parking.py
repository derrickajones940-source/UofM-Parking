from parking import get_parking_status, get_lot_status_from_storage

def test_parking_lot_is_available():
    assert get_parking_status(50, 100) == "Available"

def test_parking_lot_is_getting_full():
    assert get_parking_status(10, 100) == "Getting Full"

def test_parking_lot_is_full():
    assert get_parking_status(0, 100) == "Full"

def test_end_to_end_storage_to_edge():
    # End-to-end test simulating an API request fetching real state from storage 
    response = get_lot_status_from_storage("lot_a")
    assert response["lot_id"] == "lot_a"
    assert response["status"] == "Available"
    assert response["available_spaces"] == 50
