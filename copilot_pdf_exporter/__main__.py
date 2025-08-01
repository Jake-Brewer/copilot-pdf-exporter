"""
copilot_pdf_exporter/__main__.py

Export all Microsoft Copilot conversations to PDF using Playwright automation.

Features:
- Exports all conversations from Copilot web UI to PDF
- Configurable save directory
- Robust UI interaction with retry prompts

Usage:
    python -m copilot_pdf_exporter --save-dir "C:/path/to/save"
"""

import argparse
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright, Page

# 1. Configuration
# save_dir = Path("C:/Users/Jake/Documents/CopilotPDFs")
# save_dir.mkdir(parents=True, exist_ok=True)

SELECTORS = {
    "history_toggle": "button[data-test-history-toggle]",
    "convo_item": "button[data-test-convo-item]",
    "chat_container": "div[data-test-chat-container]",
    "convo_title": "h2[data-test-convo-title]",
}


def wait_for_or_prompt_docstring() -> None:
    """Helper to wait for a selector or prompt user to retry if not found."""


def export_all_docstring() -> None:
    """Core export routine to save all Copilot conversations as PDFs."""


def main_docstring() -> None:
    """CLI entry point for the Copilot PDF exporter script."""


# 2. Helper to wait for a selector or prompt retry
async def wait_for_or_prompt(
    page: Page, selector: str, description: str, timeout: int = 5000
) -> None:
    """
    Wait for a selector to appear on the page, or prompt the user to fix the UI and retry.

    Args:
        page (Page): Playwright page object.
        selector (str): CSS selector to wait for.
        description (str): Human-readable description of the element.
        timeout (int): Timeout in milliseconds.
    """
    while True:
        try:
            await page.wait_for_selector(selector, timeout=timeout)
            return
        except Exception as e:
            print(
                f"Could not find {description} (selector: {selector}). Exception: {e}"
            )
            input(
                "Please fix the UI (open panels, scroll history, etc.) then press ENTER to retry..."
            )


# 3. Core export routine
async def export_all(save_dir: Path) -> None:
    """
    Export all Copilot conversations to PDF files in the specified directory.

    Args:
        save_dir (Path): Directory to save PDFs.
    """
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://copilot.microsoft.com")

        print("🔑 Log in to Copilot in the browser window. Then press ENTER here.")
        input()

        # open history
        await wait_for_or_prompt(
            page, SELECTORS["history_toggle"], "history toggle button"
        )
        await page.click(SELECTORS["history_toggle"])

        # load items
        await wait_for_or_prompt(page, SELECTORS["convo_item"], "conversation items")

        # count how many chats
        items = await page.query_selector_all(SELECTORS["convo_item"])
        total = len(items)
        print(f"Found {total} conversations.")

        for idx in range(total):
            # ensure we can see the item
            while True:
                items = await page.query_selector_all(SELECTORS["convo_item"])
                if idx < len(items):
                    break
                print(
                    f"Only {len(items)} items loaded (need {idx+1}). Scroll history and press ENTER."
                )
                input()

            btn = items[idx]
            await btn.click()
            await wait_for_or_prompt(
                page, SELECTORS["chat_container"], "chat container"
            )

            # derive filename
            try:
                raw = await page.locator(SELECTORS["convo_title"]).inner_text()
            except Exception as e:
                print(
                    f"Could not get conversation title for chat {idx+1}. Exception: {e}"
                )
                raw = f"chat_{idx+1}"
            safe = "".join(c for c in raw if c.isalnum() or c in " _-").strip()[:40]
            name = f"{idx+1:03d}_{safe}.pdf"
            dest = save_dir / name

            # print to PDF
            await page.pdf(
                path=str(dest),
                format="A4",
                print_background=True,
                margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"},
            )
            print(f"✅ Saved {name}")
            await asyncio.sleep(0.5)

        await browser.close()
        print("🎉 Export complete!")


# 4. CLI and scheduling
def main() -> None:
    """
    Parse command-line arguments and run the export routine.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--save-dir",
        metavar="PATH",
        default="C:/Users/Jake/Documents/CopilotPDFs",
        help="Directory to save exported PDFs (default: %(default)s)",
    )
    args = parser.parse_args()

    save_dir = Path(args.save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    async def export_all_with_dir() -> None:
        await export_all(save_dir)

    asyncio.run(export_all_with_dir())


if __name__ == "__main__":
    main()
