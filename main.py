#!/usr/bin/python3
from playwright.sync_api import sync_playwright, Playwright

# Replace this with the actual path to your Vivaldi profile
USER_DATA_DIR = "/home/slh/.config/vivaldi/Default"

VIVALDI_EXECUTABLE = "/opt/vivaldi/vivaldi"


def run(playwright: Playwright):
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir=USER_DATA_DIR,
        executable_path=VIVALDI_EXECUTABLE,  # Use Vivaldi instead of Chromium
        headless=False,
    )

    page = browser.new_page()
    page.goto("https://www.google.com")
    page.screenshot(path="screenshot.png")

    # Keeps the browser open for debugging
    input("Press Enter to close...")

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
