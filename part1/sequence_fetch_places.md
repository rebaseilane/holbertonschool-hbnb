sequenceDiagram

%% =====================
%% FETCH PLACES
%% =====================

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
Repository-->>Facade: places list

Facade-->>API: response
API-->>User: JSON list of places