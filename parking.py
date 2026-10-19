# Simulated Storage Layer (State)
PARKING_DATABASE = {
    "lot_a": {"available_spaces": 50, "total_spaces": 100},
    "lot_b": {"available_spaces": 5, "total_spaces": 100},
}

def get_parking_status(available_spaces, total_spaces):
    if available_spaces == 0:
        return "Full"
    elif available_spaces / total_spaces <= 0.20:
        return "Getting Full"
    else:
        return "Available"

# Edge / API Layer: Fetches from storage and returns status
def get_lot_status_from_storage(lot_id):
    if lot_id not in PARKING_DATABASE:
        return {"error": "Lot not found"}

    lot = PARKING_DATABASE[lot_id]
    status = get_parking_status(lot["available_spaces"], lot["total_spaces"])

    return {
        "lot_id": lot_id,
        "available_spaces": lot["available_spaces"],
        "total_spaces": lot["total_spaces"],
        "status": status
    }
