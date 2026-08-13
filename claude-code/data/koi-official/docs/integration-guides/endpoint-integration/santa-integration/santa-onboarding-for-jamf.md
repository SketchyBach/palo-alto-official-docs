<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration/santa-onboarding-for-jamf.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration/santa-onboarding-for-jamf.md).

# Santa onboarding for Jamf

Koi integrates with Santa to collect binary execution telemetry on **macOS devices only**.\
As part of the initial onboarding, customers need to complete **two steps** to ensure Santa is installed and connected to Koi.

***

### Prerequisites

* macOS devices managed by an MDM solution (Jamf, Kandji, Intune, Workspace ONE, etc.)

***

### How to get started?

This guide walks through the Santa integration setup for **Jamf Pro**.

#### Step 1 - Install and deploy Santa

Install and deploy Santa to start collecting execution events from your endpoints.

**1) Download the Santa installer**

Santa is distributed as a **DMG** that contains a **signed PKG**.\
Download the DMG from the Northpole repository:

```
https://github.com/northpolesec/santa/releases/tag/2026.1
```

**2) Upload the PKG to Jamf Pro**

Upload the PKG to Jamf Pro:

1. In Jamf Pro, navigate to **Settings > Computer Management > Packages**.
2. Click **+ New**.
3. Under the **General** tab, choose a **Display Name**.
   * Example: `"Santa 2024.9"`
4. Click **Choose File** and upload the `santa-2024.9.dmg`.

**3) Create a deployment policy**

1. Navigate to **Computers > Policies**.
2. Click **+ New**.
3. Under the **General** payload:
   * Choose a **Display Name**.
     * Example: `"Deploy Santa"`
   * Set **Trigger** to **Recurring Check-in**.
   * Set **Execution Frequency** to **Once per computer**.
4. Click on the **Packages** payload in the left sidebar.
   * Click **Configure**.
   * Find and add the **Santa 2024.9** package.
   * Set **Action** to **Install**.
5. (Optional) Click on the **Scope** tab.
   * Scope the policy to the relevant Mac devices (typically **All Managed Clients** or a specific smart group).

***

#### Step 2 - Deploy the Koi Santa configuration profile

**1) Download the configuration profile from the Koi Deployment portal**

1. Go to the **Deployment portal** (**Settings > Deployment**).
2. Choose **Jamf** MDM
3. **Download** or **Copy** the XML file.

<figure><img src="/files/5eToXA9hVYc8vYQ1GNw8" alt=""><figcaption></figcaption></figure>

**2) Upload the file to Jamf Pro and configure required permissions**

**Create the configuration profile**

1. In Jamf Pro, go to **Computers > Configuration Profiles**.
2. Click **+ New** (top right).
3. Create an **empty** profile.

<figure><img src="/files/2EFGuwiBDteoBnpgej9T" alt=""><figcaption></figcaption></figure>

**Upload the custom settings payload**

1. Go to **Application and Custom Settings > Upload**.
2. Under **Preference Domain**, enter:\
   `com.northpolesec.santa`
3. Upload or paste the XML file.

<figure><img src="/files/WQvH0761aSOAqou2Ofjd" alt=""><figcaption></figcaption></figure>

**Configure Privacy Preferences Policy Control**

1. Go to **Privacy Preferences Policy Control**.
2. Add the following entry:
   * **Identifier:** `com.northpolesec.santa.daemon`
   * **Identifier Type:** *Bundle ID*
   * **Code Requirement:** paste the following:

```
identifier "com.northpolesec.santa.daemon" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZMCG7MLDV9
```

* Under **APP OR SERVICE**, choose **SystemPolicyAllFiles** and set it to **Allow**.

<figure><img src="/files/9yUc2EZ3x5WhrcpXP9Vp" alt=""><figcaption></figcaption></figure>

Repeat the same for:

* **Identifier:** `com.northpolesec.santa.bundleservice`
* **Code Requirement:**

```
identifier "com.northpolesec.santa.bundleservice" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = ZMCG7MLDV9
```

<figure><img src="/files/nSGpJJPE8aMlX69rUKw6" alt=""><figcaption></figcaption></figure>

**Configure System Extensions**

1. Go to **System Extensions**.
2. Add the Northpole **Team ID**:\
   `ZMCG7MLDV9`

<figure><img src="/files/e8pufR4t1VVm0jbHMgBm" alt=""><figcaption></figcaption></figure>

**(Optional) Scope the profile**

1. Go to **System Extensions > Scope**.
2. Assign it to the same Mac scope as the Santa deployment policy (for example, *All Managed Clients*).

***

### Validate the integration

After both steps are deployed, validate Santa is installed and responsive:

```bash
santactl version
santactl status
```

#### In the Koi portal

* Go to the **Binary Events** page and confirm you start seeing events from Mac devices.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration/santa-onboarding-for-jamf.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
