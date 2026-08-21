#!/usr/bin/env python3
"""Generate the README table of contents from repository Notes.md files."""

from __future__ import annotations

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPOSITORY_ROOT / "README.md"
START_MARKER = "<!-- Table of Contents Start -->"
STOP_MARKER = "<!-- Table of Contents Stop -->"
NOTE_FILENAME = "Notes.md"
EXCLUDED_DIRECTORIES = {".git", ".github", "scripts"}


def display_name(notes_path: Path) -> str:
    """Turn a notes directory name into a readable TOC label."""
    return notes_path.parent.name.replace("_", " ").replace("-", " ").title()


def find_notes() -> list[Path]:
    """Return all Notes.md files that should appear in the root TOC."""
    notes = []
    for path in REPOSITORY_ROOT.rglob(NOTE_FILENAME):
        relative_path = path.relative_to(REPOSITORY_ROOT)
        if any(part in EXCLUDED_DIRECTORIES for part in relative_path.parts[:-1]):
            continue
        notes.append(relative_path)
    return sorted(notes, key=lambda path: str(path).lower())


def build_toc() -> str:
    entries = [
        f"- [{display_name(path)}]({path.as_posix()})" for path in find_notes()
    ]
    return "## Table of Contents\n\n" + "\n".join(entries)


def update_readme() -> bool:
    """Replace only the marked TOC section. Return whether README changed."""
    readme = README_PATH.read_text(encoding="utf-8")
    start = readme.find(START_MARKER)
    stop = readme.find(STOP_MARKER)

    if start == -1 or stop == -1 or stop <= start:
        raise ValueError(
            f"{README_PATH} must contain {START_MARKER} before {STOP_MARKER}."
        )

    content_start = start + len(START_MARKER)
    updated = readme[:content_start] + "\n\n" + build_toc() + "\n\n" + readme[stop:]

    if updated == readme:
        return False

    README_PATH.write_text(updated, encoding="utf-8")
    return True


if __name__ == "__main__":
    changed = update_readme()
    print("Updated README table of contents." if changed else "README table of contents is current.")
