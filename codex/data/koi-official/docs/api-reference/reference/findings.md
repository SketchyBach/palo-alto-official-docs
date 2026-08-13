<!-- KOI source: https://docs.koi.ai/api-reference/reference/findings.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/api-reference/reference/findings.md).

# Findings

## List all findings

> Retrieves a paginated list of all findings.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2ListFindingsResponseDto":{"type":"object","properties":{"items":{"description":"List of finding definitions","type":"array","items":{"$ref":"#/components/schemas/V2FindingDefinitionDto"}},"total_count":{"type":"number","description":"Total number of items"}},"required":["total_count","items"]},"V2FindingDefinitionDto":{"type":"object","properties":{"description":{"type":"string","description":"Description of the finding"},"id":{"type":"string","description":"The unique identifier of the finding"},"name":{"type":"string","description":"The name of the finding"},"risk":{"type":"number","description":"The risk level of the finding (0-10)"}},"required":["name","risk","description","id"]}}},"paths":{"/api/external/v2/findings":{"get":{"description":"Retrieves a paginated list of all findings.","operationId":"findings_list-findings","parameters":[{"name":"page","required":false,"in":"query","description":"Page number for pagination","schema":{"minimum":1,"default":1,"type":"number"}},{"name":"page_size","required":false,"in":"query","description":"Number of results per page","schema":{"maximum":500,"default":100,"type":"number"}}],"responses":{"200":{"description":"Successfully retrieved findings","content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2ListFindingsResponseDto"}}}},"400":{"description":"Validation error. Common causes: invalid pagination parameters"},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}}},"summary":"List all findings","tags":["Findings"]}}}}
```

## Customize risk level for a finding

> Allows adjusting the risk level for a specific finding.

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2CustomizeRiskDto":{"type":"object","properties":{"finding_id":{"type":"string","description":"The ID of the finding to customize risk for"},"risk":{"type":"number","description":"The risk level to set, between 0 and 10","minimum":0,"maximum":10}},"required":["finding_id","risk"]}}},"paths":{"/api/external/v2/findings/customize-risk":{"post":{"description":"Allows adjusting the risk level for a specific finding.","operationId":"findings_customize-risk","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2CustomizeRiskDto"}}}},"responses":{"204":{"description":"Risk level customized successfully"},"400":{"description":"Validation error. Common causes: invalid risk value (must be 0-10), missing finding_id"},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"404":{"description":"Finding not found"}},"summary":"Customize risk level for a finding","tags":["Findings"]}}}}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/api-reference/reference/findings.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
