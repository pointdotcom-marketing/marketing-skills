# QA and Preflight

Complete all applicable checks before delivery. Separate mechanical validation from visual and content review.

## Mechanical checks

- The editable source file opens without repair warnings.
- The deck has the requested page count and aspect ratio.
- Required preview PNGs have the requested pixel dimensions.
- Newly created illustration PNGs preserve transparency.
- The logo, headline, subheader, illustration, benefit copy, icons, and legal footer are separate objects.
- Text remains editable and is not embedded in the illustration.
- Required fonts are present or substitutions are documented.
- All required files use clear, consistent names.

Run `scripts/preflight.py` for the checks it supports. Treat its result as evidence, not a replacement for opening and inspecting the source file.

## Visual checks

- The composition matches the intended Point visual system.
- The illustration is crisp, uncluttered, and free of generic AI-style artifacts.
- Black transparency-preview areas did not become part of the artwork.
- The headline has no single-word final line.
- Copy is not clipped, crowded, or accidentally overlapped.
- Spacing, alignment, and margins are consistent.
- Artwork is not stretched, distorted, or awkwardly cropped.
- Benefits form a consistent row and remain readable at feed size.
- Legal text is legible and placed on a sufficiently simple background.
- Logo size, clear space, contrast, colors, and proportions are correct.

Inspect rendered previews at full size and at a reduced feed-like size.

## Content and approval checks

- Supplied campaign copy is preserved unless revision was requested.
- Product facts and benefit statements come from a current approved source.
- Legal footer language is current and approved, or clearly marked as a placeholder.
- Historical ads were used only for the approved reference purpose.
- Generated illustrations remain drafts until accepted for reuse.
- Font, layout, or brand exceptions are recorded.

## Canva checks

When Canva delivery is required, complete the import verification in [pptx-canva-production.md](pptx-canva-production.md). Do not report a native Canva deliverable or clean import unless it was actually tested.

## Delivery report

Report:

1. files created
2. formats, page count, and dimensions
3. font substitutions
4. reused versus newly created illustrations
5. PowerPoint and Canva verification performed
6. remaining brand, Legal, asset-rights, or import dependencies
