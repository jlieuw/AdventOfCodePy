"""Pytest configuration and shared fixtures"""
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest

@pytest.fixture
def read_input():
    """Helper to read puzzle inputs"""
    def _read(year: int, day: int) -> str:
        input_file = project_root / f"inputs/{year}/day{day:02d}.txt"
        return input_file.read_text().strip()
    return _read