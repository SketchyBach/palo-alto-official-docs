---
url: https://docs.prismacloud.io/content-collections/search-and-investigate/c2c-tracing-vulnerabilities
fetched_at: 2026-09-16T13:35:11Z
source: prisma-cloud
---

# Code to Cloud Tracing for Vulnerabilities | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Search and Investigate 

 Code to Cloud Tracing for Vulnerabilities 

 The unified Vulnerability Explorer can identify a vulnerability in container images deployed in runtime and trace it back to it’s source in code repositories. 

 Overview 

 Traditional vulnerability scanners provide a list of vulnerabilities and the underlying binaries introducing them, after which you need to find out how to properly update the vulnerable packages and to which version. Prisma Cloud goes beyond what traditional scanners can do by allowing you to find exactly how a vulnerability was introduced into your container images. 

 The Code to Cloud (C2C) tracing engine relies on the unique set of data available to Prisma Cloud in order to identify all the vulnerabilities found on a runtime container image, match which registry image was used in the deployment, discover what pipeline was used to build it and from there, identify which Dockerfile contains the instructions to build the image, and the Package Manager file and packages pulled into it and it’s Base Image. 

 Finally, Prisma Cloud scans all the source components to find which ones have the same vulnerability found in runtime and builds the trace. 

 How C2C Tracing Works 

 For a given deployed container, Prisma Cloud determines the corresponding Image Registry from which the image is deployed. 

 From the image in the Image Registry, Prisma Cloud finds the CI/CD pipeline and CI jobs that have built the image and the code repository that triggered the CI/CD pipeline. 

 Prisma Cloud further determines the corresponding Dockerfile or Package Manager (if applicable) and it’s associated packages, which are vulnerable to the CVE under analysis. 

 If the base image is found to be vulnerable to the CVE under analysis, Prisma Cloud presents it in the graph. 

 Prerequisites 

 Make sure that you fulfill the following prerequisites: 

 Repositories are onboarded on to Prisma Cloud (only organizations are supported). 

 CI/CD systems are onboarded on to Prisma Cloud. 

 Ingested pipelines are being used to build the container images used in the production environments. 

 Registry images are scanned for vulnerabilities. 

 Runtime workloads are scanned for vulnerabilities using agentless or agent-based scanning. 

 Vulnerability policies are configured . 

 Previous Application Query Examples 

 Next Use Vulnerabilities Tracing on Investigate 

 Last updated 1 month ago 

 Was this helpful?
