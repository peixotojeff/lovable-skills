#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "lovable-imports"
SKILLS_ROOT = ROOT / "skills"


def resolve_skill_dir(ref: str) -> Path:
    candidate = Path(ref)
    if candidate.is_absolute() and candidate.exists():
        return candidate

    if candidate.exists():
        return candidate.resolve()

    by_name = SKILLS_ROOT / ref
    if by_name.is_dir():
        return by_name

    matches = list(SKILLS_ROOT.rglob(ref))
    for match in matches:
        if match.name == "SKILL.md":
            return match.parent

    raise FileNotFoundError(f"Could not resolve skill reference: {ref}")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: package_lovable_skill.py <skill-name|skill-path>", file=sys.stderr)
        return 2

    skill_dir = resolve_skill_dir(argv[1])
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print(f"Missing SKILL.md in {skill_dir}", file=sys.stderr)
        return 1

    manifest_path = ROOT / "skills-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    skill_name = skill_dir.name

    package_dir = DIST / skill_name
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(skill_md, package_dir / "SKILL.md")

    # Copy any supporting files if they exist.
    for subdir in ("references", "templates", "scripts", "assets"):
        src = skill_dir / subdir
        if src.exists():
            shutil.copytree(src, package_dir / subdir, dirs_exist_ok=True)

    zip_path = DIST / f"{skill_name}.zip"
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in package_dir.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(DIST))

    matching = next((item for item in manifest.get("skills", []) if item.get("name") == skill_name), None)
    print(json.dumps({
        "skill": skill_name,
        "package_dir": str(package_dir),
        "zip_path": str(zip_path),
        "frontmatter_name": matching.get("name") if matching else None,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
