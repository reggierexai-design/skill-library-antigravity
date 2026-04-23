# Deployment Guide

## Install locations

- Project-local: `.agent/skills`
- User-wide: `~/.gemini/antigravity/skills`

## Recommended deployment pattern

1. Keep the library repo in a stable local path.
2. Use `scripts/install_profile.py` to symlink a profile into your target skills folder.
3. Keep one narrow baseline profile per repository or per user.
4. Add more skills only when you see a repeated need.

## Example

```bash
python scripts/install_profile.py minimal_core --dest .agent/skills
python scripts/install_profile.py builder_engineering --dest .agent/skills
```

Use `--mode copy` if you prefer physical copies over symlinks.

## Updating

Pull the latest library changes, then rerun the install script for the profiles you use. If your platform does not pick up changes immediately, restart the session or the tool.

## Repo guidance

Use `AGENT_NOTES.md` for always-on instructions such as coding standards, architecture notes, or review checklists. Use skills for reusable procedures, not permanent repo facts.
