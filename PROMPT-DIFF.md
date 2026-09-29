# Prompt-and-Diff Log

## AI Prompt Used

I am developing a UofM Parking Survival App for University of Memphis students and visitors.

The concept is a parking application that helps users find parking based on parking availability, cost, parking restrictions, and walking distance. The app should show whether parking lots are Available, Getting Full, or Full. It may provide notifications when a preferred parking lot is becoming full. Users may also be able to report recent parking conditions so other users can see updated parking information.

Please act as a requirements analyst and elicit requirements for this application. Provide user stories with acceptance criteria and non-functional requirements. Also identify any questions or requirements you think should be clarified before development.

## Comparison Between My Requirements and AI Output

| Area                         | My Requirements                                | AI Output                     | Difference                    |
| ---------------------------- | ---------------------------------------------- | ----------------------------- | ----------------------------- |
| Parking availability         | Included                                       | Included                      | AI got this right             |
| Parking status               | Available, Getting Full, Full                  | Available, Getting Full, Full | AI got this right             |
| Parking cost                 | Included                                       | Included                      | AI got this right             |
| Parking restrictions         | Included                                       | Included                      | AI got this right             |
| Walking distance             | Included                                       | Included                      | AI got this right             |
| Finding available parking    | Included                                       | Included                      | AI got this right             |
| Parking alerts               | Preferred lot can alert when getting full      | Included                      | AI got this right             |
| Parking reports              | Users can report parking conditions            | Included                      | AI got this right             |
| Status change rules          | Need to define when statuses change            | Not clearly defined           | AI missed this                |
| Report age                   | Need to define what counts as recent           | Not clearly defined           | AI missed this                |
| Restriction behavior         | Need to define how restrictions affect choices | Not clearly defined           | AI missed this                |
| Walking distance calculation | Need to define how distance is calculated      | Not clearly defined           | AI missed this                |
| GPS/location tracking        | Not part of current scope                      | Suggested/implied             | AI added something not wanted |
| Maps                         | Not part of current scope                      | Suggested/implied             | AI added something not wanted |
| User accounts                | Not part of current scope                      | Suggested/implied             | AI added something not wanted |
| Payment processing           | Not part of current scope                      | Suggested/implied             | AI added something not wanted |

## Result of the Comparison

The AI output covered most of the main features of the app, but it did not provide enough detail about several important requirements. It also introduced features that are outside the current project scope.

The comparison shows why the AI output needs to be reviewed by the project team before it becomes the final set of requirements.

# Domain Model — AI Prompt and Diff

## AI Tool

GitHub Copilot

## Prompt Used

Using the M2 requirements for my UofM Parking Survival App, create a first draft of a domain model.

The app helps students find and understand parking near the University of Memphis and downtown Memphis.

The system needs to support parking information such as:

* parking lot availability
* total and available spaces
* parking cost
* parking restrictions
* walking distance
* parking status such as Available, Nearly Full, or Full
* user reports about parking conditions
* notifications when a parking lot is filling up

Create a simple domain model for the current requirements.

Use only entities that are actually supported by the requirements. Do not add unnecessary entities such as roles, permissions, audit logs, settings, authentication, or payment systems unless the requirements specifically require them.

Show the entities, important attributes, and relationships between entities.

Explain why each entity and relationship exists.

## AI First Draft

GitHub Copilot proposed the following main concepts:

* ParkingLot
* ParkingRestriction
* ParkingReport
* AlertSubscription
* Notification
* User

The AI also proposed relationships between these entities, including relationships between User and ParkingReport and between User, ParkingLot, and AlertSubscription.

## Changes I Made

I simplified the AI model to three main entities:

* ParkingLot
* ParkingReport
* Notification

### Removed ParkingRestriction as a Separate Entity

I kept parking restrictions as information associated with ParkingLot instead of making them a separate entity.

### Removed AlertSubscription

I removed AlertSubscription because the current model does not require a separate entity to represent subscriptions.

### Removed User

I removed User as a separate entity because the current requirements do not require user accounts, authentication, or stored user information.

### Kept ParkingReport

I kept ParkingReport because the application needs to represent user reports about parking conditions.

### Kept Notification

I kept Notification because the application needs to support notifications when a parking lot is filling up.

### Did Not Create ParkingStatus

I did not create ParkingStatus as a separate entity because the status can be calculated from available spaces and total spaces using the application's Python logic.

## Reason for the Changes

The main goal of my changes was to avoid over-modelling the application.

The AI draft provided useful possibilities, but I compared each entity and relationship against the current requirements. I removed concepts that were not necessary for the core functionality and kept the concepts that directly represent information the application needs.
