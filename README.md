# Point Marketing Skills

Public agent skills for Point marketing work.

[![skills.sh](https://skills.sh/b/pointdotcom-marketing/marketing-skills)](https://skills.sh/pointdotcom-marketing/marketing-skills)

## Skills

- `point-brand-voice`: Write, edit, and review Point marketing copy using the brand voice observed across `point.com`, `point.com/hei`, and `point.com/heloc`.

## Install

After this repository is published publicly:

```bash
npx skills add pointdotcom-marketing/marketing-skills --list
npx skills add pointdotcom-marketing/marketing-skills --skill point-brand-voice
```

Install all skills from this repository:

```bash
npx skills add pointdotcom-marketing/marketing-skills --skill '*'
```

## Repository Layout

This repository is intentionally set up as a multi-skill catalog:

```text
skills/
  point-brand-voice/
    SKILL.md
    references/
      page-audit.md
      voice-guide.md
    examples.md
```

Each skill lives in its own directory under `skills/` and must include a `SKILL.md` file with `name` and `description` frontmatter.

## Adding A Skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Use a lowercase kebab-case skill name that matches the directory name.
3. Keep `SKILL.md` concise and put deeper reference material in `references/`.
4. Verify discovery locally:

```bash
npx skills add . --list
```
