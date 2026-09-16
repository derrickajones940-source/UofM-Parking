
# UofM Parking Survival App — Requirements

## User Stories

### US-01 — View Parking Availability

**As a** UofM student or visitor,
**I want** to see the current status of parking lots,
**so that** I can know where parking may be available.

**Acceptance Criteria:**

* The app displays the name of each parking lot.
* Each lot has a status of Available, Getting Full, or Full.
* The user can view the status of multiple parking lots.

### US-02 — Compare Parking Costs

**As a** student or visitor,
**I want** to see the cost of each parking option,
**so that** I can avoid parking options that cost more than I want to pay.

**Acceptance Criteria:**

* The app displays the cost for each parking lot.
* Free parking is displayed as $0.
* The user can compare the costs of available parking lots.

### US-03 — View Parking Restrictions

**As a** user,
**I want** to see parking restrictions for each lot,
**so that** I can avoid parking somewhere I am not allowed to park.

**Acceptance Criteria:**

* The app displays restrictions for each parking lot.
* Restrictions are shown before the user selects a parking lot.
* A lot with a restriction identifies what type of restriction applies.

### US-04 — View Walking Distance

**As a** user,
**I want** to see the estimated walking time from a parking lot,
**so that** I can consider how far I will have to walk.

**Acceptance Criteria:**

* The app displays an estimated walking time for each parking lot.
* Walking time is displayed in minutes.
* The user can compare walking times between parking lots.

### US-05 — Find Available Parking

**As a** user,
**I want** to see parking lots that are not full,
**so that** I can focus on parking options that may be usable.

**Acceptance Criteria:**

* The app identifies lots that are Available or Getting Full.
* Full lots are not included in the available parking results.
* The results show the name and current status of each available option.

### US-06 — Receive a Parking Alert

**As a** user,
**I want** to receive a notification when my preferred parking lot is getting full,
**so that** I can look for another parking option.

**Acceptance Criteria:**

* The user can select a preferred parking lot.
* The app monitors the selected lot's status.
* A notification is generated when the selected lot changes to Getting Full.

### US-07 — Report Parking Conditions

**As a** student or visitor,
**I want** to report recent parking conditions,
**so that** other users can see updated information about a parking lot.

**Acceptance Criteria:**

* The user can select a parking lot when submitting a report.
* The user can report a parking condition.
* The report is associated with the selected parking lot.
* Other users can view recent parking reports.

## Non-Functional Requirements

### NFR-01 — Response Time

The app shall display the requested parking information within **2 seconds** when running with the required local application environment.

### NFR-02 — Test Coverage

All core parking functions shall have at least **one automated pytest test**, and all automated tests must pass before a release is considered complete.

### NFR-03 — Availability Data Freshness

When live or recently reported parking information is available, the displayed parking status shall be no more than **5 minutes old**.
