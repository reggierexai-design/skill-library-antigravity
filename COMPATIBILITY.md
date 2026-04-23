# Compatibility

This pack targets **Antigravity**.

## Assumptions

- Project-local skills live in `.agent/skills`
- Global skills commonly live in `~/.gemini/antigravity/skills`
- The platform follows the broader `SKILL.md` directory pattern used by the Agent Skills ecosystem

## Port notes

This port keeps the library conservative: skill frontmatter is reduced to standard `name` and `description`, and the rest of the platform behavior is handled through docs and profile-based installation rather than tool-specific metadata.
