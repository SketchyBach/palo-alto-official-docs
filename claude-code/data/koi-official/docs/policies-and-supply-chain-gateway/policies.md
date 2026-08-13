<!-- KOI source: https://docs.koi.ai/policies-and-supply-chain-gateway/policies.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/policies-and-supply-chain-gateway/policies.md).

# Policies

### **Introduction**

**Policies** in Koi provide a powerful way to control and manage the installation and usage of third-party software items within your corporate environments. Policies allow security teams and administrators to enforce rules, prevent risky extensions from being used, and ensure compliance with security best practices. By leveraging policies, you can maintain a safe, secure, and compliant environments without hindering employees productivity.

### **What are Policies?**

Policies in Koi are rules that define what actions should be taken when certain conditions are met. These policies help ensure that extensions being installed or used within your organization adhere to your security and governance requirements. By configuring policies, you can automate actions such as alerting, removing, or blocking extensions based on specific criteria like risk levels, security findings, publisher information or many other attributes.

### **Key Features of Policies:**

* **Automation**: Automatically monitor and manage extension installation and usage.
* **Customization**: Tailor policies to your organization’s unique security requirements.
* **Compliance**: Ensure that your environments comply with security standards and regulations.

### **How to Create Policies**

Creating policies in Koi is straightforward. Follow these steps to create and configure a new policy:

1. **Access the Policies Page**:

Navigate to the “Policies” page in your Koi dashboard.

2. **Click on “Create New Policy”**:

This will open the policy creation modal, where you can define the parameters of the policy.

3. **Define Policy Parameters**:

* **Policy Name**: Give the policy a clear and descriptive name.
* **Description**: Provide details about what this policy is meant to accomplish.
* **If extension matches**: Set the filter with the conditions that trigger the policy.
* **Then**: Specify what happens when the policy is triggered. Actions include Block or Remediate, Allow and Approve, or Send Alert.
* **Immediate Impact**: For the Block and Remediate policy, you can perform an Impact Check to identify which extensions will be impacted and remediated in advance.

4. **Save and Apply**:

Once you’ve configured the policy, click “Save” to apply it. The policy will now be active and enforceable across your environment.

### **Blocklist vs Allowlist Approach**

In Koi, policies can be managed using two approaches: **Blocklist** and **Allowlist**. Each offers a different level of control over which extensions can be installed.

#### **Blocklist Approach**

A **Blocklist** blocks specific extensions you deem risky or malicious, allowing everything else. This approach offers flexibility for employees while targeting known threats.

* **Benefits**: Employees can install any extension not on the blocklist, while security focuses on preventing known risks.
* **Use Case**: Block extensions with a high-risk score or those from unverified publishers.

#### **Allowlist Approach**

A **Allowlist** allows only pre-approved extensions, blocking everything else. This provides tighter security but less flexibility for employees.

* **Benefits**: Ensures only trusted, vetted extensions are installed, reducing overall risk.
* **Use Case**: Allow only extensions from verified publishers or those required for justified use cases.

#### **Choosing an Approach**

* **Blocklist**: Best for flexible environments, blocking only known risks.
* **Allowlist**: Ideal for high-security environments where only pre-approved extensions are allowed.

#### Switching to Allowlist

By default, Koi operates in block mode. Switching to allowlist mode requires administrator approval for any new extension installations. To ensure a smooth transition, all existing extensions will be automatically pre-approved and remain functional. These pre-approved extensions can still be installed on new devices, and any existing block policies will be removed.

To switch to allowlist mode:

1. Navigate to the Policies page.
2. Click the Switch to Allowlist button.
3. A confirmation dialog will appear. Click Enable Allowlist Mode to confirm the change.

Once in allowlist mode:

* Any new extension requests will appear on the Approvals page for admin review.
* The extension request form is accessible from the top bar of the Approvals page under Share with your team.

### **Recommended Policies**

For recommended policies check out our [Policy Library](https://docs.koi.ai/guides/index-1/policy-library)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/policies-and-supply-chain-gateway/policies.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
