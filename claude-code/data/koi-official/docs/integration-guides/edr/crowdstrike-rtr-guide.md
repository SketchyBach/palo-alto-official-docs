<!-- KOI source: https://docs.koi.ai/integration-guides/edr/crowdstrike-rtr-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/edr/crowdstrike-rtr-guide.md).

# CrowdStrike RTR Guide

This guide provides step-by-step instructions to configure CrowdStrike Falcon to distribute Koi script package via Real Time Response (RTR).

> 📘 Koi's Python-based script package is executed via lightweight bootstrap scripts written in PowerShell (for Windows), zsh (for macOS), and bash (for Linux), as supported by CrowdStrike RTR

### Prerequisites

1. Access to the CrowdStrike Falcon console with RTR permissions
2. Download your Koi script package from the deployment portal
3. The Falcon Sensor installed and active on target endpoints

### Method 1: Deploy Koi Agentless

#### 1. Upload Scripts to the Falcon Put Files Library

Complete this step for each platform (Windows, macOS).

Navigate to **Host setup and management > Response scripts and files > Put files** and click **+ Upload file**.

Upload the Koi agentless script you downloaded from the deployment portal and give it a unique file name:

| Platform | Upload as    | Notes                            |
| -------- | ------------ | -------------------------------- |
| Windows  | `Koi.ps1`    | The PowerShell bootstrap script. |
| macOS    | `koi_mac.sh` | The zsh/bash bootstrap script.   |

<details>

<summary><strong>Windows only - also upload a launcher</strong></summary>

The **Put and run file** action can't execute a `.ps1` directly, so upload a one-line batch launcher named `ps1_launcher.bat` that runs the PowerShell script for us:

```bat
start /b powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File "%~1"
```

</details>

#### 2. Create the Fusion Workflow to Run in Cadence

Build a **separate workflow for each OS** - repeat the steps below once for Windows and once for macOS. Each workflow schedules a device query every hour, loops through the detected sensors, and runs the Koi script on devices of its target platform.

Navigate to **Fusion SOAR > Workflows** and click **Create workflow > Create workflow from scratch**.

**Configure the Trigger**

* Choose **Scheduled workflow**
* Set the interval to **Hourly**

**Add the Device Query**

* Add an **Action** and select **Device Query** (Get Devices by Filter)
* Define your FQL filter to select the target devices, for example: `last_seen:>'-1d'` (devices seen in the last day)
* This will output a list of Sensor IDs (Devices) for the loop

**Start the Loop**

* Add a **Loop**
* Set **Loop Type** to **For Each**
* Set **Loop Source** to **Sensor IDs**
* Set **Processing order** to **At the same time / concurrently**
* Inside the loop, add an **Action** **-** **Get Device Details**, with **Device ID** set to **Sensor IDs instance**

**Add the platform condition**

* Add a **Condition** set to **Platform equals to** the OS this workflow targets (**Windows** or **Mac**)
* Inside the **If** branch, add the deployment action(s) for that OS, as shown below

Add actions to run the script:

<details>

<summary><strong>Windows deployment actions</strong> (add in sequence inside the If branch):</summary>

1. **RTR: Put Files** - select `Koi.ps1`, set **Device ID** to **Sensor IDs instance**, set **Target directory** to `C:\Windows\Temp\`, and set **Queue offline** to **true**
2. **RTR: Put and run file** - select `ps1_launcher.bat`, set **Device ID** to **Sensor IDs instance**, set the command-line parameters to `C:\Windows\Temp\Koi.ps1`, and set **Queue offline** to **true**
3. **RTR: Remove file** - set **Device ID** to **Sensor IDs instance**, set **File path** to `C:\Windows\Temp\Koi.ps1`, and set **Queue offline** to **true** (cleanup)

</details>

***

<details>

<summary>M<strong>acOS deployment action</strong> (add inside the If branch):</summary>

**RTR: Put and run file** - select `koi_mac.sh`, set **Device ID** to **Sensor IDs instance**, and set **Queue offline** to **true**

</details>

**End Loop**

* No action required here

Click **Save and exit** and give the workflow a name (e.g., `"Koi Deployment - Windows"`). Be sure to set the status to **On**.

You can verify the workflow was created successfully by navigating to **Workflows** and clicking **Execute Workflow** on the selected workflow.

This is generally how a single-platform workflow should look like at the end:

<figure><img src="/files/9yIO77oCW8DDpOEw971g" alt=""><figcaption></figcaption></figure>

### Method 2: Deploy Koi Installer

> !! Do steps 1 and 2 for each platform !!

#### 1. Upload Installer Files to RTR

1. Navigate to **Host setup and management > Response scripts and files > Put files**
2. Click **+ Upload file**
3. Click **Upload file** and select your Koi MSI installer
4. Give the file this exact name: (you will use it later)
   * Windows: `koi_installer.msi`
   * MacOS: `koi_installer.pkg`
5. Click **Create**

#### 2. Create Installation Scripts

Create RTR scripts to install the packages:

1. Click **+ Create script** again
2. Set **Script name** to `"Install Koi MSI"`/`"Install Koi PKG"`
3. Set **Shell type**
   1. Windows: **PowerShell**
   2. MacOS: **zsh**
4. Under **Script access** select **Users with the role of RTR Administrator or RTR Active Responder**
5. Check the box **Share script with workflows**
6. **Windows**

   ```powershell
   # Custom MSI properties
   $CustomerId   = "<YOUR_CUSTOMER_ID>"
   $CustomerSlug = "<YOUR_CUSTOMER_SLUG>"
   # Interval for the script execution, in minutes.
   $Interval     = "60"

   # Install Koi MSI and clean up
   $installerPath = "C:\Windows\Temp\koi_installer.msi"

   try {
       # Build msiexec arguments
       $arguments = @(
           "/i `"$installerPath`""
           "CUSTOMERID=$CustomerId"
           "CUSTOMERSLUG=$CustomerSlug"
           "INTERVAL=$Interval"
           "/qn"
           "/norestart"
       ) -join " "

       Start-Process -FilePath "msiexec.exe" `
                     -ArgumentList $arguments `
                     -Wait `
                     -NoNewWindow

       Write-Output "Koi installation completed"

       # Remove the installer
       if (Test-Path $installerPath) {
           Remove-Item -Path $installerPath -Force
           Write-Output "Installer cleaned up"
       }
   } catch {
       Write-Output "Error during installation: $_"
   }
   ```
7. **MacOS**

   ```zsh
   #!/bin/zsh
   # Install Koi PKG and clean up
   installer_path="/tmp/koi_installer.pkg"

   CUSTOMER_ID="<YOUR_CUSTOMER_ID>"
   XT_ENV="<YOUR_ENVIRONMENT>"

   sudo defaults write koi.security.mdm CUSTOMER_ID "$CUSTOMER_ID"
   sudo defaults write koi.security.mdm XT_ENV "$XT_ENV"

   # Install the PKG
   sudo installer -pkg "$installer_path" -target /

   if [ $? -eq 0 ]; then
       echo "Koi installation completed"
       
       # Remove the installer
       if [ -f "$installer_path" ]; then
           rm -f "$installer_path"
           echo "Installer cleaned up"
       fi
   else
       echo "Error during installation"
   fi
   ```

   Click **Create**

#### 3. Create the Fusion Workflow for Package Installation

This workflow uploads the installer file to each device, then runs a single script that installs and cleans up automatically.

1. Navigate to **Fusion > Workflows**
2. Click **Create workflow** and choose **Create workflow from scratch**
3. Configure the **Trigger**
   1. Choose **Scheduled workflow**
   2. Set the interval to **Daily** or whatever suits your needs
4. Add **Action** and select **Device Query** (Get Devices by Filter)
   1. Define your FQL filter to select the target devices, for example:
      * `last_seen:>'-1d'` (devices seen in the last day)
   2. This will output a list of Sensor IDs (Devices) for the loop
5. Start the **Loop**:
   1. Add a **Loop**
   2. Set **Loop Type** to **For Each**
   3. Set **Loop Source** to **Sensor IDs**
   4. Set **Processing order** to **At the same time / concurrently**
6. Inside the loop, add **Action**
   1. Add **Get Device Details**
   2. Set **Device ID** to **Sensor IDs instance**
7. Add platform-specific conditions using **If/Else If** logic:

   **For Windows:**

   1. Add a **Condition**
   2. Set the condition to **Platform equals to Windows**
   3. Inside the **If** branch, add the following **Actions** in sequence:
      * **Action 1:** Search for **RTR: Put Files** and select your **Windows MSI** file
        * Set **Device ID** to **Sensor IDs instance**
        * Set **Target directory** to `C:\Windows\Temp\`
        * Set **Queue offline** to **false** (or up to you)
      * **Action 2:** Search for your installation script **"Install Koi MSI"**
        * Set **Device ID** to **Sensor IDs instance**
        * Set **Queue offline** to **true**

   **For macOS:**

   4. Click **Add Else If** 5. Set the condition to **Platform equals to Mac** 6. Inside the **Else If** branch, add the following **Actions** in sequence:

   * **Action 1:** Search for **RTR: Put Files** and select your **macOS PKG** file
     * Set **Device ID** to **Sensor IDs instance**
     * Set **Target directory** to `/tmp/`
     * Set **Queue offline** to **false** (or up to you)
   * **Action 2:** Search for your installation script **"Install Koi PKG"**
     * Set **Device ID** to **Sensor IDs instance**
     * Set **Queue offline** to **true**
8. **End Loop**
   * No action required here
9. Click **Save and exit** and give the workflow a name
   * Example: `"Koi MSI/PKG Deployment"`
   * Be sure to set the status to **On**
10. You can verify the workflow was created successfully by navigating to **Workflows** and clicking **Execute Workflow** on the selected workflow

***

Depending on how many platform you've configured, this is generally how the workflow should look like at the end:

![](https://files.readme.io/c5a27567afc4ca51a6f40bd2f8a46fc38abb913da9f88d9c64523b0f94a696fb-Screenshot_2025-11-01_at_0.48.22.png)

### Support and Troubleshooting

If you encounter any issues during the integration process, please follow these steps:

1. **Check Logs:**
   * Navigate to **Falcon Console > Activity > Custom Scripts** to view script execution logs
   * Verify the workflow execution status in **Fusion > Workflows > Execution Logs**
2. **Verify Configuration:**
   * Ensure scripts are properly uploaded and shared with workflows
   * Confirm the workflow trigger is set to **On**
   * Check that device filters are correctly configured


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/edr/crowdstrike-rtr-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
