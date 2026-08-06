#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def main() -> int:
    manifest_path = ROOT / "skills-manifest.json"
    if not manifest_path.exists():
        print(f"Missing manifest: {manifest_path}", file=sys.stderr)
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    DIST.mkdir(exist_ok=True)

    bundle_dir = DIST / "lovable-skills-pack"
    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    bundle_dir.mkdir(parents=True)

    # Copy the canonical publishing files.
    for rel in ["README.md", "skills/index.md", "skills-manifest.json", "docs/publishing.md", "docs/skill-roadmap.md"]:
        src = ROOT / rel
        dst = bundle_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    # Copy the skills directory.
    skills_src = ROOT / "skills"
    skills_dst = bundle_dir / "skills"
    shutil.copytree(skills_src, skills_dst, dirs_exist_ok=True)

    zip_path = DIST / "lovable-skills-pack.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in bundle_dir.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(bundle_dir))

    print(json.dumps({
        "bundle_dir": str(bundle_dir),
        "zip_path": str(zip_path),
        "skills": len(manifest.get("skills", [])),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
