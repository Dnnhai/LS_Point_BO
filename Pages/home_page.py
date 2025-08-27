from Locators.home_page_locator import HomepageLocator


class HomePage(HomepageLocator):
    def __init__(self, page):
        super().__init__(page)

    def get_loggin_success_mesasage(self):
        return self.get_text(self.LOGIN_SUCCESS_MESAGE)

    def is_login_success(self):
        # user icon is displayed if login successfully
        return self.is_element_display(self.DASHBOAR_ADMIN)

    def click_button_member_management(self):
        self.click_on(self.MEMBER_MANAGEMENT_TAB)

    def click_button_member_register(self):
        self.click_on(self.MEMBER_REGISTER_TAB)
