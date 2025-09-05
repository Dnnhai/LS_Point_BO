import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session", autouse=True, params=["chromium", "firefox", "webkit"])
# Fixture initialize browser
def browser(request):
    with sync_playwright() as p:  # Playwright Initialization
        if request.param == "chromium":
            browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        elif request.param == "firefox":
            browser = p.firefox.launch(headless=False)
        else:
            browser = p.webkit.launch(headless=False)
        yield browser  # return
        browser.close()  # close browser after used


# Fixture initialize page
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport={"width": 1520, "height": 945})
    page = context.new_page()  # open new page
    yield page  # Return a page object for test usage.
    page.close()  # close browser after test completed
