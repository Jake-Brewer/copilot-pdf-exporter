# 🚀 Copilot PDF Exporter

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://github.com/Jake-Brewer/copilot-pdf-exporter/actions/workflows/python-app.yml/badge.svg)](https://github.com/Jake-Brewer/copilot-pdf-exporter/actions)

> Effortlessly export all your Microsoft Copilot conversations to PDF using Playwright automation.

---

## ✨ Features

- 📄 Export all conversations from Copilot web UI to PDF
- 💾 Configurable save directory
- 🔄 Robust UI interaction with retry prompts
- 🖥️ Simple CLI interface
- 🧪 Test scaffold included

---

## 📦 Requirements

- Python 3.8+
- [Playwright](https://playwright.dev/python/)

---

## ⚡ Installation

```sh
# Clone the repository
$ git clone https://github.com/Jake-Brewer/copilot-pdf-exporter.git
$ cd copilot-pdf-exporter

# Install dependencies
$ pip install -r requirements.txt

# Install Playwright browsers
$ playwright install
```

---

## 🚀 Usage

```sh
python export_copilot_pdfs.py --save-dir "C:/path/to/save"
```

### Example

```sh
python export_copilot_pdfs.py --save-dir "C:/Users/YourName/Documents/CopilotPDFs"
```

---

## 📝 Notes

- The script will prompt you to log in and interact with the Copilot UI as needed.
- Ensure you have Chromium installed via Playwright.
- All PDFs are saved in the directory you specify with `--save-dir`.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Jake-Brewer/copilot-pdf-exporter/issues) or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌐 Links

- [Playwright Python Docs](https://playwright.dev/python/)
- [GitHub Repo](https://github.com/Jake-Brewer/copilot-pdf-exporter)
