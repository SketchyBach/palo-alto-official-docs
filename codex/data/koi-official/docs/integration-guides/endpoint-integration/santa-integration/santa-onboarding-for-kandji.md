<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration/santa-onboarding-for-kandji.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration/santa-onboarding-for-kandji.md).

# Santa onboarding for Kandji

Koi integrates with Santa to collect binary execution telemetry on **macOS devices only**.\
As part of the initial onboarding, customers need to complete **two steps** to ensure Santa is installed and connected to Koi.

***

### Prerequisites

* macOS devices managed by an MDM solution (Jamf, Kandji, Intune, Workspace ONE, etc.)

***

### How to get started?

This guide walks through the Santa integration setup for **Kandji**.

#### Step 1 - Install and deploy Santa

Install and deploy Santa to start collecting execution events from your endpoints.

**1) Download the Santa installer**

Santa is distributed as a **DMG** that contains a **signed PKG**.\
Download the DMG from the Northpole repository:

```
https://github.com/northpolesec/santa/releases/tag/2026.1
```

**2) Upload the DMG to Kandji**

Upload the PKG to Kandji:

1. In Kandji, navigate to **Library > Add Library item > Custom App**.
2. Click **Add and configure**.
3. Under **Blueprints,** assign it to your desired blueprint
4. Under the **Install Details**, choose a **Disk Image**.
5. Click **Choose File** and upload the `santa-2026.1.dmg`.
6. Click **Save**

<figure><img src="/files/iocEr9ydnBKXMjdREnzo" alt=""><figcaption></figcaption></figure>

***

#### Step 2 - Deploy the Koi Santa configuration profile

**1) Download the configuration profile from the Koi Deployment portal**

1. Go to the **Deployment portal** (**Settings > Deployment**).
2. Choose **Kandji** MDM
3. **Download** the .mobileconfig file.

<figure><img src="/files/aIhY92tMOShnbRlnUYJm" alt=""><figcaption></figcaption></figure>

**2) Upload the file to Kandji and configure required permissions**

**Create the configuration profile**

1. In Kandji, go to **Library > Add Library Item -> Custom Profile**.
2. Click **Add and configure**.
3. Under **Blueprints,** assign it to your desired blueprint
4. Upload the downloaded .mobileconfig file.

<figure><img src="/files/QK91z0ECWZtUTNw13vBT" alt=""><figcaption></figcaption></figure>

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
GET https://docs.koi.ai/integration-guides/endpoint-integration/santa-integration/santa-onboarding-for-kandji.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
