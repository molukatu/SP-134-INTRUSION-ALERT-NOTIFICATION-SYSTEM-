
# SP-134: Intrusion Alert Notification System

**Student:** Michael Olukatu
**Program:** BSc Cyber Security, AFIT Kaduna
**Stack:** Python / FastAPI + PostgreSQL

## Problem
Existing IDS tools generate logs but don't notify users quickly in a clear way. Alerts get buried and seen too late.

This system detects suspicious activity, classifies severity (Low, Medium, High, Critical), and instantly notifies users via dashboard, email, and SMS.

## Features (Planned)
- User login with roles (Admin, Viewer)
- Event ingestion + Rule engine
- Alert dashboard with filter, acknowledge, resolve
- Email + SMS notifications
- PostgreSQL audit log

## Process Model
Agile Scrum - Iterative, with 2-week sprints. Chosen because requirements will evolve after prototype feedback.
## Problem
Intrusion detection tools produce large volumes of logs, but important alerts get buried in noise or reach the right person too late. Small teams and campus IT staff often miss critical events because there is no clear, prioritised, real-time way to be told.

## Target Users
- **Admin (security officer / IT administrator):** configures rules, manages users, acknowledges and resolves alerts.
- **Viewer (analyst / management):** monitors the dashboard and receives notifications, with read-only access.

## Objectives
1. Ingest security events from log sources and apply a rule engine to detect suspicious activity.
2. Classify each alert as Low, Medium, High, or Critical.
3. Notify users in real time through the dashboard and email, and by SMS where possible.
4. Let users filter, acknowledge, and resolve alerts.
5. Keep a tamper-evident audit log of all alerts and user actions in PostgreSQL.

## Scope
**In scope:** role-based login, event ingestion API, rule engine, severity classification, alert dashboard, email and SMS notifications, audit log.

**Out of scope:** deep packet inspection, automated blocking of attackers, machine-learning detection, and a native mobile app.

## Process Model: Agile Scrum
Work is done in 2-week sprints. I chose Scrum because:
- Requirements will change after prototype feedback, and the backlog can be reprioritised each sprint.
- Short cycles give a working demo early, which suits the Week 8 prototype review.
- A single-developer project benefits from small, clear sprint goals.

I rejected Waterfall because it assumes fixed requirements up front and delays testing until late, which is risky for a system with several integrations (email, SMS, database).

## Status
The dashboard in `/frontend` is a static mockup with sample data. Live data, SMS alerts, and the backend will be built in later sprints.
