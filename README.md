# Point Marketing Skills

Reusable skills that help AI agents create consistent, on-brand Point marketing work.

> [!TIP]
> **Recommended: have your agent install everything for you**
>
> Paste this into Claude, ChatGPT Work, Codex, or another agent with access to your computer:
>
> ```text
> Install every available Agent Skill from https://github.com/pointdotcom-marketing/marketing-skills globally for every compatible agent installed on this computer. Preserve each complete skill directory and its supporting files. Use `npx skills add pointdotcom-marketing/marketing-skills --skill '*' --global --yes`, verify the installation with `npx skills list --global`, and report which skills were installed and which agents can access them. Then tell me how to use /skills to find the installed skills. If anything requires a separate manual step, explain exactly what remains. Do not install ZIP files or add tracking.
> ```

> **Want to run it yourself instead?**
>
> ```bash
> npx skills add pointdotcom-marketing/marketing-skills --skill '*' --global --yes
> npx skills list --global
> ```

> [!NOTE]
> **Using ChatGPT Work or the Codex desktop app?** Install the **Point Marketing** plugin below. A workspace admin sets it up and shares it once; team members install it from **Plugins**. This is in addition to, not instead of, the cross-agent installer above.

## Available skills

| Skill | Use it for |
| --- | --- |
| [`point-brand-voice`](skills/point-brand-voice/SKILL.md) | Writing, editing, or reviewing Point marketing copy for landing pages, ads, emails, FAQs, CTAs, and product education. |
| [`point-brand-guidelines`](skills/point-brand-guidelines/SKILL.md) | Creating or reviewing Point visual work: logos, typography, color, imagery, layouts, and design systems. |
| [`point-social-ad-ideation`](skills/point-social-ad-ideation/SKILL.md) | Generating, ranking, and expanding paid social concepts into production-ready creative briefs, test plans, and disclosure plans. |

## Use a skill

After installation, type `/skills` to find the available skills. Then ask your agent for what you need and name the skill when useful:

```text
Use $point-brand-voice to rewrite this HEI landing-page section.
```

```text
Use $point-brand-guidelines to review this campaign concept for visual brand compliance.
```

```text
Use $point-social-ad-ideation to develop six distinct paid social concepts for homeowners comparing HEI and HELOC, then expand the strongest three into creative briefs.
```

## Install one skill

```bash
npx skills add pointdotcom-marketing/marketing-skills --skill point-brand-voice --global
npx skills add pointdotcom-marketing/marketing-skills --skill point-brand-guidelines --global
npx skills add pointdotcom-marketing/marketing-skills --skill point-social-ad-ideation --global
```

## ChatGPT Work and Codex desktop app

The **Point Marketing** plugin bundles the same portable skills for ChatGPT Work on the web and for Work mode or Codex in the ChatGPT desktop app.

### Workspace admin: set it up once

Run this once in Codex CLI:

```bash
codex plugin marketplace add pointdotcom-marketing/marketing-skills --ref main
```

Then restart the ChatGPT desktop app. In **Plugins**, choose **Point Marketing Skills**, install **Point Marketing**, and open the plugin details to select **Share**. Invite the marketing team or copy the share link.

### Team members: install and use it

In the ChatGPT desktop app, open **Plugins** → **Shared with you** → **Point Marketing** → **Install**. Start a new ChatGPT Work or Codex task and ask for the marketing work you need. You can also name a skill directly, such as `$point-brand-voice`, `$point-brand-guidelines`, or `$point-social-ad-ideation`.

The workspace-sharing option keeps access inside your ChatGPT workspace; the one-line installer at the top remains the best option for Claude, Codex CLI, and other compatible local agents. See OpenAI's [plugin guide](https://learn.chatgpt.com/docs/build-plugins) for more details.

## Contribute a skill

You do not need direct write access to this repository to contribute. Work from your own fork, then open a pull request for review. You will need permission to view and fork the repository; if you do not have it, use the request path below.

### Submit a pull request

1. Fork this repository to your GitHub account.
2. Clone your fork and create a branch:

   ```bash
   git clone https://github.com/<your-github-username>/marketing-skills.git
   cd marketing-skills
   git checkout -b add-<skill-name>
   ```

3. Create your skill in `skills/<skill-name>/`. Use a lowercase, kebab-case name.
4. Verify it is discoverable:

   ```bash
   npx skills add . --list
   ```

5. Commit your changes, push your branch, and open a pull request to `pointdotcom-marketing/marketing-skills:main`.

In the pull request, explain the task the skill supports, include a realistic example prompt, and link the source material or team process it captures.

Each skill should be self-contained and portable across compatible agents:

```text
skills/<skill-name>/
  SKILL.md
  references/        # Optional detailed guidance
  scripts/           # Optional reusable automation
  assets/            # Optional files used in deliverables
```

Keep core instructions in `SKILL.md`, put detailed material in `references/`, and avoid adding an extra README inside the skill folder.

### Request a skill

Have an idea but do not want to open a pull request? Reach out to Austin with:

- The task you want an agent to handle
- A real example prompt or input
- What a useful output looks like
- Any source material, team conventions, or gotchas the agent needs to know

### What makes a good skill?

A good skill captures knowledge or a repeatable workflow that an agent would not reliably know on its own. Keep it focused on one coherent task, write a clear description of what it does and when to use it, provide a sensible default workflow, and refine it against real work.

Read the official [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices) for authoring guidance and the [Agent Skills specification](https://agentskills.io/specification) for the portable `SKILL.md` format.

## Other installation options

### Local checkout

```bash
npx skills add . --skill '*'
```

### Claude plugin

```bash
claude plugin marketplace add pointdotcom-marketing/marketing-skills
claude plugin install point-marketing@point-marketing
```
