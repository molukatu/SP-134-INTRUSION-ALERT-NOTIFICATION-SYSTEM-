# User Stories — SP-134

## Admin

- As an Admin, I want to receive an email within 60 seconds when a Critical alert happens, so I can respond immediately.
- As an Admin, I want to receive an SMS for Critical alerts, so I am notified even if I am not at my computer.
- As an Admin, I want to see total alerts today, alerts by severity, and top attacker IPs on one dashboard, so I understand the threat at a glance.
- As an Admin, I want to turn email/SMS on/off and set quiet hours, so I am not spammed at night.
- As an Admin, I want to manage users and roles (Admin, Analyst, Viewer), so only trusted people can change settings.
- As an Admin, I want to export alerts to CSV, so I can share reports with my lecturer / manager.

## Analyst

- As an Analyst, I want to see all alerts sorted by severity and time, so I handle the most dangerous ones first.
- As an Analyst, I want to filter alerts by severity, IP, date, and status, so I can find specific incidents fast.
- As an Analyst, I want to mark an alert as New / Investigating / Confirmed / False Positive / Resolved, so the team knows its state.
- As an Analyst, I want to click an alert and see the full flow details (src IP, dst IP, ports, protocol, packets, bytes), so I can investigate.
- As an Analyst, I want to upload a CSV of flows to test detection, so I can check the system without live traffic.

## Viewer

- As a Viewer, I want to view the dashboard without changing anything, so I can monitor without breaking settings.
- As a Viewer, I want to view the daily summary report, so I know what happened today.

## System

- As the System, I want to validate every flow before storing it, so bad data does not crash the database.
- As the System, I want to log every notification sent, so we can prove alerts were delivered.

## Acceptance Criteria Example

**Story:** Admin receives email for Critical alert
- GIVEN a flow is classified as Critical
- WHEN the alert is created
- THEN an email is sent within 60 seconds AND a notification log is created
