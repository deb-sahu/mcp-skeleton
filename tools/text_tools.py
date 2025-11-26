"""
Text analysis tools for MCP Skeleton.

Provides text analysis capabilities including statistics and basic metrics.
"""

from typing import Dict, Any


async def text_analyzer(text: str) -> Dict[str, Any]:
    """
    Analyze text and return statistics.
    
    Note: This is a basic implementation. For production use, consider
    using NLP libraries like spaCy or NLTK for more accurate analysis.
    
    Args:
        text: The text to analyze
        
    Returns:
        Dictionary containing text statistics
    """
    words = text.split()
    characters = len(text)
    characters_no_spaces = len(text.replace(" ", ""))
    
    # Basic sentence counting - counts terminal punctuation marks
    # Note: This is simplistic and may not handle abbreviations correctly
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    # Only set to 0 if text is empty, otherwise keep the count (even if 0)
    if not text.strip():
        sentence_count = 0
    
    return {
        "text_length": characters,
        "characters_no_spaces": characters_no_spaces,
        "word_count": len(words),
        "sentence_count": sentence_count,
        "average_word_length": round(characters_no_spaces / max(len(words), 1), 2),
        "longest_word": max(words, key=len) if words else "",
        "shortest_word": min(words, key=len) if words else ""
    }
