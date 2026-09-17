---
url: https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-assets
fetched_at: 2026-09-16T08:49:17Z
source: cortex-platform
---

# Code Security assets | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Code Security 

 Code Security assets 

 Code Security provides a comprehensive view of assets detected by native Infrastructure-as-Code (IaC) and Software Composition Analysis (SCA) scanners. These assets are displayed in dedicated IaC Resources and Software Package inventories. Both are specialized, filtered views within the broader All Assets inventory. This focused approach allows you to manage and analyze your Code Security assets separately from other types in your environment. 

 Code Security assets are a part of the broader Cortex Cloud Application Security asset suite, including: 

 ASPM assets, which include Repositories . For more information about Repositories , refer to Repository as an asset . 

 Supply Chain assets, which include VCS Organizations , CI/CD Instances and CI/CD Pipelines . For more information about CI/CD Security assets, refer to Supply Chain assets . 

 Identity assets, which include Collaborators . For more information about Collaborators as assets, refer to VCS Collaborators-as-assets . 

 Code Security asset use cases 

 Visibility and context 

 Asset inventory : Maintain a comprehensive inventory of all detected assets, including their metadata and relationships to other assets. This provides a centralized view of all components within the environment 

 Code to cloud mapping : A graphical representation of the SDLC, highlighting the asset's location within. This visualization allows for a clear understanding of the asset's journey and its relationship to other components 

 Application path to production : Trace the asset's path through the application lifecycle, from its origin in code repositories to its deployment. This includes identifying all intermediate stages and dependencies 

 Security risks 

 Infrastructure as Code (IaC) misconfigurations: Identify misconfigurations associated with the IaC asset configuration, and provide details such as severity, location, when created and the assignee 

 SCA CVE vulnerabilities : Identify known vulnerabilities in open-source packages associated with an asset, including details such as severity, the CVE issue, CVSS score, when discovered and the assignee 

 License miscompliance : Identify and detail license miscompliance issues within packages associated with an asset, including severity, license category (such as strong copyleft), location, when discovered, and the assignee 

 Package Integrity : Identify and detail any package operational issues in packages associated with the asset, including severity, location, when created and the assignee 

 Previous About Code security 

 Next Software packages as assets 

 Last updated 1 month ago 

 Was this helpful?
