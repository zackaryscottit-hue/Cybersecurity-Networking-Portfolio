
# Network Access Control (NAC) & Zero Trust

## Project Overview

Deployed and configured a Network Access Control (NAC) lab to explore device authentication, network segmentation, and Zero Trust security principles.

The objective was to control network access, separate corporate and guest devices, and evaluate centralized authentication using LDAP.

## Technologies Used

- PacketFence NAC
- pfSense Firewall
- VMware Workstation
- OpenLDAP
- VLANs
- Captive Portal
- Windows Client VM

## Project Implementation

### Phase A: NAC Architecture
- Designed a network architecture separating corporate and guest devices.
- Identified authentication, authorization, and network isolation requirements.
- Evaluated Zero Trust principles for controlling network access.

### Phase B: PacketFence Deployment
- Deployed the PacketFence virtual appliance.
- Completed the initial configuration wizard.
- Accessed the PacketFence administrative web interface.

### Phase C: Network Segmentation
- Configured VLAN 10 for corporate devices.
- Configured VLAN 20 for guest devices.
- Implemented pfSense firewall rules to control network communication.
- Configured a captive portal for guest access.

### Phase D: Authentication and Validation
- Configured an LDAP authentication source using OpenLDAP.
- Tested NAC registration and authentication settings.
- Investigated connectivity issues affecting LDAP authentication.
- Reviewed device registration and access control behavior.

## Skills Demonstrated

- Network Access Control (NAC)
- Zero Trust security concepts
- VLAN segmentation
- Firewall configuration
- Captive portal administration
- LDAP integration
- Network troubleshooting
- Access control policy management

## Project Evidence

Screenshots of PacketFence deployment, VLAN configuration, authentication settings, and network access validation will be added here.

## Key Takeaways

This project strengthened my understanding of how Network Access Control solutions can improve enterprise security through device visibility, authentication, and network segmentation.

It also provided practical experience troubleshooting authentication and connectivity issues in a virtualized environment.

All testing was performed in an authorized lab environment.
