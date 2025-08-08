from Testdata.test_data import Data
from Pages.base_page import BasePage


class MemberRegPageLocators(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.BUTTON_SUBMIT = page.locator("//button//span[text()='Submit']")
        self.FULL_NAME_FIELD = page.locator("//input[@id='fullname']")
        self.EMAIL_FIELD = page.locator("//input[@id='email']")
        self.PHONE_FIELD = page.locator("//input[@id='float-input']")

        self.BIRTHDAY_FIELD = page.locator("//input[@placeholder='Select a date of birth...']")
        self.DATE_PICKER_YEAR = page.locator("//div//div//div//div[1]//div//button[2]")
        self.DATE_PICKER_BUTTON_BACK = page.locator("//*[starts-with(@class, 'p-datepicker-header')]//button[starts-with(@class, 'p-ripple p-element p-datepicker-prev')]")
        self.DATE_PICKER_2010 = page.locator("//*[starts-with(@class,'p-yearpicker')]//*[@tabindex='0']")
        self.DATE_PICKER_JAN = page.locator("//*[starts-with(@class,'p-monthpicker')]//*[@tabindex='0']")
        self.DATE_PICKER_12TH = page.locator("//*[starts-with(@class,'p-ripple p-element') and text()='12']")

        self.ID_NUMBER_FILED = page.locator("//input[@id='identityId']")
        self.CITY_FILED = page.locator("//div[@class='p-dropdown p-component p-dropdown-clearable']//span[text()='Select a city...']")
        self.CITY_THE_FIRST = page.locator("//div[text()=' Thành phố Hà Nội ']")
        self.DISTRICT_FILED = page.locator( "//div[@class='p-dropdown p-component p-dropdown-clearable']//span[text()='Select a district...']")
        self.DISTRICT_THE_FIRST = page.locator("//div[text()=' Quận Ba Đình ']")
        self.WARD_FILED = page.locator("//div[@class='p-dropdown p-component p-dropdown-clearable']//span[text()='Select a ward...']")
        self.WARD_THE_FIRST = page.locator("//div[text()=' Phường Cống Vị ']")

        self.CHOOSE_CARD_AUTO = page.locator("//label[text()='Auto issue card']")
        self.REGISTER_STORE = page.locator("//div[@class='p-dropdown p-component p-dropdown-clearable']//span[text()='Select a store...']")
        self.REGISTER_STORE_THE_WL_HN = page.locator("//li[@aria-label='LOTTE MALL WEST LAKE HN']")
        self.REGISTER_STORE_THE_LDS_HN = page.locator("//li[@aria-label='Lotte DS - Lotte Center Hanoi']")
        # self.REGISTER_STORE_THE_LDS_HN = page.locator("//li[@aria-label='LOTTE DS HN']")

        self.SELECT_CARD_TYPE = page.locator("//div[@class='p-dropdown p-component p-dropdown-clearable']//span[text()='Select a card type...']")
        self.SELECT_CARD_TYPE_WL_STANDARD = page.locator('//li[@aria-label="Standard (LM01004)"]')

        self.SELECT_CARD_TYPE_LDS_STANDARD = page.locator('//li[contains(@aria-label,"STANDARD ONLINE")]')
        # self.SELECT_CARD_TYPE_LDS_STANDARD = page.locator('//li[@aria-label="STANDARD ONLINE (LV05002)"]')

        self.MEM_REG_RESULT_POP_UP = page.get_by_text("Member Register Result")
        self.LOGIN_ID = page.locator("//div[text()='Login ID *']/following-sibling::input[@id='float-input']")
