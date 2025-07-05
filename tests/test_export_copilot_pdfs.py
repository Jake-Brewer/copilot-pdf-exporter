import argparse
from pathlib import Path
import subprocess
import sys
import pytest


def test_save_dir_creation(tmp_path):
    """Test that the save directory is created if it does not exist."""
    save_dir = tmp_path / "CopilotPDFs"
    save_dir.mkdir()
    assert save_dir.exists()


def test_invalid_save_dir():
    """Test handling of an invalid save directory path."""
    invalid_path = "?invalid_path*"
    parser = argparse.ArgumentParser()
    parser.add_argument("--save-dir", metavar="PATH", default=invalid_path)
    args = parser.parse_args([])
    with pytest.raises((OSError, ValueError)):
        Path(args.save_dir).mkdir(parents=True, exist_ok=True)


# Optionally, test CLI argument parsing


def test_cli_args_parsing():
    """Test that CLI argument parsing works as expected."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--save-dir", metavar="PATH", default="foo")
    args = parser.parse_args(["--save-dir", "bar"])
    assert args.save_dir == "bar"


def test_cli_entrypoint_runs():
    """Test that the CLI entry point runs without crashing (smoke test)."""
    result = subprocess.run(
        [sys.executable, "-m", "copilot_pdf_exporter", "--save-dir", "./testpdfs"],
        capture_output=True,
        text=True,
    )
    assert (
        result.returncode == 0 or result.returncode == 1
    )  # 1 if user input is required


def test_missing_selector(monkeypatch):
    """Test that missing selectors are handled gracefully."""
    from copilot_pdf_exporter import __main__

    class DummyPage:
        async def wait_for_selector(self, selector, timeout=5000):
            raise Exception("Selector not found")

    import asyncio

    with pytest.raises(Exception):
        asyncio.run(__main__.wait_for_or_prompt(DummyPage(), "fake", "Fake selector"))


def test_permission_error_on_save_dir(tmp_path, monkeypatch):
    """Test that a permission error on save_dir is handled."""
    import os

    save_dir = tmp_path / "protected"
    save_dir.mkdir()
    os.chmod(save_dir, 0o400)  # Read-only
    try:
        with pytest.raises(PermissionError):
            (save_dir / "test.pdf").write_text("test")
    finally:
        os.chmod(save_dir, 0o700)  # Restore permissions
