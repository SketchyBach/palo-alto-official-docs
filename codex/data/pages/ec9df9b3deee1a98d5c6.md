---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-ai-security/cortex-cloud-ai-security-use-cases
fetched_at: 2026-09-16T08:45:09Z
source: cortex-platform
---

# Cortex Cloud AI Security use cases | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cortex Cloud AI Security 

 Cortex Cloud Runtime 

 Cortex Cloud AI Security use cases 

 Learn about use cases that are relevant for Cortex Cloud AI Security. 

 Understand your AI ecosystem 

 Understanding your AI ecosystem is crucial for identifying potential vulnerabilities and ensuring the robustness of your AI operations. A comprehensive view of your AI landscape helps in pinpointing where sensitive data is processed and stored, as well as how data flows between systems. 

 To understand your AI ecosystem, use the AI Security Dashboard , which provides visibility into all the AI components. You can also see how your AI assets relate to any other asset in the environment using the Graph Search . The complete list of your AI assets can be found under AI Inventory , where you can investigate each asset. 

 Investigate an AI asset 

 To understand a specific component of your AI ecosystem and identify any findings or security issues related to it, use its asset card and links to findings, issues, and cases created for the asset. When you select an asset, you can review all the tabs on its asset card. These tabs on the asset cards provide information about the following: overview, access, data, vulnerabilities, applications, and AI ecosystems. 

 Detect AI security issues 

 Detecting the AI security issues early is pivotal to safeguarding AI-powered applications and the sensitive data they handle. AI systems, due to their complexity, can often be opaque, making it difficult to identify vulnerabilities using traditional methods. To detect security issues in your AI ecosystem, use the AI Security Issues page. 

 Secure the data for AI 

 Securing the data utilized by AI systems is critical. Cortex Cloud AI Security helps you identify the data that is impacted by your AI ecosystem, whether it's training data, data used for RAG (Retrieval Augmented Generation) or any other related data such as prompt logs. It also classifies this data, using Cortex Cloud Data Security. Data classification across your AI ecosystem allows you to identify models that are trained on sensitive data and to prioritize all identified risks and issues based on their data impact. For example, missing guardrails on a sensitive model should be treated differently due to its context. 

 Discover self-managed AI models 

 Cortex Cloud AI Security helps organizations discover self-managed AI models. 

 Self-managed AI models refer to AI models that are deployed and operated on self-managed cloud infrastructure, rather than through cloud providers' managed services. These models are often sourced from public repositories like Hugging Face, and can lead to the proliferation of shadow AI. 

 The growing use of AI in business workflows makes it increasingly important to manage and secure all AI models, whether deployed through managed services or self-managed infrastructures. Self-managed AI models, in particular, introduce unique risks, such as security vulnerabilities and compliance gaps. Tracking and securing these models is essential to reducing risks and ensuring that AI applications remain safe, secure, and compliant. 

 Comply with AI regulations 

 Cortex Cloud AI Security ensures compliance with emerging AI mandates and industry standards, which is crucial because new frameworks require unique measures to govern AI-specific vulnerabilities. For example, data poisoning is a major risk for AI applications but traditional compliance programs are not designed to handle it; however, new frameworks for AI governance include relevant measures, such as the documentation of data sources used to train AI models. In addition, AI-powered applications also add complexity for existing regulations like GDPR, due to their data processing and interconnected systems. 

 Cortex Cloud AI Security allows for continuous monitoring and visualization of compliance with leading AI standards, such as the OWASP Top Ten for LLM. 

 Complying with current industry standards can help shorten the time needed to meet future binding regulations. Cortex Cloud AI Security helps you enforce policies, maintain audit trails, and achieve compliance, providing visibility into compliance violations and helping manage your AI Inventory, which is essential for controlling model sprawl and shadow AI. 

 Manage your AI software supply chain 

 As AI becomes deeply embedded in application development, security teams need comprehensive visibility into the software supply chain. This visibility must go beyond deployed AI models and agents, extending to the underlying AI software packages and SDKs that developers use to build these systems. 

 A key aspect of Cortex Cloud AI Security is implementing a shift-left approach to AI security. This helps organizations identify and manage risks early in the development lifecycle by providing visibility into the AI software supply chain. Understanding this supply chain is crucial for both generating an AI Bill of Materials (AI-BOM) and for identifying potential vulnerabilities before they are deployed to production. This proactive stance ensures that security is addressed at the source, preventing more complex and costly issues later on. 

 Detect open-source models 

 Cortex Cloud AI Security provides detection and risk assessment for open-source models, identifying and displaying the count of open-source models on the dashboard. 

 Previous Cortex Cloud AI Security concepts 

 Next How to perform advanced AI Security investigations using XQL 

 Last updated 2 months ago 

 Was this helpful?
