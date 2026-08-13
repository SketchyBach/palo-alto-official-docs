<!-- KOI source: https://docs.koi.ai/guides/reporting.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/reporting.md).

# Reporting

Our platform allows you to generate various reports from different sections of the system, providing detailed insights tailored to your needs. Follow the steps below to generate reports from key areas.

#### Generating Reports from the Inventory Page

1. **Navigate to the Inventory Page**
   * Go to the **Inventory** page to view all extensions and their details across your environment.
2. **Click the Report Button**
   * Locate the **Report** button above the inventory table.

     ![](https://files.readme.io/748e76e1225c12e8dbab093ebf94546331e4f9428bb6bb80c9836b39c33b554e-image.png)
3. **Export Options**
   * If no query is applied:
     * The report will include your **entire inventory** with all extension details.
   * If a query is applied:
     * The report will include only the **filtered results** based on your query.

***

#### Generating Reports from the Policies Page

1. **Navigate to the Policies Page**
   * Go to the **Policies** page to manage and view your policies.
2. **Click the Report Button**
   * In the upper corner of the **Policies List**, locate the **Report** button.

     ![](https://files.readme.io/3e626fc1472d37b0456565170dd072a9daeee9c8da226b1ff583878b157837be-image.png)
3. **Export Policies**
   * The report will include all your **configured policies** with detailed information.

***

#### Generating Reports from the Audit Page

1. **Navigate to the Audit Page**
   * Go to the **Audit** page to review activities in your environment.
2. **Switch to the Activity Tab**
   * Ensure you’re on the **Activity Tab** within the Audit page.
3. **Click the Download Button**
   * In the upper-right corner above the activity table, find the **Download** button.

     ![](https://files.readme.io/bb85e37db6190a1fe54e768666bc2250d5e463c6850437a7fb58a7b8aa8347cf-image.png)
4. **Export Activity Logs**
   * The report will include a comprehensive record of all activities, such as:
     * User auditing within the platform.
     * Extension installations.
     * Firewall Mitigation actions.
     * Device registrations.

***

#### Summary

* **Inventory Page**: Export your full inventory or query results.
* **Policies Page**: Export all configured policies.
* **Audit Page**: Export detailed activity logs for user actions, mitigations, and more.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/reporting.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
