# Common behavior that can be re-use at all pages.
import logging


class BasePage:
    def __init__(self, page):
        self.page = page
        self.timeout = 10
        logging.basicConfig(level=logging.INFO)

    def navigate_to(self, url):
        try:
            logging.info(f"Navigate to link: {url}")
            self.page.goto(url, timeout=self.timeout * 50000)  # time is count by millisecond
        except Exception as e:
            logging.error(f"Failed to navigate to link: {url}- {e}")
            raise
        except TimeoutError as e:
            logging.error(f"Timeout while navigating to link: {url} - {e}")
            raise

    @staticmethod
    def click_on(my_locator):
        logging.info(f"click on the locator: {my_locator}")
        my_locator.wait_for(state="visible", timeout=10000)
        my_locator.click()
        # self.page.locator(my_locator).wait_for(state="visible", timeout=5000)
        # self.page.click(my_locator)

    @staticmethod
    def enter_text(my_locator, text):
        logging.info(f"enter text '{text}' at the locator: '{my_locator}'\n")
        my_locator.wait_for(state="visible", timeout=5000)
        my_locator.clear()
        my_locator.fill(text)
        # self.page.locator(locator).wait_for(state="visible", timeout=5000)
        # self.page.locator(locator).clear()
        # self.page.fill(locator, text)

    @staticmethod
    def get_text(my_locator):
        my_locator.wait_for(state="visible", timeout=5000)
        logging.info(f"get text from the locator: '{my_locator}', text is: '{my_locator.text_content()}'")
        # self.page.locator(locator).wait_for(state="visible", timeout=10000)
        return my_locator.text_content()

    @staticmethod
    def get_text_by_javascript(my_locator):
        my_locator.wait_for(state="visible", timeout=5000)
        value = my_locator.evaluate("el => el.value")
        logging.info(f"get text from the locator: '{my_locator}', text is: '{value}'")
        # self.page.locator(locator).wait_for(state="visible", timeout=10000)
        return value

    @staticmethod
    def is_element_display(my_locator):
        logging.info(f"waiting for element has locator: '{my_locator}' is appear")
        my_locator.wait_for(state="visible", timeout=50000)
        return my_locator.is_visible()
