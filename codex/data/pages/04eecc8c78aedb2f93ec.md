---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/model-security-to-secure-your-ai-models/get-started-with-ai-model-security/scanning-models
fetched_at: 2026-08-13T14:05:22Z
source: ai-security
---

# Scanning Models Clear

Scanning Models 

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

 Scanning Models 

 Updated on 

 Jul 31, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Updated on 

 Jul 31, 2026 

 Focus 

 Home 

 Prisma AIRS 

 Secure Your AI Models with AI Model Security 

 Get Started with AI Model Security 

 Scanning Models 

 Download PDF 

 Prisma AIRS 

 Scanning Models 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma AIRS Docs 

 Activation & Onboarding 

 Administration 

 AI Model Security 

 AI Red Teaming 

 Release Notes 

 New Features 

 Previous 

 Custom Rules 

 Next 

 Organize Security Scans with Custom Labels 

 Scanning Models 

 Scan a Hugging Face model, local model, or object storage model using
 CLI/SDK. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Model Security) 

 Prisma AIRS AI Model Security License 

 Once your Security Group is configured, you can scan models through
 either the CLI or Python SDK. The process varies slightly depending on whether you're
 scanning Hugging Face AI models or local models. 

 While scanning a model using Python SDK: 
 you will need to use ModelSecurityAPIClient which is the base
 object to perform API calls. 

 you can configure the base_url using environment variables or
 in your code. 

 When you scan using SDK, it's your responsibility to enforce allow or block decisions
 according to the scan evaluation outcomes. 

 When you scan using CLI, the CLI will exit with a non-zero exit code if the model is
 unsafe. 

 AI Model Security can handle up to 1,000 files per scan. 

 You cannot delete a scan. 

 Scan a Hugging Face Model 

 Scan a Local Model 

 Scan a Model from Object Storage 

 Customize Model Scans 

 Scan a Hugging Face Model 

 Scan a model hosted on Hugging Face. 

 Scan a Hugging Face Model 

 To scan a model hosted on Hugging Face, provide the model URI and your security group
 UUID. For Hugging Face AI models, only model_uri is required. 

 Before you start the model scanning
 process: 
 Ensure that the security group source type must match the source of the
 model that you are scanning. For example, you cannot use a S3 security group
 on a Hugging Face. 

 Verify and ensure that HuggingFace.co domain (https://huggingface.co/) is
 allowed. 

 Ensure that the ignore_patterns and
 allow_patters do not overlap with each other. 

 We don’t support private Hugging Face repositories. You can only scan public Hugging
 Face repositories. If you want to scan private Hugging Face repository, then you can
 download the model and scan it using local model scan. 

 When creating a scan, you can attach up to 50 custom labels
 to help organize your scans . 

 Scan using CLI 

 model-security scan \
 --security-group-uuid "12345678-1234-1234-1234-123456789012" \
 --model-uri "https://huggingface.co/microsoft/DialoGPT-medium" \
 -l env=production 

 Scan using Python SDK 

from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient (
 base_url="https://api.sase.paloaltonetworks.com/aims"
)

result = client.scan (
 security_group_uuid="12345678-1234-1234-1234-123456789012",
 model_uri="https://huggingface.co/microsoft/DialoGPT-medium",
 labels={ "env": "production" }
)

print(f"Scan completed: {result.eval_outcome}") 

 The AI Model Security automatically fetches the latest version from Hugging Face. To
 scan a specific version, include the version parameter. 

 Scan using CLI 

model-security scan \
 --security-group-uuid "12345678-1234-1234-1234-123456789012" \
 --model-uri "https://huggingface.co/microsoft/DialoGPT-medium" \
 --model-version "7b40bb0f92c45fefa957d088000d8648e5c7fa33" 

 Scan using Python SDK 

from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient (
 base_url="https://api.sase.paloaltonetworks.com/aims"
)
result = client.scan (
 security_group_uuid="12345678-1234-1234-1234-123456789012",
 model_uri="https://huggingface.co/microsoft/DialoGPT-medium",
 model_version="7b40bb0f92c45fefa957d088000d8648e5c7fa33"
) 

 Filter Files in Hugging Face Scans 

 Large Hugging Face repositories may contain files you don't need to scan. Use global
 patterns to include or exclude specific files. 

 Scan using CLI 

model-security scan \
 --security-group-uuid "12345678-1234-1234-1234-123456789012" \
 --model-uri "https://huggingface.co/microsoft/DialoGPT-medium" \
 --allow-patterns "*.bin" "*.json" \
 --ignore-patterns "*.md" "*.txt" 

 Scan using Python SDK 

from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient (
 base_url="https://api.sase.paloaltonetworks.com/aims"
)
result = client.scan (
 security_group_uuid="12345678-1234-1234-1234-123456789012",
 model_uri="https://huggingface.co/microsoft/DialoGPT-medium",
 allow_patterns=["*.bin", "*.json"],
 ignore_patterns=["*.md", "*.txt"]
)

 Scan a Local Model 

 Scan a model that is stored locally. 

 Scan a Local Model 

 For models stored locally, specify the path to the model directory. To scan a model
 from the local disk, only model_path is required. 

 Before you start the model scanning
 process: 
 Ensure that the security group source type must match the source of the
 model that you are scanning. For example, you cannot use a Hugging Face
 security group on a local model. If you don’t provide any model URI, then by
 default local disk source type is used. 

 Validate that the model path points to the correct storage location. 

 The ignore_patterns and allow_patters 
 is not applicable for local model scans. 

 Running a model scan can consume up to 4GB memory depending on the size and
 type of the model. Therefore, ensure that the environment used for the
 scanning has sufficient resources. Verify if you've enough space to download
 and sàve the model being scanned. 

 Use model_path to specify the local disk location for
 models. 

 When creating a scan, you can attach up to 50 custom labels
 to help organize your scans . 

 Scan using CLI 

model-security scan \
 --security-group-uuid "12345678-1234-1234-1234-123456789012" \
 --model-path "path/to/local/model" \
 -l env=production 

 Scan using Python SDK 

from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient (
 base_url="https://api.sase.paloaltonetworks.com/aims"
)
result = client.scan (
 security_group_uuid="12345678-1234-1234-1234-123456789012",
 model_path="path/to/local/model",
 labels={ "env": "production" }
) 

 Scan a Model from Object Storage 

 Scan a model from object storages like Amazon S3, Google Cloud Storage, Azure Blob
 Storage, JFrog Artifactory, and Gitlab Model Registry. 

 Scan a Model from Object Storage 

 We support object storages Amazon S3, Google Cloud Storage, Azure Blob Storage, JFrog
 Artifactory, and Gitlab Model Registry. To scan an AI model from these cloud storage
 models, provide the URL of these models as model_uri parameter
 while calling the scan on the SDK. 

 The model security SDK will perform the download for you and queue the model for
 scan. 

 When creating a scan, you can attach up to 50 custom labels
 to help organize your scans . 

 Scan using CLI 

model-security scan \
 --security-group-uuid "12345678-1234-1234-1234-123456789012" \

 --model-uri "<model_uri>" \
 --model-name "production-classifier" \
 --model-author "ml-team" \
 --model-version "v2.1" \
 -l env=production

 Scan using Python SDK 

from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient (
 base_url="https://api.sase.paloaltonetworks.com/aims"
)
result = client.scan (
 security_group_uuid="12345678-1234-1234-1234-123456789012",

 model_uri="<model_uri>",
 model_name="production-classifier",
 model_author="ml-team",
 model_version="v2.1",
 labels={ "env": "production" }
) 

 The model_uri parameter must use the format of supported cloud
 storage platforms: 

 Amazon S3 ( s3:// ) 

 Google Cloud Storage ( gs:// ) 

 Azure Blob Storage
 ( https://[account].blob.core.windows.net/ ) 

 JFrog Artifactory ( https://[instance].jfrog.io/ ) 

 GitLab Model Registry
 ( https://[gitlab-instance]/-/ml/models/ ) 

 The CLI shows scan results in real-time as they finish. Each scan tests the model
 against all active rules in your Security Group. The output shows whether the model
 passes or fails based on your rule configuration. 

 A model fails if any blocking rule detects a violation. Non-blocking rules record
 findings without preventing the model from being approved. 

 Customize Model Scans 

 Customize your AI model scans. 

 Customize Model Scans 

 You can configure scan execution and adjust result timeout settings. 

 Customize Scan using CLI 

model-security scan \
 --security-group-uuid "12345678-1234-1234-1234-123456789012" \
 --model-uri "<model_uri>" \
 --poll-interval-secs 10 \
 --poll-timeout-secs 900 \
 --download-timeout-secs 1800 \ # Object storage download timeout
 --download-dir "/custom/download/path"\ # Object storage download location
 --cleanup-download-dir \ # Cleanup downloads after scan
 --block-on-errors

 Customize Scan using Python SDK 

from model_security_client.api import ModelSecurityAPIClient

# Initialize the client with download configuration
client = ModelSecurityAPIClient (
 base_url="https://api.sase.paloaltonetworks.com/aims",
 download_timeout_secs=1800, # Object storage download timeout
 download_dir="/custom/download/path", # Object storage download location
 cleanup_download_dir=True # Cleanup downloads after scan
)

# Perform scan with polling configuration
result = client.scan (
 security_group_uuid="12345678-1234-1234-1234-123456789012",
 model_uri="<model_uri>",
 poll_interval_secs=10,
 poll_timeout_secs=900,
) 

 Following are the configuration options to customize the scan for AI models. 

 Configuration Option Description Default Value 

 download_timeout_secs ( Object storage scans only ) Specify the timeout duration
 for model downloads from cloud storage. 600 seconds 

 download_dir ( Object storage scans only ) Specify the destination
 directory for downloading models from object storage. ~/.cache/airsms/ 

 cleanup_download_dir ( Object storage scans only ) Remove downloaded models
 after scanning to conserve disk space. False 

 poll_interval_secs Specify the frequency of scan status checks. 5 seconds 

 poll_timeout_secs Specify the maximum wait time for scan completion. 600 seconds 

 block_on_errors ( CLI only ) CLI exits with an error code when scan
 errors occurs. NA 

 Previous 

 Custom Rules 

 Next 

 Organize Security Scans with Custom Labels 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 Next-Generation Firewalls 

 CN-Series 

 Firewalls 

 VM-Series 

 Cloud-Delivered Security Services 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Enterprise DLP 

 Network Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 AI Model Security 

 Prisma AIRS 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
