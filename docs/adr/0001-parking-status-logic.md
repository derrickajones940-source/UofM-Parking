# ADR-001: Calculating Parking Status in Application Code

* **Status:** Accepted
* **Date:** 2026-09-29

## Context
My app needs to show whether a parking lot is "Available," "Nearly Full," or "Full" based on open spaces. I needed to decide where this calculation should happen in my code.

## The Decision
I decided to write simple Python code (`if/else` statements) to calculate the status directly inside the main application file.

## Alternatives Considered

### Alternative 1: Calculating inside a Database (SQL)
* **Why it was not chosen:** Setting up and managing a database for simple calculations takes too much setup time and makes unit testing harder for a single-developer project.

### Alternative 2: Using an External Cloud API
* **Why it was not chosen:** Calling an external service adds extra network lag, risks paid API fees, and introduces unnecessary points of failure.

## Consequences

### What this makes easier:
* **Fast testing:** I can test my logic instantly with basic unit tests without running a database server.
* **Simple setup:** The code runs anywhere without configuring external tools or database connections.

### What this makes HARDER:
* **No saved history:** If the app restarts, current status data isn't saved to disk.
* **Hard to share data:** If multiple users open the app at once, they can't share live data through a common database without extra setup.
