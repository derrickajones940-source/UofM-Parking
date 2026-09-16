# AI Elicitation Output

## User Stories

### US-01: View Parking Availability

**As a** University of Memphis student or visitor,
**I want** to see the current availability of parking lots,
**so that** I can find a parking space more easily.

**Acceptance Criteria:**

* The app displays available parking lots.
* Each parking lot has a status of Available, Getting Full, or Full.
* Users can view multiple parking lots.

### US-02: Compare Parking Costs

**As a** user,
**I want** to see the cost of parking at each lot,
**so that** I can choose an affordable parking option.

**Acceptance Criteria:**

* The parking cost is displayed for each lot.
* Free parking is shown as $0.
* Users can compare the costs of different lots.

### US-03: View Parking Restrictions

**As a** user,
**I want** to see parking restrictions for each lot,
**so that** I can avoid parking where I am not allowed.

**Acceptance Criteria:**

* Restrictions are displayed before the user chooses a lot.
* The type of restriction is clearly identified.

### US-04: View Walking Distance

**As a** user,
**I want** to see the walking distance from a parking lot to campus,
**so that** I can choose a convenient parking location.

**Acceptance Criteria:**

* An estimated walking time is displayed in minutes.
* Users can compare walking distances between parking lots.

### US-05: Find Available Parking

**As a** user,
**I want** to see parking options that are not full,
**so that** I can quickly find a place to park.

**Acceptance Criteria:**

* Available lots are included in the results.
* Lots marked Getting Full are included.
* Lots marked Full are excluded from available results.

### US-06: Receive a Parking Alert

**As a** user,
**I want** to receive an alert when my preferred parking lot is getting full,
**so that** I can find another parking option before it becomes full.

**Acceptance Criteria:**

* The user can select a preferred parking lot.
* The app monitors the selected lot.
* The user receives a notification when the lot changes to Getting Full.

### US-07: Report Parking Conditions

**As a** user,
**I want** to report current parking conditions,
**so that** other users can see recent parking information.

**Acceptance Criteria:**

* The user can select a parking lot.
* The user can submit a parking condition report.
* The report is associated with the selected parking lot.
* Other users can see recent reports.

## Non-Functional Requirements

### NFR-01: Response Time

The app shall display requested parking information within **2 seconds** when running in the required local application environment.

### NFR-02: Automated Testing

Each core parking function shall have at least **one automated pytest test**, and all automated tests shall pass before a release is considered complete.

### NFR-03: Data Freshness

When live or recently reported parking information is available, the displayed parking status shall be **no more than 5 minutes old**.

