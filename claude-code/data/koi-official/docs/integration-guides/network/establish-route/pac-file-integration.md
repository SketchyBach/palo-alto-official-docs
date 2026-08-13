<!-- KOI source: https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration.md).

# PAC File Integration

This guide explains how to integrate Koi using **PAC (Proxy Auto-Configuration) files** to selectively route marketplace traffic through Koi's gateway while leaving other traffic unaffected.

***

### **What is a PAC File?**

A **Proxy Auto-Configuration (PAC) file** is a JavaScript function that determines how web requests are handled by browsers and applications. PAC files allow you to:

* **Selective Routing**: Route specific domains through designated proxies
* **Conditional Logic**: Apply different proxy rules based on URL patterns, IP ranges, or other conditions
* **Fallback Options**: Define backup proxy servers or direct connections
* **Dynamic Configuration**: Update proxy settings without manual client reconfiguration

**Key Advantage for Koi:** PAC files enable precise control over which traffic flows through Koi's gateway, ensuring only marketplace domains are intercepted while maintaining normal routing for all other traffic.

***

### **How PAC Files Work with Koi**

When properly configured, the PAC file acts as a traffic director:

1. **User requests software installation** from a marketplace (Chrome Web Store, npm, etc.)
2. **PAC file evaluates the request** against its rules
3. **Marketplace domains** are routed through Koi's gateway for policy enforcement
4. **All other traffic** flows directly or through existing proxies unchanged

This approach provides **surgical precision** - only the traffic that needs Koi's security controls is affected.

***

### **PAC File Distribution Methods**

Koi offers flexible options to suit your existing infrastructure and deployment preferences.

***

{% hint style="info" %}
Code Packages clients (such as npm & pypi) doesn't respect the PAC File and should be configured seperatly.

See [Code Packages](/integration-guides/code-packages.md)
{% endhint %}

***

#### **Method 1: Automatic Distribution via Script-Package**

**Overview:** Koi automatically generates and distributes the PAC file using an automated script package.

**How it works:**

1. Koi generates a customized PAC file for your environment
2. You enable the PAC file deployment via script package in your deployment portal
3. The script-package automatically deploys the PAC file to your endpoints
4. Client systems are configured to use the PAC file URL
5. Updates are automatically distributed when marketplace domains change

**Advantages:**

* **Zero Configuration**: Fully automated setup and maintenance
* **Centralized Management**: Single point of control for all endpoints
* **Consistent Deployment**: Ensures uniform configuration across your organization

**Best for:** Organizations wanting hands-off PAC file management with automatic updates.

***

#### **Method 2: Customer-Managed Distribution**

**Overview:** Koi provides a ready-to-use PAC file that you distribute through your existing infrastructure.

**How it works:**

1. Koi generates a PAC file tailored to your environment
2. You download the PAC file from your deployment portal
3. You distribute and host the PAC file using your preferred method (GPO, MDM, web server, etc.)
4. You configure client systems to use your hosted PAC file URL

**Advantages:**

* **Full Control**: Complete ownership of PAC file hosting and distribution
* **Integration Flexibility**: Works with existing deployment tools and processes
* **Custom Hosting**: Host on your preferred infrastructure (internal web servers, CDN, etc.)
* **Policy Integration**: Combine with existing Group Policy or MDM configurations

**Best for:** Organizations with established configuration management systems or specific hosting requirements.

***

#### **Method 3: Manual Setup**

**Overview:** Configure proxy settings directly on individual endpoints. Best for local testing or a small rollout.

**How it works:**

Copy your customer-specific PAC file URL from the deployment portal, then follow the steps for your OS:

**Windows:**

1. Open Settings > Network & Internet > Proxy
2. Enable Automatically detect settings
3. Under Use setup script, enter the PAC file URL and enable it

**macOS:**

1. Open System Settings > Network
2. Select your active interface (Wi-Fi or Ethernet)
3. Click Details (or Advanced on older Macs)
4. Open the Proxies tab
5. Check Automatic Proxy Configuration
6. Paste the PAC file URL and click OK, then Apply

**Advantages:**

* No additional tooling required
* Fast to set up for a single machine or small group
* Useful for validating configuration before broader rollout

**Best for:** Individual devices, local testing, or small-scale pilots before deploying via script package or MDM.

***

### **PAC File Content Example**

Here's a simplified example of what a Koi PAC file contains:

```javascript
function FindProxyForURL(url, host) {
  if (shExpMatch(host, "marketplace.visualstudio.com") || 
        shExpMatch(host, "marketplace.cursorapi.com") || 
        shExpMatch(host, "chromewebstore.google.com") || 
        shExpMatch(host, "*.gallery.vsassets.io") || 
        shExpMatch(host, "open-vsx.org") 
    ) {
        var port = "8090"
        var markerIp = dnsResolve("proxy.koisecurity.com");
        if (markerIp) {
            port = markerIp.substring(4, 6) + markerIp.substring(7, 9);
      }
      return "PROXY example.gateway.koi.security:" + port;
  }
  return "DIRECT";
}
```

**Note:** Actual PAC files include comprehensive marketplace domain lists and sophisticated routing logic tailored to your environment.

***

### **Implementation Considerations**

| Factor                       | Script-Package | Customer-Managed | Manual Setup     |
| ---------------------------- | -------------- | ---------------- | ---------------- |
| **Setup Complexity**         | Low            | Medium           | Low              |
| **Maintenance**              | Automatic      | Manual           | Manual           |
| **Update Speed**             | Immediate      | As scheduled     | As scheduled     |
| **Infrastructure Control**   | Koi-managed    | Customer-managed | Customer-managed |
| **Existing PAC Integration** | New deployment | New deployment   | New deployment   |

***

### **Getting Started**

1. **Review** your current proxy configuration and identify any existing PAC files
2. **Choose** the distribution method that best fits your infrastructure
3. **Contact** Koi Support to discuss your PAC file requirements
4. **Test** the PAC file configuration in a controlled environment before full deployment

***

### **PAC File Testing**

Before organization-wide deployment, Koi recommends:

* **Pilot Testing**: Deploy to a small group of users first
* **Connectivity Verification**: Ensure marketplace access works correctly
* **Policy Validation**: Confirm Koi's security policies are properly applied
* **Fallback Testing**: Verify behavior when Koi's gateway is unavailable


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/network/establish-route/pac-file-integration.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
