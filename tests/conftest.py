"""
Shared test fixtures and utilities for the Vibe Coding Builders Hackathon Guide test suite.
"""
import os
import sys
import pytest
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# File paths used across tests
GUIDE_HTML = PROJECT_ROOT / "guide.html"
COVER_HTML = PROJECT_ROOT / "cover.html"
GUIDE_PDF = PROJECT_ROOT / "hackathon-ideas-guide.pdf"
README_MD = PROJECT_ROOT / "README.md"
CHANGELOG_MD = PROJECT_ROOT / "CHANGELOG.md"
FEATURES_MD = PROJECT_ROOT / "FEATURES.md"
CONTRIBUTING_MD = PROJECT_ROOT / "CONTRIBUTING.md"
LICENSE_FILE = PROJECT_ROOT / "LICENSE"

# Directories
DOCS_DIR = PROJECT_ROOT / "docs"
FEATURES_DIR = PROJECT_ROOT / "features"
TESTS_DIR = PROJECT_ROOT / "tests"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
RELEASES_DIR = PROJECT_ROOT / "releases"
ASSETS_DIR = PROJECT_ROOT / "assets"

# Expected feature docs (10 ideas)
EXPECTED_FEATURES = [f"idea-{str(i).zfill(2)}-{name}.md" for i, name in enumerate([
    "trend-to-app",
    "competitor-dashboard",
    "dev-pulse",
    "niche-discovery-bot",
    "micro-saas-launchpad",
    "signal-validator",
    "pivot-predictor",
    "provider-marketplace",
    "research-agent",
    "revenue-calculator",
], 1)]

# Expected docs
EXPECTED_DOCS = [
    "how-to-use-30d-skill.md",
    "hackathon-workflow.md",
    "skill-commands-reference.md",
]

# Branding elements
ZAI_BRAND = "z.ai"
ROMMARK_BRAND = "rommark.dev"
DISCOUNT_CODE = "ROK78RJKNW"
DISCOUNT_URL = "https://z.ai/subscribe?ic=ROK78RJKNW"

# Required sections in feature docs
REQUIRED_FEATURE_SECTIONS = [
    "Quick Stats",
    "The Problem",
    "The Solution",
    "Architecture",
    "Data Flow",
    "Skill API Mapping",
    "Tech Stack",
    "Implementation Steps",
    "Demo Script",
]


@pytest.fixture
def project_root():
    """Return the project root directory."""
    return PROJECT_ROOT


@pytest.fixture
def guide_html_content():
    """Read and return the guide HTML content."""
    return GUIDE_HTML.read_text(encoding="utf-8")


@pytest.fixture
def cover_html_content():
    """Read and return the cover HTML content."""
    return COVER_HTML.read_text(encoding="utf-8")


@pytest.fixture
def readme_content():
    """Read and return the README content."""
    return README_MD.read_text(encoding="utf-8")


@pytest.fixture
def changelog_content():
    """Read and return the CHANGELOG content."""
    return CHANGELOG_MD.read_text(encoding="utf-8")


@pytest.fixture
def features_content():
    """Read and return the FEATURES content."""
    return FEATURES_MD.read_text(encoding="utf-8")
