"""
Tests for Text Tools
====================

Example test cases showing how to test text processing logic.
Replace these tests with tests for YOUR data processing.
"""

import pytest
from tools.text_tools import text_analyzer


@pytest.mark.asyncio
async def test_text_analyzer_basic():
    """Test basic text analysis."""
    text = "Hello world"
    result = await text_analyzer(text)
    
    assert result["text_length"] == 11
    assert result["word_count"] == 2
    assert result["characters_no_spaces"] == 10
    assert result["sentence_count"] == 0  # No terminal punctuation


@pytest.mark.asyncio
async def test_text_analyzer_empty_string():
    """Test analysis of empty string."""
    result = await text_analyzer("")
    
    assert result["word_count"] == 0
    assert result["text_length"] == 0
    assert result["characters_no_spaces"] == 0
    assert result["sentence_count"] == 0


@pytest.mark.asyncio
async def test_text_analyzer_multiple_sentences():
    """Test analysis of multiple sentences."""
    text = "Hello world. This is a test. Testing is important."
    result = await text_analyzer(text)
    
    assert result["sentence_count"] == 3
    assert result["word_count"] > 5


@pytest.mark.asyncio
async def test_text_analyzer_statistics():
    """Test that analysis includes all expected statistics."""
    text = "The quick brown fox jumps over the lazy dog"
    result = await text_analyzer(text)
    
    assert "word_count" in result
    assert "text_length" in result
    assert "characters_no_spaces" in result
    assert "sentence_count" in result
    assert "average_word_length" in result
    assert "longest_word" in result
    assert "shortest_word" in result
    assert result["longest_word"] == "quick"  # Longest word by length

