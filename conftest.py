
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session", autouse=True)
# Fixture initialize browser
def browser():
    with sync_playwright() as p:  # Khởi tạo Playwright
        browser = p.chromium.launch(headless=False)  # p.firefox.launch(headless=False)
        yield browser  # return
        browser.close()  # close browser after used


# Fixture initialize page
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1520, "height": 945})
    page = context.new_page()  # open new page
    yield page  # Return a page object for test usage.
    page.close()  # close browser after test completed
