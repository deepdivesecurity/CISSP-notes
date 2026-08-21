#!/usr/bin/env python3
"""Generate the README table of contents from files in CISSP domain directories."""

from __future__ import annotations

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPOSITORY_ROOT / "README.md"
START_MARKER = "<!-- Table of Contents Start -->"
STOP_MARKER = "<!-- Table of Contents Stop -->"
DOMAIN_DIRECTORY_PREFIX = "domain_"


def display_name(path: Path | str) -> str:
    """Turn a path component into a readable TOC label."""
    return Path(path).stem.replace("_", " ").replace("-", " ").title()


def find_domain_files() -> dict[Path, list[Path]]:
    """Return every file under each top-level domain directory."""
    domain_files = {}
    for domain_directory in REPOSITORY_ROOT.iterdir():
        if not (
            domain_directory.is_dir()
            and domain_directory.name.startswith(DOMAIN_DIRECTORY_PREFIX)
        ):
            continue

        files = sorted(
            (path.relative_to(REPOSITORY_ROOT) for path in domain_directory.rglob("*") if path.is_file()),
            key=lambda path: str(path).lower(),
        )
        if files:
            domain_files[domain_directory.relative_to(REPOSITORY_ROOT)] = files
    return domain_files


def build_toc() -> str:
    entries = []
    for domain, files in find_domain_files().items():
        entries.append(f"- {display_name(domain)}")
        for path in files:
            relative_to_domain = path.relative_to(domain)
            label = " / ".join(display_name(part) for part in relative_to_domain.parts)
            entries.append(f"  - [{label}]({path.as_posix()})")
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
