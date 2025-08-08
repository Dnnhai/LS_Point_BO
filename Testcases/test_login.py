import time
import logging
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Testdata.test_data import Data


class TestLogin:
    def test_login_success(self, page):
        login_page = LoginPage(page)
        login_page.login(Data.USERNAME_DEV_WL, Data.PASSWORD_DEV_WL)
        login_page.enter_otp_number(Data.TOTP_SECRET_DEV_WL)
        login_page.click_button_verify()
        home_pg = HomePage(page)
        account_icon = home_pg.is_login_success()
        assert account_icon, "Loggin FAIL"
        mess = home_pg.get_loggin_success_mesasage()
        assert mess == 'Login successfully', "Loggin FAIL"

    def test_login_fail_with_wrong_password(self, page):
        login_page = LoginPage(page)
        login_page.login(Data.USERNAME_DEV_WL, "invalid-passwword")
        err_mess = login_page.get_error_mesasage_login_wrong_pw()
        assert err_mess == "Password is incorrect", "FAIL"

    def test_login_user_not_found(self, page):
        login_page = LoginPage(page)
        login_page.login("User_not_found", "invalid-passwword")
        err_mess = login_page.get_error_user_not_found()
        assert err_mess == "User not found", "FAIL"
