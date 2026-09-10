---
url: https://docs.koi.ai/api-reference/reference
fetched_at: 2026-09-06T10:23:58.369Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Agent Activity | API Reference

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
API ReferenceReference
Agent Activity
List agent-activity events in a time window
GET
https://api.prod.koi.security
/api/external/v2/agent-activity/events

Lists agent-activity events across your organization within a required time window

Authorizations
bearerAuth
Authorization
string
required
Bearer authentication header of the form Bearer <token>.
Query parameters
created_at_gte
string · date-time
required

Window lower bound (ISO 8601). Required. The window may not exceed 24 hours.

Example: 2026-06-14T00:00:00.000Z
created_at_lte
string · date-time
required

Window upper bound (ISO 8601). Required. Cannot be in the future.

Example: 2026-06-15T00:00:00.000Z
page
number · min: 1
optional

Page number for pagination

Default: 1
Example: 1
page_size
number · max: 500
optional

Number of results per page

Default: 100
Example: 100
session_id
string
optional

Only events belonging to this session — drill into one session's timeline

Responses
200

Successfully retrieved agent-activity events

application/json
data
object · V2EventResponse[]
required
total_count
number
required

Total events in the window

Example: 42
400

Invalid query parameters

401

Unauthorized

application/json
GET
/api/external/v2/agent-activity/events
HTTP
Ask
Copy
GET /api/external/v2/agent-activity/events?created_at_gte=2026-06-14T00%3A00%3A00.000Z&created_at_lte=2026-06-15T00%3A00%3A00.000Z HTTP/1.1

Host: api.prod.koi.security

Authorization: Bearer YOUR_SECRET_TOKEN

Accept: */*


Test it
200

Successfully retrieved agent-activity events

Ask
Copy
{

  "data": [

    {

      "agent": "claude_code",

      "hits": [

        {

          "action": "command",

          "target": "cat /etc/passwd"

        }

      ],

      "host": "macbook-pro",

      "policy_id": "pol_abc",

      "session_id": "b1f0…",

      "timestamp": "text",

      "verdict": "block"

    }

  ],

  "total_count": 42

}
List agent sessions
GET
https://api.prod.koi.security
/api/external/v2/agent-activity/sessions

Lists AI coding-agent sessions across your organization within a required time window

Authorizations
bearerAuth
Authorization
string
required
Bearer authentication header of the form Bearer <token>.
Query parameters
action
string
optional

Filter by an action category the session touched

agent
string · enum
optional

Filter by coding agent

Possible values: cursorclaude_codecodexcopilotgemini_cliantigravity
created_at_gte
string · date-time
required

Window lower bound (ISO 8601). Required. The window may not exceed 30 days.

Example: 2026-06-01T00:00:00.000Z
created_at_lte
string · date-time
required

Window upper bound (ISO 8601). Required. Cannot be in the future.

Example: 2026-06-15T00:00:00.000Z
filter
string
optional

Advanced query-builder filter (JSON string) over the same fields, combined (AND) with the first-class filters

governed_by
string
optional

Only sessions governed by this runtime-hardening policy id

host
string
optional

Filter by endpoint hostname

mcp
string
optional

Filter by an MCP server the session touched

model
string
optional

Filter by AI model

page
number · min: 1
optional

Page number for pagination

Default: 1
Example: 1
page_size
number · max: 500
optional

Number of results per page

Default: 100
Example: 100
skill
string
optional

Filter by a skill the session used

sort_by
string · enum
optional

Sort column

Default: start_time
Possible values: start_timeend_timeevent_counthostagent
sort_direction
string · enum
optional

Sort direction

Default: desc
Possible values: ascdesc
user_email
string
optional

Filter by user email

verdict
string · enum
optional

Only sessions containing at least one event with this enforcement decision

Possible values: allowaskblock
Responses
200

Successfully retrieved agent sessions

application/json
data
object · V2AgentSessionResponse[]
required
total_count
number
required

Total sessions matching the window and filters

Example: 128
400

Invalid query parameters

401

Unauthorized

application/json
GET
/api/external/v2/agent-activity/sessions
HTTP
Ask
Copy
GET /api/external/v2/agent-activity/sessions?created_at_gte=2026-06-01T00%3A00%3A00.000Z&created_at_lte=2026-06-15T00%3A00%3A00.000Z HTTP/1.1

Host: api.prod.koi.security

Authorization: Bearer YOUR_SECRET_TOKEN

Accept: */*


Test it
200

Successfully retrieved agent sessions

Ask
Copy
{

  "data": [

    {

      "agent": "claude_code",

      "decisions": {

        "allow": 100,

        "ask": 3,

        "block": 2

      },

      "end_time": "text",

      "event_count": 42,

      "governed_by": [

        "pol_abc"

      ],

      "host": "macbook-pro",

      "models": [

        "claude-opus-4"

      ],

      "session_id": "b1f0…",

      "start_time": "text",

      "user_emails": [

        "dev@acme.com"

      ]

    }

  ],

  "total_count": 128

}
Previous
Overview and evolution
Next
Alerts

Last updated 1 month ago
