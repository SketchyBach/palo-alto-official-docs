---
url: https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/reference-and-developer-docs/role-based-access-control/cloud-security-and-posture-management-permissions/application-security-permissions/application-security-3rd-party-tools-permissions
fetched_at: 2026-09-06T09:47:19Z
source: cortex-platform
---

# Application Security - 3rd Party tools permissions | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XDR 

 Cortex XDR 5.x Documentation 

 Reference and developer docs 

 Role-Based Access Control 

 Cloud Security and Posture Management permissions 

 Application Security permissions 

 Cortex XDR 5.x 

 Application Security - 3rd Party tools permissions 

 Configure permissions for third-party Application Security tools. 

 Provides visibility into supply chain security, including external tools integrated with your development pipeline and a catalog of known supply chain components. 

 Supply Chain Tools 

 External security tools integrated with your development pipeline (e.g., SonarQube, Snyk, Semgrep, Veracode, 3rd Party AppSec Collector). Shows tool status, risk factors, permissions, and version information. To access Supply Chain Tools, go to Modules → Application Security → 3rd Party Tools → Supply Chain Tools 

 For more information, see Supply Chain assets . 

 Permission 

 Description 

 Roles Example 

 None 

 No access to Supply Chain Tools. 

 SOC Tier-1 and Tier-2 Analysts: Supply chain data is rarely needed for incident investigation at these tiers. 

 View 

 Read-only access to supply chain tools data. Users can browse, filter, and view tool details. They cannot add, configure, or remove tools. 

 SOC Tier-3 Analyst: May need to review supply chain tools during software supply chain attack investigations. 

 Threat Hunter: Reviews supply chain tools to identify potential supply chain attack vectors 

 View/Edit 

 Full access to manage supply chain tools. Includes all View capabilities plus: add new tools, configure tool settings, remove tools, and manage tool integrations. 

 Security Engineer: Manages supply chain tool integrations. 

 Supply Chain Catalog 

 A catalog of known supply chain components and their security status, including pipeline tools discovered across CI/CD configurations. To access the Supply Chain Catalog, go to Modules → Application Security → 3rd Party Tools → Supply Chain Catalog. 

 For more information, see Supply Chain assets . 

 Permission 

 Description 

 Roles Example 

 None 

 No access to Supply Chain Catalog. 

 SOC Tier-1 and 2 Analysts: Supply chain data is rarely needed for incident investigation at this tier. 

 View 

 Read-only access to the supply chain catalog. Users can browse, filter, and view catalog entries. They cannot update or manage catalog entries. 

 SOC Tier-3 Analyst: May need to review the supply chain catalog during software supply chain attack investigations. 

 Threat Hunter: Reviews the supply chain catalog to identify potential supply chain attack vectors 

 View/Edit 

 Full access to manage the supply chain catalog. Includes all View capabilities plus: update catalog entries and manage catalog data. 

 Security Engineer: Reviews the catalog for risk assessment 

 Required and recommended permissions 

 To effectively configure Application Security pipelines and investigate the resulting code vulnerabilities, administrators and analysts require visibility into the underlying VCS integrations, data sources, and issue queues. Consider adding the following permissions: 

 Permission 

 Permission Level 

 Reason 

 Integrations 

 View or View/Edit 

 View: Recommended for Supply Chain Catalog to view integration context for catalog entries. Strongly recommended for Supply Chain Tools to view the tool integration status and connectivity 

 View/Edit: Strongly recommended for Supply Chain Tools to configure 3rd party tool integrations (Snyk, SonarQube, Semgrep, Veracode, etc.). 

 Data Sources 

 View 

 Recommended. View connected data sources for the catalog context and view connected data sources for the supply chain tool context. 

 Graph Search 

 View 

 Recommended for Supply Chain Catalog. Understand asset relationships for catalog components. 

 Threat Intel 

 View 

 Recommended for Supply Chain Tools. Correlate supply chain tool findings with threat intelligence. 

 Previous Application Security - Policy Management permissions 

 Next Configurations - Application Security permissions 

 Last updated 5 days ago 

 Was this helpful?
