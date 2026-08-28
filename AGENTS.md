# Plugin packaging

Treat `skills/` as the canonical copy of every Point skill. After adding or editing a skill, run:

```bash
python3 scripts/sync-plugin-packaging.py
```

The command mirrors the canonical skill set into the ChatGPT/Codex plugin with relative symlinks and bumps the Claude and ChatGPT/Codex plugin manifests together once per change. For an intentional minor or major release, pass the target with `--version X.Y.Z`.

Before finishing any change under `skills/` or `plugins/`, run:

```bash
python3 scripts/sync-plugin-packaging.py --check
```

Completion requires matching native plugin versions and one valid ChatGPT/Codex symlink for every canonical skill.
