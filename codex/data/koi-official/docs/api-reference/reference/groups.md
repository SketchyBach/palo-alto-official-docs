<!-- KOI source: https://docs.koi.ai/api-reference/reference/groups.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/api-reference/reference/groups.md).

# Groups

## List all device groups

> Retrieves a list of all device groups for the customer with device details.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2ListGroupsResponseDto":{"type":"object","properties":{"groups":{"description":"Array of device groups","type":"array","items":{"$ref":"#/components/schemas/V2GroupDto"}},"total_count":{"type":"number","description":"Total number of items"}},"required":["total_count","groups"]},"V2GroupDto":{"type":"object","properties":{"created_at":{"type":"string","description":"Group creation timestamp","format":"date-time"},"devices":{"description":"Devices in the group","type":"array","items":{"$ref":"#/components/schemas/V2GroupDeviceDto"}},"id":{"type":"number","description":"Group ID"},"name":{"type":"string","description":"Group name"}},"required":["id","name","created_at","devices"]},"V2GroupDeviceDto":{"type":"object","properties":{"id":{"type":"string","description":"Device ID"},"name":{"type":"string","description":"Device name (hostname)"}},"required":["id","name"]}}},"paths":{"/api/external/v2/groups":{"get":{"description":"Retrieves a list of all device groups for the customer with device details.","operationId":"groups_list-groups","parameters":[{"name":"page","required":false,"in":"query","description":"Page number for pagination","schema":{"minimum":1,"default":1,"type":"number"}},{"name":"page_size","required":false,"in":"query","description":"Number of results per page","schema":{"maximum":500,"default":100,"type":"number"}}],"responses":{"200":{"description":"Successfully retrieved groups","content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2ListGroupsResponseDto"}}}},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}}},"summary":"List all device groups","tags":["Groups"]}}}}
```

## Create device groups

> Creates one or more device groups for the customer. Maximum 9 groups per customer.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2CreateGroupDto":{"type":"object","properties":{"creator":{"type":"string","description":"Identifier to attribute as the creator of the groups (e.g. an email or a service/automation name). Applies to every group in this request.","maxLength":255},"groups":{"description":"List of groups to create","type":"array","items":{"$ref":"#/components/schemas/V2CreateGroupInputDto"}}},"required":["groups"]},"V2CreateGroupInputDto":{"type":"object","properties":{"device_ids":{"description":"List of device IDs to add to the group (can be empty or omitted)","type":"array","items":{"type":"string"}},"name":{"type":"string","description":"Group name"}},"required":["name"]},"CreateGroupResponseDtoV2":{"type":"object","properties":{"groups":{"description":"Array of groups that were created","type":"array","items":{"$ref":"#/components/schemas/V2GroupDto"}}},"required":["groups"]},"V2GroupDto":{"type":"object","properties":{"created_at":{"type":"string","description":"Group creation timestamp","format":"date-time"},"devices":{"description":"Devices in the group","type":"array","items":{"$ref":"#/components/schemas/V2GroupDeviceDto"}},"id":{"type":"number","description":"Group ID"},"name":{"type":"string","description":"Group name"}},"required":["id","name","created_at","devices"]},"V2GroupDeviceDto":{"type":"object","properties":{"id":{"type":"string","description":"Device ID"},"name":{"type":"string","description":"Device name (hostname)"}},"required":["id","name"]}}},"paths":{"/api/external/v2/groups":{"post":{"description":"Creates one or more device groups for the customer. Maximum 9 groups per customer.","operationId":"groups_create-groups","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2CreateGroupDto"}}}},"responses":{"201":{"description":"Groups created successfully","content":{"application/json":{"schema":{"$ref":"#/components/schemas/CreateGroupResponseDtoV2"}}}},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"409":{"description":"Group name already exists or maximum limit reached"}},"summary":"Create device groups","tags":["Groups"]}}}}
```

## Update device group

> Updates an existing device group name.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2UpdateGroupDto":{"type":"object","properties":{"name":{"type":"string","description":"New name for the device group"}},"required":["name"]}}},"paths":{"/api/external/v2/groups/{group_id}":{"put":{"description":"Updates an existing device group name.","operationId":"groups_update-group","parameters":[{"name":"group_id","required":true,"in":"path","description":"ID of the group to update","schema":{"type":"number"}}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2UpdateGroupDto"}}}},"responses":{"204":{"description":"Group updated successfully"},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"404":{"description":"Group not found"},"409":{"description":"A group with this name already exists"}},"summary":"Update device group","tags":["Groups"]}}}}
```

## Add device to group

> Adds a device to a specified group.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}}},"paths":{"/api/external/v2/groups/{group_id}/devices/{device_id}":{"post":{"description":"Adds a device to a specified group.","operationId":"groups_add-device-to-group","parameters":[{"name":"device_id","required":true,"in":"path","description":"ID of the device to add to the group","schema":{"type":"string"}},{"name":"group_id","required":true,"in":"path","description":"ID of the group","schema":{"type":"number"}}],"responses":{"204":{"description":"Device added to group successfully"},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"404":{"description":"Group or device not found"},"409":{"description":"Device is already in a group"}},"summary":"Add device to group","tags":["Groups"]}}}}
```

## Remove device from group

> Removes a device from a specified group.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}}},"paths":{"/api/external/v2/groups/{group_id}/devices/{device_id}":{"delete":{"description":"Removes a device from a specified group.","operationId":"groups_remove-device-from-group","parameters":[{"name":"device_id","required":true,"in":"path","description":"ID of the device to remove from the group","schema":{"type":"string"}},{"name":"group_id","required":true,"in":"path","description":"ID of the group","schema":{"type":"number"}}],"responses":{"204":{"description":"Device removed from group successfully"},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"404":{"description":"Group or device not found, or device is not in this group"}},"summary":"Remove device from group","tags":["Groups"]}}}}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/api-reference/reference/groups.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
