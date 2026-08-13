<!-- KOI source: https://docs.koi.ai/integration-guides/remote-development-environments/coder/deploying-koi-on-coder-workspaces.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/remote-development-environments/coder/deploying-koi-on-coder-workspaces.md).

# Deploying Koi on Coder workspaces

Coder workspaces are ephemeral Linux environments, but the software inside them - IDE extensions, CLIs, agent plugins - is just as much a part of your fleet as anything running on any other workstation. \
This guide walks through running the Koi MDM script package inside each workspace on a schedule, so every Coder workspace is protected by the full Koi suite just like the rest of your endpoints - Discovery, Governance, and Remediation.

This guide provides two methods: baking the script into your workspace image, or wiring it in through Terraform. Pick whichever fits how your team manages Coder.

***

### Requirements

* Linux workspace with `python3`, `curl`, and `sudo` installed
* Non-root user with passwordless `sudo` (see build/Dockerfile)
* Outbound HTTPS to Koi API

***

### Get the script

In the Koi platform, go to **Settings → Deployment** and click **Deploy new script**. Make the following selections in the wizard:

<table><thead><tr><th width="371.7265625">Step</th><th>Selection</th></tr></thead><tbody><tr><td>Deployment method</td><td><strong>Manual</strong></td></tr><tr><td>OS</td><td><strong>Linux</strong></td></tr><tr><td>Installation Method</td><td><strong>Agentless</strong></td></tr><tr><td>Type</td><td><strong>Script Package</strong></td></tr><tr><td>Version updates</td><td><strong>On</strong> (recommended — auto-updates)</td></tr></tbody></table>

Click **Next**, then **Download**. You get an `mdm.pyz.sh` file pre-configured for your tenant.

***

### Install options

Choose one of the two patterns below. Both run the script hourly inside the workspace; the difference is whether the script ships in the image or is pulled in by Terraform at provision time.

#### Option 1 — Bake into the Dockerfile + cron

Best when you maintain your own Coder workspace images and want the script present the moment the workspace boots, with no Terraform changes.

Copy `mdm.pyz.sh` next to your Dockerfile, then:

```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends cron \
 && rm -rf /var/lib/apt/lists/*

COPY mdm.pyz.sh /opt/koi/mdm.pyz.sh
RUN chmod +x /opt/koi/mdm.pyz.sh

RUN echo "0 * * * * coder /opt/koi/mdm.pyz.sh >/var/log/koi-mdm.log 2>&1" \
      > /etc/cron.d/koi-mdm \
 && chmod 0644 /etc/cron.d/koi-mdm
```

Start `cron` at workspace boot via your Coder agent `startup_script`:

```hcl
resource "coder_agent" "main" {
  startup_script = "sudo service cron start"
}
```

#### Option 2 — Terraform `coder_script`

Best when you'd rather keep the script out of the image and manage it alongside your Coder templates. Drop `mdm.pyz.sh` next to your `.tf` files and reference it from a `coder_script` resource — no image changes needed:

```hcl
resource "coder_script" "koi_mdm" {
  agent_id     = coder_agent.main.id
  display_name = "Koi MDM"
  run_on_start = true
  cron         = "0 * * * *"   # hourly
  script       = file("${path.module}/mdm.pyz.sh")
}
```

***

### Verify the install

After the first scheduled run - usually expected within a few hours - each Coder workspace should appear as a managed endpoint in your Koi portal inventory, with the discovered items inside it listed in the inventory and item reports.

If a workspace doesn't surface:

* **Option 1** — check `/var/log/koi-mdm.log` inside the workspace for script errors, and confirm `cron` is running (`service cron status`).
* **Option 2** — open the workspace in Coder and review the `Koi MDM` script logs in the agent panel.
* In both cases, confirm the workspace can reach the Koi API over outbound HTTPS.

Once the first report lands, the workspace is treated like any other endpoint — visible in inventory, scored by Wings, and available to query and alert on alongside the rest of your fleet.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/remote-development-environments/coder/deploying-koi-on-coder-workspaces.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
