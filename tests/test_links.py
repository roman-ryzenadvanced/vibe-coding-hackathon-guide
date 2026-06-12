"""
Tests for link validation in project files.
Checks that all referenced URLs and internal links are properly formatted.
"""
import pytest
import re
from pathlib import Path
from conftest import (
    PROJECT_ROOT,
    GUIDE_HTML,
    COVER_HTML,
    README_MD,
    EXPECTED_FEATURES,
    EXPECTED_DOCS,
)


class TestInternalLinks:
    """Test that internal file references in README point to existing files."""

    @pytest.fixture(autouse=True)
    def setup(self, readme_content):
        self.content = readme_content

    def test_changelog_link(self):
        assert "CHANGELOG.md" in self.content, "README must link to CHANGELOG.md"
        assert (PROJECT_ROOT / "CHANGELOG.md").exists(), "CHANGELOG.md must exist"

    def test_license_link(self):
        assert "LICENSE" in self.content, "README must link to LICENSE"
        assert (PROJECT_ROOT / "LICENSE").exists(), "LICENSE must exist"

    def test_features_link(self):
        assert "FEATURES.md" in self.content, "README must link to FEATURES.md"
        assert (PROJECT_ROOT / "FEATURES.md").exists(), "FEATURES.md must exist"

    def test_contributing_link(self):
        assert "CONTRIBUTING.md" in self.content, "README must link to CONTRIBUTING.md"
        assert (PROJECT_ROOT / "CONTRIBUTING.md").exists(), "CONTRIBUTING.md must exist"


class TestExternalLinks:
    """Test that external URLs in key files are properly formatted."""

    def test_readme_has_github_repo_link(self, readme_content):
        assert "github.com/roman-ryzenadvanced/last30days-skill" in readme_content, \
            "README must link to last30days-skill repo"

    def test_readme_has_zai_link(self, readme_content):
        assert "z.ai" in readme_content, "README must reference z.ai"

    def test_readme_has_rommark_link(self, readme_content):
        assert "rommark.dev" in readme_content, "README must reference rommark.dev"

    def test_cover_has_discount_url(self, cover_html_content):
        assert "z.ai/subscribe?ic=ROK78RJKNW" in cover_html_content, \
            "Cover must link to discount URL"

    def test_guide_has_discount_url(self, guide_html_content):
        assert "z.ai/subscribe?ic=ROK78RJKNW" in guide_html_content, \
            "Guide must link to discount URL"


class TestRepoStructureLinks:
    """Test that the repository structure documented in README matches actual files."""

    @pytest.fixture(autouse=True)
    def setup(self, readme_content):
        self.content = readme_content

    def test_guide_html_listed(self):
        assert "guide.html" in self.content, "README must list guide.html"

    def test_cover_html_listed(self):
        assert "cover.html" in self.content, "README must list cover.html"

    def test_pdf_listed(self):
        assert "hackathon-ideas-guide.pdf" in self.content, "README must list PDF"

    def test_docs_dir_listed(self):
        assert "docs/" in self.content, "README must list docs/ directory"

    def test_features_dir_listed(self):
        assert "features/" in self.content, "README must list features/ directory"

    def test_tests_dir_listed(self):
        assert "tests/" in self.content, "README must list tests/ directory"


class TestMarkdownLinkFormat:
    """Test that markdown links in documentation are properly formatted."""

    @pytest.mark.parametrize("filepath", [
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "CHANGELOG.md",
        PROJECT_ROOT / "FEATURES.md",
        PROJECT_ROOT / "CONTRIBUTING.md",
    ])
    def test_markdown_links_valid_format(self, filepath):
        if not filepath.exists():
            pytest.skip(f"{filepath.name} does not exist")
        content = filepath.read_text(encoding="utf-8")
        # Find all markdown links [text](url)
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, url in links:
            if not url.startswith('http') and not url.startswith('#'):
                # Internal link - check file exists
                target = PROJECT_ROOT / url
                assert target.exists() or (PROJECT_ROOT / url.split('#')[0]).exists(), \
                    f"Broken internal link in {filepath.name}: [{text}]({url})"
