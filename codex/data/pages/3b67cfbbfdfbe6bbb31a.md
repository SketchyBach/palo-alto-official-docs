---
url: https://docs.koi.ai/api-reference/reference/remediations
fetched_at: 2026-09-06T09:19:27.172Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Remediations | API Reference

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
API ReferenceReference
Remediations
List remediation suggestions
GET
https://api.prod.koi.security
/api/external/v2/remediations

Returns a list of remediation suggestions based on the provided filters

Authorizations
bearerAuth
Authorization
string
required
Bearer authentication header of the form Bearer <token>.
Query parameters
hostname
string
optional

The hostname to filter by

Example: laptop-01
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
platform
string · enum
optional

Platform identifier

Possible values: chromeedgebravetalonarcoperacometatlasdiachromiumvsccurpycharmwebstormintellijideaicdatagripcliongolandrubyminephpstormrustroverdataspellaquariderfleetwritersidewordexcelpowerpointoutlookfirefoxhomebrewhuggingfaceollamanppwindsurfkiroclaudeclaude_codeclaude_desktopcodexnpmpypisoftware_macsoftware_windowssoftware_linuxbinary_macantigravitychocolateygitall_agentsopenclaw
reason
string
optional

The reason for the remediation

Example: Out of policy
risk_level
string · enum
optional

The risk level to filter by

Possible values: lowmediumhighcriticalpending
sort_by
string · enum
optional

Sort by field

Example: item_display_name
Possible values: item_display_namehostnamerisk_levelplatform
sort_direction
string · enum
optional

Sort direction

Example: asc
Possible values: ascdesc
status
string · enum
optional

The remediation status to filter by

Possible values: openpendingremediateddismissed
Responses
200

Successfully retrieved remediations

application/json
items
object · V2RemediationItemDto[]
required

Array of remediation items

total_count
number
required

The total number of items

Example: 100
400

Bad Request

application/json
401

Unauthorized

application/json
GET
/api/external/v2/remediations
HTTP
Ask
Copy
GET /api/external/v2/remediations HTTP/1.1

Host: api.prod.koi.security

Authorization: Bearer YOUR_SECRET_TOKEN

Accept: */*


Test it
200

Successfully retrieved remediations

Ask
Copy
{

  "items": [

    {

      "device_id": "2ghaecad-7510-4b9f-bece-cb35309334d7",

      "dismissed_at": "2024-01-15T10:30:00Z",

      "dismissed_by": "admin@example.com",

      "flagged_at": "2024-01-15T10:30:00Z",

      "hostname": "laptop-01",

      "item_display_name": "My Extension",

      "item_id": "ext-123",

      "last_script_run": "2024-01-15T10:30:00Z",

      "platform": "vscode",

      "reason": "Out of policy",

      "risk_level": "high",

      "status": "open",

      "triggered_at": "2024-01-15T10:30:00Z",

      "triggered_by": "admin@example.com",

      "version": "1.0.0"

    }

  ],

  "total_count": 100

}
Previous
Private Items
Next
Reports

Last updated 1 month ago
