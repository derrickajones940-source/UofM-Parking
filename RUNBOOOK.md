# Operations Runbook: UofM Parking Service

## Incident: High Rate of HTTP 500 Errors on Lot Status Lookups

### 1. Observable Symptom
Monitoring alert triggers due to HTTP 500 responses exceeding 5% on `/api/lots/{lot_id}` over a 5-minute window.

### 2. Diagnostic Steps
1. SSH into host and filter for error logs:
   ```bash
   grep '"level": "ERROR"' /var/log/uofm_parking/app.log | tail -n 20
