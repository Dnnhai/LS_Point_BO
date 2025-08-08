from Testdata.test_data import Data
from Pages.base_page import BasePage


class LoginPageLocators(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # self.navigate_to(Data.BASE_URL_DEV)
        # self.username = page.get_by_role("textbox", name="Enter username...")
        self.USERNAME = page.locator('//input[@name="username"]')
        self.PASSWORD = page.get_by_role("textbox", name="Enter password...")
        self.LOGIN_BUTTON = page.get_by_role("button", name="Login")
        self.AUTHEN_BOARD = page.get_by_text(
            "Two-factor AuthenticationEnter 6-digit code from your two factor authentication")
        self.BUTTON_VERIFY = page.get_by_role("button", name="Verify")
        self.OTP_INPUTS = [self.page.locator(f"input:nth-child({i})") for i in range(1, 7)]

        self.WRONG_PW_TOAST = page.locator("//div[text()='Password is incorrect']")
        self.USER_NOT_FOUND_TOAST = page.locator("//div[text()='User not found']")

'''

    @staticmethod
    def TOTP_DIGIT(index):
        return f'//input[@type="text"][{(index + 1)}]'
        # return f'input[type="text"] >> nth={index}' # another way to return dynamic xpath.
'''