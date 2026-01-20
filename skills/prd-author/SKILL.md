---
name: prd-author
description: Create and maintain a full PRD by interviewing the user, selecting FE/BE scope, and writing a PRD-<project>.md file in the current project directory. Use when a user asks to create a PRD, requirements doc, planning document, or when PRD fields are missing and need to be completed.
---

# PRD Author

## Overview
Create a complete PRD through a structured interview, then save it as `PRD-<project>.md` in the current working directory using the template in `assets/prd_template.md`.

## Workflow

1) Select scope
- Ask which scope to write: `FE`, `BE`, or `FE+BE`.
- If the user wants a codename or project name, suggest a short list and let them pick.

2) Initialize the PRD file
- Use `scripts/init_prd.py` to create the file from the template.
- File naming: `PRD-<project>.md` where `<project>` is a lowercase slug.
- Do not overwrite an existing PRD unless the user confirms.

3) Interview for core PRD sections
- Problem/Opportunity
- Goals and Non-goals
- Users/Personas
- Scope (in/out)
- Requirements: functional and non-functional
- Success metrics
- Risks/Assumptions
- Milestones
- Open questions
- References

4) Interview for role-specific sections
- If `FE`, ask only FE section questions.
- If `BE`, ask only BE section questions.
- If `FE+BE`, ask both.

FE questions (compact checklist)
- IA/navigation and key screens?
- Primary components and state ownership?
- API integration plan (endpoints + data shapes)?
- Loading/error/empty UX expectations?
- Accessibility targets?
- Performance budget (TTI/LCP or payload constraints)?
- Analytics/telemetry needs?
- Testing strategy?

BE questions (compact checklist)
- Domain model and key entities?
- API list with request/response shape?
- Data store and schema decisions?
- Auth/authz requirements?
- Async processing or background jobs?
- Observability: logs/metrics/traces?
- Scaling/performance constraints?
- Security concerns?
- Data migration/backfill?
- Testing strategy?

5) Write and refine
- Update the PRD file section-by-section as answers arrive.
- Keep unknowns in the Open Questions list instead of guessing.

## Resources

### scripts/
- `scripts/init_prd.py`: create a PRD skeleton from the template and role selection.

### assets/
- `assets/prd_template.md`: the PRD template with FE/BE sections and placeholder markers.
