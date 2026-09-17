---
url: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference/custom-cortex-checks-and-signature-verification
fetched_at: 2026-09-16T08:46:32Z
source: cortex-platform
---

# Custom Cortex checks and signature verification | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Cortex CLOUD Runtime Security 

 Cortex CLI 

 Cortex CLI for Code Security 

 Cortex CLI Cortex Cloud Application Security command line reference 

 Cortex Cloud Runtime 

 Custom Cortex checks and signature verification 

 Load custom Cortex checks and optionally verify their signatures. 

 Cortex CLI supports custom Cortex checks from a local directory or Git repository. You can optionally verify custom Python checks cryptographically before the CLI loads them. 

 Overview 

 Use --external-checks-dir or --external-checks-git to load custom Cortex checks. To verify their integrity and authenticity, use --external-checks-public-key . 

 Supported flags 

 --external-checks-dir : Specifies a local directory containing custom checks. 

 --external-checks-git : Specifies a Git repository containing custom checks. 

 --external-checks-public-key : Specifies the public key file used to verify signed checks. You can repeat this flag to support key rotation. 

 Enforcement and exit codes 

 Signature verification is opt-in. CLI behavior depends on whether you provide a public key and whether the check signature is valid 

 No verification: Without a public key, the CLI loads checks without verification. The scan runs normally. It returns exit code 1 if it finds scan issues 

 Successful verification: With a valid public key and a correctly signed check, the scan runs with signature verification enabled. It returns exit code 1 if it finds scan issues 

 Wrong key: If the check uses a different private key, the CLI refuses the scan before custom code runs. It returns exit code 2 

 Tampered file: If a signed check changes after signing, verification fails. The CLI refuses the scan and returns exit code 2 

 Workflow: Sign and verify custom checks 

 1. Generate a P-256 key pair 

 Keep private.pem secret. 

 2. Sign the custom check (.py) and append the trailer 

 3. Run the scan with the matching public key 

 Previous Cortex CLI Cortex Cloud Application Security command line reference 

 Next Cortex CLI pre-commit hooks 

 Last updated 2 days ago 

 Was this helpful?
