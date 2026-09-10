---
url: https://docs.koi.ai/integration-guides/remote-development-environments/sagemaker-preview
fetched_at: 2026-09-06T09:19:40.120Z
source: koi-official-browser
capture_method: authenticated official browser
---

# SageMaker [Preview]

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
DocumentationIntegration GuidesRemote Development Environments
SageMaker [Preview]

Amazon SageMaker is AWS's managed machine learning platform for building, training, and deploying AI and machine learning models. Organizations use SageMaker to develop custom AI applications and host production inference endpoints at scale.

Koi provides native support for Amazon SageMaker, enabling organizations to discover and continuously assess the security posture of SageMaker-hosted AI assets.

Koi Support for SageMaker

By deploying the SageMaker Endpoint Integration, you can enable:

Discovery of supported SageMaker AI assets.

AI-native risk analysis and security findings.

Continuous inventory and monitoring of deployed assets.

Discovered SageMaker assets are processed through Koi's standard risk pipeline and are available throughout the product, including inventory views, dashboards, reports, and APIs.

For deployment instructions, see Deploy the SageMaker Endpoint Integration.

Prevention

Prevention is supported separately through the Koi Network Integration.

SageMaker Deployment 

Koi supports two deployment components for Amazon SageMaker. Both integrations are deployed using Amazon SageMaker Lifecycle Configuration, which automatically configure the SageMaker environment during startup.

SageMaker Endpoint Integration – Enables discovery, inventory, and AI-native risk assessment of your SageMaker AI assets.

Network Integration – Enables prevention by routing traffic through Koi to enforce AI security policies.

You can deploy the Endpoint Integration on its own, or add the Network Integration for complete visibility and prevention.

Requirements

Access to the Koi console.

Permission create and attach lifecycle configurations on AWS. 

SageMaker Endpoint Integration

In Koi platform, navigate to Settings > Deployment.

Under Endpoints deployment click Deploy new script

On the endpoint deployment modal, under Generate Script choose: 

Deployment method: Amazon SageMaker

OS: Linux

Installation method: Agentless 

Type: Script package

Set the Version updates toggle by acording to your preference. 

Press next and download the script. 

Follow the deployment steps:

SageMaker Network Integration

From the deployment page, select Network Integration.

Set up your network integration and select the Amazon SageMaker Deployment Method. 

Follow the routing steps:




Previous
Deploying Koi on Coder workspaces
Next
Okta integration

Last updated 1 month ago
