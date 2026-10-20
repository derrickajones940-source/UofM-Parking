# Prompt and Diff Log - UofM Parking Application

## Milestone 1: The Walking Skeleton & CI Pipeline
- **User Prompt / Goal**: Implement an end-to-end thin slice from storage state to edge API response, with a green GitHub Actions CI pipeline.
- **Key Changes**:
  - Created `parking.py` with an in-memory database (`PARKING_DATABASE`), core logic (`get_parking_status`), and an edge API handler (`get_lot_status_from_storage`).
  - Created initial test suite in `tests/test_parking.py`.
  - Configured GitHub Actions workflow in `.github/workflows/ci.yml` running `python3 -m pytest`.
  - Verified a successful green CI run on GitHub.

---

## Milestone 2: Test Suite Enhancement, Coverage, & Bug Injection
- **User Prompt / Goal**: Write formal unit and acceptance tests, generate a test coverage report, and execute a subtle boundary bug-injection demonstration.
- **Key Changes**:
  - Expanded `tests/test_parking.py` to separate core logic unit tests (`test_parking_lot_is_available`, `test_parking_lot_is_getting_full`, `test_parking_lot_is_full`) and an acceptance test (`test_acceptance_end_to_end_lot_status`).
  - Installed `pytest-cov` and generated a code coverage report confirming high line coverage across `parking.py`.
  - Executed bug-injection demonstration:
    1. **Fault Diff**: Injected a subtle boundary error in `parking.py` by changing the threshold comparison operator from `<= 0.20` to `< 0.20`.
    2. **Suite Failure**: Ran `python3 -m pytest` and proved the test suite successfully caught the fault on the `20 / 100` boundary condition (`test_parking_lot_is_getting_full` failed).
    3. **Fix & Restoration**: Reverted the operator back to `<= 0.20` and verified the test suite returned to a clean green status.
