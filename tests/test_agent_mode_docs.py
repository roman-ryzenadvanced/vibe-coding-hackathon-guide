"""
Tests for Agent Mode documentation across all docs.
Validates that the "Please use this skill" pattern is documented
in README, guide.html, and all docs/ files.
"""
import pytest
from pathlib import Path
from conftest import GUIDE_HTML, PROJECT_ROOT

DOCS_DIR = PROJECT_ROOT / "docs"
README = PROJECT_ROOT / "README.md"

SKILL_URL = "https://github.com/roman-ryzenadvanced/last30days-skill"
PATTERN = "Please use this skill"


class TestAgentModeInReadme:
    """Test that README.md has Agent Mode on chat.z.ai instructions."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.content = README.read_text(encoding="utf-8")

    def test_has_agent_mode_section(self):
        assert "Agent Mode" in self.content, "README must have Agent Mode section"

    def test_has_please_use_this_skill(self):
        assert PATTERN in self.content, f"README must include '{PATTERN}' pattern"

    def test_has_skill_url(self):
        assert SKILL_URL in self.content, "README must include the skill GitHub URL"

    def test_has_chat_z_ai(self):
        assert "chat.z.ai" in self.content, "README must mention chat.z.ai"

    def test_has_zero_install_mention(self):
        content_lower = self.content.lower()
        assert "zero" in content_lower or "no install" in content_lower or "no local" in content_lower or "don't need to install" in content_lower, \
            "README must mention zero/no-install nature of chat.z.ai usage"

    def test_has_how_pattern_works_table(self):
        assert "How the" in self.content and "Pattern Works" in self.content, \
            "README must explain how the pattern works"

    def test_has_agent_mode_prompts(self):
        # Should have at least 3 example prompts
        prompt_count = self.content.count(PATTERN)
        assert prompt_count >= 3, f"README should have at least 3 '{PATTERN}' examples, found {prompt_count}"

    def test_has_specificity_tip(self):
        assert "specific" in self.content.lower(), "README must mention prompt specificity tip"


class TestAgentModeInDocs:
    """Test that docs/ files have Agent Mode instructions."""

    def test_how_to_use_has_agent_mode(self):
        filepath = DOCS_DIR / "how-to-use-30d-skill.md"
        content = filepath.read_text(encoding="utf-8")
        assert PATTERN in content, f"{filepath.name} must include '{PATTERN}' pattern"
        assert SKILL_URL in content, f"{filepath.name} must include skill URL"
        assert "chat.z.ai" in content, f"{filepath.name} must mention chat.z.ai"

    def test_commands_reference_has_agent_mode(self):
        filepath = DOCS_DIR / "skill-commands-reference.md"
        content = filepath.read_text(encoding="utf-8")
        assert PATTERN in content, f"{filepath.name} must include '{PATTERN}' pattern"
        assert "Zero Install" in content or "zero install" in content, \
            f"{filepath.name} must mention Zero Install"

    def test_hackathon_workflow_has_agent_mode(self):
        filepath = DOCS_DIR / "hackathon-workflow.md"
        content = filepath.read_text(encoding="utf-8")
        assert PATTERN in content, f"{filepath.name} must include '{PATTERN}' pattern"
        assert SKILL_URL in content, f"{filepath.name} must include skill URL"

    def test_how_to_use_has_copy_paste_prompts(self):
        filepath = DOCS_DIR / "how-to-use-30d-skill.md"
        content = filepath.read_text(encoding="utf-8")
        assert "Copy-Paste" in content or "copy" in content.lower(), \
            "how-to-use doc must have copy-paste prompts section"

    def test_how_to_use_has_output_format(self):
        filepath = DOCS_DIR / "how-to-use-30d-skill.md"
        content = filepath.read_text(encoding="utf-8")
        assert "Key Findings" in content, "how-to-use doc must describe Agent Mode output format"
        assert "What I learned" in content, "how-to-use doc must describe Agent Mode output format"

    def test_how_to_use_has_tips_section(self):
        filepath = DOCS_DIR / "how-to-use-30d-skill.md"
        content = filepath.read_text(encoding="utf-8")
        assert "Tips for Better Agent Mode" in content, "how-to-use doc must have Agent Mode tips"

    def test_commands_ref_has_templates_table(self):
        filepath = DOCS_DIR / "skill-commands-reference.md"
        content = filepath.read_text(encoding="utf-8")
        assert "Copy-Paste Templates" in content, "commands ref must have copy-paste templates table"


class TestAgentModeInGuideHtml:
    """Test that guide.html has Agent Mode page."""

    @pytest.fixture(autouse=True)
    def setup(self, guide_html_content):
        self.content = guide_html_content

    def test_has_dedicated_agent_mode_page(self):
        assert "Use Agent Mode on chat.z.ai" in self.content, \
            "guide.html must have dedicated Agent Mode page"

    def test_has_please_use_this_skill_pattern(self):
        assert PATTERN in self.content, \
            f"guide.html must include '{PATTERN}' pattern"

    def test_has_skill_url(self):
        assert SKILL_URL in self.content, \
            "guide.html must include the skill GitHub URL"

    def test_agent_mode_in_commands_reference(self):
        # The commands reference section in guide.html should also mention it
        assert "chat.z.ai" in self.content, \
            "guide.html must mention chat.z.ai in commands section"
