# RexBot Antigravity Skill Library v0.6

**RexBot / Rex Hub community release for Antigravity.**

This is the Antigravity-specific port of the RexBot generalist skill library. It keeps the same deep playbooks, profiles, and category coverage as the OpenClaw release, but the docs, install paths, examples, and packaging are rewritten for Antigravity.

## What is in this pack

- **185 skills**
- **22 curated profiles**
- **21 internal orchestration or safety skills**
- **76 skills intended for model-side discovery**
- **109 slash-first specialist skills**
- **619.4 average words per skill**

## Platform fit

- The Antigravity ecosystem commonly uses `.agent/skills` for project-local skills and `~/.gemini/antigravity/skills` for global installs.
- Community examples commonly invoke Antigravity skills with `@skill-name`, and some setups also expose `/skill-name` aliases.
- Antigravity skill packs generally follow the same `SKILL.md` directory format used by the broader Agent Skills ecosystem.
- Use a lightweight workspace note or project README for always-on guidance, and reserve skills for reusable workflows that should load when needed.

## Quick start

1. Put this library somewhere stable on disk.
2. Install a profile with `python scripts/install_profile.py minimal_core`.
3. Start with a narrow profile before you install the whole catalog.
4. Keep repo-wide standing guidance in `AGENT_NOTES.md` or an equivalent workspace note, and use skills for repeatable workflows.

## Invocation

- Explicit use: `@skill-name or /skill-name`
- Discovery: Use `@skill-name` or `/skill-name` depending on your Antigravity surface.

## Recommended rollout

- Start with `minimal_core`
- Add one domain profile such as `builder_engineering`, `docs_support`, `research_operator`, or `security_quality`
- Treat `full_library` as a power-user profile, not a default

## Important files

- `START_HERE.md`
- `TRAINING_MANUAL.md`
- `SYSTEM_OVERVIEW.md`
- `DEPLOYMENT_GUIDE.md`
- `AGENT_INTEGRATION_GUIDE.md`
- `PROFILE_SELECTION_GUIDE.md`
- `SKILL_ROUTING_GUIDE.md`
- `AUTHORING_GUIDE.md`
- `CATALOG.md`
- `CATALOG_DETAILED.md`

## Attribution

- Publisher: **RexBot / Rex Hub**
- Homepage: `https://reggierexai-design.github.io/rexhub/`
- Status: community-maintained, not an official Antigravity bundle
