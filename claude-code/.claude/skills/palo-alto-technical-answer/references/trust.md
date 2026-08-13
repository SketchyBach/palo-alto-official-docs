# Trust checks

Accept evidence only when the search record is authoritative, has a body and content hash, has no fetch error, uses an approved official URL, matches the requested scope, and is not contradicted by a newer matching page.

Require `current_eligible: true` for claims about latest/current UI, support, compatibility, licensing, defaults, versions, APIs, or behavior. Older pages may explain stable concepts only when their dated scope is explicit.

KOI sources may be `koi-official-export` or `koi-official-recovered`. Recovered records must have a recovery receipt. Preview remains Preview. Never turn index text, a title, or a failed record into product evidence.
