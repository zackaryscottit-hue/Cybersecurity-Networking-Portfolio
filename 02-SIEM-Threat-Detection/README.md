# SIEM Implementation & Threat Detection

## Project Overview

Deployed and configured a Security Information and Event Management (SIEM) lab to collect, monitor, and analyze security events from Windows and Linux systems.

The objective was to improve threat visibility, investigate suspicious authentication activity, create security dashboards, and practice event correlation.

## Technologies Used

- Wazuh
- Kibana
- Windows Sysmon
- Windows Event Logs
- Winlogbeat
- Ubuntu Linux
- VMware Workstation

## Project Implementation

### Phase A: SIEM Deployment
- Configured Wazuh on an Ubuntu virtual machine.
- Connected a Windows endpoint for security event collection.
- Configured Sysmon to capture detailed endpoint activity.

### Phase B: Log Collection & Analysis
- Collected Windows security events and Sysmon telemetry.
- Investigated failed login attempts.
- Examined PowerShell execution activity and suspicious processes.

### Phase C: Security Dashboards & Alerting
- Created Kibana visualizations for:
  - Top source IP addresses
  - Failed login attempts over time
  - PowerShell execution activity
- Configured an alert for repeated authentication failures.
- Investigated why the alert threshold was not reached during testing.

### Phase D: Event Correlation
- Developed a correlation query to identify process execution and related network activity within a five-minute window.
- Validated matching security events.
- Documented correlation results for further analysis.

## Skills Demonstrated

- SIEM deployment and configuration
- Centralized log collection
- Windows endpoint monitoring
- Security event investigation
- Dashboard creation
- Detection rule configuration
- Event correlation and troubleshooting

## Project Evidence

Screenshots of SIEM dashboards, alert configurations, and event correlation results will be added here.

## Key Takeaways

This project strengthened my understanding of how security operations teams collect and analyze endpoint telemetry, investigate suspicious behavior, and improve detection capabilities through centralized monitoring.

All testing was conducted in an authorized virtual lab environment.
