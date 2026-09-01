---
name: point-partner-creative-review
description: Review partner-, affiliate-, broker-, or publisher-submitted creative featuring Point for obvious first-pass brand, copy, product, disclosure, production, and customer-journey issues before human Brand, Content, or Compliance review. Use for ads, tiles, scripts, emails, landing pages, documents, or creative batches; not for final compliance approval or net-new campaign ideation.
---

# Point Partner Creative Review

Return a short, prioritized first pass that removes obvious defects before human review. The result is review support, not approval.

## Mandatory output contract

Use a plain, copy-pasteable list. Never use a Markdown table, HTML table, grid, columns, or a table-like layout—even for a large batch and even if the user asks for more detail. Do not use **Review status** or **Findings** headings. Do not recreate the old `Action | Location | Category | Finding | Change / Owner` format.

Start with exactly three short, unheaded lines separated by blank lines:

> Obvious issues found.
>
> Scope: Slides 8–10 of the Strand placements deck.
>
> Top priority: Slide 10's Disruptive Media ad uses a fabricated Point logo, calls the HEI a loan, and links to a non-Point domain.

Keep the scope line to the file or deck name plus the reviewed range or asset count; do not inventory individual assets or add a parenthetical breakdown. Keep the top-priority line to one sentence naming the location and defect; leave rationale, product principles, and corrective detail to the priority bullet. Do not format these three lines as headings or list items.

Then use only the priority headings that have findings, with exactly three `#` characters:

### P0 — Blockers

- Slide 10 — Uses a fabricated Point logo. Replace it with an approved logo asset.

### P1 — Required fixes

- Slide 8, headline — Describes the HEI as a loan. Replace it with current approved product language.

### P2 — Verify or route

- Slide 9, footer — No licensing identifier is visible. Compliance should confirm whether one is required for this placement and market.

Keep each bullet on one line and preferably under 35 words in the form `Location — issue. Action.` Default to 3–5 bullets total; four is a strong target for a small multi-asset review, not a quota. Use fewer when they cover the decisions, and exceed five only when another distinct issue would materially change whether an asset advances or who must act.

Compress by decision, not by category. Combine related defects on the same asset when they share one correction, and combine repeated issues across assets when they have the same correction. Split findings only when their priority or required action differs.

Before returning, remove any bullet that is optional polish, already covered by a higher-priority finding, routine downstream QA, or a verification gap that would not change the decision. The final list should answer only: what blocks advancement, what must be fixed, and what material point needs an owner to verify.

Do not add separate category, rationale, or owner fields. Include why something matters only when the risk is not obvious, and name an owner only when that owner must verify or supply the correction. Do not include subjective polish or nice-to-have rewrites in the default review. End after the final bullet; do not add a closing summary, approval disclaimer, or owner recap.

Omit **Needs context / not reviewed** by default. Use it only when a missing or inaccessible item prevents judgment on a likely material risk; do not list normal later-stage needs such as reviewing final executions, additional frames, or click-path QA unless their absence prevents this first pass. If no obvious issue is found, write one short paragraph beginning **No obvious issues found in the reviewed material.** Include the scope and state that the result is a first pass, not approval.

## Priorities

- **P0 — Blocker:** materially misleading product framing or claim, fabricated or seriously misused Point identity, an unauthorized or misleading destination, or another severe issue that makes the creative unsuitable to advance as-is.
- **P1 — Required fix:** a clear brand, copy, disclosure, journey, legibility, or production defect that must be corrected before approval.
- **P2 — Verify or route:** a potentially material claim, disclosure, state rule, qualification, destination behavior, or contextual choice that requires an authoritative source or owner.

Use P0 sparingly. Order findings by priority, then by asset.

## Required guidance

Read [review-rubric.md](references/review-rubric.md) for every review.

- Use `point-brand-guidelines` when the submission has a visual component. Compare Point logos and fonts with its approved bundled assets.
- Use `point-brand-voice` when the submission contains copy or product messaging.
- Use `point-social-ad-ideation` only when the user also asks to create, replace, or substantially improve a concept.

Treat current Legal- or Compliance-approved materials and current product sources as authoritative. Historical creative and prior reviews show issue patterns; they are not current claim or disclosure sources.

## Review method

- Establish the assets in scope, intended brand relationship, audience or market when relevant, destination, and current comparison sources. Continue with harmless assumptions; use P2 when missing context could change the judgment.
- Inspect the submitted artifact itself and anchor each finding to a filename, slide, page, frame, headline, CTA, footer, timestamp, or visual region. List inaccessible material under **Needs context / not reviewed**.
- Apply every relevant section of the rubric, but report only observable defects and material verification gaps. Do not pad the result with general best practices or optional craft feedback.
- Treat partner styling as intentional unless it misuses a Point element, conflicts with the stated brand mode, creates an untrustworthy handoff, or makes the set internally inconsistent.
- Do not call creative legally compliant, approved, or safe to publish. Compliance determines compliance; Brand and Content own judgment calls in their domains.

## Scope boundary

Complete the requested analysis only. Editing the partner's files, contacting the partner, submitting to Compliance, or marking work approved requires a separate user request.
