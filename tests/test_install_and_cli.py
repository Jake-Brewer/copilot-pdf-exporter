import subprocess
import sys


def test_package_installable():
    """Test that the package can be installed and imported."""
    try:
        __import__("copilot_pdf_exporter")
    except ImportError:
        assert (
            False
        ), "copilot_pdf_exporter package could not be imported after install."


def test_cli_invocation():
    """Test that the CLI entry point runs and returns expected exit codes."""
    result = subprocess.run(
        [sys.executable, "-m", "copilot_pdf_exporter", "--save-dir", "./testpdfs"],
        capture_output=True,
        text=True,
    )
    # Accept 0 (success) or 1 (user input required)
    assert result.returncode in (0, 1)
    assert (
        "Copilot" in result.stdout or "Log in" in result.stdout or result.stderr == ""
    )
