<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration.md).

# Santa integration

### Santa integration

Koi integrates with Santa to provide **application control** on **macOS devices**.\
It gives you **complete discovery of binary executions** (what ran, where, and by whom) and **enforcement** of what binaries are allowed or blocked across devices in your org.

{% hint style="info" %}
**Onboarding (2 steps):**

1. **Deploy Santa** to your managed Macs (agent install via MDM).
2. **Deploy the Koi Santa configuration profile** (`.mobileconfig`) so Santa is connected to Koi and uses your org’s policy.
   {% endhint %}

***

### Prerequisites

* **macOS devices** managed by an MDM solution (Jamf, Kandji, Intune, Workspace ONE, etc.)

***

### How to get started

This guide walks through the Santa integration setup using any MDM.

{% hint style="info" %}
Onboarding by MDM: \
**Jamf Pro:** Follow the Jamf-specific walkthrough: [Santa onboarding for Jamf](/integration-guides/endpoint-integration/santa-integration/santa-onboarding-for-jamf.md).\
**Kandji:** Follow the Kandji walkthrough: [Santa onboarding for Kandji](/integration-guides/endpoint-integration/santa-integration/santa-onboarding-for-kandji.md).
{% endhint %}

***

### Step 1 - Install and deploy Santa (macOS)

Install and deploy Santa to start collecting execution events from your macOS devices.

#### 1) Download the Santa installer

Santa is distributed as a **DMG** that contains a **signed PKG**.\
Download the latest installer from the Santa releases page:

<https://github.com/northpolesec/santa/releases/tag/2026.1>

#### 2) Deploy Santa using your MDM

In your MDM:

1. Upload the Santa installer (DMG/PKG, depending on what your MDM supports).
2. Create an app deployment policy for **macOS**.
3. (Optional) Scope it to the relevant devices (typically all managed Macs, or a specific device group).
4. Deploy.

***

### Step 2 - Deploy the Koi Santa configuration profile (.mobileconfig)

#### 1) Download the configuration profile from the Koi Deployment portal

1. Go to the **Deployment portal** (**Settings > Deployment**).
2. Download (or copy) the provided Santa configuration profile content.

#### 2) Upload and deploy the configuration profile via your MDM

In your MDM:

1. Create a new **macOS Configuration Profile**.
2. Upload the downloaded `.mobileconfig` file (or paste the XML content into a custom settings payload, based on your MDM capabilities).
3. Ensure the profile is scoped to the same Mac devices as the Santa deployment policy.
4. Deploy.

***

### Required permissions (MDM configuration)

Some environments require additional macOS permissions to allow Santa to operate and report correctly. The exact UI differs per MDM, but the required items are typically:

* **Privacy Preferences Policy Control** entries for Santa services
* **System Extensions** approval (if applicable in your Santa version and macOS policy)

If your MDM requires identifiers, you may need to allow the relevant Santa bundle IDs and Team ID provided by your Santa distribution.

***

### Validate the integration

#### On a Mac endpoint

After both steps are deployed, validate Santa is installed and responsive:

```
santactl version
santactl status
```

#### In the Koi portal

Go to the **Binary Events** page and confirm you start seeing events from macOS devices.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
