---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/model-security-to-secure-your-ai-models/manage-ai-model-versions-using-content-based-fingerprinting
fetched_at: 2026-08-13T14:05:48Z
source: ai-security
---

# Manage AI Model Versions Using Content-Based Fingerprinting  Clear

Manage AI Model Versions Using Content-Based Fingerprinting 

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

 Manage AI Model Versions Using Content-Based Fingerprinting 

 Updated on 

 Fri Jul 31 13:38:14 PDT 2026 

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

 Fri Jul 31 13:38:14 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 Secure Your AI Models with AI Model Security 

 Manage AI Model Versions Using Content-Based Fingerprinting 

 Download PDF 

 Prisma AIRS 

 Manage AI Model Versions Using Content-Based Fingerprinting 

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

 Understanding Model Security Scan Results 

 Next 

 Understanding Model Security Rules 

 Manage AI Model Versions Using Content-Based Fingerprinting 

 Use content-based fingerprinting to uniquely identify, track, and manage AI model
 versions across cloud and local environments in AI Runtime Security. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Model Security) 

 Prisma AIRS AI Model Security License 

 When you scan an AI model, AI Model Security acts as a centralized registry that catalogs
 your model alongside its scan results to maintain a persistent identity. Within this
 system, a model serves as a namespace for its various versions, which you establish by
 providing a specific model display name during the scanning process. If you scan the
 exact same model but provide a different display name during each scan, the system will
 treat them as entirely separate model and model version entities. 

 To accurately track your models as they evolve or move across different environments, AI
 Model Security calculates a unique fingerprint based purely on the content of the model
 artifacts rather than relying on fragile storage locations. For any given model name,
 subsequent scans that produce the exact same fingerprint are automatically attributed to
 the same existing model version, regardless of whether the model originated from Google
 Cloud Storage, Amazon S3, or Hugging Face. Conversely, if a scan reveals a modified
 model with a different fingerprint under that same model name, the system securely
 tracks the evolution by registering it as a new, distinct model version. 

 To ensure this content-based identification functions seamlessly across all your deployed
 environments, you must use Model Security SDK version 1.1.0 or higher when scanning
 cloud storage and local models. Adhering to this minimum SDK version guarantees that the
 system calculates fingerprints for your local and cloud models in a manner that is
 completely compatible with Hugging Face models, ensuring your registration and
 versioning history remains consistent and reliable across your entire AI
 infrastructure. 

 Scan a Model With a Model Name 

 To register your model with a recognizable business identity during the scanning
 process, you can assign a custom display name using either the Command Line
 Interface (CLI) or the software development kit (SDK). By assigning a
 customer-defined display name, you replace obscure file paths with recognizable
 model identities across your platform UI and API responses. 

 Scan using CLI 

 You can initiate a scan and apply a display name directly from your terminal using
 the scan command. By providing your security group UUID, the
 model's location URI, and your desired identifier using the
 --model-name parameter, the system automatically catalogs the
 model under that specific name and begins tracking its
 versions. 

 model-security scan \
 --security-group-uuid "12345678-1234-1234-1234-123456789012" \
 --model-uri "https://huggingface.co/microsoft/DialoGPT-medium" \
 --model-name "my-model" 

 Scan using Python SDK 

 To programmatically scan and name your model, you can use the Python SDK to interface
 with the centralized registry. After initializing the client with your designated
 API endpoint, you execute the scan method. By passing the security
 group UUID, the model URI, and your chosen model_name , your script
 will trigger the scan and return the rich model identity metadata directly to your
 application. 

 from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient(
 base_url="https://api.sase.paloaltonetworks.com/aims"
)

result = client.scan(
 security_group_uuid="12345678-1234-1234-1234-123456789012",
 model_uri="https://huggingface.co/microsoft/DialoGPT-medium",
 model_name="my-model"
)

print(f"Scan completed: {result.eval_outcome}")
print(f"Scanned model version: {result.model_version_uuid}")

 When your scan's evaluation outcome remains in a pending or
 error status, the system might return a model version UUID of
 "00000000-0000-0000-0000-000000000000" within the scan result response. You must
 treat this specific placeholder string as a non-existent value, handling it exactly
 as if the system had returned no model version UUID at all. 

 Viewing Models and Model Scan Results 

 List of Models 

 To view a comprehensive catalog of your registered AI models across the
 centralized platform, you can retrieve a filtered list of your models using
 either the Web Interface, or CLI, or SDK. This functionality aligns with AI
 Model Security's enhanced integration capabilities for maintaining a
 platform-wide model catalog. 

 List Models using CLI 

 You can query your centralized registry from the terminal by executing the
 list-models command and applying various operational
 filters to narrow down the results. By using flags such as
 --latest-version-source-types "S3" ,
 --latest-version-outcomes "ALLOWED" , and
 --latest-version-formats "pytorch" , you can securely
 isolate models based on their storage origins, security evaluation statuses, and
 file formats. You can also define specific chronological boundaries using the
 --start-time , --end-time , and
 --latest-version-scan-time-before parameters to find models
 scanned or registered within a particular time window. Finally, passing a
 specific string using the --search-query flag alongside sorting
 ( --sort-order "asc" ) and pagination ( --limit
 50 ) flags allows you to efficiently locate exactly what you
 need. 

 model-security list-models \
 --latest-version-source-types "S3" \
 --latest-version-outcomes "ALLOWED" \
 --latest-version-formats "pytorch" \
 --latest-version-scan-time-before "2025-03-01 T00:00:00" \
 --start-time "2025-01-01 T00:00:00" \
 --end-time "2025-12-31 T23:59:59" \
 --search-query "my-model" \
 --sort-order "asc" \
 --limit 50 

 List Models using SDK 

 To programmatically retrieve and filter your overarching model catalog, you can
 use the Python SDK to interface directly with the platform. After initializing
 the ModelSecurityAPIClient with your designated API endpoint,
 you can call the list_models method. This method accepts
 parameters equivalent to the CLI, allowing you to pass Python lists for source
 types and outcomes, standard strings for formats and search queries, and
 specific timezone-aware datetime objects to bound your search
 temporally. 

 from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient(
 base_url="https://api.sase.paloaltonetworks.com/aims"
)

result = client.list_models(
 latest_version_source_types=["S3"],
 latest_version_outcomes=["ALLOWED"],
 latest_version_formats="pytorch",
 latest_version_scan_time_before=datetime(2025, 3, 1, tzinfo=timezone.utc),
 start_time=datetime(2025, 1, 1, tzinfo=timezone.utc),
 end_time=datetime(2025, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
 search_query="my-model",
 sort_order="asc",
 limit=50
) 

 View Model Details 

 To view the details of a specific AI model entity, you can utilize either the CLI
 or SDK by referencing the model's unique identifier (UUID). This capability
 leverages AI Model Security's Model Identity Lookup feature, which allows you to
 query and resolve overarching model identity information using a model ID. 

 View Models using CLI 

 You can retrieve the overarching model details from your terminal by executing
 the get-model command and providing the target UUID using the
 --uuid 
 parameter: 

 model-security get-model --uuid "12345678-1234-1234-1234-123456789012" 

 This command queries the centralized registry to return the primary metadata
 associated with that specific model entity, such as its assigned display
 name. 

 View Models using SDK 

 To programmatically retrieve the model entity details, you can use the Python SDK
 to initialize a client and fetch the data: 

 from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient(
 base_url="https://api.sase.paloaltonetworks.com/aims"
)

model_result = client.get_model(uuid="12345678-1234-1234-1234-123456789012")

print(f"Name: {model_result.name}")
print(f"Latest Version Outcome: {model_result.latest_version_outcome}")

 In this script, the client queries the platform to resolve the specific model
 reference and prints out its high-level attributes, including the assigned model
 name and the evaluation outcome of its latest version. 

 List a Model Versions 

 To review the complete history of a specific model, you can list all of its
 associated versions using either CLI or SDK. This capability leverages AI Model
 Security's version tracking framework, allowing you to seamlessly trace the
 evolution of your AI models over time 

 View a Model's Versions using CLI 

 You can retrieve a model's version history from your terminal by executing the
 list-model-versions command. You must provide the target
 model's unique identifier via the --uuid parameter. To further
 customize your query, you can organize the output by appending the
 --sort-order "desc" flag to view the most recent versions
 first, and you can restrict the total number of returned entries using the
 --limit 
 flag: 

 model-security list-model-versions \
 --uuid "12345678-1234-1234-1234-123456789012" # this is the model UUID
 --sort-order "desc" \
 --limit 50 

 View a Model's Versions using SDK 

 To programmatically list the model versions, you can use the Python SDK to
 interface with the centralized registry. After initializing the
 ModelSecurityAPIClient with your platform endpoint, you
 call the list_model_versions method. By passing the model's
 UUID along with the sort_order and limit 
 arguments, your script will fetch the sorted version records directly into your
 application: 

 from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient(
 base_url="https://api.sase.paloaltonetworks.com/aims"
)

result = client.list_model_versions(
 uuid="12345678-1234-1234-1234-123456789012",
 sort_order="desc",
 limit=50
) 

 View Model Version Details 

 View Model Version Details using CLI 

 You can retrieve the model version details from your terminal by executing the
 get-model-version command and passing the target UUID using
 the --uuid 
 parameter: 

 model-security get-model-version --uuid "12345678-1234-1234-1234-123456789012" 

 This
 command queries the AI Model Security registry to return the metadata associated
 with that specific model version. 

 View Model Version Details using SDK 

 To programmatically retrieve the model version details, you can use the Python
 SDK to initialize a client and fetch the
 data: 

 from model_security_client.api import ModelSecurityAPIClient

# Initialize the client
client = ModelSecurityAPIClient(
 base_url="https://api.sase.paloaltonetworks.com/aims"
)

mv_result = client.get_model_version(uuid="12345678-1234-1234-1234-123456789012")

print(f"Revision: {mv_result.revision}")
print(f"Latest Evaluation Outcome: {mv_result.last_eval_outcome}")

 In this script, the client queries the platform for the specific model version
 entity and prints out its revision history and the latest evaluation
 outcome. 

 Previous 

 Understanding Model Security Scan Results 

 Next 

 Understanding Model Security Rules 

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
