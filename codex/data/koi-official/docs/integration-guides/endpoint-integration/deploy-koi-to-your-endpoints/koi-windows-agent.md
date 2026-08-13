<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/koi-windows-agent.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/koi-windows-agent.md).

# Koi Windows Service

Koi provides a service that runs on Windows endpoints, giving you full control and visibility into the device’s status and activity.

### Installation

You will be provided with a MSI installer (will be referenced as `Koi.msi`).

To install the service, run the following command:

```shell
msiexec /i Koi.msi CUSTOMERID='<customer_id>' CUSTOMERSLUG='<customer_slug>'
```

* The `/qn` signals a quite installation.
* The service runs periodically, by default the interval is 1 hour.<br>

To change the default interval, install with the following command:

```shell
msiexec /i Koi.msi INTERVAL=<interval_in_minutes>
```

### Updating the MSI&#x20;

To update the MSI package, simply run the same installation command&#x20;

```shellscript
msiexec /i Koi.msi /qn
```

### Starting the Service

By default, the service is installed in `automatic` mode and starts after installation.&#x20;

The Windows Service name is: `KoiService`.

It is possible to control the service using the `sc.exe` tool.

To start the service run the following command (make sure you are running it as an administrator):

```shell
sc.exe start KoiService
```

Check it started correctly with:

```shell
sc.exe query KoiService
```

To stop the service run:

```shellscript
sc.exe start KoiService
```

### Uninstalling the Koi Service

Uninstalling the Koi service can be executed in two ways:&#x20;

1. Removing the service and its related files&#x20;
2. Rolling back any deployed configuration that was made by the script and then deleting the service and its related files.

To simply remove the service run the following:

```shell
msiexec /x Koi.msi
```

To rollback and then remove the service run the following:&#x20;

```shellscript
msiexec /x Koi.msi ROLLBACK=yes
```

**Notes**

* It is recommended to remove the service using an MDM / EDR tool that properly supports removing software using the Microsoft Installer App.

### Updating script package run via the service

The service will be updated according to the [mode of the script package](/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/managed-vs-manual-modes.md) you chose working with.

* Manual
  * Download the latest version of `mdm.ps1` from the deployment portal.
  * Save it to `C:\ProgramData\Koi` installation folder.
* Managed - will get updated automatically.

### Debugging the installation

After the installation, verify the following:

* The installation folder `C:\ProgramData\Koi` exists.
* It contains `KoiService.exe` and `mdm.ps1`.
* A service named `KoiService` is registered (Open `services.msc` or run `sc.exe query KoiService`).
* A `KoiService.log` file appears in the installation folder once the service is running.

To generate a detailed installation log, run:

```shell
msiexec /i Koi.msi CUSTOMERID='<customer_id>' CUSTOMERSLUG='<customer_slug>' /l*v "<path to installation log>"
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/koi-windows-agent.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
