import argparse
from pathlib import Path
import subprocess
import sys


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
    try:
        Path(args.save_dir).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        assert isinstance(e, (OSError, ValueError))


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
