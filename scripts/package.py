#!/usr/bin/env python3
"""
Package the AI ChatNav extension for Chrome Web Store upload.

Validates all manifest-referenced files exist, then creates a .zip
containing only the src/ directory contents.

Usage:
    python scripts/package.py             # Build the .zip
    python scripts/package.py --check     # Validate only (for CI)
    python scripts/package.py --dry-run   # Show what would be packaged
"""

import argparse
import json
import os
import sys
import zipfile
from pathlib import Path


def find_project_root():
    """Find the project root by looking for src/manifest.json."""
    # Try current directory first
    if Path("src/manifest.json").exists():
        return Path.cwd()
    # Try script's parent directory
    script_dir = Path(__file__).resolve().parent.parent
    if (script_dir / "src" / "manifest.json").exists():
        return script_dir
    raise FileNotFoundError("Cannot find src/manifest.json. Run from project root.")


def get_version(root):
    """Read version from aichatnav/_version.py."""
    version_file = root / "aichatnav" / "_version.py"
    if not version_file.exists():
        # Fallback: read from manifest.json
        manifest = json.loads((root / "src" / "manifest.json").read_text(encoding="utf-8"))
        return manifest.get("version", "0.0.0")

    content = version_file.read_text(encoding="utf-8")
    # Extract MAJOR, MINOR, PATCH
    import re
    major = re.search(r"^MAJOR\s*=\s*(\d+)", content, re.MULTILINE)
    minor = re.search(r"^MINOR\s*=\s*(\d+)", content, re.MULTILINE)
    patch = re.search(r"^PATCH\s*=\s*(\d+)", content, re.MULTILINE)
    if all([major, minor, patch]):
        return f"{major.group(1)}.{minor.group(1)}.{patch.group(1)}"
    return "0.0.0"


def validate_manifest(root):
    """Validate all files referenced in manifest.json exist in src/."""
    src = root / "src"
    manifest_path = src / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = []

    # Check icons
    icons = manifest.get("icons", {})
    for size, path in icons.items():
        if not (src / path).exists():
            errors.append(f"Icon missing: {path} ({size}px)")

    # Check content scripts
    for cs in manifest.get("content_scripts", []):
        for js_file in cs.get("js", []):
            if not (src / js_file).exists():
                errors.append(f"Content script missing: {js_file}")
        for css_file in cs.get("css", []):
            if not (src / css_file).exists():
                errors.append(f"Stylesheet missing: {css_file}")

    # Check options page
    options_page = manifest.get("options_page")
    if options_page and not (src / options_page).exists():
        errors.append(f"Options page missing: {options_page}")

    # Check background/service worker
    bg = manifest.get("background", {})
    sw = bg.get("service_worker")
    if sw and not (src / sw).exists():
        errors.append(f"Service worker missing: {sw}")

    return errors


def collect_files(src_dir):
    """Collect all files in src/ for packaging."""
    files = []
    for path in sorted(src_dir.rglob("*")):
        if path.is_file():
            rel = path.relative_to(src_dir)
            files.append((path, str(rel)))
    return files


def build_package(root, output_dir, version, dry_run=False):
    """Build the .zip package."""
    src = root / "src"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    zip_name = f"aichatnav-v{version}.zip"
    zip_path = output_dir / zip_name

    files = collect_files(src)
    total_size = sum(f[0].stat().st_size for f in files)

    print(f"Packaging AI ChatNav v{version}")
    print(f"  Source: {src}")
    print(f"  Files: {len(files)}")
    print(f"  Size: {total_size / 1024:.1f} KB (uncompressed)")

    if dry_run:
        print(f"\n  Would create: {zip_path}")
        print("\n  Contents:")
        for abs_path, rel_path in files:
            size = abs_path.stat().st_size
            print(f"    {rel_path:40s} {size:>8,d} bytes")
        return str(zip_path)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for abs_path, rel_path in files:
            zf.write(abs_path, rel_path)

    zip_size = zip_path.stat().st_size
    print(f"  Output: {zip_path}")
    print(f"  Compressed: {zip_size / 1024:.1f} KB")
    return str(zip_path)


def main():
    parser = argparse.ArgumentParser(
        description="Package AI ChatNav for Chrome Web Store"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Validate only, don't build (exit 1 if errors)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be packaged without creating the zip"
    )
    parser.add_argument(
        "--output", "-o", default="dist",
        help="Output directory (default: dist)"
    )
    args = parser.parse_args()

    try:
        root = find_project_root()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Always validate
    errors = validate_manifest(root)
    if errors:
        print("Validation errors:", file=sys.stderr)
        for err in errors:
            print(f"  [X] {err}", file=sys.stderr)
        return 1

    version = get_version(root)

    if args.check:
        print(f"AI ChatNav v{version}: all manifest references valid")
        return 0

    build_package(root, args.output, version, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
