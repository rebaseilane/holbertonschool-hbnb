sequenceDiagram

%% =====================
%% REVIEW SUBMISSION
%% =====================

actor User
participant API
participant Facade
participant ReviewModel
participant Repository
participant Database

User->>API: POST /reviews
API->>Facade: create_review(data)

Facade->>ReviewModel: validate_review(data)
ReviewModel-->>Facade: validation result

Facade->>Repository: save(review)
Repository->>Database: INSERT review

Database-->>Repository: success
Repository-->>Facade: review saved

Facade-->>API: success response
API-->>User: 201 Created