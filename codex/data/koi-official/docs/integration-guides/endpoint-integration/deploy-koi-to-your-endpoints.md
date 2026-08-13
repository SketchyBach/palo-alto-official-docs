<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints.md).

# Deploy Koi to your endpoints

Go to Settings → Deployment and start a new deployment. Koi asks you five things, then builds your script.

#### Step 1 - Generate your script

**1. Deployment method** Choose the MDM or EDR your organization uses to deploy software to devices: Jamf, Intune, Kandji, SCCM, Hexnode, Workspace ONE, Salt, CrowdStrike, SentinelOne, Cortex, FleetDM, or Tanium. Don't use any of these? Choose **Manual**.&#x20;

**2. OS** Choose the operating system of the devices you want to protect, for example **macOS**.

**3. Installation Method** Choose how Koi runs on the device:

* **Agentless** - the lightweight script, scheduled and run by your existing MDM or EDR. Koi uses the deployment infrastructure you already have, with no extra agent to install.
* **Installed** - A native service (macOS Launch Daemon or Windows Service) that runs the script and manages its own schedule. You deploy it once, then it takes over.

**4. Type** Choose the format of the script:

* **Script Package** - a readable script (Python, with Bash wrappers for macOS/Linux and PowerShell for Windows). This pairs with Agentless.
* **Binary** - a compiled binary version of the script.

**5. Version updates** Choose how the script stays current:

* Leave on **Automatic** so Koi keeps the script up to date. This is **Managed mode**: a lightweight wrapper fetches the latest signed script automatically, so the installed service stays current with zero maintenance.&#x20;
* Turning it off uses **Manual mode**, where you re-download the script from the portal yourself when new versions are released.&#x20;
* For more info See [Auto-Update Vs. Manual modes](/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/managed-vs-manual-modes.md).

<figure><img src="/files/r2IDoYAJP94uPZXMySxI" alt=""><figcaption></figcaption></figure>

<details>

<summary><strong>If you choose Agentless</strong></summary>

{% stepper %}
{% step %}

### Step 1 - Download your script

Select **Download** to save the Koi script package.
{% endstep %}

{% step %}

### Step 2 - Deploy your script through your MDM or EDR

Koi shows the exact steps for the tool you chose.

For example In Jamf:

* **Upload the script and create a reccuring policy**

<figure><img src="/files/oC5mQONQhjlaAKaBgNWV" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/WbDVmCRrmvVAwTjYs7Jv" alt=""><figcaption></figcaption></figure>

{% endstep %}
{% endstepper %}

</details>

***

<details>

<summary><strong>If you choose Installed</strong></summary>

Choose **Installed** when you want Koi to run as a native service on the device and manage its own schedule, instead of relying on a recurring MDM or EDR policy. The service runs as the **macOS Launch Daemon** or the **Koi Windows Service**. You deploy it once, and from then on the service runs the Koi script on its own, no recurring policy needed.

Installed is a good fit when you don't use one of the supported MDM or EDR tools, or you prefer to install Koi directly on the device.

{% stepper %}
{% step %}

### Step 1 - Download your script

Select **Download** to get the installer, the Koi package (`.pkg`) on macOS or the Koi installer (`.msi`) on Windows.

<figure><img src="/files/NKIkJTtxfjy4ytsM7b3B" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Step 2 - Install on the device

Koi shows the exact steps and commands for the operating system you chose. Copy them straight from your UI, the code comes pre-filled with your customer ID, so you don't have to fill anything in by hand.

* macOS - install the Koi package (`.pkg`). For more detail see [Koi Launch Daemon](/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/koi-launch-daemon.md).
* Windows - install the Koi installer (`.msi`). For more detail see [Koi Windows Service](/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/koi-windows-agent.md).

When the install finishes, the Koi service starts on its own and runs the script on the interval you set (the default is **1 hour**).

For example In Intune:

<figure><img src="/files/J9viKO0bcIptl9kmLj2X" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/nzIHGetBpLKFB9SoG6At" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/1tI3XgP13hbYKdhw4ZI5" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

</details>

#### Confirm your devices are connected

Once the policy runs on your devices, they start reporting to Koi. Go back to **Settings → Deployment** to confirm everything is working.

**Check the overall status**

* The deployment shows a **Deployed** badge when it's live.
* **Covered endpoints** shows how many devices are connected, with a coverage bar so you can see your progress at a glance.

**Check each script**

Under **Scripts**, every script you deployed appears in its own row, showing the operating system, the number of **Endpoints** reporting to it, and a **Running** status. **Running** means devices are actively checking in with that script.

<figure><img src="/files/dquu7f1Qq3pps3z9Rdh4" alt=""><figcaption></figcaption></figure>

**See which devices are connected**

Select the arrow on any script (or **See endpoints**) to open **Covered endpoints**, where you can see every device that script reached:

* **Hostname** - the device name.
* **Last seen** - when the device last reported to Koi.
* **Registered at** - when the device first connected.
* **Script version** - the version of the Koi script running on it.
* **Serial** - the device serial number.

<figure><img src="/files/p6NjHYvTcUsVjnTGRjVb" alt=""><figcaption></figcaption></figure>

#### Step 5 - Roll out to the rest of your devices

When your test group looks healthy, widen the policy **Scope** in your MDM or EDR to the rest of your devices.

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
