# Sequence Diagram - Fetch Places

## Purpose
This diagram shows how a user retrieves a list of places.

---

## Diagram

```mermaid
sequenceDiagram

actor User
participant API
participant Facade
participant Repository
participant Database

User->>API: GET /places
API->>Facade: get_places()

Facade->>Repository: retrieve_places()
Repository->>Database: SELECT * FROM places

Database-->>Repository: places data
Repository-->>Facade: list of places

Facade-->>API: response
API-->>User: JSON places list