import logging
import pyotp
from Locators.login_page_locators import LoginPageLocators
from Pages.base_page import BasePage
from Testdata.test_data import Data


class LoginPage(LoginPageLocators):
    def __init__(self, page):
        super().__init__(page)
        self.navigate_to(Data.BASE_URL_DEV)
        # self.navigate_to(Data.BASE_URL_STG)

    # def login(self, username, password):
    # self.enter_text(LoginPageLocators.USERNAME, username)
    # self.enter_text(LoginPageLocators.PASSWORD, password)
    # self.click_on(LoginPageLocators.BUTTON_LOGIN)

    def login(self, user_name, pass_word):
        self.enter_text(self.USERNAME, user_name)
        self.enter_text(self.PASSWORD, pass_word)
        self.click_on(self.LOGIN_BUTTON)

    def enter_otp_number(self, totp_secrect):
        self.AUTHEN_BOARD.wait_for(state="visible", timeout=5000)
        otp_code = pyotp.TOTP(totp_secrect).now()
        for i, digit in enumerate(otp_code):
            self.OTP_INPUTS[i].fill(digit)

    def click_button_verify(self):
        self.BUTTON_VERIFY.click()

    def get_error_mesasage_login_wrong_pw(self):
        if self.is_element_display(self.WRONG_PW_TOAST):
            return self.WRONG_PW_TOAST.text_content()

    def get_error_user_not_found(self):
        if self.is_element_display(self.USER_NOT_FOUND_TOAST):
            return self.get_text(self.USER_NOT_FOUND_TOAST)


"""
    def get_error_mesasage_login_fail(self):
        if self.is_element_display(LoginPageLocators.WRONG_PASSWORD_TOAST):
            return self.get_text(LoginPageLocators.WRONG_PASSWORD_TOAST)

    def get_error_user_not_found(self):
        if self.is_element_display(LoginPageLocators.USER_NOT_FOUND_TOAST):
            return self.get_text(LoginPageLocators.USER_NOT_FOUND_TOAST)

    def enter_otp_number(self):
        if self.is_element_display(LoginPageLocators.AUTHEN_BOARD):
            otp_code = pyotp.TOTP(Data.TOTP_SECRET).now()
            for i, digit in enumerate(otp_code):
                self.otp_inputs[i].fill(digit)
            # for i, digit in enumerate(otp_code):
            #    self.enter_text(LoginPageLocators.TOTP_DIGIT(i), digit)

            ## for i in range(len(otp_code)):
            #    # self.enter_text(LoginPageLocators.TOTP_DIGIT(i), otp_code[i])

            # self.click_on(LoginPageLocators.BUTTON_VERIFY)
        else:
            logging.error(f"element is not displayed") """
