# Sequence Diagram - Place Creation

## Purpose
This diagram shows how a user creates a new place listing.

---

## Diagram

```mermaid
sequenceDiagram

actor User
participant API
participant Facade
participant PlaceModel
participant Repository
participant Database

User->>API: POST /places
API->>Facade: create_place(data)

Facade->>PlaceModel: validate_place(data)
PlaceModel-->>Facade: validation result

Facade->>Repository: save(place)
Repository->>Database: INSERT place

Database-->>Repository: success
Repository-->>Facade: place saved

Facade-->>API: success response
API-->>User: 201 Created