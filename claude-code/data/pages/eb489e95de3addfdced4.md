---
url: https://docs.paloaltonetworks.com/prisma-access-browser/administration/investigate-prisma-access-browser-events/genai-prompt-events
fetched_at: 2026-08-13T17:23:08Z
source: palo-alto-main
---

# GenAI Prompt Events Clear

GenAI Prompt Events 

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

 GenAI Prompt Events 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Updated on 

 Tue Jul 28 09:38:39 PDT 2026 

 Focus 

 Home 

 Prisma Browser 

 Prisma Access Browser Administration 

 Explore Prisma Browser Events 

 GenAI Prompt Events 

 Download PDF 

 Prisma Browser 

 GenAI Prompt Events 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Browser Docs 

 Activation & Onboarding 

 Getting Started 

 Deployment 

 Administration 

 Integrations 

 User Guide 

 Previous 

 Prisma Browser Investigations 

 Next 

 Prisma Browser Event Types 

 GenAI Prompt Events 

 Use the Events view to filter, search, and review GenAI Prompt events generated
 when the Prisma Browser applies a GenAI Prompt rule. 

 Where Can I Use This? What Do I Need? 

 Strata Cloud Manager 

 Prisma Browser standalone 

 Prisma Access with Prisma Browser bundle
 license or Prisma Browser standalone license 

 Superuser or Prisma Browser 
 role 

 When the Prisma Browser applies a GenAI Prompt rule, it generates a
 GenAI Prompt event. GenAI Prompt events are a distinct event type and
 can be isolated from other activity events in the Events view. 

 Each GenAI Prompt event record includes the following fields: 

 Field Description 

 Provider The GenAI application where the prompt was submitted (for
 example, ChatGPT, Claude, or Gemini). 

 Action Whether the prompt was allowed or blocked by the matched
 rule. 

 Prompt Collected Whether the full text of the prompt was included in the
 event. 

 Attached Files Metadata for any files included with the prompt. File names are
 recorded; file content is not collected. 

 To filter by event type, use the Event Type filter in
 the Events view and select GenAI Prompt . 

 To filter events by whether the prompt text was captured, use the
 Prompt Collected filter and select
 Yes or No . 

 To search events by prompt content: 

 This option is available only for events generated
 by rules where prompt collection was enabled. For details on enabling prompt
 collection, see Manage Prisma Browser Access and Data Control Rules . 

 Enter a search term in the Events search field. 

 Set the search scope to Search GenAI
 prompts . 

 The Events view returns all GenAI Prompt events where the collected
 prompt text contains the specified term. 

 To view the full text of a collected prompt: 

 Select a GenAI Prompt event in the Events view to open the event
 detail drawer. 

 Select View next to the Prompt Content
 field. 

 The Prisma Browser displays the full text of the prompt as
 submitted by the user at the time of the event. 

 The View link appears only
 for events where prompt collection was enabled on the matched rule. For
 events where prompt collection was not enabled, the Prompt Collected field
 displays No and no prompt text is available. 

 Previous 

 Prisma Browser Investigations 

 Next 

 Prisma Browser Event Types 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Prisma Browser 

 Administration 

 Prisma Access 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
