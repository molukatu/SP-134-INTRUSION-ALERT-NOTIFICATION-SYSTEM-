# Software Requirements Specification (SRS)
## SP-134: Intrusion Alert Notification System

**Version:** 1.0
**Date:** 11 November 2026
**Author:** Michael Olukatu
**Program:** BSc Cyber Security, AFIT Kaduna

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for SP-134, a web-based Intrusion Alert Notification System. It detects suspicious network activity and notifies administrators in real-time via dashboard, email, and SMS.

### 1.2 Scope
The system is for a small / medium network (e.g. university lab, small office). It monitors network flow logs, classifies them as benign or suspicious, stores alerts in a database, and notifies the admin.

This is the Phase 1 version. The advanced open-set continual learning engine is planned as a Final Year extension (see Section 8).

### 1.3 Definitions
- **Flow:** A summary of network traffic (source IP, dest IP, port, protocol, packets, bytes, duration).
- **Alert:** A record created when a flow is classified as suspicious.
- **Admin:** The security administrator who receives and manages alerts.
- **Analyst:** A user who reviews alerts and marks them True/False Positive.

## 2. Stakeholders
- **Admin:** Receives alerts, manages users, configures thresholds.
- **Analyst:** Reviews alerts, confirms or dismisses them.
- **Viewer:** Can view dashboard, cannot change settings.

## 3. Functional Requirements

### FR1: Ingest Flows
- FR1.1 System shall accept flow logs via REST API (POST /api/flows) and CSV upload.
- FR1.2 System shall validate each flow (required fields, valid IPs/ports).
- FR1.3 System shall store all flows in PostgreSQL.

### FR2: Detect Intrusions
- FR2.1 System shall classify each flow as Benign or Suspicious using rule-based checks + a simple ML model (Phase 1).
- FR2.2 Rules shall include: port scan (many ports from one IP in short time), brute force (many failed logins), unusual traffic volume, known bad ports/protocols.
- FR2.3 System shall assign a severity to each alert: Low, Medium, High, Critical.
- FR2.4 System shall assign a confidence score (0-100%) to each detection.

### FR3: Alert Management
- FR3.1 System shall create an alert record for every suspicious flow.
- FR3.2 System shall show alerts on the dashboard sorted by severity and time.
- FR3.3 System shall allow Analyst to mark an alert as: New, Investigating, Confirmed, False Positive, Resolved.
- FR3.4 System shall allow filtering alerts by severity, IP, date, status.

### FR4: Notifications
- FR4.1 System shall send an email notification for High and Critical alerts within 60 seconds.
- FR4.2 System shall send an SMS notification for Critical alerts within 60 seconds.
- FR4.3 System shall allow Admin to turn email/SMS on/off and set quiet hours.
- FR4.4 System shall log every notification sent (recipient, channel, time, status).

### FR5: Dashboard & Reports
- FR5.1 System shall show: total alerts today, alerts by severity, top attacker IPs, recent alerts.
- FR5.2 System shall allow exporting alerts to CSV.
- FR5.3 System shall show a daily summary report.

### FR6: Users & Security
- FR6.1 System shall require login for all pages except login page.
- FR6.2 System shall support roles: Admin, Analyst, Viewer.
- FR6.3 System shall hash passwords and use JWT / session auth.
- FR6.4 System shall log all login attempts.

## 4. Non-Functional Requirements
- **NFR1 Performance:** API shall respond in < 500ms for dashboard queries. Detection shall process 100 flows/sec.
- **NFR2 Availability:** System shall be available 99% of the time during lab hours.
- **NFR3 Usability:** Dashboard shall be usable on mobile and desktop. No training needed for basic use.
- **NFR4 Security:** All passwords hashed, all inputs validated, no SQL injection.
- **NFR5 Maintainability:** Code shall be structured as FastAPI routers + services + models.

## 5. Data Model (Phase 1)
- **users:** id, name, email, phone, password_hash, role, created_at
- **flows:** id, src_ip, dst_ip, src_port, dst_port, protocol, packets, bytes, duration, timestamp
- **alerts:** id, flow_id, type, severity, confidence, status, created_at
- **notifications:** id, alert_id, channel (email/sms), recipient, status, sent_at

## 6. API Endpoints (Phase 1)
- POST /api/auth/login
- POST /api/flows
- GET /api/alerts
- GET /api/alerts/{id}
- PATCH /api/alerts/{id}/status
- GET /api/dashboard/summary
- GET /api/alerts/export

## 7. Assumptions & Constraints
- Phase 1 uses synthetic / lab-generated flow data, not live packet capture.
- SMS will use a free-tier provider / mock in development.
- Single server deployment (no clustering).

## 8. Future Work (Final Year Extension)
- Open-set detection: detect attack families never seen before using Mahalanobis / energy scoring.
- Continual learning: learn new attacks without forgetting old ones using class-balanced replay + distillation.
- Human-in-the-loop: analyst labels only ~6% of flows per window.
- Real dataset evaluation: CIC-IDS2017 / UNSW-NB15.

---
*End of SRS v1.0*
