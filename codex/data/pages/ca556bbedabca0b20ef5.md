---
url: https://cortex-docs.paloaltonetworks.com/python-development-quick-start-guide
fetched_at: 2026-09-16T08:58:39Z
source: cortex-platform
---

# Cortex XSOAR Platform Overview | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Python Development Quick Start Guide 

 Cortex XSOAR Python Development Quick Start Guide 

 Cortex XSOAR Platform Overview 

 How the Cortex XSOAR platform is structured. 

 Cortex XSOAR uses Python scripts to automate, integrate, and extend functionality. It is implemented as a single Linux service (demisto) and provides: 

 The Cortex XSOAR UI 

 Control and execution of integrations for collecting threat and incident data 

 Incident response orchestration and automation through playbooks 

 Over 700 Marketplace content packs provide out-of-th- box (OOTB) integrations and playbooks supported by a common base of 300+ commands and automation scripts. While automations do support JavaScript and PowerShell, the most comprehensive support is for Python-based development. 

 The Cortex XSOAR service uses two mechanisms for communication: the REST API and standard input/ouput/error streams provided by Linux. The Cortex XSOAR browser-based UI uses the REST API. Scripts may also use the REST API for additonal functionality. The standard input/output/error streams are internal to the Cortex XSOAR server for communicating with automation scripts executed within Docker and Podman containers and are not directly accessed by user developed scripts. 

 cortex-xsoar-high-level-architecture.png 

 Next Where Cortex XSOAR Uses Python Scripts 

 Last updated 2 months ago 

 Was this helpful?
