Source: https://docs.koi.ai/integration-guides/network/establishing-trust/deploy-koi-root-ca-via-jamf-pro.md

# Deploy Koi Root CA via Jamf Pro

This guide explains how to deploy Koi's PAC file using Jamf Pro. The approach is to use a configuration profile to ensure robustness for the configuration set. Once the PAC file is set the endpoint should route through Koi's proxy for the defined marketplaces.

### Prerequisites

Access to Jamf Pro. An already established method of trust, see Establishing Trust Access to Koi deployment portal.

***

### Steps to integrate

#### Access Jamf Pro

1. Sign in to Jamf Pro (web UI).
   1. Make sure you have an account that can edit Configuration Profiles.
2. Navigate to the Configuration Profiles area.
   1. From the left sidebar select Computers, then Configuration Profiles.

#### Create a new profile (or edit an existing one)

1. Click New (or click the profile you want to modify).
2. In the payload list choose Certificates (or Certificate).
3. Click Upload and select your Root CA file (DER/PEM).
   1. Download Koi's Root CA. The certificate is located in your Koi deployment portal → Network Integration → Establish network trust.
   2. Jamf Pro accepts `DER` format.
   3. `openssl x509 -inform PEM -in {Koi Root CA}.pem -outform DER -out {Koi Root CA}.cer`
4. Name the profile (e.g., Koi Root CA), add description.
5. Switch to Scope and add target computers/groups.
6. Save → devices will receive the cert at next check-in.

#### Set Scope (who gets it)

1. Switch to the Scope tab of the profile.
2. Add target computers (Static Group, Smart Group, or individual devices).
3. Use Exclusions as needed.
4. Deploy; Save/apply the profile (if not already saved). Jamf Pro will deliver the profile at next check-in


---

---
