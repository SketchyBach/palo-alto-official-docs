---
url: https://docs.paloaltonetworks.com/best-practices/zero-trust-best-practices/zero-trust-best-practices/the-five-step-methodology/step-1-asset-discovery-and-prioritization
fetched_at: 2026-08-13T15:30:35Z
source: palo-alto-main
---

# Step 1: Asset Discovery and Prioritization Clear

Step 1: Asset Discovery and Prioritization 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Best Practices Implementing Zero Trust with Palo Alto Networks 

 : 
 Step 1: Asset Discovery and Prioritization 

 Updated on 

 Fri Jan 26 17:49:21 PST 2024 

 Focus 

 Download PDF 

 Filter

 Expand all | Collapse all 

 Zero Trust Best Practices 

 What Is Zero Trust and Why Do I Need It? 

 High-Level Zero Trust Best Practice Concepts 

 How Do I Start My Zero Trust Implementation? 

 The Five Steps to Approaching Zero Trust 

 Step 1: Asset Discovery and Prioritization 

 Step 2: Map and Verify Transactions 

 Step 3: Standards and Designs 

 Step 4: Implementation 

 Step 5: Report and Maintenance 

 Zero Trust Resources 

 Updated on 

 Fri Jan 26 17:49:21 PST 2024 

 Focus 

 Home 

 Best Practices 

 Best Practices Implementing Zero Trust with Palo Alto Networks 

 Zero Trust Best Practices 

 The Five Steps to Approaching Zero Trust 

 Step 1: Asset Discovery and Prioritization 

 Download PDF 

 Best Practices Implementing Zero Trust with Palo Alto Networks 

 Step 1: Asset Discovery and Prioritization 

 Table of Contents 

 Filter

 Expand all | Collapse all 

 Zero Trust Best Practices 

 What Is Zero Trust and Why Do I Need It? 

 High-Level Zero Trust Best Practice Concepts 

 How Do I Start My Zero Trust Implementation? 

 The Five Steps to Approaching Zero Trust 

 Step 1: Asset Discovery and Prioritization 

 Step 2: Map and Verify Transactions 

 Step 3: Standards and Designs 

 Step 4: Implementation 

 Step 5: Report and Maintenance 

 Zero Trust Resources 

 Step 1: Asset Discovery and Prioritization 

 Identify assets that are valuable to your business so
you can prioritize what you need to protect first. 

 To protect your assets and ensure normal business operation,
you need to know what those assets are and how they are used so
that you can: 

 Understand exactly which users, devices/infrastructure,
applications, data, and services are part of your network or have
access to your network. Understand the different access requirements
of different user groups and key individual users. 

 Prioritize how you roll out Zero Trust to protect those assets. 

 You can’t protect assets that you don’t know exist. When you
identify all assets in all locations (on-premises, cloud, remote,
third-party, etc.), you can protect all assets. Unknown users, applications,
and infrastructure, including unmanaged IoT devices, are potential
security vulnerabilities. Discovering internet-connected IoT devices
may reveal devices that are vulnerable to attack—not only expected
devices such as printers, cameras, and other unmanaged terminals,
but also unexpected internet-connected devices such as coffee mug
warmers and personal fans. 

 How you prioritize what to protect first depends on several factors: 

 What is important to your business and critical to running
your business? Different businesses place different values on different
assets. Evaluate your infrastructure, applications, and other assets to
identify what is important to your business. 

 Industry standards and local regulations such as General
Data Protection Regulation (GDPR), the Health Insurance Portability
and Accountability Act (HIPAA), and payment card industry (PCI)
standards. 

 Evaluation of the sensitivity if an asset is exposed: 

 Low sensitivity assets—Exposure causes limited harm to the
enterprise. For example, non-critical data and applications with
limited user bases that don’t access critical data or infrastructure. 

 Moderate sensitivity assets—Exposure risks serious harm to
the enterprise or its customers. For example, business data and
applications, email, voice, and video communication, and infrastructure and
services whose compromise impacts the enterprise. 

 High sensitivity assets—Exposure causes severe harm to the
enterprise or its customers. For example, information theft that
requires a breach notification, personally identifiable information
(PII), critical intellectual property such as code, designs, architectures,
etc., critical infrastructure such as the enterprise’s public key
infrastructure (PKI) and critical servers, and critical services
such as Active Directory (AD), DNS, and DHCP. 

 Palo Alto Networks Zero Trust Advisory Service can
help you prioritize your Zero Trust rollout with advisory and roadmap
services and can help you design and implement your Zero Trust deployment. 

 Start the transition with your most valuable assets, which are
often in your data center or in the cloud, where you store source
code, customer data, and other business-critical, proprietary assets. 

 Use the following methods to gain visibility into traffic and
help identify users, applications, and infrastructure: 

 The Cloud Identity Engine (CIE) aggregates
identity information across IAMs, User-ID identifies users
and user groups, and Device-ID identifies IoT/unmanaged
devices. 

 The team’s knowledge of the business. For example, business
leaders can speak to the strategic value of applications. 

 Insert one or more next-generation firewalls transparently
into your network in virtual wire (vwire) mode,
which is a passthrough mode that requires no topology changes because
vwire interfaces don’t have IP or MAC addresses, to gain visibility
into traffic. Check Traffic logs to view and
analyze traffic. If you have managed firewalls, use Panorama logs. 

 View logs in Strata Logging Service and use
 third-party asset discovery tools that work with Strata Logging Service from one of Palo Alto Networks’ integrated partners . 

 Use SaaS Security API to discover
users, assets, and data for SaaS applications and gain visibility into those applications . 

 Use Policy Optimizer to help
identify key applications on existing Security policy rules. (Policy
Optimizer even shows you all of the applications on port-based rules.) 

 Use Application Dependency Mapping tools to discover application
dependencies (the resources an application uses, such as databases,
load balancers, servers, etc.) automatically. 

 Previous 

 The Five Steps to Approaching Zero Trust 

 Next 

 Step 2: Map and Verify Transactions 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
