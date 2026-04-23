# Deployment Guide

## Install locations

- Project-local: `.agent/skills`
- User-wide: `~/.gemini/antigravity/skills`

## Recommended deployment pattern

1. Keep the library repo in a stable local path.
2. Use `scripts/install_profile.py` to symlink a profile into your target skills folder.
3. Keep one narrow baseline profile per repository or per user.
4. Add more skills only when you see a repeated need.
