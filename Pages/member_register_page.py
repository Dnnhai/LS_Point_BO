import logging
from Pages.base_page import BasePage
from Utils.user_data_generator import UserDataGenerator
from Locators.member_register_page_locators import MemberRegPageLocators


class MemberRegisterPage(MemberRegPageLocators):
    def __init__(self, page):
        super().__init__(page)

    def click_submit_button(self):
        #self.BUTTON_SUBMIT.click()
        self.click_on(self.BUTTON_SUBMIT)

    def enter_fullname(self):
        #self.FULL_NAME_FIELD.fill(UserDataGenerator.generate_random_name())
        self.enter_text(self.FULL_NAME_FIELD, UserDataGenerator.generate_random_name())

    def enter_email(self):
        self.enter_text(self.EMAIL_FIELD, UserDataGenerator.generate_email())

    def enter_phone_number(self):
        self.enter_text(self.PHONE_FIELD, UserDataGenerator.generate_phone_number())

    def selelect_day_of_birth(self):
        self.click_on(self.BIRTHDAY_FIELD)
        self.click_on(self.DATE_PICKER_YEAR)
        self.click_on(self.DATE_PICKER_BUTTON_BACK)
        self.click_on(self.DATE_PICKER_2010)
        self.click_on(self.DATE_PICKER_JAN)
        self.click_on(self.DATE_PICKER_12TH)

    def enter_identity_number(self):
        self.enter_text(self.ID_NUMBER_FILED, UserDataGenerator.generate_random_ID())

    def choose_location(self):
        try:
            self.click_on(self.CITY_FILED)
            self.click_on(self.CITY_THE_FIRST)
        except:
            pass

        self.click_on(self.DISTRICT_FILED)
        self.click_on(self.DISTRICT_THE_FIRST)

        self.click_on(self.WARD_FILED)
        self.click_on(self.WARD_THE_FIRST)

    def select_add_card_method_auto(self):
        self.click_on(self.CHOOSE_CARD_AUTO)

    def choose_register_store_WL_HN(self):
        self.click_on(self.REGISTER_STORE)
        self.click_on(self.REGISTER_STORE_THE_WL_HN)

    def choose_register_store_LDS(self):
        self.click_on(self.REGISTER_STORE)
        self.click_on(self.REGISTER_STORE_THE_LDS_HN)

    def chose_card_type_WL_standard(self):
        self.click_on(self.SELECT_CARD_TYPE)
        self.click_on(self.SELECT_CARD_TYPE_WL_STANDARD)
        #self.SELECT_CARD_TYPE.click()
        #self.SELECT_CARD_TYPE_STANDARD.click()

    def chose_card_type_LDS_standard(self):
        self.click_on(self.SELECT_CARD_TYPE)
        self.click_on(self.SELECT_CARD_TYPE_LDS_STANDARD)

    def is_register_result_display(self):
        # ret self.is_element_display(MemberRegPageLocators.MEMBER_REGISTER_POPUP)
        return self.is_element_display(self.MEM_REG_RESULT_POP_UP)