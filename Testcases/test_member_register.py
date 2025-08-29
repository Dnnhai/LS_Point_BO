import time
import logging

import pytest

from Testdata.test_data import Data
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.member_register_page import MemberRegisterPage
from Utils.utils import Utils


class TestMemberRegister:

    # @pytest.mark.skip
    def test_register_new_member_WestLake(self, page):
        login_page = LoginPage(page)
        login_page.login(Data.USERNAME_DEV_WL, Data.PASSWORD_DEV_WL)
        assert login_page.is_OTP_form_display(), "fail"

        login_page.enter_otp_number(Data.TOTP_SECRET_DEV_WL)
        login_page.click_button_verify()
        page.wait_for_load_state("networkidle")

        home_pg = HomePage(page)
        home_pg.click_button_member_management()
        home_pg.click_button_member_register()

        reg_mem_pg = MemberRegisterPage(page)
        # page.pause()
        reg_mem_pg.enter_fullname()
        reg_mem_pg.enter_email()
        reg_mem_pg.enter_phone_number()
        reg_mem_pg.selelect_day_of_birth()
        reg_mem_pg.enter_identity_number()
        reg_mem_pg.choose_location()

        reg_mem_pg.select_add_card_method_auto()
        reg_mem_pg.choose_register_store_WL_HN()
        reg_mem_pg.chose_card_type_WL_standard()

        reg_mem_pg.click_submit_button()
        page.wait_for_load_state("networkidle")
        result = reg_mem_pg.is_register_result_display()
        assert result == 1
        login_id = reg_mem_pg.get_text_by_javascript(reg_mem_pg.LOGIN_ID)
        logging.info(f"new user: {login_id}")
        Utils.save_to_file(login_id + " - WL")

    # @pytest.mark.skip
    def test_register_new_member_LDS(self, page):
        login_page = LoginPage(page)
        login_page.login(Data.USERNAME_DEV_LDS, Data.PASSWORD_DEV_LDS)
        assert login_page.is_OTP_form_display(), "fail"
        
        login_page.enter_otp_number(Data.TOTP_SECRET_DEV_LDS)
        login_page.click_button_verify()
        page.wait_for_load_state("networkidle")

        home_pg = HomePage(page)
        home_pg.click_button_member_management()
        home_pg.click_button_member_register()

        reg_mem_pg = MemberRegisterPage(page)
        reg_mem_pg.enter_fullname()
        reg_mem_pg.enter_email()
        reg_mem_pg.enter_phone_number()
        reg_mem_pg.selelect_day_of_birth()
        reg_mem_pg.enter_identity_number()
        time.sleep(1)
        reg_mem_pg.choose_location()

        reg_mem_pg.select_add_card_method_auto()
        reg_mem_pg.choose_register_store_LDS()
        reg_mem_pg.chose_card_type_LDS_standard()
        reg_mem_pg.click_submit_button()

        # Check if the result pop up is displayed
        page.wait_for_load_state("networkidle")
        assert reg_mem_pg.is_register_result_display(), "no Result"
        login_id = reg_mem_pg.get_text_by_javascript(reg_mem_pg.LOGIN_ID)
        logging.info(f"New user: {login_id}")
        Utils.save_to_file(login_id + " - LDS")
