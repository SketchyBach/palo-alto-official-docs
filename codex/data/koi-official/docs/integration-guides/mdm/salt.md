<!-- KOI source: https://docs.koi.ai/integration-guides/mdm/salt.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/mdm/salt.md).

# Salt Guide

This document provides step-by-step instructions on integrating **Koi** into your environment with Salt.\
In this guide, we’re going to create a new Salt state and schedule it to run periodically on the minions.

## Configuration Guide

**Prerequisites**

* Access to your Salt-Master.
* The configuration script provided by Koi.
* Internet access from managed devices (salt-minions).

**Integration Steps**

1. Upload the Koi script to your Salt Master at `/srv/salt/koi/files/koi_script.sh`
2. Ensure the file has executable permissions.

   ```
   chmod +x /srv/salt/koi/files/koi_script.sh
   ```
3. Create a new Salt State File named `/srv/salt/koi/init.sls` and add the following configuration:

   ```
   koi_configuration:
     cmd.script:
       - source: salt://koi/files/koi_script.sh
   ```
4. Create a new schedule in `/srv/salt/scheduler.sls`:

   ```
   schedule_koi:
     schedule.present:
       - function: state.apply
       - job_args:
         - koi
       - minutes: 60
       - enabled: True
       - splay: 300
       - maxrunning: 1
       - run_on_start: True
   ```
5. Apply the new scheduled Koi state:\
   \&#xNAN;*(replace `'*'` with your desired target group, or leave it in order to apply to all minions)*

   ```
   salt '*' state.apply scheduler
   ```
6. Verify deployment

   Run the Koi state manually to verify it executes correctly:

   ```
   salt '*' state.apply koi
   ```

   Then check the job history to confirm successful execution:

   ```
   salt-run jobs.list_jobs
   salt-run jobs.lookup_jid <jid_number>
   ```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/mdm/salt.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
