---
url: https://docs.prismacloud.io/admin-guide/32/secrets/secrets-stores/hashicorp-vault
fetched_at: 2026-09-16T13:37:36Z
source: prisma-cloud
---

# HashiCorp Vault | 32 | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 32 

 Secrets 

 Secrets stores 

 HashiCorp Vault 

 You can integrate Prisma Cloud with HashiCorp Vault. Prisma Cloud supports the K/V Secrets Engine v2 in Vault 0.10.x, and K/V Secrets Engine v1 in Vault 0.9.x and older. Prisma Cloud does not support K/V Secrets Engine v1 in Vault 0.10.x. 

 First configure Prisma Cloud to access HashiCorp Vault, then create rules to inject the relevant secrets into the relevant containers. 

 In Console, go to Manage > Authentication > Secrets . 

 Click Add store . 

 Enter a name for the vault. This name is used when you create rules to inject secrets into specific containers. 

 For Type , select HashiCorp Vault . Choose the version that matches the version of Vault installed in your environment. 

 Fill out the rest of the form, specifying how to connect to your vault. 

 Click Add . 

 After clicking Add , Prisma Cloud tries conecting to your vault. If it is successful, the dialog closes, and an entry is added to the table. Otherwise, any connection errors are displayed directly in the configuration dialog. 

 Next, inject a secret into a container . 

 Previous CyberArk Enterprise Password Vault 

 Next Inject secrets into containers 

 Last updated 2 months ago 

 Was this helpful?
