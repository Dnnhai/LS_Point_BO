# List of locator of Homepage that can be used for automate.
from Testdata.test_data import Data
from Pages.base_page import BasePage


class HomepageLocator(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.LOGIN_SUCCESS_MESAGE = page.locator("//div[text()='Login successfully']")
        self.USER_ICON = page.locator('//p-avatar[@icon="pi pi-user"]')

        # Member Management group
        #self.MEMBER_MANAGEMENT_TAB = page.locator("//app-menu//ul//li[3]")
        self.MEMBER_MANAGEMENT_TAB = page.locator("a").filter(has_text="Member Management")
        self.MEMBER_REGISTER_TAB = page.locator("//app-menu//ul//li[3]//ul//li[1]")
        self.MEMBER_LIST_TAB = page.locator("//app-menu//ul//li[3]//ul//li[2]")
