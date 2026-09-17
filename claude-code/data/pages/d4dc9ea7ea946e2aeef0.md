---
url: https://docs.paloaltonetworks.com/next-gen-trust-security/next-gen-trust-security/about-vaas/integrations-overview/notification-providers-overview
fetched_at: 2026-09-16T07:25:23Z
source: palo-alto-main
---

# Notification Providers Overview Clear

Updated on 

 Fri Sep 04 10:31:48 PDT 2026 

 Focus 

 Home 

 Next‑Gen Trust Security 

 Next-Gen Trust Security 

 Next-Gen Trust Security Overview 

 Welcome to Integrations 

 Notification Providers Overview 

 Next‑Gen Trust Security 

 Notification Providers Overview 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Next-Gen Trust Security Docs 

 Getting Started 

 Previous 

 Setting Up a HashiCorp Integration 

 Next 

 Configure PagerDuty as a Notification Provider 

 Notification Providers Overview 

 Next-Gen Trust Security integrates with notification providers to deliver real-time alerts and updates about certificate lifecycle events and system health. These integrations enable you to route notifications to your preferred communication and incident management platforms, ensuring your team stays informed about critical certificate events. 

 By configuring notification providers, you enable Next-Gen Trust Security to: 

 Send alerts for certificate expiration events 

 Notify teams about certificate authority health changes 

 Deliver notifications to multiple channels simultaneously 

 Integrate certificate monitoring into existing incident response workflows 

 Notification provider integrations require initial configuration in both Next-Gen Trust Security and the target platform. Once configured, you can create notifications in the Notification Rules that route events to your chosen delivery channels. 

 Supported Notification Providers 

 The following notification platforms are supported: 

 PagerDuty – Integrates with PagerDuty incident management for on-call alerting 

 Zoom Team Chat – Sends notifications to Zoom Team Chat channels 

 Each provider requires its own connection configuration and authentication setup before notifications can be delivered. 

 How Notification Integrations Work 

 At a high level, notification provider integration follows this sequence: 

 Configure the notification platform (create services, channels, or endpoints). 

 Add the notification provider in Next-Gen Trust Security. 

 Create notifications in the Notification Rules using the provider as a delivery channel. 

 Configure event filters and recipients for each notification. 

 The specific steps vary by notification provider and platform. 

 Next Steps 

 Choose your notification provider to begin configuration: 

 Configure PagerDuty 

 Configure Zoom Team Chat 

 For information about creating notifications after configuring providers, see Notification Center overview . 

 Previous 

 Setting Up a HashiCorp Integration 

 Next 

 Configure PagerDuty as a Notification Provider
