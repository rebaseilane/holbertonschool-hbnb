/*
 * File: package_diagram.md
 * Author: HBnB Evolution Project
 * Description: High-Level Package Diagram for HBnB application
 *              showing the three-layer architecture and facade pattern.
 *              This document includes both the UML diagram (Mermaid)
 *              and explanatory notes for the system architecture.
 *
 * Architecture:
 * - Presentation Layer (API / Services)
 * - Business Logic Layer (Models)
 * - Persistence Layer (Database Access)
 *
 * The system uses the Facade Pattern to simplify communication
 * between layers by providing a unified interface.
 */

# HBnB Evolution - High-Level Package Diagram

## 1. UML Package Diagram (Mermaid.js)

```mermaid
classDiagram

%% =========================
%% PRESENTATION LAYER
%% =========================
class PresentationLayer {
    <<Layer>>
    +API Endpoints
    +Services
    +FacadeInterface
}

%% =========================
%% BUSINESS LOGIC LAYER
%% =========================
class BusinessLogicLayer {
    <<Layer>>
    +User
    +Place
    +Review
    +Amenity
}

%% =========================
%% PERSISTENCE LAYER
%% =========================
class PersistenceLayer {
    <<Layer>>
    +Repositories
    +DatabaseHandler
}

%% =========================
%% FACADE PATTERN FLOW
%% =========================

PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Data Access / ORM
PersistenceLayer --> BusinessLogicLayer : Query Results
BusinessLogicLayer --> PresentationLayer : Response Objects
