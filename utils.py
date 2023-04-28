import json
from time import sleep
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_browser(headless=False, preserve_browser=False):
    browser_options = webdriver.ChromeOptions()

    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId":
        "Save as PDF",
        "version":
        2,
    }
    prefs = {
        "printing.print_preview_sticky_settings.appState":
        json.dumps(settings),
        "behavior": "allow",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        "profile.default_content_settings.popups": 0,
        "profile.default_content_setting_values.automatic_downloads": 1,
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
    }
    browser_options.add_experimental_option("prefs", prefs)
    browser_options.add_argument("--kiosk-printing")
    browser_options.add_argument("--window-size=1920,1080")
    if headless:
        browser_options.add_argument("--headless")
    browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser_options.add_experimental_option("useAutomationExtension", False)
    if preserve_browser:
        browser_options.add_experimental_option("detach", True)
    browser_options.add_argument("--enable-javascript")
    browser_options.add_argument("log-level=3")
    browser_options.add_argument("--no-sandbox")
    browser_options.add_argument("--disable-setuid-sandbox")
    browser_options.add_argument("--ignore-certificate-errors")
    browser_options.add_argument("--lang=en-US,en;q=0.9")
    browser_options.add_argument("--disable-dev-shm-usage")
    browser_options.add_argument("--disable-accelerated-2d-canvas")
    browser_options.add_argument("--disable-gpu")
    browser_options.add_argument("--allow-running-insecure-content")
    #new added
    browser_options.add_argument('--dns-prefetch-disable')
    browser_options.add_argument("--aggressive-cache-discard")
    browser_options.add_argument("--disable-cache")
    browser_options.add_argument("--disable-offline-load-stale-cache")
    browser_options.add_argument("--disk-cache-size=0")
    browser_options.add_argument("--no-proxy-server")
    browser_options.add_argument("--silent")
    browser_options.add_argument("--disable-browser-side-navigation")
    browser_options.add_argument("--disable-infobars")
    browser_options.add_argument("enable-automation")
    # browser_options.page_load_strategy = 'eager'

    # browser_options.binary_location = '/usr/bin/google-chrome-stable'

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=browser_options)

    browser.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )

    stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    return browser