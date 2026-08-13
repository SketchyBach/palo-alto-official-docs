<!-- KOI source: https://docs.koi.ai/api-reference/readme/overview-and-evolution.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/api-reference/readme/overview-and-evolution.md).

# Overview and evolution

### **Koi API v2**

Koi API v2 is designed to give your team a faster, more intuitive, and more reliable integration experience from day one. The new version focuses on developer productivity, clarity, and consistency, so you can build, automate, and scale with more confidence.

By standardizing the API around widely adopted REST patterns, we reduce the integration effort required from your teams and make it easier to plug Koi into your existing tools, workflows, and automation pipelines.

***

### **Key Improvements**

API v2 introduces a modernized, more consistent foundation that simplifies integration, reduces friction, and gives developers a clearer and more reliable way to work with Koi at scale. The improvements below are designed to make every interaction with the API more predictable, intuitive, and error resistant.

#### **1. True RESTful Design**

**v2 embraces REST conventions more strictly**, making the API behavior more predictable and intuitive.

* **Resource-based URL structure**: Endpoints are organized around resources (e.g., `/approval-requests`, `/devices`, `/groups`)
* **Proper HTTP methods**: We use the full range of HTTP verbs (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) with their standard meanings
* **Meaningful HTTP status codes**: Operations return appropriate status codes (e.g., `201 Created` for new resources, `204 No Content` for successful updates with no response body, `409 Conflict` for duplicate resources)
* **Resource identifiers in URLs**: IDs are placed in the URL path (e.g., `/approval-requests/:id/approve`) rather than in request bodies

**What this means for you**: The API feels more natural and predictable. If you've worked with other modern REST APIs, v2 will feel immediately familiar.

#### **2. Consistent Naming Conventions**

**v2 uses snake\_case consistently** across all request parameters and response fields, aligning with common API standards and database conventions.

**Examples**:

* `displayName` → `item_display_name`
* `pageSize` → `page_size`
* `riskLevel` → `risk_level`
* `publisherName` → `publisher_name`

**What this means for you**: All field names follow a single, predictable convention that's easier to read and remember.

#### **3. Better Request and Response Structure**

**v2 provides clearer, more consistent data structures** with improved organization of input and output properties.

* **Query parameters for filtering and pagination**: GET requests use query parameters consistently (e.g., `?page=1&page_size=100&risk_level=high`)
* **Required parameters are explicit**: Required fields are clearly separated from optional fields with proper API documentation
* **Structured response envelopes**: List endpoints return consistent response shapes with `total_count` and data arrays
* **Simplified item identification**: Item lookup now uses separate `item_id`, `marketplace`, and `version` parameters instead of composite unique identifiers

**What this means for you**: Request construction is more straightforward, and response parsing is more predictable. You'll spend less time debugging parameter issues.

#### **4. Enhanced Error Handling**

**v2 provides more actionable error messages** that help you quickly identify and resolve issues.

* **Descriptive error responses**: Error messages clearly explain what went wrong and often suggest how to fix it
* **Specific HTTP status codes**: Different error conditions return distinct status codes (e.g., `400 Bad Request` for validation errors, `404 Not Found` for missing resources, `409 Conflict` for constraint violations)
* **Validation feedback**: Field-level validation errors specify exactly which parameters are invalid and why
* **Better documentation of error cases**: API documentation explicitly lists possible error responses for each endpoint

**What this means for you**: Less time troubleshooting integration issues. When something goes wrong, you'll know exactly what needs to be fixed.

#### **5. Improved API Organization**

**v2 restructures endpoints for better logical grouping** and resource independence.

* **Cleaner URL hierarchy**: Resource relationships are expressed more clearly through URL structure

**What this means for you**: It's easier to discover and understand available endpoints. The API structure reflects how you naturally think about the resources you're managing.

#### **6. Transaction-Based Batch Operations**

**v2 uses an all-or-nothing approach for batch operations**, ensuring data consistency and predictable behavior.

When you send a request containing multiple items (for example, creating multiple remediation entries or updating several devices at once), v2 validates all items before processing any of them. If even one item in the batch is invalid or malformed, the entire request fails and no changes are made.

* **Complete validation upfront**: All items in a batch are validated before any processing begins
* **Atomic operations**: Either all items succeed or none do—no partial updates
* **Clear feedback**: Error responses identify exactly which items failed validation and why

**What this means for you**: You never have to worry about partial failures leaving your data in an inconsistent state. When a batch request succeeds, you know all items were processed. When it fails, you know nothing changed and can fix the issues before retrying.

#### **7. Enhanced Documentation**

**v2 comes with more comprehensive API documentation** that makes integration easier.

* **Detailed parameter descriptions**: Every field includes clear descriptions, expected formats, and examples
* **Complete response schemas**: Full documentation of response structures with all possible fields
* **Error documentation**: Explicit documentation of error responses and status codes
* **Type safety**: Better type definitions that enable stronger validation

**What this means for you**: Less guesswork and fewer support requests. The documentation helps you succeed the first time.

***

### **Getting Started with v2**

The v2 API is available at the same base URL with `/v2` prefix instead of `/v1`. Authentication remains unchanged, so your existing API keys will work with both versions.

#### **Questions and Support**

We're here to help you succeed with v2, check the API documentation or contact us for clarification

The v2 API represents our commitment to providing a world-class integration experience. We're excited to see what you'll build with it.

<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/api-reference/readme/overview-and-evolution.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
