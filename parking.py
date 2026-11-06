import json
import uuid
from datetime import datetime

def log_event(level, message, **kwargs):
    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "message": message,
        **kwargs
    }
    print(json.dumps(record))

def get_lot_status_from_storage(lot_id: str):
    request_id = str(uuid.uuid4())
    log_event("INFO", "Starting parking status lookup", request_id=request_id, lot_id=lot_id, action="lookup_start")

    # Your existing logic here...

    log_event("INFO", "Successfully retrieved parking status", request_id=request_id, lot_id=lot_id, action="lookup_success")
    return {"lot_id": lot_id, "status": "Available"}
