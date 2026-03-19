"""
Version information for aichatnav.

This file is the canonical source for version numbers.
The __version__ string is automatically updated by git hooks
with build metadata (branch, build number, date, commit hash).

Format: MAJOR.MINOR.PATCH[-PHASE]_BRANCH_BUILD-YYYYMMDD-COMMITHASH
Example: 0.1.0_main_4-20260317-a1b2c3d4

To sync versions: python scripts/sync-versions.py
To bump version: python scripts/sync-versions.py --bump patch
"""

# Version components - edit these for version bumps
MAJOR = 0
MINOR = 2
PATCH = 3
PHASE = "alpha"  # Per-MINOR feature set: None, "alpha", "beta", "rc1", etc.
PRE_RELEASE_NUM = 1  # PEP 440 pre-release number (e.g., a1, b2)
PROJECT_PHASE = "prealpha"  # Project-wide: "prealpha", "alpha", "beta", "stable"

# Auto-updated by git hooks - do not edit manually
__version__ = "0.2.3-alpha_main_9-20260318-72b22733"
__app_name__ = "aichatnav"


def get_version():
    """Return the full version string including branch and build info."""
    return __version__


def get_display_version():
    """Return a human-friendly version string with project phase."""
    base = get_base_version()
    if PROJECT_PHASE and PROJECT_PHASE != "stable":
        return f"{PROJECT_PHASE.upper()} {base}"
    return base


def get_base_version():
    """Return semantic version only (e.g., '0.1.0' or '0.1.0-alpha')."""
    base = f"{MAJOR}.{MINOR}.{PATCH}"
    if PHASE:
        base += f"-{PHASE}"
    return base


def get_manifest_version():
    """Return version suitable for manifest.json (no phase, just M.M.P)."""
    return f"{MAJOR}.{MINOR}.{PATCH}"
