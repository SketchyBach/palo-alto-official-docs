---
url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-red-teaming/identify-ai-system-risks-with-ai-red-teaming/get-started-with-prisma-airs-ai-red-teaming/targets/custom-target-adapters/test-and-validate-a-custom-target-adapter
fetched_at: 2026-08-13T14:06:10Z
source: ai-security
---

# Test and Validate a Custom Target Adapter Clear

Test and Validate a Custom Target Adapter 

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

 Test and Validate a Custom Target Adapter 

 Updated on 

 Fri Jul 24 03:07:12 PDT 2026 

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

 Fri Jul 24 03:07:12 PDT 2026 

 Focus 

 Home 

 Prisma AIRS 

 AI Red Teaming 

 Identify AI System Risks with AI Red Teaming 

 Get Started with Prisma AIRS AI Red Teaming 

 Targets 

 Custom Target Adapters 

 Test and Validate a Custom Target Adapter 

 Download PDF 

 Prisma AIRS 

 Test and Validate a Custom Target Adapter 

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

 Build a Custom Target Adapter 

 Next 

 Attach a Custom Target Adapter to a Target 

 Test and Validate a Custom Target Adapter 

 Use the AI Red Teaming adapter editor to iterate on your adapter script and validate
 it end-to-end before activating it for use by targets. 

 Where Can I Use This? What Do I Need? 

 Prisma AIRS (AI Red Teaming) 

 AI Red Teaming License 

 Network Channel
 client v1.4.0 or later 

 Adapter sidecar
 enabled 

 You author and validate an adapter code in the AI Red Teaming web interface before
 attaching it to any target. Validation runs end-to-end. It loads your code and
 round-trips a real test prompt through the Network Channel to your target, exactly
 as a scan would. 

 Start from the built-in template in the Adapter Code and fill in your variables and
 secrets. 

 Navigate to AI Red Teaming Custom Adapters and select Create Adapter . The adapter
 editor opens with a built-in Python template. 

 Define your Adapter name, execution logic, and adapter credentials. 

 Enter your Adapter Name . 

 Write or paste your adapter code in the editor. Implement the required
 functions following the patterns in Build a Custom Target Adapter . 

 Configure your adapter variables. 

 Add each key and value that your script reads using
 context.vars , and mark each as a
 Variable . 

 Add each key and value that your script reads using
 context.secrets , and mark each as a
 Secret . 

 Select a Network Channel for testing and Validate
 Adapter to run an end-to-end test. 

 AI Red Teaming loads your script and sends a real test prompt through the
 Network Channel to your target. The result and your script's
 print() (log output) are displayed. A Validate run does
 not save your adapter script or settings. 

 Use print() statements
 in your script while iterating. The output appears during Validate runs but
 not during scans. For deeper debugging during a scan, check the adapter
 sidecar container logs on your cluster. 

 Edit the Adapter Code and Run Validate Adapter until the adapter produces the
 expected output. 

 Select Save as Draft to save without validating if you
 need to step away mid-edit. 

 A Network Channel is not required for a
 draft. 

 Select Create Adapter to validate end-to-end and, on
 success, mark the adapter active and usable by targets. 

 A Network Channel is required to activate an
 adapter. 

 After adding an adapter successfully, you can add a target using the created
 adapter or view all your adapters. 

 You can also edit an existing adapter settings. 

 Previous 

 Build a Custom Target Adapter 

 Next 

 Attach a Custom Target Adapter to a Target 

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

 AI Red Teaming 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
