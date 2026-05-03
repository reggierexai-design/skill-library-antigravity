#!/usr/bin/env python3
"""
Convert upgraded OpenClaw v1.0 skills to Antigravity format.
Key differences:
- "OpenClaw tool pattern" → "Antigravity tool pattern"
- Tool references adapted for Antigravity (agent-oriented, multi-step workflows)
"""

import os, re

SRC_DIR = r"E:\rexhub-repos\skill-library-openclaw\skills"
DEST_DIR = r"E:\rexhub-repos\skill-library-antigravity\skills"

ANTIGRAVITY_TOOL_PATTERNS = {
    "att": [
        "- Use web search tools to research competitor content and current platform conventions.",
        "- Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.",
        "- When external claims appear, verify before publishing with `safe_external_claims`.",
        "- After drafting, run `att_proof_mining` to verify every claim has backing.",
    ],
    "core": [
        "- Use file inspection to load relevant files and context before planning.",
        "- Use command execution to check workspace state (git status, file structure) before and after actions.",
        "- After execution, use `core_verify_done` to confirm the result meets the stated objective.",
    ],
    "eng": [
        "- Use command execution to run diagnostic commands, read logs, and check system state.",
        "- Use file inspection to read source files, configs, and error output directly.",
        "- Use file editing for targeted code changes. Prefer `eng_minimal_patch` scope discipline.",
        "- After changes, use `eng_test_strategy` to verify the fix works and nothing else broke.",
    ],
    "prod": [
        "- Use web search tools to review competitor products and user feedback on review sites.",
        "- Use file inspection to load analytics data, user research files, and product specs.",
        "- After design work, run `core_review_changes` to check for scope creep.",
    ],
    "data": [
        "- Use command execution to run data queries and analysis scripts.",
        "- Use file inspection to load data exports, schema files, and query results.",
        "- After analysis, use `data_quality_checks` to validate findings before presenting.",
    ],
    "ops": [
        "- Use command execution to check system status, run deployments, and verify infrastructure state.",
        "- Use file inspection to load runbooks, config files, and incident history.",
        "- After operational changes, use `ops_change_management` to document what changed and why.",
    ],
    "pm": [
        "- Use file inspection to load project plans, roadmaps, and stakeholder communications.",
        "- Use command execution to check project status (git logs, CI results, milestone tracking).",
        "- After planning, use `pm_scope_tradeoffs` to pressure-test scope decisions.",
    ],
    "qa": [
        "- Use command execution to run test suites, check CI results, and verify deployment state.",
        "- Use file inspection to load test plans, bug reports, and acceptance criteria.",
        "- After testing, use `qa_release_smoke_test` to confirm release readiness.",
    ],
    "sec": [
        "- Use command execution to run security scanning tools, check dependency vulnerabilities, and audit configs.",
        "- Use file inspection to load security policies, auth configurations, and access control files.",
        "- After security review, use `sec_threat_model` to assess residual risk.",
    ],
    "sales": [
        "- Use web search tools to research prospect companies, news, and relevant context before outreach.",
        "- Use file inspection to load CRM data, call notes, and deal history.",
        "- After sales planning, use `att_proof_mining` to ensure every claim in materials is backed.",
    ],
    "res": [
        "- Use web search tools to gather competitor data, market reports, and source material.",
        "- Use file inspection to load interview transcripts, survey data, and research notes.",
        "- After research, use `core_evidence_research` to rate source quality and confidence.",
    ],
    "safe": [
        "- Use file inspection to load configs, credentials, and access control files for auditing.",
        "- Use command execution to verify system state, check permissions, and test security controls.",
        "- After safety review, use `core_risk_gate` to assess whether the change can proceed.",
    ],
    "doc": [
        "- Use file inspection to load existing docs, code comments, and API definitions.",
        "- Use command execution to check code structure and generate API schemas when needed.",
        "- After writing docs, use `doc_docs_feedback_loop` to plan for ongoing accuracy.",
    ],
    "des": [
        "- Use file inspection to load design specs, component libraries, and existing UI copy.",
        "- Use web search tools to review competitor designs and accessibility standards.",
        "- After design work, use `des_accessibility_review` to verify compliance.",
    ],
    "solo": [
        "- Use command execution to check current project status, deadlines, and shipping readiness.",
        "- Use file inspection to load personal productivity notes, goals, and rhythm files.",
        "- Pair with `solo_scope_guard` to prevent scope expansion during execution.",
    ],
    "vibe": [
        "- Use command execution to run AI-assisted code generation, debugging, and deployment commands.",
        "- Use file inspection to load prompts, code templates, and AI tool configurations.",
        "- After building, use `vibe_debug_no_code` to test without deep technical knowledge.",
    ],
    "comm": [
        "- Use platform APIs to check community channels, respond to members, and manage discussions.",
        "- Use file inspection to load community guidelines, feedback data, and engagement metrics.",
        "- After community actions, use `comm_retention_audit` to check member retention trends.",
    ],
    "legal": [
        "- Use web search tools to look up regulation references and compliance requirements.",
        "- Use file inspection to load existing legal documents, terms, and privacy policies.",
        "- After legal review, flag anything that needs actual attorney review. This skill assists, not replaces counsel.",
    ],
    "finance": [
        "- Use file inspection to load financial data, pricing spreadsheets, and revenue reports.",
        "- Use command execution to run calculations and financial models.",
        "- After financial analysis, use `finance_burn_rate` to cross-check sustainability.",
    ],
    "ai": [
        "- Use command execution to run model evaluations, prompt tests, and benchmarking scripts.",
        "- Use file inspection to load prompt templates, eval datasets, and model configurations.",
        "- After AI system design, use `ai_eval_harness` to validate performance claims.",
    ],
}

DEFAULT_TOOL_PATTERN = [
    "- Use file inspection to load relevant context files before starting.",
    "- Use command execution to verify current state before and after changes.",
    "- After completing, verify the result meets the stated objective.",
]

converted = 0

for skill_name in sorted(os.listdir(SRC_DIR)):
    src_path = os.path.join(SRC_DIR, skill_name, "SKILL.md")
    if not os.path.exists(src_path):
        continue
    
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace section header (handle all variants)
    content = content.replace("## OpenClaw tool pattern", "## Antigravity tool pattern")
    content = content.replace("## Claude Code tool pattern", "## Antigravity tool pattern")
    content = content.replace("## Codex tool pattern", "## Antigravity tool pattern")
    
    # Replace tool names in the tool pattern section
    cat = skill_name.split("_")[0] if "_" in skill_name else "other"
    
    # General replacements for tool pattern section
    replacements = [
        ("`exec`", "command execution"),
        ("`read`", "file inspection"),
        ("`write`", "file writing"),
        ("`edit`", "file editing"),
        ("`web_fetch`", "web search tools"),
        ("`Bash`", "command execution"),
        ("`Read`", "file inspection"),
        ("`Write`", "file writing"),
        ("`Edit`", "file editing"),
        ("`WebFetch`", "web search tools"),
        ("`shell`", "command execution"),
        ("`shell` with `curl`", "web search tools"),
    ]
    
    # Find and replace within tool pattern section only
    pattern = r'(## Antigravity tool pattern\s*\n)((?:- .*\n)+)'
    match = re.search(pattern, content)
    if match:
        section = match.group(2)
        for old, new in replacements:
            section = section.replace(old, new)
        content = content[:match.start(2)] + section + content[match.end(2):]
    
    # Remove disable-model-invocation
    content = re.sub(r'\ndisable-model-invocation: [^\n]+', '', content)
    
    # Write
    dest_skill_dir = os.path.join(DEST_DIR, skill_name)
    os.makedirs(dest_skill_dir, exist_ok=True)
    dest_path = os.path.join(dest_skill_dir, "SKILL.md")
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    converted += 1

print(f"Converted: {converted} skills from OpenClaw v1.0 to Antigravity format")
