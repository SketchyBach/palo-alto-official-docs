---
url: https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-app-embedded
fetched_at: 2026-09-16T13:36:32Z
source: prisma-cloud
---

# Deploy WAAS for App-Embedded | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Compute Edition 

 Admin Guide 

 34 

 Web-Application and API Security (WAAS) 

 Deploying WAAS 

 Deploy WAAS for App-Embedded 

 In some environments, Prisma Cloud Defender must be embedded directly inside the container it is protecting. This type of Defender is known as an App-Embedded Defender. App-Embedded Defender can secure these types of containers with all WAAS protection capabilities. 

 The only difference is that App-Embedded Defender runs as a reverse proxy to the container it’s protecting. As such, when you set up WAAS for App-Embedded, you must specify the exposed external port where App-Embedded Defender can listen, and the port (not exposed to the Internet) where your web application listens. WAAS for App-Embedded forwards the filtered traffic to your application’s port - unless an attack is detected and you set your WAAS for App-Embedded rule to Prevent . 

 When testing your Prisma Cloud-protected container, be sure you update the security group’s inbound rules to permit TCP connections on the external port you entered in the WAAS rule. This is the exposed port that allows you to access your web application’s container. To disable WAAS protection, disable the WAAS rule, and re-expose the application’s real port by modifying the security group’s inbound rule. 

 To embed App-Embedded WAAS into your container or Fargate task: 

 Create a Rule for App-Embedded 

 Open Console, and go to Defend > WAAS > App-Embedded . 

 Select Add rule . 

 Enter a Rule name and Notes (Optional) for describing the rule. 

 Choose the rule Scope by specifying the resource collection(s) to which it applies. 

 Collections define a combination of App IDs to which WAAS should attach itself to protect the web application: 

 (Optional) Enable API endpoint discovery . 

 When enabled, the Defender inspects the API traffic to and from the protected API. Defender reports a list of the endpoints and their resource path in Compute > Monitor > WAAS > API discovery . 

 Save the rule. 

 Add an App (policy) to the rule 

 Select a WAAS rule to add an App in. 

 Select Add app . 

 In the App Definition tab, enter an App ID . 

 The combination of Rule name and App ID must be unique across In-Line and Out-Of-Band WAAS policies for Containers, Hosts, and App-Embedded. 

 If you have a Swagger or OpenAPI file, click Import , and select the file to load. 

 If you do not have a Swagger or OpenAPI file, manually define each endpoint by specifying the host, port, and path. 

 In Endpoint Setup , click Add Endpoint . 

 Specify endpoint in your web application that should be protected. Each defined application can have multiple protected endpoints. 

 Enter HTTP host (optional, wildcards supported). 

 HTTP hostnames are specified in the form of [hostname]:[external port]. 

 The external port is defined as the TCP port on the host, listening for inbound HTTP traffic. If the value of the external port is "80" for non-TLS endpoints or "443" for TLS endpoints it can be omitted. Examples: "*.example.site", "docs.example.site", "www.example.site:8080", etc. 

 Enter App ports as the internal port your app listens on. Specify the TCP port listening for inbound HTTP traffic. 

 If your application uses TLS or gRPC , you must specify a port number. 

 Enter Base path (optional, wildcards supported): 

 Base path for WAAS to match when applying protections. 

 Examples: "/admin", "/" (root path only), "/*", /v2/api", etc. 

 Enter WAAS port (only required for Windows, App-Embedded or when using "Remote host" option) as the external port WAAS listens on. The external port is the TCP port for the App-Embedded Defender to listen on for inbound HTTP traffic. 

 If your application uses TLS, set TLS to On . 

 You can select the TLS protocol (1.0, 1.1, 1.2, and 1.3 for WAAS In-Line, and 1.0, 1.1, and 1.2 for WAAS Out-Of-Band) to protect the API endpoint and enter the TLS certificate in PEM format. 

 You can select Response headers to add or override HTTP response headers in responses sent from the protected application. 

 Select Create response header . 

 To facilitate inspection, after creating all endpoints, click View TLS settings in the endpoint setup menu. 

 WAAS TLS settings: 

 Certificate - Copy and paste your server’s certificate and private key into the certificate input box (e.g., cat server-cert.pem server-key > certs.pem ). 

 Minimum TLS version - A minimum version of TLS can be enforced by WAAS In-Line to prevent downgrading attacks (the default value is TLS 1.2). 

 HSTS - The HTTP Strict-Transport-Security (HSTS) response header lets web servers tell browsers to use HTTPS only, not HTTP. When enabled, WAAS would add the HSTS response header to all HTTPS server responses (if it is not already present) with the preconfigured directives - max-age , includeSubDomains , and preload . 

 max-age=<expire-time> - Time, in seconds, that the browser should remember that a site is only to be accessed using HTTPS. 

 includeSubDomains (optional) - If selected, HSTS protection applies to all the site’s subdomains as well. 

 preload (optional) - For more details, see the following link . 

 If you application requires API protection , for each path define the allowed methods and the parameters. 

 Continue to App Firewall settings, select the protections to enable and assign them with actions . 

 Configure the DoS protection thresholds. 

 Continue to Access Control tab and select access controls to enable. 

 Select the bot protections you want to enable. 

 Select the required Custom rules . 

 Proceed to Advanced settings for more WAAS controls. 

 Select Save . 

 The Rule Overview page shows all the WAAS rules created. 

 Select a rule to display the Rule Resources , and for each application a list of protected endpoints and the protections enabled for each endpoint are displayed. 

 Test protected endpoint using the following sanity tests . 

 Go to Monitor > Events , click on WAAS for containers/hosts/App-Embedded , and observe the events generated. 

 For more information, see the WAAS analytics help page . 

 Previous Deploy WAAS Out-Of-Band for Hosts 

 Next Deploy WAAS for Serverless 

 Last updated 1 month ago 

 Was this helpful?
