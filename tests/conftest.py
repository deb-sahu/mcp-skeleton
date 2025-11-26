"""
Pytest Configuration
====================

Shared fixtures and configuration for all tests.
Add your custom fixtures here.
"""

import pytest


@pytest.fixture
def sample_text():
    """Fixture providing sample text for testing."""
    return "The quick brown fox jumps over the lazy dog"


@pytest.fixture
def sample_numbers():
    """Fixture providing sample numbers for testing."""
    return {"a": 10, "b": 5}


# Add more fixtures as needed for your tests
# Example:
# @pytest.fixture
# async def db_connection():
#     """Fixture providing database connection."""
#     conn = await connect_to_db()
#     yield conn
#     await conn.close()

