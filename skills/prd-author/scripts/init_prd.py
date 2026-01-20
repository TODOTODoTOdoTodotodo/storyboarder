#!/usr/bin/env python3
import argparse
import datetime
import os
import re
import sys


def slugify(name: str) -> str:
    value = name.strip().lower()
    value = re.sub(r"[^a-z0-9\s_-]", "", value)
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-") or "project"


def load_template(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def strip_section(content: str, start_marker: str, end_marker: str) -> str:
    pattern = re.compile(
        r"\n?" + re.escape(start_marker) + r".*?" + re.escape(end_marker) + r"\n?",
        re.DOTALL,
    )
    return re.sub(pattern, "\n", content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a PRD file from template.")
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument(
        "--role",
        required=True,
        choices=["fe", "be", "both"],
        help="Scope selection",
    )
    parser.add_argument(
        "--outdir",
        default=os.getcwd(),
        help="Output directory (default: cwd)",
    )
    parser.add_argument("--owner", default="TBD", help="Owner name")
    parser.add_argument("--force", action="store_true", help="Overwrite if exists")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "..", "assets", "prd_template.md")
    template_path = os.path.abspath(template_path)

    if not os.path.isfile(template_path):
        print(f"Template not found: {template_path}", file=sys.stderr)
        return 1

    project_slug = slugify(args.project)
    filename = f"PRD-{project_slug}.md"
    output_path = os.path.join(os.path.abspath(args.outdir), filename)

    if os.path.exists(output_path) and not args.force:
        print(f"PRD already exists: {output_path}", file=sys.stderr)
        return 2

    content = load_template(template_path)
    today = datetime.date.today().isoformat()
    scope_label = "FE" if args.role == "fe" else "BE" if args.role == "be" else "FE+BE"

    content = content.replace("{{PROJECT_NAME}}", args.project)
    content = content.replace("{{DATE}}", today)
    content = content.replace("{{OWNER}}", args.owner)
    content = content.replace("{{SCOPE}}", scope_label)

    if args.role == "fe":
        content = strip_section(content, "<!-- BE_SECTION_START -->", "<!-- BE_SECTION_END -->")
    elif args.role == "be":
        content = strip_section(content, "<!-- FE_SECTION_START -->", "<!-- FE_SECTION_END -->")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
