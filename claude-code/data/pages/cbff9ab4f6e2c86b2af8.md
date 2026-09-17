---
url: https://cortex-docs.paloaltonetworks.com/data-security-documentation/agentic-ai-and-cortex-agentic-assistant/data-security-agent
fetched_at: 2026-09-16T08:58:40Z
source: cortex-platform
---

# Data security agent | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Data Security 

 Cortex Data Security Documentation 

 Agentic AI & Cortex Agentic Assistant 

 Data security agent 

 The Data security agent is a system agent in the Cortex Agentic Assistant . It gives you a natural language interface to your data security program. From a single chat, you can ask questions about your data, take action on what you find, and create custom data patterns. 

 The Data security agent supports three main types of task: 

 Answer questions about your data. 

 Take actions. 

 Write custom data patterns. 

 Answer questions about your data 

 Ask questions in natural language about any data the platform has discovered and classified, and the agent returns answers grounded in your inventory, posture findings, and detections. For example: 

 Which data stores contain unencrypted PII? 

 Show me the publicly exposed assets that hold financial data. 

 Which AI agents accessed sensitive data in the last 30 days? 

 Summarize the highest-risk data issues from the past week. 

 Take actions 

 The agent can open tickets in ticketing systems such as Jira and share information through communication channels such as Slack, Microsoft Teams, and email. For example, you can ask the agent to open a Jira ticket for an over-exposed data store, or post a summary of new high-severity issues to a Slack channel. 

 Available actions depend on which integrations are active in your tenant and which actions are assigned to the agent. The agent runs within your tenant permissions, and sensitive actions require explicit approval. See Agentic Assistant security . 

 Write custom data patterns 

 The agent can help you create custom data patterns to identify sensitive data that is specific to your organization. Describe the data you want to detect, and the agent helps generate the pattern definition. Once saved, a custom data pattern runs on all data in the same way as any out-of-the-box pattern. For the full procedure on building and validating patterns, see How to create and validate a custom data pattern . 

 Previous Agentic Assistant security 

 Next Plan and prepare 

 Last updated 3 months ago 

 Was this helpful?
