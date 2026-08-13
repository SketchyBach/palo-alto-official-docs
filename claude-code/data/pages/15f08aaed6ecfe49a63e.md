---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-model-security/model-security-to-secure-your-ai-models/get-started-with-ai-model-security/organize-security-scans-with-custom-labels/organize-security-scans-with-custom-labels-replace-labels
fetched_at: 2026-08-13T14:05:38Z
source: ai-security
---

# Set Scan Labels Clear

Set Scan Labels 

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

 Set Scan Labels 

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

 Get Started with AI Model Security 

 Organize Security Scans with Custom Labels 

 Set Scan Labels 

 Download PDF 

 Prisma AIRS 

 Set Scan Labels 

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

 Set Scan Labels 

 Replace the complete set of existing labels on the scan with the new provided
 labels. 

 SetLabels API 

 Replace the complete set of existing labels on the scan with the new provided
 labels. 

 Using
 CLI 

 model-security set-scan-labels \
 --scan-uuid "550e8400-e29b-41d4-a716-446655440000" \
 --labels '[{"key":"env","value":"staging"},{"key":"version","value":"v2-0"},{"key":"deployed","value":"false"}]'

 Using Python
 SDK 

 from uuid import UUID
from model_security_client.api import ModelSecurityAPIClient
from model_security_client.generated.data.models.LabelsCreateRequestSchema import LabelsCreateRequestSchema
from model_security_client.generated.data.models.LabelSchema import LabelSchema

client = ModelSecurityAPIClient(
 base_url="https://api.sase.paloaltonetworks.com/aims"
)

scan_uuid = UUID("550e8400-e29b-41d4-a716-446655440000")

# Replace all existing labels
client.set_scan_labels(
 scan_uuid=scan_uuid,
 data=LabelsCreateRequestSchema(
 labels=[
 LabelSchema(key="env", value="staging"),
 LabelSchema(key="version", value="v2-0"),
 LabelSchema(key="deployed", value="false"),
 ]
 )
)

print(f"Labels set for scan {scan_uuid} (all previous labels removed)")

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
