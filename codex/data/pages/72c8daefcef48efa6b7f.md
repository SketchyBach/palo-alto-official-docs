---
url: https://cortex-docs.paloaltonetworks.com/cortex-agentix/detect-investigate-and-respond-to-threats/agentic-assistant-chat/chat-with-the-agentic-assistant-from-slack
fetched_at: 2026-09-06T10:19:27Z
source: cortex-platform
---

# Chat with the Agentic Assistant from Slack | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex AgentiX 

 Cortex AgentiX Documentation 

 Detect, Investigate, and Respond to Threats 

 Agentic Assistant chat 

 Cortex AgentiX 

 Chat with the Agentic Assistant from Slack 

 Chat with an Agentic Assistant agent from Slack in Cortex AgentiX. 

 Slack chats with the Agentic Assistant bridge the gap between where your team collaborates and where security operations happen by enabling you to interact with agents directly within you daily communication workflow without needing to log in to Cortex AgentiX. 

 Access the chat from Slack 

 Prerequisite 

 Before you can interact with the Cortex Agentic Assistant in Slack, the Slack v3 integration must be set up correctly. For more information, see the Slack v3 integration documentation . 

 To perform actions in Slack, your Slack email must match your Cortex AgentiX user email. This ensures the system can strictly follow your assigned permissions (RBAC). If you do not have the required permissions to interact with agents, the system will block the action. 

 Once the setup is done, you can initiate a chat or interact with the Cortex Agentic Assistant from Slack by tagging your configured bot name in a thread (for example @Your bot name ). Cortex Agentic Assistant returns a dropdown menu of available agents to select. 

 Note 

 Only public agents are supported via Slack. 

 Considerations for Slack interactions with Agentic Assistant agents 

 When interacting with the Cortex Agentic Assistant directly within Slack, keep the following in mind to maintain session integrity and secure access: 

 Chat context 

 When an agent is tagged, the system automatically pulls in the last five messages in the thread (or up to the last bot interaction) so the agent understands the conversation's history. 

 Single player model 

 The first user to tag the bot becomes the initiator, and only this user can issue commands. If another user tries to send a prompt, they receive an Access Denied message. 

 The reset command 

 To hand off a session to another user or start fresh, any user in the Slack thread can type @Your bot name reset . This ends the session and allows a new initiator to take over. 

 Approving sensitive actions (hard locks) 

 Sensitive actions require approval. In Slack, this triggers a hard lock where the agent refuses text input and displays Approve (green) and Deny (red) buttons, and only the initiator can click these buttons. If the initiator does not respond within two weeks, the request is automatically denied and the chat will close. 

 Providing feedback 

 After a final result or remediation is executed, you can provide feedback directly in Slack using thumbs up or thumbs down. 

 Additional considerations 

 Small tables (less than 5 rows) are rendered as Markdown, while larger tables will be summarized with a link to view the full results. Code and logs will use standard Slack code blocks. 

 Chat artifacts are not visible via Slack. 

 Chat timeout 

 Slack sessions follow a timeout policy of two weeks of inactivity (matching the UI data retention policy), after which the session automatically closes. 

 Slack interaction with the Agentic Assistant example 

 The following is an example scenario describing how you can monitor shift priorities, track SLAs, and review pending automations in Cortex AgentiX directly from Slack. 

 Initiation 

 Check the daily queue by opening your team's Slack channel and tagging @Your bot name with the prompt, "What are the top issues I should prioritize today and show me all issues with an overdue SLA?". 

 Agent selection 

 The bot responds with a dropdown menu of available public agents, and you select the appropriate agent to handle the request. 

 Status update 

 The agent processes the request and replies in the thread, providing a summarized list of the highest-priority issues and any automations currently waiting for user input. 

 Note 

 If a team member in the channel sees the summary and attempts to ask the agent, "Give me more details on the first SLA issue," the team member receives an access denied message because the active session is only available to you, the initiator. 

 Handoff 

 The session can remain open for up to two weeks, after which it automatically closes. To end a session, type @Your bot name reset so the rest of the team can engage. 

 Another team member can then tag @Your bot name to initiate a new session. Because the system pulls the last five messages in the thread, the agent understands the history of the conversation. The team member can simply prompt, "Assign the first overdue issue from that summary to me," and the agent will know which issue is being referenced. 

 Previous Chat with an Agentic Assistant agent 

 Next Create and run XQL queries with Agentic Assistant chat 

 Last updated 2 months ago 

 Was this helpful?
