"""
Tests for Z.ai + rommark.dev branding consistency across all project files.
Ensures dual branding, discount code, and design standards are maintained.
"""
import pytest
from pathlib import Path
from conftest import (
    PROJECT_ROOT,
    GUIDE_HTML,
    COVER_HTML,
    README_MD,
    FEATURES_MD,
    ZAI_BRAND,
    ROMMARK_BRAND,
    DISCOUNT_CODE,
    DISCOUNT_URL,
)


class TestZaiBranding:
    """Test Z.ai branding presence and consistency."""

    def test_zai_in_readme(self, readme_content):
        assert ZAI_BRAND in readme_content, f"README must contain {ZAI_BRAND}"

    def test_zai_in_guide_html(self, guide_html_content):
        assert ZAI_BRAND in guide_html_content, f"guide.html must contain {ZAI_BRAND}"

    def test_zai_in_cover_html(self, cover_html_content):
        assert ZAI_BRAND in cover_html_content, f"cover.html must contain {ZAI_BRAND}"

    def test_zai_in_features(self, features_content):
        assert ZAI_BRAND in features_content or "z.ai" in features_content.lower(), \
            f"FEATURES.md must reference {ZAI_BRAND}"

    def test_zai_purple_gradient_in_html(self, guide_html_content):
        assert "6C5CE7" in guide_html_content, "Must use Z.ai primary purple (#6C5CE7)"

    def test_zai_teal_accent_in_html(self, guide_html_content):
        assert "00CEC9" in guide_html_content, "Must use Z.ai teal accent (#00CEC9)"


class TestRommarkBranding:
    """Test rommark.dev branding presence and consistency."""

    def test_rommark_in_readme(self, readme_content):
        assert ROMMARK_BRAND in readme_content, f"README must contain {ROMMARK_BRAND}"

    def test_rommark_in_guide_html(self, guide_html_content):
        assert ROMMARK_BRAND in guide_html_content, f"guide.html must contain {ROMMARK_BRAND}"

    def test_rommark_in_cover_html(self, cover_html_content):
        assert ROMMARK_BRAND in cover_html_content, f"cover.html must contain {ROMMARK_BRAND}"

    def test_rommark_orange_gradient_in_html(self, guide_html_content):
        assert "FF6B35" in guide_html_content, "Must use rommark.dev primary orange (#FF6B35)"

    def test_rommark_gold_accent_in_html(self, guide_html_content):
        assert "FFB347" in guide_html_content, "Must use rommark.dev gold accent (#FFB347)"


class TestDualBranding:
    """Test that both brands appear together in key locations."""

    def test_both_brands_in_readme_title(self, readme_content):
        assert ZAI_BRAND in readme_content and ROMMARK_BRAND in readme_content, \
            "README must feature both brands"

    def test_both_brands_in_cover(self, cover_html_content):
        assert ZAI_BRAND in cover_html_content and ROMMARK_BRAND in cover_html_content, \
            "Cover must feature both brands"

    def test_both_brands_in_guide_header(self, guide_html_content):
        assert ZAI_BRAND in guide_html_content and ROMMARK_BRAND in guide_html_content, \
            "Guide must feature both brands"

    def test_brand_multiplication_symbol(self, cover_html_content):
        assert "&times;" in cover_html_content or "x" in cover_html_content, \
            "Brands must be separated with multiplication symbol"

    def test_both_brand_logos_on_cover(self, cover_html_content):
        assert "brand-logo zai" in cover_html_content, "Cover must have Z.ai logo class"
        assert "brand-logo rommark" in cover_html_content, "Cover must have rommark.dev logo class"


class TestDiscountBanner:
    """Test the 10% OFF discount banner integration."""

    def test_discount_code_in_readme(self, readme_content):
        assert DISCOUNT_CODE in readme_content, f"README must contain discount code {DISCOUNT_CODE}"

    def test_discount_url_in_readme(self, readme_content):
        assert DISCOUNT_URL in readme_content, f"README must contain discount URL {DISCOUNT_URL}"

    def test_discount_code_in_cover(self, cover_html_content):
        assert DISCOUNT_CODE in cover_html_content, f"Cover must contain discount code {DISCOUNT_CODE}"

    def test_discount_url_in_cover(self, cover_html_content):
        assert DISCOUNT_URL in cover_html_content, f"Cover must contain discount URL {DISCOUNT_URL}"

    def test_discount_code_in_guide(self, guide_html_content):
        assert DISCOUNT_CODE in guide_html_content, f"Guide must contain discount code {DISCOUNT_CODE}"

    def test_discount_url_in_guide(self, guide_html_content):
        assert DISCOUNT_URL in guide_html_content, f"Guide must contain discount URL {DISCOUNT_URL}"

    def test_10_percent_off_in_cover(self, cover_html_content):
        assert "10% OFF" in cover_html_content, "Cover must show 10% OFF text"

    def test_10_percent_off_in_guide(self, guide_html_content):
        assert "10% OFF" in guide_html_content, "Guide must show 10% OFF text"


class TestDesignConsistency:
    """Test design consistency across HTML files."""

    def test_dark_mode_in_guide(self, guide_html_content):
        dark_colors = ["0A0A1A", "060612", "12122A", "1A1A3E"]
        assert any(c in guide_html_content for c in dark_colors), "Guide must use dark mode colors"

    def test_dark_mode_in_cover(self, cover_html_content):
        dark_colors = ["0A0A1A", "060612"]
        assert any(c in cover_html_content for c in dark_colors), "Cover must use dark mode colors"

    def test_consistent_font_loading(self, guide_html_content, cover_html_content):
        assert "Inter" in guide_html_content, "Guide must use Inter font"
        assert "Inter" in cover_html_content, "Cover must use Inter font"

    def test_mono_font_for_code(self, guide_html_content):
        assert "JetBrains Mono" in guide_html_content, "Guide must use JetBrains Mono for code"

    def test_glass_morphism_style(self, guide_html_content):
        assert "Glass_Canvas" in guide_html_content or "glass" in guide_html_content.lower() or \
               "rgba" in guide_html_content, "Guide should use glass/frosted UI patterns"
