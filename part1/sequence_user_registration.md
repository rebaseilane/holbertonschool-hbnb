# Sequence Diagram - User Registration

## Purpose
This diagram shows how a user registers an account in the HBnB system.

---

## Diagram

```mermaid
sequenceDiagram

actor User
participant API
participant Facade
participant UserModel
participant Repository
participant Database

User->>API: POST /users (register)
API->>Facade: create_user(data)

Facade->>UserModel: validate_user(data)
UserModel-->>Facade: validation result

Facade->>Repository: save(user)
Repository->>Database: INSERT user

Database-->>Repository: success
Repository-->>Facade: user saved

Facade-->>API: success response
API-->>User: 201 Created