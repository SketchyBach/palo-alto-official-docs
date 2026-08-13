<!-- KOI source: https://docs.koi.ai/api-reference/reference/users.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/api-reference/reference/users.md).

# Users

## List users

> Lists all users

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"ListUsersResponseDto":{"type":"object","properties":{"users":{"description":"Array of users","type":"array","items":{"$ref":"#/components/schemas/UserDto"}}},"required":["users"]},"UserDto":{"type":"object","properties":{"created_at":{"format":"date-time","type":"string","description":"The time the user was created"},"email":{"type":"string","description":"The email address of the user"},"first_name":{"type":"string","description":"The first name of the user"},"id":{"type":"string","description":"The unique identifier of the user"},"last_name":{"type":"string","description":"The last name of the user"},"role":{"type":"string","description":"The role of the user"},"status":{"type":"string","description":"The status of the user","enum":["enabled","disabled","invited"]}},"required":["id","first_name","last_name","created_at","email","role"]}}},"paths":{"/api/external/v2/users":{"get":{"description":"Lists all users","operationId":"users_get-users","parameters":[],"responses":{"200":{"description":"Successfully retrieved users","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ListUsersResponseDto"}}}},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}}},"summary":"List users","tags":["Users"]}}}}
```

## Create user

> Creates a new user with the given email and role

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}},"schemas":{"V2CreateUserRequestDto":{"type":"object","properties":{"email":{"type":"string","description":"The email of the user to add"},"role":{"type":"string","description":"The role the user should get"}},"required":["email","role"]},"UserDto":{"type":"object","properties":{"created_at":{"format":"date-time","type":"string","description":"The time the user was created"},"email":{"type":"string","description":"The email address of the user"},"first_name":{"type":"string","description":"The first name of the user"},"id":{"type":"string","description":"The unique identifier of the user"},"last_name":{"type":"string","description":"The last name of the user"},"role":{"type":"string","description":"The role of the user"},"status":{"type":"string","description":"The status of the user","enum":["enabled","disabled","invited"]}},"required":["id","first_name","last_name","created_at","email","role"]}}},"paths":{"/api/external/v2/users":{"post":{"description":"Creates a new user with the given email and role","operationId":"users_create-user","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/V2CreateUserRequestDto"}}}},"responses":{"201":{"description":"User created successfully","content":{"application/json":{"schema":{"$ref":"#/components/schemas/UserDto"}}}},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}}},"summary":"Create user","tags":["Users"]}}}}
```

## Delete user

> Removes a user

```json
{"openapi":"3.0.0","info":{"title":"KOI API","version":"1.1"},"servers":[{"url":"https://api.prod.koi.security","description":"Production"}],"security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"scheme":"bearer","bearerFormat":"JWT","type":"http"}}},"paths":{"/api/external/v2/users/{user_id}":{"delete":{"description":"Removes a user","operationId":"users_delete-user","parameters":[{"name":"user_id","required":true,"in":"path","schema":{"type":"string"}}],"responses":{"204":{"description":"User deleted successfully"},"400":{"description":"Bad Request","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}},"401":{"description":"Unauthorized","content":{"application/json":{"schema":{"type":"object","properties":{"message":{"type":"string"}}}}}}},"summary":"Delete user","tags":["Users"]}}}}
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/api-reference/reference/users.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
