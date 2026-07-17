# Marketing Skills

Agent skills for Point.com marketing team usage.

This repository is published for Point team access, but it is for internal use only.

## Skills

- `point-brand-voice`: Write, edit, and review Point marketing copy using the brand voice observed across `point.com`, `point.com/hei`, and `point.com/heloc`.
- `point-brand-guidelines`: Apply and review Point's official visual identity across logos, typography, color, imagery, and design patterns.

## Install

Install a single skill from the published repository:

```bash
npx skills add pointdotcom-marketing/marketing-skills --list
npx skills add pointdotcom-marketing/marketing-skills --skill point-brand-voice
npx skills add pointdotcom-marketing/marketing-skills --skill point-brand-guidelines
```

Install all skills from the published repository:

```bash
npx skills add pointdotcom-marketing/marketing-skills --skill '*'
```

From a local checkout:

```bash
npx skills add . --list
npx skills add . --skill point-brand-voice
npx skills add . --skill point-brand-guidelines
```

Install all skills from a local checkout:

```bash
npx skills add . --skill '*'
```

## Claude Plugin

Claude can install these skills as the `point-marketing` plugin. Add this repository as a marketplace once:

```bash
claude plugin marketplace add pointdotcom-marketing/marketing-skills
```

Then install the plugin:

```bash
claude plugin install point-marketing@point-marketing
```

Validate the plugin locally before releasing changes:

```bash
claude plugin validate . --strict
```

## Repository Layout

This repository is intentionally set up as a multi-skill catalog and Claude plugin:

```text
.claude-plugin/
  plugin.json
  marketplace.json
skills/
  point-brand-voice/
    SKILL.md
    references/
      page-audit.md
      voice-guide.md
    examples.md
  point-brand-guidelines/
    SKILL.md
    references/
      visual-guidelines.md
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
