from parking import get_parking_status


def test_parking_lot_is_available():
    assert get_parking_status(50, 100) == "Available"


def test_parking_lot_is_getting_full():
    assert get_parking_status(10, 100) == "Getting Full"


def test_parking_lot_is_full():
    assert get_parking_status(0, 100) == "Full"
