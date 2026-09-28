# KOI / Agentic Endpoint Security update — 28 September 2026

This is a focused live-documentation review. It does not claim a complete refresh of the authenticated KOI corpus. The last full authenticated KOI browser capture in this project was 6 September 2026.

## Skills: KOI/AES and Prisma AIRS

KOI/AES already provides skill discovery and inventory on managed endpoints, AI-native risk analysis through Wings, and controls over skill use in supported AI coding agents. Its Private Items Scan also accepts an internally developed skill's `SKILL.md` for analysis before distribution. A matching skill found later on a managed endpoint inherits that scan's risk assessment. A private skill that has not been uploaded is listed as unknown, without an associated risk assessment. The private-item documentation describes uploading `SKILL.md`; it does not establish that KOI uploads and scans the entire skill bundle in that workflow.

Prisma AIRS AI Skill Security is a separate Preview service. It analyzes an uploaded ZIP containing `SKILL.md` and referenced files, then applies configurable rules to produce an Allowed or Blocked verdict. The current documentation says no separate AI Skill Security license is required during Preview, but an AI Skill Security deployment profile, tenant association, and proper access are required. The deployment documentation says this Preview is available in the US region only. KOI/AES ownership or entitlement is not documented as automatically activating the AIRS profile.

The practical choice is to use the existing KOI/AES skill inventory, Wings findings, and private `SKILL.md` scan where that meets the requirement. Use the separate AIRS Preview workflow when an assessment of the complete uploaded skill bundle and its AIRS rule verdict is needed. Confirm post-Preview commercial terms with Palo Alto Networks before making a purchasing commitment.

## Verified KOI changes

The September 2026 KOI release notes document command policies with a resource target (script package 1.84.14 or newer), Discovery & Remediation Scope in Preview (script package 1.86.0 or newer), deeper inventory and policy APIs, and a Threat Center with organization impact. August 2026 notes document AI-native risk analysis for plugins and skills in Preview, private skill scanning, runtime policy templates, Prisma AIRS Runtime integration in Preview, and Go package discovery. These are product release notes; availability in a particular tenant still needs checking.

## Official sources checked live on 28 September 2026

- [KOI What's new](https://docs.koi.ai/get-started/whats-new-in-koi)
- [KOI AI Agent Extensions Risk](https://docs.koi.ai/risk-and-threat-intelligence/ai-agent-extensions-risk)
- [KOI Private Items Scan](https://docs.koi.ai/guides/private-items-scan)
- [KOI agentic endpoint guide](https://docs.koi.ai/guides/protect-the-agentic-endpoint-with-koi)
- [Prisma AIRS AI Skill Security](https://docs.paloaltonetworks.com/prisma-airs/ai-supply-chain-security/ai-supply-chain-security/ai-skill-security)
- [Prisma AIRS AI Skill Security deployment profile](https://docs.paloaltonetworks.com/prisma-airs/ai-supply-chain-security/ai-supply-chain-security/ai-skill-security/create-a-deployment-profile-for-prisma-airs-ai-skill-security)
