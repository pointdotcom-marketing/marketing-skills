# PowerPoint and Canva Production

Build the PowerPoint as the editable source of truth unless the assignment explicitly makes Canva primary.

## PowerPoint construction

- Match the requested dimensions; use `4:5` for `1080 × 1350` social templates.
- Use native text boxes for all copy.
- Use native shapes for simple backgrounds, rules, and geometric accents when practical.
- Place approved logos without altering their proportions or colors.
- Place the main illustration as a separate transparent image or supported vector object.
- Group related elements only when the group remains easy to select and edit.
- Avoid unsupported filters, masks, blending modes, or effects that may rasterize or change during import.
- Do not use a full-slide image to simulate editability.

## Canva compatibility

Prefer broadly supported PowerPoint features:

- standard text boxes
- common fills and strokes
- simple groups
- PNG or SVG source artwork
- ordinary image placement and cropping
- explicit line breaks rather than fragile auto-fit behavior

Expect licensed fonts, transparency, gradients, SVG handling, and grouped objects to require verification after import.

## Canva delivery decision

- If native Canva access is available, import the source deck and inspect every page before sharing the native asset or link.
- If native Canva access is unavailable, deliver the PowerPoint as `Canva-import-ready` and do not call it a native Canva file.
- If import cannot be tested, state that clean import is a production target rather than a verified result.

## Import verification

After importing, confirm:

- slide dimensions and page count are correct
- all text remains editable
- fonts are present or substitutions are documented
- logo proportions and color are unchanged
- the main illustration remains separate from copy
- benefits and icons remain individually editable
- legal text is legible and inside the safe area
- transparency, gradients, and image crops match the source deck
- no object shifted, clipped, disappeared, or changed stacking order
