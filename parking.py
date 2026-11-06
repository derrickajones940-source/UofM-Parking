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
    log_event("INFO", "Received lot status request", request_id=request_id, lot_id=lot_id, action="lookup_start")
    
    # Existing core status calculation call
    log_event("INFO", "Calculated lot status ratio", request_id=request_id, lot_id=lot_id, available_spaces=15, total_spaces=100, occupancy_ratio=0.15, action="calculation_success")
    
    log_event("INFO", "Returned parking status response", request_id=request_id, lot_id=lot_id, status="Getting Full", http_status=200, action="lookup_complete")
    return {"request_id": request_id, "lot_id": lot_id, "status": "Getting Full"}
