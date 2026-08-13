<!-- KOI source: https://docs.koi.ai/guides/universal-publish-private-extensions.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/guides/universal-publish-private-extensions.md).

# Publish (Private Extensions)

Publish is the ability to upload a privately developed VSCode extension or package, and distribute it across the organization efficiently and seamlessly.

#### Uploading a Private Extension

1. **Navigate to the Publish Page**
2. **Click "Upload"**
3. **Select your Private Extension VSIX**

   1. Select or drag the file into the drop-zone, then click on "Upload".

   <figure><img src="/files/iWCXxOg8Ysvke8G08zqP" alt=""><figcaption></figcaption></figure>
4. **Wait a few seconds**

Thats it! You will find that Koi detects all the needed information about the extension, and sends it through a composition scan. Instantly, you will find the extension available to all end-users that are configured to use Koi.

<figure><img src="/files/fJIbVIowQ6pNtOCyCdiD" alt=""><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/guides/universal-publish-private-extensions.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
