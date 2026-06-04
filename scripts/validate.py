#!/usr/bin/env python3
"""Validate recipe metadata and local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "recipes"
CATALOG = ROOT / "catalog.json"
REQUIRED_FIELDS = {"id", "title", "summary", "difficulty", "time_saved", "tags"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} is missing front matter")
    try:
        _, block, _ = text.split("---\n", 2)
    except ValueError:
        fail(f"{path.relative_to(ROOT)} has invalid front matter")

    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)} has invalid metadata line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def local_markdown_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    return [
        link.split("#", 1)[0]
        for link in links
        if link
        and not link.startswith(("http://", "https://", "mailto:"))
        and not link.startswith("#")
    ]


def main() -> None:
    if not CATALOG.exists():
        fail("catalog.json is missing")

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_ids = {item["id"] for item in catalog}
    catalog_files = {item["file"] for item in catalog}

    recipe_paths = sorted(p for p in RECIPES.glob("*.md") if p.name != "_template.md")
    recipe_ids: set[str] = set()

    for path in recipe_paths:
        meta = parse_front_matter(path)
        missing = REQUIRED_FIELDS - set(meta)
        if missing:
            fail(f"{path.relative_to(ROOT)} missing fields: {', '.join(sorted(missing))}")
        recipe_id = meta["id"]
        recipe_ids.add(recipe_id)
        expected_file = f"recipes/{path.name}"
        if recipe_id not in catalog_ids:
            fail(f"{recipe_id} is missing from catalog.json")
        if expected_file not in catalog_files:
            fail(f"{expected_file} is missing from catalog.json")
        text = path.read_text(encoding="utf-8")
        if f"# {meta['title']}" not in text:
            fail(f"{path.relative_to(ROOT)} missing matching H1 title")
        if "## Copy-Paste Prompt" not in text:
            fail(f"{path.relative_to(ROOT)} missing Copy-Paste Prompt section")
        if "## Output Contract" not in text:
            fail(f"{path.relative_to(ROOT)} missing Output Contract section")

    extra = catalog_ids - recipe_ids
    if extra:
        fail(f"catalog.json contains recipes without files: {', '.join(sorted(extra))}")

    for path in [
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "ROADMAP.md",
    ]:
        for link in local_markdown_links(path):
            target = (path.parent / link).resolve()
            if not target.exists():
                fail(f"{path.relative_to(ROOT)} links to missing file: {link}")

    print(f"OK: validated {len(recipe_paths)} recipes")


if __name__ == "__main__":
    main()
