#!/usr/bin/env python3
"""Generate the README table of contents from Markdown notes in source directories."""

from __future__ import annotations

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPOSITORY_ROOT / "README.md"
START_MARKER = "<!-- Table of Contents Start -->"
STOP_MARKER = "<!-- Table of Contents Stop -->"


def display_name(path: Path | str) -> str:
    """Turn a path component into a readable TOC label."""
    words = Path(path).stem.replace("_", " ").replace("-", " ").title().split()
    acronyms = {"Cissp": "CISSP", "Isc2": "ISC2", "Linkedin": "LinkedIn"}
    return " ".join(acronyms.get(word, word) for word in words)


def find_source_files() -> dict[Path, list[Path]]:
    """Return Markdown notes grouped by their top-level source directory."""
    source_files = {}
    for source_directory in sorted(
        REPOSITORY_ROOT.iterdir(), key=lambda path: path.name.lower()
    ):
        if not source_directory.is_dir() or source_directory.name.startswith("."):
            continue

        files = sorted(
            (
                path.relative_to(REPOSITORY_ROOT)
                for path in source_directory.rglob("*.md")
                if path.is_file()
                and not any(
                    part.startswith(".")
                    for part in path.relative_to(source_directory).parts
                )
            ),
            key=lambda path: str(path).lower(),
        )
        if files:
            source_files[source_directory.relative_to(REPOSITORY_ROOT)] = files
    return source_files


def build_toc() -> str:
    entries = []
    for source, files in find_source_files().items():
        entries.append(f"- {display_name(source)}")
        rendered_directories = set()
        for path in files:
            relative_to_source = path.relative_to(source)
            directories = relative_to_source.parts[:-1]
            for index in range(len(directories)):
                directory = Path(*directories[: index + 1])
                if directory in rendered_directories:
                    continue
                rendered_directories.add(directory)
                indent = "  " * (index + 1)
                entries.append(f"{indent}- {display_name(directories[index])}")

            indent = "  " * (len(directories) + 1)
            entries.append(
                f"{indent}- [{display_name(relative_to_source.name)}]({path.as_posix()})"
            )
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
