---
url: https://docs.paloaltonetworks.com/vm-series/deployment/public-cloud/set-up-the-vm-series-firewall-on-aws/integrate-kms-for-cloud-native-key-management-aws
fetched_at: 2026-08-13T17:41:52Z
source: palo-alto-main
---

# Use AWS Secrets Manager to Store VM-Series Certificates Clear

Use AWS Secrets Manager to Store VM-Series Certificates 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Use AWS Secrets Manager to Store VM-Series Certificates 

 Updated on 

 Jul 8, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Updated on 

 Jul 8, 2026 

 Focus 

 Home 

 VM-Series 

 VM-Series Firewall on AWS 

 Use AWS Secrets Manager to Store VM-Series Certificates 

 Download PDF 

 VM-Series 

 Use AWS Secrets Manager to Store VM-Series Certificates 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 VM-Series Firewall Docs 

 Activation & Onboarding 

 Getting Started 

 Upgrade 

 Deployment 

 Select a Document 

 Public Cloud 

 Private Cloud 

 Previous 

 AWS Shared VPC Monitoring 

 Next 

 Use Case: Secure the EC2 Instances in the AWS Cloud 

 Use AWS Secrets Manager to Store VM-Series Certificates 

 Integrate cloud-native key managers to store certificates. 

 Where Can I Use This? What Do I Need? 

 AWS 

 AWS account 

 Amazon Machine Image (AMI) ID 

 VM-Series License (PAYG or BYOL) 

 VM-Series plugin 

 Panorama 

 Panorama plugin for AWS 

 You can integrate cloud-native key managers to store certificates. Private
 keys used for certificates are not stored on a firewall’s hard drive, thereby
 eliminating security problems. Administrators retain certificates and private keys
 in cloud storage. The firewall uses AWS Secrets Manager to retrieve the certificates
 and private keys from cloud storage, and uses them for features like decryption and
 IPSec. 

 Only VM-Series firewalls are supported to enable certificate retrieval via AWS
 Secrets Manager. If you're using AWS Secrets Manager certificates, you can’t
 downgrade to an earlier version of PAN-OS. 

 For outbound and inbound decryption, upload the certificates to the native key
 manager and provide the required access permissions to the NGFW. 
 An NGFW on a public
 cloud can use AWS Secrets Manager for storing certificates. With such cases, the
 required access management policies are configured, using PAN-OS or the CLI, for the
 same instances. 

 For environments using autoscaling, an instance boots up in a state with the
 necessary certificates retrieved and ready to decrypt traffic without additional
 manual configuration. 

 When a certificate is updated in the cloud, it must be reimported as a new
 certificate onto the firewall. Assign IAM roles to an instance to enable the
 instance to retrieve certificates from the AWS Secrets Manager store. The IAM role
 must have Get permission for Secrets from AWS Secrets Manager. 

 All certificates are deleted when a master key changes and then refetched upon
 commit. When the configuration is synchronized to the passive firewall under HA,
 the certificate is automatically downloaded by the management daemon on the
 passive firewall. As a result, the certificate itself isn’t synchronized. 

 In the AWS Management Console, create an IAM role or select a role that was
 previously created. The IAM role you use must have read and write
 privileges. 

 Select the IAM Role policy in
the Instances section of the AWS Console
to view the Secrets Manager . 

 In the Permissions tab, select
the Secrets Manager . You’ll use this screen
to view public and private keys. 

 In the Secrets screen, select
the name of the secrets file associated with the IAM role. 

 In the Secret field, select Key/value to
display the private and public key. Both keys should be the same.
Additionally, private or public keys must match the format AWS expects
in Secrets Manager. If the format does not match, key retrieval
fails. 

 The Rotation configuration option must be Disabled.
 This feature isn’t supported. 

 Return to your resource group and select the VM-Series
firewall. Click Identity > User Assigned and
add the Managed Identity . 

 Return to Secrets Manager and select Certificates .
Import your certificate. 

 Log in to the VM-Series firewall. 

 Select Device > Certificate Management > Certificates
> Import . 

 Under Cloud , enter the certificate
name and set the file format. 

 Select Cloud , choose AWS from
the Cloud Platform drop-down: 

 Enter the Certificate Name ;
copy this from the Certificate Name field
in AWS Secrets Manager > Secrets . 

 Select AWS for the Cloud Platform . 

 Enter the Cloud Secret Name ;
copy this from Secret name field in AWS Secrets
Manager > Secrets . 

 You can specify the Algorithm in
the Certificate Information screen. Choose the algorithm
for your configuration, either RSA or Elliptical Curve
DSA . By default, the algorithm is set to use RSA . Configure
the certificate to use either Forward Trust Certificate , Forward
Untrust Certificate , or Trusted Root CA . You can alternately
select all algorithms for the certificate. 

 Click OK . 

 Commit your changes. 

 Verify that the certificate was added successfully: 

 Select Device > Certificate Management
> Certificates . 

 Your new certificate should be listed. 

 Certificate details are not displayed in the Certificates 
 screen.
To view this information in the CLI, use the command: 

 show shared certificate <cert-name> 

 Certificate details are not displayed in the Certificates 
 screen.
 To view this information in the CLI, use the command:

 show shared certificate <cert-name> 

 You can
 confirm the configuration of certificate integration in Panorama. Use the
 Device Certificate window to determine if the certificate is
 used. Keep in mind that because data isn’t stored in the running
 configuration (the hard drive), all fields in the Device Certificates
 table are empty, except for the Usage field (if configured) and
 the Cloud Secret Name . 

 Previous 

 AWS Shared VPC Monitoring 

 Next 

 Use Case: Secure the EC2 Instances in the AWS Cloud 

 On This Page 

 Activation and Onboarding 

 Strata Cloud Manager 

 Next-Generation Firewalls 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 VM-Series 

 Plugins 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 AI Access Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Shared Policy for NGFWs and Prisma Access 

 IPSec VPN 

 Security Policy 

 Quantum Security 

 Endpoints 

 GlobalProtect 

 Resources 

 All Release Notes 

 Compatibility Matrix 

 Experts Corner 

 Cloud Infrastructure Protection 

 Network Security 

 Deployment 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
