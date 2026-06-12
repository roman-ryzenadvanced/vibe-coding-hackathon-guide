"""
Tests for the cover page HTML.
Validates cover page layout, branding elements, and discount banner.
"""
import pytest
from conftest import (
    COVER_HTML,
    ZAI_BRAND,
    ROMMARK_BRAND,
    DISCOUNT_CODE,
    DISCOUNT_URL,
)


class TestCoverHtmlExists:
    """Test that the cover HTML file exists and is non-empty."""

    def test_cover_html_exists(self):
        assert COVER_HTML.exists(), "cover.html must exist"

    def test_cover_html_non_empty(self):
        content = COVER_HTML.read_text(encoding="utf-8")
        assert len(content) > 500, "cover.html must have substantial content"


class TestCoverBranding:
    """Test that Z.ai and rommark.dev branding is present on the cover."""

    @pytest.fixture(autouse=True)
    def setup(self, cover_html_content):
        self.content = cover_html_content

    def test_has_zai_brand(self):
        assert ZAI_BRAND in self.content, f"Cover must contain {ZAI_BRAND} branding"

    def test_has_rommark_brand(self):
        assert ROMMARK_BRAND in self.content, f"Cover must contain {ROMMARK_BRAND} branding"

    def test_has_dual_brand_layout(self):
        assert "brand-row" in self.content or "brand-logo" in self.content, "Must have dual brand layout"

    def test_has_zai_gradient(self):
        assert "6C5CE7" in self.content or "gradient-zai" in self.content, "Must use Z.ai purple gradient"

    def test_has_rommark_gradient(self):
        assert "FF6B35" in self.content or "gradient-rommark" in self.content, "Must use rommark.dev orange gradient"


class TestCoverTitle:
    """Test the cover page title and hierarchy."""

    @pytest.fixture(autouse=True)
    def setup(self, cover_html_content):
        self.content = cover_html_content

    def test_has_hackathon_title(self):
        assert "HACKATHON" in self.content, "Cover must show HACKATHON title"

    def test_has_vibe_coding(self):
        assert "VIBE CODING" in self.content, "Cover must show VIBE CODING"

    def test_has_kicker_text(self):
        assert "Hackathon Ideas Guide" in self.content, "Cover must have kicker text"

    def test_has_subtitle(self):
        assert "battle-tested" in self.content or "10 " in self.content, "Cover must reference 10 ideas"


class TestCoverDiscountBanner:
    """Test the 10% OFF discount banner on the cover."""

    @pytest.fixture(autouse=True)
    def setup(self, cover_html_content):
        self.content = cover_html_content

    def test_has_discount_banner(self):
        assert "badge-banner" in self.content, "Cover must have discount banner"

    def test_has_10_percent_off(self):
        assert "10% OFF" in self.content, "Banner must show 10% OFF"

    def test_has_discount_code(self):
        assert DISCOUNT_CODE in self.content, f"Banner must contain discount code {DISCOUNT_CODE}"

    def test_has_discount_url(self):
        assert DISCOUNT_URL in self.content, f"Banner must link to {DISCOUNT_URL}"

    def test_has_coding_plans_reference(self):
        assert "Coding Plans" in self.content or "coding plans" in self.content, "Must reference coding plans"


class TestCoverMetaInfo:
    """Test cover page metadata elements."""

    @pytest.fixture(autouse=True)
    def setup(self, cover_html_content):
        self.content = cover_html_content

    def test_has_10_ideas_count(self):
        assert "10 Ideas" in self.content or "10 " in self.content, "Must show 10 ideas count"

    def test_has_data_sources_count(self):
        assert "16+" in self.content, "Must show 16+ data sources"

    def test_has_30_day_reference(self):
        assert "30" in self.content, "Must reference 30-day timeline"

    def test_has_skill_reference(self):
        assert "last30days" in self.content, "Must reference last30days skill"

    def test_has_github_url(self):
        assert "github.com" in self.content, "Must link to GitHub repo"


class TestCoverLayout:
    """Test cover page CSS layout properties."""

    @pytest.fixture(autouse=True)
    def setup(self, cover_html_content):
        self.content = cover_html_content

    def test_has_poster_class(self):
        assert "poster" in self.content, "Cover must use poster layout class"

    def test_has_page_size_css(self):
        assert "210mm" in self.content, "Must have A4 page width"

    def test_has_dark_background(self):
        assert "060612" in self.content or "0A0A1A" in self.content, "Must use dark background"

    def test_has_centered_layout(self):
        assert "center" in self.content, "Must have centered content layout"

    def test_has_google_fonts(self):
        assert "fonts.googleapis.com" in self.content, "Must load Google Fonts"
