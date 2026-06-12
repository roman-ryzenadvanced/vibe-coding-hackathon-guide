"""
Tests for the guide HTML structure and content.
Validates that all required sections, branding, and content are present.
"""
import pytest
from pathlib import Path
from conftest import (
    GUIDE_HTML,
    ZAI_BRAND,
    ROMMARK_BRAND,
    DISCOUNT_CODE,
    DISCOUNT_URL,
)


class TestGuideHtmlExists:
    """Test that the guide HTML file exists and is non-empty."""

    def test_guide_html_exists(self):
        assert GUIDE_HTML.exists(), "guide.html must exist"

    def test_guide_html_non_empty(self):
        content = GUIDE_HTML.read_text(encoding="utf-8")
        assert len(content) > 1000, "guide.html must have substantial content"


class TestGuideHtmlStructure:
    """Test the structural elements of the guide HTML."""

    @pytest.fixture(autouse=True)
    def setup(self, guide_html_content):
        self.content = guide_html_content

    def test_has_html_doctype(self):
        assert "<!DOCTYPE html>" in self.content, "Must have HTML5 doctype"

    def test_has_head_section(self):
        assert "<head>" in self.content and "</head>" in self.content

    def test_has_body_section(self):
        assert "<body>" in self.content and "</body>" in self.content

    def test_has_css_styles(self):
        assert "<style>" in self.content and "</style>" in self.content

    def test_has_multiple_pages(self):
        page_count = self.content.count('class="page')
        assert page_count >= 7, f"Expected at least 7 page divs, found {page_count}"


class TestGuideContentSections:
    """Test that all required content sections are present."""

    @pytest.fixture(autouse=True)
    def setup(self, guide_html_content):
        self.content = guide_html_content

    def test_has_why_section(self):
        assert "WHY THIS GUIDE" in self.content or "WHY" in self.content, "Must have 'Why' section"

    def test_has_project_ideas_section(self):
        assert "PROJECT IDEAS" in self.content or "HACKATHON IDEAS" in self.content, "Must have ideas section"

    def test_has_data_sources_section(self):
        assert "DATA SOURCES" in self.content, "Must have data sources section"

    def test_has_getting_started_section(self):
        assert "GETTING STARTED" in self.content, "Must have getting started section"

    def test_has_workflow_section(self):
        assert "WORKFLOW" in self.content, "Must have workflow section"

    def test_has_pro_tips_section(self):
        assert "PRO TIPS" in self.content or "WINNING" in self.content, "Must have pro tips section"

    def test_has_resources_section(self):
        assert "RESOURCES" in self.content or "QUICK REFERENCE" in self.content, "Must have resources section"


class TestGuideIdeaCards:
    """Test that all 10 idea cards are present."""

    @pytest.fixture(autouse=True)
    def setup(self, guide_html_content):
        self.content = guide_html_content

    def test_has_10_ideas(self):
        idea_count = 0
        for i in range(1, 11):
            if f"IDEA {i:02d}" in self.content:
                idea_count += 1
        assert idea_count >= 10, f"Expected 10 ideas, found {idea_count}"

    def test_idea_1_trend_to_app(self):
        assert "Trend-to-App" in self.content, "Must have Idea 1: Trend-to-App Builder"

    def test_idea_2_competitor_dashboard(self):
        assert "Competitor Intelligence" in self.content, "Must have Idea 2: Competitor Intelligence Dashboard"

    def test_idea_3_dev_pulse(self):
        assert "Developer Pulse" in self.content, "Must have Idea 3: Developer Pulse Newsletter"

    def test_idea_4_niche_discovery(self):
        assert "Niche Discovery" in self.content, "Must have Idea 4: Niche Discovery Bot"

    def test_idea_5_micro_saas(self):
        assert "Micro-SaaS" in self.content, "Must have Idea 5: Micro-SaaS Launch Pad"

    def test_idea_6_signal_validator(self):
        assert "Signal Validator" in self.content, "Must have Idea 6: Social Signal Validator"

    def test_idea_7_pivot_predictor(self):
        assert "Pivot Predictor" in self.content, "Must have Idea 7: Pivot Predictor"

    def test_idea_8_provider_marketplace(self):
        assert "Provider Marketplace" in self.content, "Must have Idea 8: Provider Marketplace Finder"

    def test_idea_9_research_agent(self):
        assert "Research Agent" in self.content, "Must have Idea 9: AI Research Agent"

    def test_idea_10_revenue_calculator(self):
        assert "Revenue Calculator" in self.content, "Must have Idea 10: Vibe Coder Revenue Calculator"


class TestGuideSkillCommands:
    """Test that skill command examples are present."""

    @pytest.fixture(autouse=True)
    def setup(self, guide_html_content):
        self.content = guide_html_content

    def test_has_last30days_command(self):
        assert "/last30days" in self.content or "last30days" in self.content, "Must reference the skill command"

    def test_has_competitors_flag(self):
        assert "--competitors" in self.content, "Must show --competitors flag"

    def test_has_emit_flag(self):
        assert "--emit" in self.content, "Must show --emit flag"

    def test_has_install_command(self):
        assert "npx skills add" in self.content, "Must show install command"

    def test_has_comparison_syntax(self):
        assert "vs" in self.content, "Must show comparison syntax"


class TestGuideDataSources:
    """Test that data source information is present."""

    @pytest.fixture(autouse=True)
    def setup(self, guide_html_content):
        self.content = guide_html_content

    def test_mentions_reddit(self):
        assert "Reddit" in self.content, "Must mention Reddit as a source"

    def test_mentions_twitter(self):
        assert "Twitter" in self.content or "X" in self.content, "Must mention X/Twitter"

    def test_mentions_youtube(self):
        assert "YouTube" in self.content, "Must mention YouTube"

    def test_mentions_hacker_news(self):
        assert "Hacker News" in self.content, "Must mention Hacker News"

    def test_mentions_github(self):
        assert "GitHub" in self.content, "Must mention GitHub"

    def test_mentions_polymarket(self):
        assert "Polymarket" in self.content, "Must mention Polymarket"

    def test_mentions_tiktok(self):
        assert "TikTok" in self.content, "Must mention TikTok"
