---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-posture-and-runtime-security-data-sources/container-registry-scanning/registry-components
fetched_at: 2026-08-13T15:03:57Z
source: cortex-platform
---

# Registry Components | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

Registry Components | Cortex Documentation Portal 

 ⌘ Ctrl k 

 Blog Support 
 More 

 Home 

 Products 

 Guides 

 Release Notes 

 API 

 Reference 

 AI Assistant 

 Good afternoon 
 I'm here to help you with the docs. 

 What is this page about? What should I read next? Can you give an example? 

 ⌘ Ctrl i 

 AI Based on your context 
 Send 

 Learn about Cortex XSIAM 

 Navigate the Cortex XSIAM docs 

 Get started with Cortex XSIAM 

 Agentic AI in Cortex XSIAM 

 Cortex XSIAM product licenses 

 In-product support ticket creation 

 Supported web browsers 

 Use the interface 

 Manage API keys 

 Onboard Cortex XSIAM 

 How to onboard Cortex XSIAM 

 Plan and prepare 

 Deployment steps 

 Post-deployment 

 Configure Cortex XSIAM 

 Learn how to configure Cortex XSIAM 

 Data management 

 Cortex XSIAM Data Sources and Connectors 

 What are Cortex XSIAM data sources and connectors? 

 Complete data source and connector catalog 

 Vendor-specific data sources and connectors 

 Connectors 

 Standard data sources 

 Cloud service provider (CSP) onboarding 

 Generic on-premise data collectors 

 Palo Alto Networks integrations 

 Cloud Posture and Runtime Security data sources 

 How to onboard on-premise assets to Cloud Data Security 

 How to onboard Databricks 

 How to onboard Microsoft 365 

 Ingest logs and data from Okta 

 How to onboard Snowflake 

 Activate AppSec Transporter 

 Container Registries 

 Registry Components 

 How Container Registry Scanning Works 

 Configure registry scanning for cloud accounts 

 Modify the container registry scanning scope 

 Scan re-evaluation process 

 Connect Docker Hub registry 

 Connect Docker V2 compliant container registry 

 Connect GitLab container registry 

 Connect Harbor registry 

 Connect JFrog container registry 

 Connect Sonatype Nexus registry 

 External alerts using External Issue Mapping 

 Administration and troubleshooting 

 Marketplace 

 Configure the Cortex Agentic Assistant 

 Cortex MCP server 

 Automations 

 Engines 

 Remote repository management 

 Customize cases and issues 

 XQL query management 

 Multi-Tenant 

 Managed Services configuration in Cortex 

 Protect your endpoints 

 Endpoint security 

 Endpoint DLP 

 Detect, Investigate, and respond to threats 

 Monitor dashboards and reports 

 Investigation and response 

 Agentic Assistant chat 

 Asset management 

 Threat management 

 Attack surface management 

 Vulnerability management 

 Exposure management 

 Cortex Advanced Email Security 

 Identity Threat Detection and Response (ITDR) 

 Cloud Security 

 Monitor and track compliance adherence 

 Cloud security rules and policies 

 Cortex Cloud Data Classification 

 Cortex Data Security 

 Cloud Identity Security 

 Network exposure detection 

 Cortex Cloud SaaS Security 

 Cortex Cloud AI Security 

 Serverless function posture security 

 Cortex Cloud Application Security 

 Cloud workload policies and rules 

 Base image rules 

 Web and API Security (WAAS) 

 Serverless function runtime security 

 Reference and developer docs 

 Cortex XSIAM XQL 

 Graph Search 

 Cortex CLI 

 Role-Based Access Control 

 API documentation 

 Reference 

 Migrating to a new Broker VM image 

 Learn more about migrating to the latest broker VM image 

 Standalone Broker VM 

 Broker VM high availability cluster node 

 On this page 

 For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSIAM 

 Cortex XSIAM Documentation 

 Configure Cortex XSIAM 

 Cortex XSIAM Data Sources and Connectors 

 Cloud Posture and Runtime Security data sources 

 Container Registries 

 Registry Components 

 To understand how container registry scanning works, it's essential to understand its core components: 

 Container registry: A container registry is a service for publishing, maintaining, and securely distributing container images, providing a centralized hub for managing and accessing containerized application components across your organization. This scanning helps to enable proactive identification and remediation of security risks before deployment which means you will be using only trusted and compliant images in production environments. 

 Container image repository: Within a container registry, container images are organized into multiple repositories to improve management, access control, collaboration, and security isolation. Each repository should ideally contain images related to a specific application, service, or project, allowing for granular permissioning and security policies. Images within a repository often share a common base image or purpose, making it easier to apply consistent security controls across related components. 

 Image Tags: Image tags are essential for identifying and managing container image versions within a repository, enabling the selection and deployment of appropriate builds. From a security perspective, tags facilitate tracking vulnerable images, deploying patched versions, and maintaining image provenance for auditing. While human-readable tags like myapp:latest (reassignable) and myapp:v1.0.0 are common, using immutable tags such as myapp@sha256:abc123 provides a cryptographically secure and verifiable reference. There are two common formats for referencing image tags: 

 image:tag – A human-readable label that can be reassigned to different versions. For example, myapp:latest or myapp:v1.0.0. 

 image@sha – A cryptographic hash that provides an immutable reference to a specific image version. For example, myapp@sha256:abc123. 

 Image Digest: A cryptographic digest (SHA-256 hash) uniquely identifies a container image's content, providing a strong guarantee of immutability. Unlike user-defined image tags, which can be reassigned, using the digest as a tag ensures that even if an image is renamed or retagged, its content remains verifiably identical, making it a critical element for security auditing and ensuring the integrity of deployed applications. Relying on image digests helps prevent potential supply chain attacks where malicious actors might attempt to replace images with compromised versions. 

 Previous Container Registries Next How Container Registry Scanning Works 

 Last updated 15 days ago 

 Was this helpful? 

 ‍ 

 Trust Center 

 ‍ 

 Privacy 

 ‍ 

 Terms of Use 

 ‍ 

 Legal 

 © 2026 Palo Alto Networks, Inc. All rights reserved. 

 Was this helpful?
