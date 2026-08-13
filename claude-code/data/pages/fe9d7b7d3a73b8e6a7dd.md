---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/ion-cli-reference/use-cli-commands/dump-commands/dump-service-link-summary
fetched_at: 2026-08-13T17:30:35Z
source: palo-alto-main
---

# dump servicelink summary Clear

dump servicelink summary 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 dump servicelink summary 

 Updated on 

 Jun 2, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Jun 2, 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Use CLI Commands 

 Dump Commands 

 dump servicelink summary 

 Download PDF 

 Prisma SD-WAN 

 dump servicelink summary 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 dump serviceendpoints 

 Next 

 dump servicelink stats 

 dump servicelink summary 

 Use the dump servicelink summary command
to display information on standard VPNs. Information includes the
name of the standard VPN, status, parent interface, extended state
of the VPN, IP addresses of the local and standard VPN endpoints,
Type (GRE or IPsec), and the IPsec profile. 

 Command 

 dump servicelink summary ( all | sltype=) 

 Options 

 all Enter all to display summary of all the standard
VPNs. 

 sltype Enter type to view the summary of all the standard
VPNs matching the type. 

 Command Notes 

 Role Super, Read Only, Monitor 

 Related Commands 

 dump servicelink stats 

 dump servicelink status 

 Introduced in Release 4.7.1 

 Example 

 dump servicelink summary all
 -------------- SERVICE LINKS ----------------------------------
 Total : 2
 TotalUP : 1
 TotalDown : 1
 ---------------------------------------------------------------
 SlDev SlName Status ExtState ParentDev LocalIP Peer Type IpsecProfile
 ---------------------------------------------------------------
 sl2 Gre down gre_keepalive_configured eth3 10.9.18.209 10.9.18.36 GRE N/A
 sl1 ubuntu up tunnel_up eth3 10.9.18.209 10.9.18.35 IPsec Ubuntu 

 dump servicelink summary all
-------------- SERVICE LINKS ----------------------------------
Total : 2
TotalUP : 0
TotalDown : 2
---------------------------------------------------------------
Vrf SlDev SlName Status ExtState ParentDev LocalIP Peer Type IpsecProfile 
---------------------------------------------------------------
blue sl2 service_link-1709200539046021828 down peer_address_unresolved eth2 70.0.0.1 IPsec ZSCALER_IKEV2 

green sl1 service_link-1704789489196015028 down proposal_mismatch_ike eth2 70.0.0.1 70.0.0.2 IPsec ZSCALER_IKEV2 

dump servicelink summary sltype=ipsec 
-------------- SERVICE LINKS ----------------------------------
Total : 2
TotalUP : 0
TotalDown : 2
---------------------------------------------------------------
Vrf SlDev SlName Status ExtState ParentDev LocalIP Peer Type IpsecProfile 
---------------------------------------------------------------
green sl1 service_link-1704789489196015028 down retransmit_send eth2 70.0.0.1 255.255.255.0 IPsec ZSCALER_IKEV2 

blue sl2 service_link-1709200539046021828 down peer_address_unresolved eth2 70.0.0.1 IPsec ZSCALER_IKEV2 

 dump servicelink summary sltype=gre 
-------------- SERVICE LINKS ----------------------------------
Total : 0
TotalUP : 0
TotalDown : 0
---------------------------------------------------------------
Vrf SlDev SlName Status ExtState ParentDev LocalIP Peer Type IpsecProfile 
--------------------------------------------------------------- 

 The ExtState in
the command output displays the status of the standard VPN. The
following table describes the various reasons for the VPN tunnel
down status: 

 Extended State Description 

 liveliness_failed If the liveliness is configured and if probe
does not get the response through the tunnel, the tunnel manager
marks the tunnel down with the extended status as liveliness failed. 

 parent_no_ip The underlay parent interface on which the
standard VPN tunnel is configured does not have the IP address. 

 peer_address_unresolved If there is no peer IP address to use. 

 invalid_service_endpoint Service endpoint configured is not present. 

 peer_auth_failed Peer authentication failed. 

 parse_error If the control message parsing failed during
tunnel bring up. 

 cert_expired If the certificates are expired. 

 cert_revoked If the certificates are revoked. 

 no_issuer_cert No Issuer certificate found. 

 retransmit_send_timeout If no response is seen from the remote. 

 proposal_mismatch_ike Proposal mismatch in phase-1. 

 proposal_mismatch_child Proposal mismatch in phase-2. 

 admin_down Service link is admin down. 

 StandbySpoke Spoke is Stand up. 

 bringup_wait Scenarios to move to this state: 

 After
unloading the VPN connection. 

 If the load connection request fails. 

 If the terminate SA request fails. 

 bring up When the config is complete and trying to bring
up the connection. 

 hold_down When the tunnel flaps 3 times with in 120 sec
(2 min), we mark the tunnel to be in hold downstate. 

 internal_resource_unavailable Parsing psk failed in tunnelmgr. 

 duplicate_endpoints Already a tunnel is UP with the same Source
and Remote IP. 

 local_auth_failed Received authentication failed. 

 peer_auth_failed Detected authentication failed. 

 parse_error Parsing control message failed. 

 retransmit_send_timeout No reply from peer retry in progress. 

 half_open_timeout Timeout for negotiating child sa in phase2. 

 proposal_mismatch_ike Phase1 proposal mismatch (ike). 

 proposal_mismatch_child Phase2 proposal mismatch (ipsec). 

 transform_selector_mismatch Phase2 selectors mismatch (ipsec). 

 install_child_sa_failed Installing child sa failed. 

 install_child_policy_failed Installing child policy failed. 

 authorization_failed When explicit authorization rules are defiled
(remote identity). 

 cert_expired When the certificate is expired. 

 cert_revoked Certificate is revoked. 

 no_issuer_cert No issuer certificate found. 

 unique_replace Session is uniquely identified uniquely. 

 unique_keep Keep the session with unique ids. 

 vip_failure Virtual interface creation failed. 

 retransmit_send No reply from peer, hence retry in progress. 

 standby_spoke Standby spoke. 

 lowerlayerdown Lower layer is down. 

 liveliness_configured When the tunnel comes up and if liveliness
is configured. 

 tunnel_bringup_up_wait When the tunnel is in bringup wait state. 

 tunnel_bringup When the tunnel is in bringup state (loading
the config to charon). 

 multiple_ike_session When tunnel is reset because of multi ike. 

 invalid_auth_param When the secret is invalid. 

 config_changed Configuration was updated. 

 load_failed Loading the configuration failed. 

 gre_keepalive_configured GRE keepalive is configured. 

 Previous 

 dump serviceendpoints 

 Next 

 dump servicelink stats 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 SASE 

 CLI 

 Reference 

 Prisma SASE 

 Prisma SD-WAN ION CLI Reference 

 Prisma SD-WAN 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
