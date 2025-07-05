# Copilot PDF Exporter

Export all your Microsoft Copilot conversations to PDF using Playwright automation.

## Features

- Exports all conversations from Copilot web UI to PDF
- Configurable save directory
- Robust UI interaction with retry prompts

## Requirements

- Python 3.8+
- Playwright

## Installation

```sh
pip install -r requirements.txt
playwright install
```

## Usage

```sh
python export_copilot_pdfs.py --save-dir "C:/path/to/save"
```

## Example

```sh
python export_copilot_pdfs.py --save-dir "C:/Users/YourName/Documents/CopilotPDFs"
```

## Notes

- The script will prompt you to log in and interact with the Copilot UI as needed.
- Ensure you have Chromium installed via Playwright.
