---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/onboard-cortex-xsoar/engines/configure-engines/configure-an-engine-to-use-custom-certificates
fetched_at: 2026-09-06T10:44:36Z
source: cortex-platform
---

# Configure an Engine to Use Custom Certificates | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Onboard Cortex XSOAR 

 Engines 

 Configure Engines 

 Cortex XSOAR 6.13 

 Configure an Engine to Use Custom Certificates 

 Configure custom engine certificates in Cortex XSOAR 6.13. 

 For communication tasks that go through an engine, you can replace the default self-signed certificate for the engine with your own certificate. 

 Find the two files created by the engine. The default location is /usr/local/demisto . 

 d1.key.pem 

 d1.cert.pem 

 Replace the contents of these files with your own certificates. 

 Change file owner to demisto: 

 chown -R demisto:demisto d1.key.pem 

 chown -R demisto:demisto d1.cert.pem 

 Set the file permissions: 

 chmod 600 d1.key.pem 

 chmod 644 d1.cert.pem 

 (Optional) If you are using a key passphrase for your custom certificate, add the passphrase to your engine configuration: 

 Go to Settings → Engines . 

 Create New Engine and provide an engine name or select an existing engine and Edit Configuration . 

 Select Use a passphrase for the engine certificate private key . 

 Click Save . 

 Previous Configure Access to Communication Tasks through an Engine 

 Next Notify Users When an Engine Disconnects 

 Last updated 1 month ago 

 Was this helpful?
