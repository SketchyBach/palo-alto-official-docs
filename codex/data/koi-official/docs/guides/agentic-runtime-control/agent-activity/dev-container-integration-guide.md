<!-- KOI source: https://docs.koi.ai/guides/agentic-runtime-control/agent-activity/dev-container-integration-guide.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/agentic-runtime-control/agent-activity/dev-container-integration-guide.md).

# Dev Container Integration Guide

To enable Koi's AI agent monitoring in Docker-based development environments, you need to mount the agent configuration files into your container. This allows agents like Cursor and Claude Code running inside the container to use the same hooks configuration as your host system.

The hooks capture AI agent activity and write events to `agent_activity.jsonl`. This file serves as a temporary buffer where hooks dump their payload data, which is then collected by the Koi script package for processing and reporting.

## Dockerfile Setup

Add the following to your Dockerfile to create the required directories and activity log file:

```dockerfile
# Create directories for AI agent hooks (Cursor, Claude Code) and activity logs
# Activity log path must match the volume mount in docker-compose.devcontainer.yml
RUN mkdir -p /etc/cursor /etc/claude-code "/Library/Application Support/Koi" && \
    chmod 755 /etc/cursor /etc/claude-code "/Library/Application Support/Koi" && \
    touch "/Library/Application Support/Koi/agent_activity.jsonl" && \
    chmod 666 "/Library/Application Support/Koi/agent_activity.jsonl"
```

## Volume Mounts

Add these volume mounts to your `docker-compose.yml` or dev container configuration.

#### macOS

```yaml
volumes:
  - "/Library/Application Support/Cursor/hooks.json:/etc/cursor/hooks.json:ro"
  - "/Library/Application Support/ClaudeCode/managed-settings.json:/etc/claude-code/managed-settings.json:ro"
  - "/Library/Application Support/Koi:/Library/Application Support/Koi"
```

#### Windows

```yaml
volumes:
  - "C:\\ProgramData\\Cursor\\hooks.json:/etc/cursor/hooks.json:ro"
  - "C:\\ProgramData\\ClaudeCode\\managed-settings.json:/etc/claude-code/managed-settings.json:ro"
  - "C:\\ProgramData\\Koi:C:\\ProgramData\\Koi"
```

## Notes

* Hook configuration files (`hooks.json`, `managed-settings.json`) are mounted as read-only (`:ro`) since they only need to be read by the agents.
* The Koi directory is mounted with read-write access to allow hooks to write activity data to `agent_activity.jsonl`.
* Ensure the script package has access to the activity log path on the host system for data collection.
* **Docker Desktop on macOS**: You must grant Docker access to the `/Library/Application Support` directory. Go to **Settings → Resources → File Sharing → Add** and add `/Library/Application Support` to the list of shared paths.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/agentic-runtime-control/agent-activity/dev-container-integration-guide.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
