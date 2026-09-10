---
url: https://cortex-docs.paloaltonetworks.com/mcp-integration-contributor-guide/python-implementation
fetched_at: 2026-09-06T11:16:32Z
source: cortex-platform
---

# Python implementation | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Integrations 

 MCP Integration Contributor Guide 

 Python implementation 

 Your MCP integration's main function should do the following: 

 Create an MCPApiModule Client instance with the vendor’s MCP server URL and authentication details. 

 Route commands to the appropriate handler. 

 Use MCPApiModule for all MCP operations. 

 Handle errors using extract_root_error_message() and return_error() . 

 Always close the client connection in a finally block. 

 Key principles 

 Use hard-coded vendor-specific values (server URL, auth type, command prefix, server name) as constants. 

 Extract only user-configurable parameters from demisto.params() , including tokens, credentials, and custom headers. 

 Use BaseException in error handling to catch async exception groups. 

 Mark the main function with # pragma: no cover . 

 For a simple token-based example, see Packs/GitHubMCP/Integrations/GitHubMCP/GitHubMCP.py . For a multi-auth example, see Packs/GenericMCP/Integrations/GenericMCP/GenericMCP.py 

 Previous MCPApiModule 

 Next Authentication patterns 

 Last updated 24 days ago 

 Was this helpful?
