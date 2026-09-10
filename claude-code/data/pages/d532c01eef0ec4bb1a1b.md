---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/cloud-posture-and-runtime-security-data-sources/container-registry-scanning/registry-components
fetched_at: 2026-09-06T09:28:13Z
source: cortex-platform
---

# Registry Components | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

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

 Cortex XSIAM Data Ingestion 

 Registry Components 

 Learn about the container registry components that Cortex XSIAM uses for registry scanning. 

 To understand how container registry scanning works, it's essential to understand its core components: 

 Container registry: A container registry is a service for publishing, maintaining, and securely distributing container images, providing a centralized hub for managing and accessing containerized application components across your organization. This scanning helps to enable proactive identification and remediation of security risks before deployment which means you will be using only trusted and compliant images in production environments. 

 Container image repository: Within a container registry, container images are organized into multiple repositories to improve management, access control, collaboration, and security isolation. Each repository should ideally contain images related to a specific application, service, or project, allowing for granular permissioning and security policies. Images within a repository often share a common base image or purpose, making it easier to apply consistent security controls across related components. 

 Image Tags: Image tags are essential for identifying and managing container image versions within a repository, enabling the selection and deployment of appropriate builds. From a security perspective, tags facilitate tracking vulnerable images, deploying patched versions, and maintaining image provenance for auditing. While human-readable tags like myapp:latest (reassignable) and myapp:v1.0.0 are common, using immutable tags such as myapp@sha256:abc123 provides a cryptographically secure and verifiable reference. There are two common formats for referencing image tags: 

 image:tag – A human-readable label that can be reassigned to different versions. For example, myapp:latest or myapp:v1.0.0. 

 image@sha – A cryptographic hash that provides an immutable reference to a specific image version. For example, myapp@sha256:abc123. 

 Image Digest: A cryptographic digest (SHA-256 hash) uniquely identifies a container image's content, providing a strong guarantee of immutability. Unlike user-defined image tags, which can be reassigned, using the digest as a tag ensures that even if an image is renamed or retagged, its content remains verifiably identical, making it a critical element for security auditing and ensuring the integrity of deployed applications. Relying on image digests helps prevent potential supply chain attacks where malicious actors might attempt to replace images with compromised versions. 

 Previous Container Registries 

 Next How Container Registry Scanning Works 

 Last updated 1 month ago 

 Was this helpful?
