Source: https://docs.koi.ai/integration-guides/network/establish-route/fortinet-fortigate-guide.md

# Fortinet FortiGate Guide

This guide describes how to configure **FortiGate** to forward HTTP/HTTPS traffic to **Koi Proxy** using **proxy chaining**. This setup ensures that traffic destined for specific domains is routed through Koi Proxy for inspection and policy enforcement.

***

## Prerequisites

Before starting, ensure you have the following:

* Access to your **FortiGate Admin Console** (Web or CLI).
* **Administrator privileges** to configure web proxy settings and security policies.
* **Koi Proxy CA certificate**, provided by Koi.
* **Covered domain names** - domains that should be forwarded to Koi Proxy. The list is provided by Koi.
* **Koi Proxy server address and port**

***

## Step 1 – Download and Upload the Koi CA Certificate

1. Obtain the **Koi Proxy CA certificate** from your Koi support team.
2. Log in to your **FortiGate Admin Console**.
3. Navigate to: **System → Certificates**
4. Click **Import → CA Certificate**.
5. Select the **Koi CA certificate file** and upload it.
6. Confirm the certificate is listed under **Trusted CA Certificates**.

> **Note:** This step ensures FortiGate trusts Koi Proxy when forwarding HTTPS traffic.

***

## Step 2 – Configure the Web Proxy Forwarding Server

1. In the FortiGate GUI, go to: **Network → Forwarding Servers**.
2. Click **Create New** and configure the following:
   * **Name:** `KoiProxy`.
   * **Type:** `Web Proxy Forwarding Server`.
   * **IP Address / FQDN:** `<Koi Proxy server address>`.
   * **Port:** `<Koi Proxy port>`.
   * **Authentication:** `None` (unless specified by Koi).
3. Click **OK** to save.

***

## Step 3 – Create a Proxy Policy for Target Domains

1. Navigate to: **Policy & Objects → Proxy Policy**
2. Click **Create New**.
3. Configure:
   * **Incoming Interface:** Your internal network interface (e.g., `LAN`)
   * **Outgoing Interface:** `Forwarding Server`
   * **Source:** `all` or specify internal subnets
   * **Destination:** Create an **Address Group** for Koi’s **covered domain names**:
     * Go to **Policy & Objects → Addresses → Create New**
     * Select **FQDN** type for each domain and add all domains provided by Koi
     * Group them into **"Koi-Domains"**
   * **Service:** `HTTP, HTTPS`
   * **Action:** `Forward to Proxy`
   * **Forward Server:** `KoiProxy`
4. Enable **SSL Inspection** and select the profile that trusts the **Koi CA certificate**.
5. Click **OK** to save the policy.

***

## Step 4 – Verify the Configuration

1. From a client machine behind FortiGate, attempt to access one of the covered domains.
2. Verify:
   * The traffic is being forwarded to Koi Proxy.
   * SSL certificates are trusted (no browser warnings).
   * Policy matches are logged in FortiGate under:
     * `Log & Report → Forward Traffic`

***

## Summary

By configuring FortiGate to forward specific domain traffic to Koi Proxy, you ensure that HTTP and HTTPS requests are routed through Koi for inspection and policy enforcement.

These steps provide a secure, reliable, and seamless connection between endpoints and Koi services.


---

---
