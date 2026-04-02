import pytest
import logging
from playwright.sync_api import sync_playwright
import os

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Config
BASE_URL = os.getenv("BASE_URL", "https://test.mstart.co.in")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO
    )
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context, base_url):
    page = context.new_page()
    page.goto(base_url)
    yield page
    page.close()


@pytest.fixture
def base_url():
    return BASE_URL


# Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=screenshot_path)
            logger.error(f"Screenshot saved: {screenshot_path}")


@pytest.fixture(autouse=True)
def test_logger(request):
    logger.info(f"START: {request.node.name}")
    yield
    logger.info(f"END: {request.node.name}")