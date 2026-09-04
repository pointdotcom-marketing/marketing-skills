---
name: webflow-dev
description: Build or revise Webflow pages from supplied designs by reusing the site's existing classes, components, assets, responsive patterns, and interactions. Use for design-to-Webflow implementation, section rebuilds, responsive parity work, or Webflow cleanup where the existing site is the implementation system and the design is the visual source of truth.
---

# Webflow Development

Treat the existing Webflow site as the implementation system and the supplied design as the visual source of truth. Match the design by composing existing classes, components, assets, and patterns. Introduce new classes only when the design requires structure or behavior the site does not already provide.

## Design-source tools

Route by the design source named in the request:

- When the request or design reference names Figma, use Figma Desktop MCP to inspect and work from the design.
- When the request or design reference names Paper, use Paper Desktop MCP to inspect and work from the design.
- When both are named, use each MCP for the material hosted in that source.

Use this routing even when the user does not explicitly say “MCP.” Do not use browser or desktop computer-use automation to inspect or operate Figma or Paper. If the corresponding Desktop MCP is unavailable or cannot access the design, report the limitation and request access or an exported design rather than switching tools silently.

## 1. Establish scope and safety

Before editing:

1. Confirm the active site, page, branch, and Designer mode.
2. Identify the supplied design reference and exact artboard or frame being implemented.
3. Confirm whether publishing or staging was requested.
4. Keep work on the current branch and unpublished unless explicitly instructed otherwise.
5. Preserve shared components and global class definitions unless the request requires a site-wide change.

Completion criterion: the exact Webflow target and design reference are known, and publishing boundaries are explicit.

## 2. Inventory the existing system

Before creating elements, inspect:

- The current page structure.
- Comparable sections elsewhere on the page or site.
- Existing components and component properties.
- Existing global and combo classes.
- Existing image, illustration, icon, and logo assets.
- Existing responsive behavior at every configured breakpoint.

Prioritize established utilities such as `content-section`, `page-padding`, `container-*`, `max-width-*`, `heading-*`, `text-size-*`, `text-color-*`, `text-weight-*`, `padding-*`, `margin-*`, `button` and its established variants, and existing grid, card, testimonial, slider, form, and CTA patterns.

Completion criterion: every planned section has a reuse map identifying the existing classes, components, and assets it will use.

## 3. Enforce a class budget

Use existing global classes for typography, color, width, spacing, alignment, buttons, and common layout behavior.

Create a class only for:

- A section-specific layout with no existing equivalent.
- A repeated structural pattern unique to the section.
- A necessary interaction hook.
- A responsive adjustment that existing utilities cannot express.

Class requirements:

- Use one semantic class across repeated elements.
- Keep typography and color on existing utility classes.
- Prefer a structural parent class plus shared child classes.
- Attach every new class to an active element and give it a clear purpose.
- Use stable semantic names rather than temporary suffixes such as `v2`, `new`, `build`, or `clean`.

Do not create one class per heading, paragraph, card, or icon; duplicate an existing class under a page-specific name; or create a new card or grid system before checking existing patterns. Leave no prototype, replacement, hidden duplicate, or unused classes behind.

Completion criterion: the section uses the smallest defensible number of new structural classes and no new typography-only classes.

## 4. Implement section by section

Work in the design's exact section order. For each section:

1. Inspect its hierarchy, copy, dimensions, spacing, typography, colors, imagery, and responsive intent.
2. Inspect the corresponding Webflow section.
3. Record every difference before editing.
4. Make targeted changes using the reuse map.
5. Review the section visually before moving on.

The design controls section order, copy and labels, image selection and crop, information hierarchy, layout proportions, spacing rhythm, responsive composition, and interaction affordances. Read available details directly from the design rather than inferring them from an earlier draft.

Completion criterion: record a one-line checkpoint verdict for the section covering spacing, typography, contrast, alignment, assets, responsive behavior, and design parity.

## 5. Preserve asset fidelity

Reuse an existing Webflow asset when it matches the design. When a required asset is absent:

1. Export it from the source design in an appropriate format and resolution.
2. Import it once with a descriptive name and useful alt text.
3. Reuse the imported asset rather than creating duplicates.

Prefer existing site assets or icon components for icons and illustrations. Preserve source SVG artwork when available. Use inline SVG only when no reusable asset or component exists. Match specific design icons rather than substituting generic symbols.

Verify image selection, aspect ratio, object fit, object position, resolution, and alt text.

## 6. Treat interactions as functional requirements

Sliders, tabs, accordions, forms, and filters must work, not merely resemble the design.

For a testimonial slider, verify:

- Multiple slides exist.
- Each slide supports its own quote, name, role, and image.
- Previous and next controls change slides.
- Only the active slide is exposed visually and accessibly.
- Controls have accessible names.
- Keyboard interaction works.
- Slide dimensions remain stable when content length changes.
- Behavior works at desktop, tablet, and mobile breakpoints.
- The implementation uses an existing native component when practical.

Scope custom code to the section and use stable class hooks.

## 7. Treat warnings as blockers

After Webflow tool operations:

- Inspect partial-success messages and dropped-style warnings.
- Verify that requested global classes were actually applied.
- Check computed styles when duplicate or combo-class behavior is ambiguous.
- Confirm custom-code embeds contain the intended code.
- Verify managed images resolve to the correct assets.

A successful tool response is not proof of a successful implementation.

## 8. Clean up before completion

Remove only superseded elements and styles created during the current task. Before deleting a style, verify that no active element uses it, confirm it belongs to the superseded implementation, and confirm its replacement.

Final cleanup must leave:

- No duplicate sections.
- No hidden abandoned implementations.
- No placeholder copy or imagery.
- No dead custom code.
- No unused task-created classes.
- No unexplained one-off typography or color classes.

## 9. Verify the completed page

Review the page against the design from top to bottom at desktop/base, tablet, mobile landscape, and mobile portrait breakpoints.

For every section verify exact copy, asset and crop, typography hierarchy, color and contrast, container width and alignment, vertical spacing, borders and backgrounds, interaction behavior, responsive stacking, and reuse of global classes.

Keep the page unpublished and unstaged during verification.

Completion criterion: every design section is accounted for, every interaction has been exercised, every responsive view has been checked, and the class audit contains no unexplained additions.

## Handoff

Report:

1. Sections reviewed.
2. Differences corrected.
3. Existing components, utilities, and assets reused.
4. New classes added, with a one-line justification for each.
5. Interactions tested.
6. Breakpoints verified.
7. Anything intentionally left unchanged and why.
8. Confirmation that the page remains unpublished.
