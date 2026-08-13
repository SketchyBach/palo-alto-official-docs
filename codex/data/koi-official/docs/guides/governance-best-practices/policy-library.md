<!-- KOI source: https://docs.koi.ai/guides/governance-best-practices/policy-library.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/governance-best-practices/policy-library.md).

# Policy Library

The Policy Library provides out-of-the-box prebuilt policy templates that can be quickly enabled to streamline your governance and security processes. These templates cover a wide range of use cases and can be tailored to meet your organization’s specific requirements. This guide explains how to access, navigate, and use the Policy Library.

#### Accessing the Policy Library

1. **Navigate to the Policies Page**
   * Go to the **Policies** page in the platform.
2. **Open the Policy Library**, this will open the **Policy Library Drawer**, where you can explore and enable prebuilt policies.

![](https://files.readme.io/2397689fef5107e202352238d14743624919cef8fe56435b434540384d17b23c-image.png)

![](https://files.readme.io/f8c7d0e1022d6556e8711fca66ed17ed632e164d59d51d641bf09d671e208939-image.png)

***

#### Understanding the Policy Library

The Policy Library is organized into categories to help you quickly find the most relevant policies for your needs:

**Categories**

* **Must Haves**: Essential policies to address common risks and enforce baseline security.
* **Recommended**: Policies that enhance security and governance with minimal friction.
* **AI**: Policies to manage AI-related extensions and packages.
* **Composition**: Policies targeting code composition, such as embedded files or dependencies.
* **Publisher**: Policies focusing on publisher verification and trustworthiness.
* **Compliance**: Policies ensuring adherence to legal and organizational requirements.
* **Security Operations**: Alert-focused policies for SOC teams.

Each policy in the library includes:

* **Name**: A descriptive title of the policy.
* **Description**: A brief overview of what the policy does.
* **Type**: The action taken by the policy (Block, Allow, Alert).

***

#### Exploring and Reviewing Policies

1. **Browse Policies by Category**
   * Use the categories to filter policies relevant to your goals.
   * Example: Select **AI** to view policies related to AI-powered extensions.
2.

```
![](https://files.readme.io/829d7def7f166e9674eba6ee0ec040c2b455b94683b7ac17fa4b77533e3a940f-image.png)
```

```
**View and configure Policy details**
```

* Each policy includes:
  * **Name**: e.g., "Block High-Risk Extensions."
  * **Description**: e.g., "Prevent the installation of extensions flagged for high risk."
  * **Type**: e.g., Block.
* **Configure policy**:

  * Click the **"Configure"** button to get full details of the policy.
  * Review the logic behind the policy before enabling it.

  ![](https://files.readme.io/0d23e6ae216696e88a40c269e2561ecc5f90f7ae57bc3140cc150eb5f1bc4969-image.png)

  * Click **"Create policy"** button to enable it.
  * The policy can be viewed and managed in the **Custom policies** table.

***

#### Best Practices

* **Review before enabling**: always review the **"Policy details"** to understand the policy condition and adjust it to your needs.
* **Start with Must-Haves**: Focus on **Must Haves** and **Recommended** categories to build a strong baseline.
* **Tailor to Needs**: Explore policies in categories like **Compliance** and **AI** for domain-specific requirements.

***

#### Conclusion

The Policy Library makes it simple to enforce security and governance standards with minimal effort. By leveraging prebuilt templates, you can quickly address risks, ensure compliance, and optimize your organization’s extension and package management.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/governance-best-practices/policy-library.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
