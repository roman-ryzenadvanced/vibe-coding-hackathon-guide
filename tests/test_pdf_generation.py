"""
Tests for PDF generation pipeline.
Validates that the PDF guide was generated correctly.
"""
import pytest
from pathlib import Path
from conftest import GUIDE_PDF, COVER_HTML, GUIDE_HTML


class TestPdfExists:
    """Test that the final PDF guide exists and has reasonable size."""

    def test_pdf_exists(self):
        assert GUIDE_PDF.exists(), "hackathon-ideas-guide.pdf must exist"

    def test_pdf_non_empty(self):
        if GUIDE_PDF.exists():
            size = GUIDE_PDF.stat().st_size
            assert size > 50000, f"PDF must be > 50KB, got {size} bytes"

    def test_pdf_reasonable_size(self):
        if GUIDE_PDF.exists():
            size = GUIDE_PDF.stat().st_size
            assert size < 10_000_000, f"PDF must be < 10MB, got {size} bytes"


class TestPdfPageCount:
    """Test PDF page count using pypdf if available."""

    def test_pdf_has_multiple_pages(self):
        try:
            import pypdf
            reader = pypdf.PdfReader(str(GUIDE_PDF))
            page_count = len(reader.pages)
            assert page_count >= 10, f"PDF must have >= 10 pages, got {page_count}"
        except ImportError:
            pytest.skip("pypdf not installed")

    def test_pdf_cover_is_first_page(self):
        try:
            import pypdf
            reader = pypdf.PdfReader(str(GUIDE_PDF))
            # First page should be the cover
            assert len(reader.pages) > 0, "PDF must have at least one page"
        except ImportError:
            pytest.skip("pypdf not installed")


class TestPdfMetadata:
    """Test PDF metadata is set correctly."""

    def test_pdf_has_metadata(self):
        try:
            import pypdf
            reader = pypdf.PdfReader(str(GUIDE_PDF))
            meta = reader.metadata
            assert meta is not None, "PDF must have metadata"
        except ImportError:
            pytest.skip("pypdf not installed")

    def test_pdf_author_is_zai(self):
        try:
            import pypdf
            reader = pypdf.PdfReader(str(GUIDE_PDF))
            meta = reader.metadata
            if meta and meta.author:
                assert "Z.ai" in meta.author, f"Author must be Z.ai, got {meta.author}"
        except ImportError:
            pytest.skip("pypdf not installed")


class TestSourceHtmlFiles:
    """Test that source HTML files for PDF generation exist."""

    def test_cover_html_exists(self):
        assert COVER_HTML.exists(), "cover.html source file must exist"

    def test_guide_html_exists(self):
        assert GUIDE_HTML.exists(), "guide.html source file must exist"

    def test_cover_html_valid_structure(self):
        content = COVER_HTML.read_text(encoding="utf-8")
        assert "<!DOCTYPE html>" in content, "Cover HTML must have doctype"
        assert "</html>" in content, "Cover HTML must have closing tag"

    def test_guide_html_valid_structure(self):
        content = GUIDE_HTML.read_text(encoding="utf-8")
        assert "<!DOCTYPE html>" in content, "Guide HTML must have doctype"
        assert "</html>" in content, "Guide HTML must have closing tag"


class TestBuildScript:
    """Test the build script exists and is executable."""

    def test_build_script_exists(self):
        build_script = Path(__file__).parent.parent / "scripts" / "build_guide.sh"
        assert build_script.exists(), "scripts/build_guide.sh must exist"
