import pytest
import os
import allure
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, page):
    yield
    rep = getattr(request.node, "rep_call", None)

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
