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
python -m copilot_pdf_exporter --save-dir "C:/path/to/save"
```

### More Usage Examples

- Save to a custom directory:

  ```sh
  python -m copilot_pdf_exporter --save-dir "D:/Backups/CopilotPDFs"
  ```

- Use the default directory:

  ```sh
  python -m copilot_pdf_exporter
  ```

---

## 📝 Notes

- The script will prompt you to log in and interact with the Copilot UI as needed.
- Ensure you have Chromium installed via Playwright.
- All PDFs are saved in the directory you specify with `--save-dir`.

---

## 🛠️ Troubleshooting

- **Playwright not installed:**
  - Run `pip install -r requirements.txt` and `playwright install`.
- **Chromium not found:**
  - Run `playwright install` to ensure all browsers are available.
- **Permission errors on save:**
  - Make sure the save directory exists and you have write permissions.
- **Selector not found errors:**
  - The Copilot UI may have changed. Open the required panels or update selectors in the script.
- **Other issues:**
  - Check the [issues page](https://github.com/Jake-Brewer/copilot-pdf-exporter/issues) or open a new issue for help.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

Please ensure your code follows the project style and passes all tests before submitting.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌐 Links

- [Playwright Python Docs](https://playwright.dev/python/)
- [GitHub Repo](https://github.com/Jake-Brewer/copilot-pdf-exporter)
