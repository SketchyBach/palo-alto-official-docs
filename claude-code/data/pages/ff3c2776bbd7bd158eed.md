---
url: https://docs.koi.ai/api-reference/reference/devices
fetched_at: 2026-09-06T09:17:51.457Z
source: koi-official-browser
capture_method: authenticated official browser
---

# Devices | API Reference

For the complete documentation index, see llms.txt. This page is also available as Markdown.
Ask
API ReferenceReference
Devices
List all devices
GET
https://api.prod.koi.security
/api/external/v2/devices

Retrieves a list of all devices registered.

Authorizations
bearerAuth
Authorization
string
required
Bearer authentication header of the form Bearer <token>.
Query parameters
last_seen_gte
string · date
optional

Filter devices last seen after the specified date

Example: 2023-12-31
last_seen_lte
string · date
optional

Filter devices last seen before the specified date

Example: 2023-12-31
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
status
string · enum
optional

Filter by device status. 'active'/'stale' filter by activity health (derived from last-seen recency); 'archived' filters devices whose lifecycle status is archived.

Example: active
Possible values: activestalearchived
Responses
200

Successfully retrieved devices

application/json
devices
object · V2DeviceDto[]
required

Array of devices

total_count
number
required

Total number of devices

Example: 100
400

Bad Request

application/json
401

Unauthorized

application/json
GET
/api/external/v2/devices
HTTP
Ask
Copy
GET /api/external/v2/devices HTTP/1.1

Host: api.prod.koi.security

Authorization: Bearer YOUR_SECRET_TOKEN

Accept: */*


Test it
200

Successfully retrieved devices

Ask
Copy
{

  "devices": [

    {

      "hostname": "laptop-01",

      "id": "550e8400-e29b-41d4-a716-446655440000",

      "last_logged_on_user": "user@example.com",

      "last_seen": "2024-01-15T10:30:00Z",

      "network_user": "network-user",

      "os": "windows",

      "registered_at": "2024-01-15T10:30:00Z",

      "serial": "SN123456",

      "status": "active"

    }

  ],

  "total_count": 100

}
Archive a device
POST
https://api.prod.koi.security
/api/external/v2/devices/
{device_id}
/archive

Archives a device, marking it as inactive. This is typically used for devices that are no longer in use.

Authorizations
bearerAuth
Authorization
string
required
Bearer authentication header of the form Bearer <token>.
Path parameters
device_id
string
required

ID of the device to archive

Example: 550e8400-e29b-41d4-a716-446655440000
Body
application/json
archived_by_user_email
string
required

Email of the user initiating the archive action

Example: user@example.com
Responses
204

Device archived successfully

No content

400

Bad Request

application/json
401

Unauthorized

application/json
404

Device not found

POST
/api/external/v2/devices/{device_id}/archive
HTTP
Ask
Copy
POST /api/external/v2/devices/{device_id}/archive HTTP/1.1

Host: api.prod.koi.security

Authorization: Bearer YOUR_SECRET_TOKEN

Content-Type: application/json

Accept: */*

Content-Length: 45



{

  "archived_by_user_email": "user@example.com"

}
Test it
204

Device archived successfully

No content

Previous
Audit Logs
Next
Findings

Last updated 1 month ago
