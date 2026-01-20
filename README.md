# Storyboarder PRD Skills

Storyboarder provides two Codex skills to create and load PRD documents with a consistent structure. It supports FE/BE scoped PRDs and saves files as `PRD-<project>.md` in the current project directory.

## Features
- Guided PRD interview with FE/BE scope selection
- Consistent PRD template with role-specific sections
- PRD loader that validates completeness and prompts for missing sections
- Project-local skills that can be synced to global Codex skills

## Getting Started

1) Sync skills to global Codex skills

```bash
rsync -a ./skills/ ~/.codex/skills/
```

2) Start a PRD interview

```text
$prd-author
```

3) Load an existing PRD

```text
$prd-loader
```

4) Generate a PRD file from the template directly (optional)

```bash
./skills/prd-author/scripts/init_prd.py --project <name> --role fe|be|both --outdir . --owner <owner>
```

## TODO
- Fill BE section details in a real PRD (domain model, APIs, data store, auth, async, observability, scaling, security, migration, testing).
- Decide success metric targets beyond latency (accuracy/quality thresholds) if needed.
- Confirm scope details for in/out and user persona specifics.
