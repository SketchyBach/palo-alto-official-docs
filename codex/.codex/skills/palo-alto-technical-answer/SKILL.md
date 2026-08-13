---
name: palo-alto-technical-answer
description: Give fast, concise, technically precise answers from the project's verified official Palo Alto Networks and KOI documentation corpus. Use for questions about Cortex, Cortex XDR/XSIAM/Cloud, Strata, Prisma SASE or Access, Identity/Idira, AI security, KOI, APIs, features, behavior, requirements, licensing, compatibility, errors, or troubleshooting when the user wants an answer rather than a full implementation procedure.
---

# Palo Alto Technical Answer

Use the local corpus only. Never use model memory to fill a documentation gap.

## Retrieve quickly

1. Determine product, feature, version, management plane, and deployment scope from the question.
2. Run `python scripts/search.py "<product + exact feature/error terms>" --mode answer --json`.
3. Open the best matching `local_path`. Open a second page only for version-sensitive, compatibility, licensing, security-impacting, or ambiguous claims.
4. Check `current_eligible`, source, content date, and URL. Apply `references/trust.md`.
5. If no exact verified result exists, say what is not documented. Do not broaden with `--any` unless discovering alternate terminology; never cite a merely related result as proof.

For KOI debugging questions, repeat the focused search with `--include-field`. Use field correspondence only to suggest environment-specific checks or known workarounds. Label Maxim's statements as `Palo Alto presales/support-derived guidance`; label Or/Sergey content as customer observation or question. Official documentation remains the authority for product capabilities and supported configuration.

## Respond

- Lead with the answer in one or two sentences.
- Add only scope, prerequisite, limitation, or distinction needed to prevent a wrong conclusion.
- Keep the normal answer under 180 words unless the question genuinely requires more.
- Cite the official URL next to each material paragraph.
- End with `Verified:` and the product/version or management plane plus content date.
- When evidence is insufficient, say exactly: `I'm sorry, I don't know. I couldn't verify this in the available official documentation.` Briefly identify the missing product/version/scope evidence when known. Do not add speculation afterward.
- Ask one short clarification instead of guessing when product, version, management plane, OS, or deployment mode could change the answer.

For a request containing guide, steps, walkthrough, "how do I", configure, set up, deploy, connect, onboard, integrate, migrate, install, enable, or implement, use `palo-alto-integration-guide` instead.
