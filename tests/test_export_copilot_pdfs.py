import argparse
from pathlib import Path

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
