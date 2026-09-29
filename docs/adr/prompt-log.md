# Prompt-and-Diff Log

## ADR-001: Calculating Parking Status in Application Code

### Prompt

I need to write ADR-001 for my UofM Parking Survival App. The architecture decision is where the parking status calculation should happen.

The app needs to determine whether a parking lot is "Available," "Nearly Full," or "Full" based on the number of open spaces.

I decided to calculate the status directly in the Python application code using simple `if/else` statements.

The ADR should include:

* Context
* The Decision
* At least two alternatives considered
* Why each alternative was not chosen
* Consequences, including what the decision makes easier and harder

The alternatives are:

1. Calculating the status inside a database using SQL.
2. Using an external cloud API.

### Diff / Changes Made

Before this decision was documented:

* The parking status logic existed as Python application code.
* The project did not have an ADR documenting why the calculation was performed in application code.
* There was no documented comparison between application code, database calculations, and external APIs.

After this decision was documented:

* Added ADR-001 documenting the decision to use Python `if/else` statements.
* Documented SQL/database calculations as an alternative.
* Documented an external cloud API as a second alternative.
* Explained why the alternatives were not selected.
* Documented the benefits of simple testing and setup.
* Documented the limitations involving saved history and sharing live data between multiple users.

### Human Review

I reviewed the ADR and confirmed that it describes the actual architecture decision for the parking-status calculation in my project.

The decision keeps the calculation simple and local to the application while leaving database or external-service integration as possible future changes if the application grows.

