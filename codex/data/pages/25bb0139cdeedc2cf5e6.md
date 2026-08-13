---
url: https://docs.paloaltonetworks.com/best-practices/10-1/data-center-best-practices/data-center-best-practices-checklist/deploy-data-center-best-practices-checklist/intra-data-center-traffic-policy
fetched_at: 2026-08-13T15:31:36Z
source: palo-alto-main
---

# Intra-Data-Center Traffic Policies Clear

Intra-Data-Center Traffic Policies 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 Strata Copilot

 Data Center Best Practice Security Policy 

 : 
 Intra-Data-Center Traffic Policies 

 Updated on 

 Wed May 06 14:58:35 PDT 2026 

 Focus 

 Download PDF 

 End-of-Life (EoL)

 Filter

 Version 

 10.1 (EoL) 

 10.2 

 10.1 (EoL) 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 Data Center Security Policy Best Practices Checklist 

 Plan Your Data Center Best Practice Deployment 

 Deploy Data Center Best Practices 

 Global Data Center Objects, Policies, and Actions 

 User Data Center Traffic Policies 

 Internet-to-Data-Center Traffic Policies 

 Data-Center-to-Internet Traffic Policies 

 Intra-Data-Center Traffic Policies 

 Data Center Security Policy Rulebase Order 

 Follow Post-Deployment Data Center Best Practices 

 Data Center Best Practice Security Policy 

 What Is a Data Center Best Practice Security Policy? 

 Why Do I Need a Data Center Best Practice Security Policy? 

 Data Center Best Practice Methodology 

 How Do I Deploy a Data Center Best Practice Security Policy? 

 How to Assess Your Data Center 

 How to Decrypt Data Center Traffic 

 Create the Data Center Best Practice Decryption Profiles 

 Exclude Unsuitable Traffic from Data Center Decryption 

 Create a Data Center Segmentation Strategy 

 How to Segment the Data Center 

 How to Segment Data Center Applications 

 How to Create Data Center Best Practice Security Profiles 

 Create the Data Center Best Practice Antivirus Profile 

 Create the Data Center Best Practice Anti-Spyware Profile 

 Create the Data Center Best Practice Vulnerability Protection Profile 

 Create the Data Center Best Practice File Blocking Profile 

 Create the Data Center Best Practice WildFire Analysis Profile 

 Use Cortex XDR Agent to Protect Data Center Endpoints 

 Create Data Center Traffic Block Rules 

 Define the Initial User-to-Data-Center Traffic Security Policy 

 User-to-Data-Center Traffic Security Approaches 

 Create User-to-Data-Center Application Allow Rules 

 Create User-to-Data-Center Authentication Policy Rules 

 Create User-to-Data-Center Decryption Policy Rules 

 Define the Initial Internet-to-Data-Center Traffic Security Policy 

 Internet-to-Data-Center Traffic Security Approach 

 Create Internet-to-Data-Center Application Allow Rules 

 Create Internet-to-Data-Center Decryption Policy Rules 

 Create Internet-to-Data-Center DoS Protection Policy Rules 

 Define the Initial Data-Center-to-Internet Traffic Security Policy 

 Data-Center-to-Internet Traffic Security Approaches 

 Create Data-Center-to-Internet Application Allow Rules 

 Create Data-Center-to-Internet Decryption Policy Rules 

 Define the Initial Intra-Data-Center Traffic Security Policy 

 Intra-Data-Center Traffic Security Approach 

 Create Intra-Data-Center Application Allow Rules 

 Create Intra-Data-Center Decryption Policy Rules 

 Order the Data Center Security Policy Rulebase 

 Log and Monitor Data Center Traffic 

 What Data Center Traffic to Log and Monitor 

 Monitor Data Center Block Rules and Tune the Rulebase 

 Log Intra Data Center Traffic That Matches the Intrazone Allow Rule 

 Log Data Center Traffic That Matches No Interzone Rules 

 Maintain the Data Center Best Practice Rulebase 

 Use Palo Alto Networks Assessment and Review Tools 

 Updated on 

 Wed May 06 14:58:35 PDT 2026 

 Focus 

 Home 

 Best Practices 

 Data Center Best Practice Security Policy 

 Data Center Security Policy Best Practices Checklist 

 Deploy Data Center Best Practices 

 Intra-Data-Center Traffic Policies 

 Download PDF 

 Data Center Best Practice Security Policy 

 Intra-Data-Center Traffic Policies 

 Table of Contents 

 Filter

 Version 

 10.1 (EoL) 

 10.2 

 10.1 (EoL) 

 10.0 (EoL) 

 9.1 (EoL) 

 Expand all | Collapse all 

 Data Center Security Policy Best Practices Checklist 

 Plan Your Data Center Best Practice Deployment 

 Deploy Data Center Best Practices 

 Global Data Center Objects, Policies, and Actions 

 User Data Center Traffic Policies 

 Internet-to-Data-Center Traffic Policies 

 Data-Center-to-Internet Traffic Policies 

 Intra-Data-Center Traffic Policies 

 Data Center Security Policy Rulebase Order 

 Follow Post-Deployment Data Center Best Practices 

 Data Center Best Practice Security Policy 

 What Is a Data Center Best Practice Security Policy? 

 Why Do I Need a Data Center Best Practice Security Policy? 

 Data Center Best Practice Methodology 

 How Do I Deploy a Data Center Best Practice Security Policy? 

 How to Assess Your Data Center 

 How to Decrypt Data Center Traffic 

 Create the Data Center Best Practice Decryption Profiles 

 Exclude Unsuitable Traffic from Data Center Decryption 

 Create a Data Center Segmentation Strategy 

 How to Segment the Data Center 

 How to Segment Data Center Applications 

 How to Create Data Center Best Practice Security Profiles 

 Create the Data Center Best Practice Antivirus Profile 

 Create the Data Center Best Practice Anti-Spyware Profile 

 Create the Data Center Best Practice Vulnerability Protection Profile 

 Create the Data Center Best Practice File Blocking Profile 

 Create the Data Center Best Practice WildFire Analysis Profile 

 Use Cortex XDR Agent to Protect Data Center Endpoints 

 Create Data Center Traffic Block Rules 

 Define the Initial User-to-Data-Center Traffic Security Policy 

 User-to-Data-Center Traffic Security Approaches 

 Create User-to-Data-Center Application Allow Rules 

 Create User-to-Data-Center Authentication Policy Rules 

 Create User-to-Data-Center Decryption Policy Rules 

 Define the Initial Internet-to-Data-Center Traffic Security Policy 

 Internet-to-Data-Center Traffic Security Approach 

 Create Internet-to-Data-Center Application Allow Rules 

 Create Internet-to-Data-Center Decryption Policy Rules 

 Create Internet-to-Data-Center DoS Protection Policy Rules 

 Define the Initial Data-Center-to-Internet Traffic Security Policy 

 Data-Center-to-Internet Traffic Security Approaches 

 Create Data-Center-to-Internet Application Allow Rules 

 Create Data-Center-to-Internet Decryption Policy Rules 

 Define the Initial Intra-Data-Center Traffic Security Policy 

 Intra-Data-Center Traffic Security Approach 

 Create Intra-Data-Center Application Allow Rules 

 Create Intra-Data-Center Decryption Policy Rules 

 Order the Data Center Security Policy Rulebase 

 Log and Monitor Data Center Traffic 

 What Data Center Traffic to Log and Monitor 

 Monitor Data Center Block Rules and Tune the Rulebase 

 Log Intra Data Center Traffic That Matches the Intrazone Allow Rule 

 Log Data Center Traffic That Matches No Interzone Rules 

 Maintain the Data Center Best Practice Rulebase 

 Use Palo Alto Networks Assessment and Review Tools 

 End-of-Life (EoL)

 Intra-Data-Center Traffic Policies 

 Configure Security policy and Decryption policy
for traffic between data center servers and application tiers. 

 Intra-Data-Center
Security Policy 

 Intra-Data-Center
Decryption Policy 

 Create intra-data-center application allow rules
to protect data center servers from other data center servers that
may be compromised. 

 A common application architecture consists of three server
tiers: web servers, application servers, and database servers. Apply best
practice Security profiles to most traffic between server tiers
to prevent threats. Don’t apply Security profiles to low-value,
high-volume traffic such as mailbox replication and backup flows—the
firewall already inspected the original flows, so spending CPU cycles
on them provides no extra value. Do create allow rules for these
applications to prevent misuse. For each rule, configure Log
at Session End on the Actions tab
and set up Log Forwarding to track and analyze rule violations. 

 This
example configures rules that allow traffic between application
server tiers for two proprietary internal finance applications for which
we created custom applications : Billing-App and Payment-App . 

 Allow finance application
traffic between the web server tier and the application server tier. 

 Allow finance application traffic between the application
server tier and the database server tier. 

 Create intra-data-center Decryption
policy rules to decrypt the traffic allowed in the preceding Security
policy rules. 

 The data center is a perfect place for attackers to hide
because many people think the data center is safe and don’t look
for intruders. But the same basic tenet that’s true in the rest
of the network holds true in the data center: you can’t protect
yourself against what you can’t see. Decrypt encrypted data center
traffic so that the firewall can inspect traffic, control access,
make threats visible, and protect your valuable assets. 

 Not
all data center traffic is encrypted. Don’t spend resources to decrypt
unencrypted (cleartext) traffic. 

 This rule decrypts traffic flowing between the
web server tier and the application server tier for the Finance department’s
billing servers. 

 This rule decrypts the traffic flowing between the application
server tier and the database server tier for the Finance department’s
billing servers. 

 Previous 

 Data-Center-to-Internet Traffic Policies 

 Next 

 Data Center Security Policy Rulebase Order 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
