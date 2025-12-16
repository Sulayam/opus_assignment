# Vendor Onboarding Workflow – Opus Lab Assignment

## Overview

This repository contains the backend services used to support the **Vendor Onboarding Workflow Automation** lab assignment built using the Opus platform.

The Opus workflow automates a previously manual, email-driven vendor onboarding process by orchestrating validation, duplicate detection, compliance screening, document collection, escalation, and final vendor creation.
This backend simulates real enterprise systems such as a Vendor Master Database, Compliance Verification Service, Document Repository, and Workflow Audit Log.

The focus of this repository is **integration realism, auditability, and separation of concerns**, not UI or frontend development.

---

## System Architecture

### Opus Platform

* Orchestrates workflow logic
* Handles email intake, decision agents, human tasks, and branching
* Calls backend services using External Service nodes

### Backend (This Repository)

* **Framework:** FastAPI
* **Database:** SQLite
* **Authentication:** HTTP Basic Auth
* **Purpose:** Simulate external enterprise systems

---

## Folder Structure

```
.
├── main.py                 # FastAPI app and API routes
├── database.py             # SQLite connection and migrations
├── models.py               # Database write operations
├── compliance/             # Compliance rules and sanctions simulation
│   ├── engine.py
│   ├── models.py
│   └── rules.py
├── documents/              # Country-specific document logic
│   ├── matrix.py
│   ├── schemas.py
│   └── service.py
├── schema.sql              # Database schema
├── vendor_master.db        # SQLite database (local development)
├── requirements.txt
```

---

## Simulated External Systems

### Vendor Master Database

* Stores vendor records
* Supports duplicate detection by vendor name
* Tracks vendor lifecycle status

### Workflow Audit Log

* Stores all major workflow state transitions
* Uses JSON `details` column for extensibility

### Compliance Verification Service

* Simulates sanctions screening
* Logs compliance results with policy codes and outcomes

### Document Repository (Metadata)

* Stores document review results
* Tracks missing documents and reviewer notes

---

## Authentication

All endpoints are protected using **HTTP Basic Authentication**.

Credentials are loaded from environment variables:

```
VALID_USERNAME
VALID_PASSWORD
```

Authentication uses constant-time comparison to avoid timing attacks.

---

## API Endpoints

### Health & Metadata

* `GET /`
* `GET /health`

### Vendor Operations

* `POST /vendor/create`
  Creates a new vendor record

* `GET /vendor/check-duplicate/{vendor_name}`
  Checks for existing vendor by name

* `POST /vendor/log`
  Writes workflow audit logs

### Document Handling

* `POST /docs/requirements`
  Returns required documents based on country

* `POST /docs/file-storage`
  Logs document submission and review details

* `POST /vendor/document-issue`
  Logs missing or rejected document cases

### Compliance

* `POST /compliance/check`
  Runs compliance and sanctions checks

* `GET /compliance/rules/{country}`
  Returns country-specific compliance/document rules

### Testing

* `POST /test`
  Used to validate authentication and POST request behavior from Opus

---

## Database

### Tables

* `vendors`
* `workflow_logs`
* `compliance_logs`
* `document_file_storage`
* `document_issues`

The database schema is defined in `schema.sql` and initialized on application startup.

Minimal migrations are handled automatically to support iterative development.

---

## Opus Workflow Integration

Each Opus **External Service node** maps directly to one of the endpoints above.

The workflow:

1. Parses vendor request emails
2. Validates required fields
3. Performs duplicate detection
4. Runs compliance screening
5. Computes escalation logic
6. Collects and verifies documents
7. Logs every major state transition
8. Finalizes vendor onboarding

This backend is intentionally stateless at the API layer and persistent at the database layer, mirroring real internal service design.

---

## Known Testing Limitation

* POST requests with HTTP Basic Auth work correctly when tested using `curl`
* GET requests from Opus External Service nodes authenticate successfully
* POST requests from Opus External Service nodes reach the FastAPI application but return `401 Unauthorized`

Authentication logic, environment variables, routing, and database writes are verified independently.
This appears to be a platform-level request construction or header propagation issue specific to Opus POST executions and does not impact workflow design or backend correctness.

---

## Purpose of This Repository

This repository exists to:

* Demonstrate realistic external system integrations for the Opus workflow
* Provide auditability and persistence
* Support human-in-the-loop decisions
* Mirror production-style service boundaries

It is intentionally minimal and backend-only, aligned with the scope of the lab assignment.

---

## Author

Sulayam Abdul Rehman
AI / ML Engineer
Vendor Onboarding Workflow Automation – Opus Lab Assignment
