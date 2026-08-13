<!-- KOI source: https://docs.koi.ai/api-reference/reference/devices.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/api-reference/reference/devices.md).

# Devices

## List all devices

> Retrieves a list of all devices registered.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2ListDevicesResponseDto":{"type":"object","properties":{"devices":{"description":"Array of devices","type":"array","items":{"$ref":"#/components/schemas/V2DeviceDto"}},"total_count":{"type":"number","description":"Total number of devices"}},"required":["devices","total_count"]},"V2DeviceDto":{"type":"object","properties":{"hostname":{"type":"string","description":"Device hostname"},"id":{"type":"string","description":"Device ID"},"last_logged_on_user":{"type":"string","description":"Last logged on user"},"last_seen":{"type":"string","description":"Last seen timestamp","format":"date-time"},"network_user":{"type":"string","description":"Network user"},"os":{"type":"string","description":"Operating system","enum":["windows","mac","linux"]},"registered_at":{"type":"string","description":"Device registration timestamp","format":"date-time"},"serial":{"type":"string","description":"Device serial number"},"status":{"type":"string","description":"Device status","enum":["active","stale","archived"]}},"required":["id","hostname","os","status","last_logged_on_user","network_user","serial","registered_at","last_seen"]}}},"paths":{"/api/external/v2/devices":{"get":{"description":"Retrieves a list of all devices registered.","operationId":"devices_list-devices","parameters":[{"name":"last_seen_gte","required":false,"in":"query","description":"Filter devices last seen after the specified date","schema":{"format":"date","type":"string"}},{"name":"last_seen_lte","required":false,"in":"query","description":"Filter devices last seen before the specified date","schema":{"format":"date","type":"string"}},{"name":"page","required":false,"in":"query","description":"Page number for pagination","schema":{"minimum":1,"default":1,"type":"number"}},{"name":"page_size","required":false,"in":"query","description":"Number of results per page","schema":{"maximum":500,"default":100,"type":"number"}},{"name":"status","required":false,"in":"query","description":"Filter by device status. 'active'/'stale' filter by activity health (derived from last-seen recency); 'archived' filters devices whose lifecycle status is archived.","schema":{"type":"string","enum":["active","stale","archived"]}}],"responses":{"200":{"description":"Successfully retrieved devices","content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2ListDevicesResponseDto"}}}},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}}},"summary":"List all devices","tags":["Devices"]}}}}
```

## Archive a device

> Archives a device, marking it as inactive. This is typically used for devices that are no longer in use.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2ArchiveDeviceDto":{"type":"object","properties":{"archived_by_user_email":{"type":"string","description":"Email of the user initiating the archive action"}},"required":["archived_by_user_email"]}}},"paths":{"/api/external/v2/devices/{device_id}/archive":{"post":{"description":"Archives a device, marking it as inactive. This is typically used for devices that are no longer in use.","operationId":"devices_archive-device","parameters":[{"name":"device_id","required":true,"in":"path","description":"ID of the device to archive","schema":{"type":"string"}}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2ArchiveDeviceDto"}}}},"responses":{"204":{"description":"Device archived successfully"},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"404":{"description":"Device not found"}},"summary":"Archive a device","tags":["Devices"]}}}}
```

## Get device inventory

> Retrieves the inventory of a specific device.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2GetDeviceInventoryResponseDto":{"type":"object","properties":{"inventory":{"description":"Array of inventory items","type":"array","items":{"$ref":"#/components/schemas/V2DeviceInventoryItemDto"}},"total_count":{"type":"number","description":"Total number of inventory items"}},"required":["inventory","total_count"]},"V2DeviceInventoryItemDto":{"type":"object","properties":{"activation_status":{"description":"Activation status","allOf":[{"$ref":"#/components/schemas/ActivationStatus"}]},"first_seen":{"type":"string","description":"First seen timestamp"},"item_display_name":{"type":"string","description":"Item display name"},"item_id":{"type":"string","description":"Item ID"},"last_seen":{"type":"string","description":"Last seen timestamp"},"local_full_path":{"type":"string","description":"Local full path"},"marketplace":{"type":"string","description":"Marketplace display name","nullable":true},"platform":{"type":"string","description":"Platform display name","enum":["antigravity","aqua","arc","brave","brew","chatgpt_atlas","chocolatey","chrome","chromium","claude","claude_code","claude_desktop","clion","codex","comet","cursor","datagrip","dataspell","dia","edge","excel","firefox","fleet","goland","hugging_face","ollama","intellij_community","intellij","kiro","mac","npm","notepad++","opera","outlook","phpstorm","powerpoint","prisma_access_browser","pycharm","pypi","rider","rubymine","rustrover","vscode","webstorm","windsurf","word","windows","writerside"]},"publisher":{"type":"string","description":"Publisher name"},"risk_level":{"type":"string","description":"Risk level","enum":["low","medium","high","critical","pending"]},"version":{"type":"string","description":"Item version"}},"required":["item_id","version","item_display_name","publisher","marketplace","platform","first_seen","last_seen","risk_level","local_full_path","activation_status"]},"ActivationStatus":{"type":"string","enum":["enabled","disabled","N/A"],"description":"Activation status"}}},"paths":{"/api/external/v2/devices/{device_id}/inventory":{"get":{"description":"Retrieves the inventory of a specific device.","operationId":"devices_get-device-inventory","parameters":[{"name":"device_id","required":true,"in":"path","description":"ID of the device to retrieve inventory for","schema":{"type":"string"}},{"name":"finding_id","required":false,"in":"query","description":"Filter by finding id","schema":{"type":"string"}},{"name":"page","required":false,"in":"query","description":"Page number for pagination","schema":{"minimum":1,"default":1,"type":"number"}},{"name":"page_size","required":false,"in":"query","description":"Number of results per page","schema":{"maximum":500,"default":100,"type":"number"}}],"responses":{"200":{"description":"Successfully retrieved device inventory","content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2GetDeviceInventoryResponseDto"}}}},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"404":{"description":"Device not found"}},"summary":"Get device inventory","tags":["Devices"]}}}}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/api-reference/reference/devices.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
