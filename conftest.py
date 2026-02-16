import pytest
import os
import allure
from utils.logger import get_logger
from playwright.sync_api import sync_playwright

logger = get_logger(__name__)

@pytest.fixture(scope="function")
def page(page, request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=true)
    context = browser.new_context()
    page = context.new_page()

    yield page

    # Only run failure logic if rep_call exists
    rep = getattr(request.node, "rep_call", None)

    # Screenshot on failure
    if rep and rep.failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        screenshot_path = f"reports/screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        logger.error(f"Test Failed. Screenshot saved at {screenshot_path}")

    context.close()
    browser.close()
    playwright.stop()

# THIS IS CRITICAL — must use hookwrapper=True
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
