---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/secrets-security/appsec-secret-158
fetched_at: 2026-09-16T09:11:34Z
source: cortex-platform
---

# MySQL User Name detected in code | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 Secrets Security 

 MySQL User Name detected in code 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_SECRET_158 

 Category 

 Database Credentials 

 Severity 

 LOW 

 Framework 

 Git 

 Impact 

 The MySQL User Name is a required component of the database credentials. 

 If the corresponding password is also exposed, an attacker can gain unauthorized access and manipulate sensitive data in the database. 

 How to Fix 

 To remediate exposed Database credentials: 

 Log in to your database administration tool or console. 

 Identify the database user associated with the exposed connection string. 

 Rotate the password for that specific database user immediately. 

 Update the connection strings in your application configuration or secrets manager. 

 Restart your application instances if necessary to apply the new connection string. 

 Next, remove the secret from your codebase: 

 Locate the exposed connection string in your codebase. 

 Replace the hardcoded value with a secure variable or reference. 

 Finally, clean your version control history: 

 Permanently remove the sensitive data from your version control history to ensure it cannot be retrieved. 

 Previous LDAP Credentials detected in code 

 Next MySQL Password detected in code 

 Last updated 1 month ago 

 Was this helpful?
