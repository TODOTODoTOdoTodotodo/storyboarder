---
name: prd-loader
description: Load an existing PRD-<project>.md into context before handling requests. Use when a user asks to load a PRD, prepare context for work, or when tasks should be grounded in the project PRD.
---

# PRD Loader

## Overview
Locate the PRD file in the current project directory, load it into context, and validate that required sections are present. If missing, chain to `prd-author` to complete gaps.

## Workflow

1) Locate the PRD
- Search the current directory for `PRD-*.md`.
- If multiple files exist, ask the user to pick one.
- If none exist, call `prd-author` to create one.

2) Load and summarize
- Read the selected PRD and keep it in context.
- Provide a short recap: goals, scope, key requirements, and open questions.

3) Validate completeness
- Check that core sections are present and non-empty:
  - Problem/Opportunity
  - Goals and Non-goals
  - Users/Personas
  - Requirements (functional and non-functional)
  - Success Metrics
  - Risks/Assumptions
  - Milestones
- If missing or empty, chain to `prd-author` with only the missing sections.

4) Confirm readiness
- Tell the user the PRD is loaded and ready for task execution.
