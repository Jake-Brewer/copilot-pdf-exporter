import pytest
from pathlib import Path


def test_save_dir_creation(tmp_path):
    # Simulate save dir creation
    save_dir = tmp_path / "CopilotPDFs"
    save_dir.mkdir()
    assert save_dir.exists()
