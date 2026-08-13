Source: https://docs.koi.ai/integration-guides/edr/palo-alto-cortex-xdr.md

# Palo Alto Cortex XDR

This guide provides step-by-step instructions to deploy the Koi Script Package to your managed endpoints using Palo Alto Networks Cortex XDR.

***

## Prerequisites

* **Access to the Cortex XDR Management Console with permissions** to create and run scripts.
* **Python Script Package** - found in your Deployment Portal.
* **Endpoints with Cortex XDR Agent** installed and active.

***

## Step 1: Download the Koi Script

1. **Log in to the Koi Deployment Portal**.
2. **Download the correct version** for each operating system you plan to deploy to (e.g., Windows, macOS).
   1. If your environment includes multiple OS types, ensure you download all relevant versions to cover your deployment needs.
3. **Keep the Script Package unmodified** unless instructed by Koi Support.

### Optional - Test the Script Locally

1. **Ensure Python 3.8+ is installed** on your test machine.
2. **Run the script** through Python.
3. **Review Koi's deployment portal**.
   1. You should see your endpoint under the Endpoints section.
   2. **Review the output or logs** to verify the script completes successfully. This step ensures that no environment-specific issues block deployment.

***

## Step 2: Upload the Script to Cortex XDR

1. Log in to Cortex XDR Console.
2. Navigate to **Incident Response → Response → Action Center → Agent Script Library**.
3. Click **+ New Script**.
4. **Upload** the Script Package.
5. **Fill out** the necessary details in the form:
   1. Name: Koi Script Package.
   2. Description: Deploy Koi Script Package for endpoint registration, discovery, or remediation tasks.
   3. Supported OS: Make sure you have uploaded the correct script for the OS.
6. Save the script. It will now be available in the Script Library.

***

## Step 4: Deploy the Script Manually

1. Go to **Incident Response → Response → New Action → Run Endpoint Script**.
2. **Choose Koi's Script Package**, defined in "Step 2: Upload the Script to Cortex XDR".
3. **Select one or more** target endpoints.
4. Click **Next**.
5. Click **Run and wait for completion**.
6. **Review the execution results** to confirm success.
   1. See the endpoints under the Endpoints section in Koi's Deployment Portal..

***

## Step 5: Orchestrating Recurring Execution

Cortex XDR’s native interface allows on-demand execution only.

For recurring, automated execution at scale, organizations typically integrate with:

* Cortex XSOAR Playbooks (for scheduling and orchestration).

  OR
* Custom scripts or tools calling the XDR public API (advanced use cases).

***

## Step 6: Uninstall Koi (Rollback)

Run rollback on each endpoint (Administrator on Windows, `sudo` on macOS). Cortex XDR’s Run Endpoint Script action cannot uninstall Koi by itself, it always runs in normal discovery mode.

**Windows:** use the Cortex script you already have:

`$env:KOI_ROLLBACK = "1"`\
`python "C:\path\to\mdm-cortex.py"`

If anything remains, download `mdm.pyz.ps1` from the Deployment Portal (standard package, not the Cortex wrapper) and run:

`powershell -ExecutionPolicy Bypass -File ".\mdm.pyz.ps1" --rollback`

**macOS:** download `mdm.pyz.sh` from the Deployment Portal (standard package, not `mdm-cortex.py`), then:

`chmod +x mdm.pyz.sh`\
`sudo ./mdm.pyz.sh --rollback`

Verify: `C:\ProgramData\Koi` (Windows) or `/Library/Application Support/Koi` (macOS) is removed, and Koi entries are gone from agent hook files (e.g. Cursor `hooks.json`).

> Note: `mdm-cortex.py --rollback` does not work. On Windows, use the `KOI_ROLLBACK` environment variable as shown above.


---

---
