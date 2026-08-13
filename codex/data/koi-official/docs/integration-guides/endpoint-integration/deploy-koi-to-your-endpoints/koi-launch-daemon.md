<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/koi-launch-daemon.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/koi-launch-daemon.md).

# Koi Launch Daemon

### Overview

The launch daemon:

* Starts automatically at system boot (`RunAtLoad: true`)
* Repeats execution of the script package at a specific interval
* Logs output to `/var/log/koi.security.mdm.out`
* Logs errors to `/var/log/koi.security.mdm.err`

#### Prerequisites

Before installing the Koi package, you must configure `CUSTOMER_ID` and `XT_ENV` in the `koi.security.mdm` defaults. These values are available in your deployment portal.

For MDM deployments, refer to your specific MDM integration guide for detailed configuration steps.

For manual installation, run the following commands before installing the package:

```bash
sudo defaults write koi.security.mdm CUSTOMER_ID 'your_customer_id'
sudo defaults write koi.security.mdm XT_ENV 'your_xt_env'
```

(optional, the default is 1 hour) In order to set the Interval time, add this interval parameter (in seconds):

```bash
sudo defaults write koi.security.mdm INTERVAL 3600
```

### Installation

Koi provides a `.pkg` file that installs:

* The script package at `/usr/local/bin/koi.security.mdm.sh`
* The launch daemon plist at `/Library/LaunchDaemons/koi.security.mdm.plist`
* Automatically loads the daemon

The package can be deployed through MDM solutions (Jamf, Kandji, etc..) or installed manually:

```bash
sudo installer -pkg koi-security-mdm.pkg -target /
```

### Verify Installation

**Check if daemon is loaded:**

```bash
sudo launchctl list | grep koi.security
```

**Verify plist syntax:**

```bash
plutil -lint /Library/LaunchDaemons/koi.security.mdm.plist
```

**View logs:**

```bash
tail -f /var/log/koi.security.mdm.out
tail -f /var/log/koi.security.mdm.err
```

### Uninstall

To remove the Koi Launch Daemon, follow the macOS steps in [Uninstall Koi](/integration-guides/endpoint-integration/uninstall-koi.md). The uninstall script reverts Koi-managed configurations, stops and unloads the launch daemon, clears any launchd overrides, removes all installed files, and verifies that no Koi components remain.

#### Verify Uninstallation

Contact technical support to request the verification script, which confirms the agent has been fully removed.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/koi-launch-daemon.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
