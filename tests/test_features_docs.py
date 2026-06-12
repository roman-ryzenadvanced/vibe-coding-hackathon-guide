"""
Tests for feature documentation files.
Validates that all 10 feature docs exist and contain required sections.
"""
import pytest
from pathlib import Path
from conftest import FEATURES_DIR, EXPECTED_FEATURES, REQUIRED_FEATURE_SECTIONS


class TestFeatureDocsExist:
    """Test that all expected feature docs exist."""

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_feature_doc_exists(self, filename):
        filepath = FEATURES_DIR / filename
        assert filepath.exists(), f"Feature doc must exist: {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_feature_doc_non_empty(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert len(content) > 200, f"Feature doc must have substantial content: {filename}"


class TestFeatureDocSections:
    """Test that each feature doc has all required sections."""

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_quick_stats(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Quick Stats" in content, f"Missing 'Quick Stats' section in {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_problem_section(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Problem" in content, f"Missing 'Problem' section in {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_solution_section(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Solution" in content, f"Missing 'Solution' section in {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_architecture(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Architecture" in content, f"Missing 'Architecture' section in {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_data_flow(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Data Flow" in content or "data flow" in content, f"Missing 'Data Flow' in {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_skill_api_mapping(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Skill API" in content or "skill" in content.lower(), f"Missing 'Skill API Mapping' in {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_tech_stack(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Tech Stack" in content or "tech stack" in content, f"Missing 'Tech Stack' in {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_implementation_steps(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Implementation" in content, f"Missing 'Implementation Steps' in {filename}"

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_demo_script(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            assert "Demo" in content, f"Missing 'Demo Script' in {filename}"


class TestFeatureDocDifficultyRatings:
    """Test that each feature doc has a valid difficulty rating."""

    VALID_DIFFICULTIES = ["Beginner", "Intermediate", "Advanced"]

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_has_difficulty_rating(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            has_difficulty = any(d in content for d in self.VALID_DIFFICULTIES)
            assert has_difficulty, f"Must have a valid difficulty rating in {filename}"


class TestFeatureDocWordCount:
    """Test that each feature doc meets minimum word count for substantive sections."""

    @pytest.mark.parametrize("filename", EXPECTED_FEATURES)
    def test_minimum_word_count(self, filename):
        filepath = FEATURES_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            words = len(content.split())
            assert words >= 100, f"Feature doc must have >= 100 words, got {words} in {filename}"
