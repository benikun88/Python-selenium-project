import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage


class TopBar(BasePage):
    CLICK_LOGIN = (By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
    CART_ICON_BTN = (By.CSS_SELECTOR, ".action.showcart")
    SEARCH_TEXT_BOX = (By.CSS_SELECTOR, "#search")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[title='Search']")
    TOP_BAR_ITEMS = (By.CSS_SELECTOR, ".level-top.ui-corner-all")
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "div[class='panel header'] li[class='greet welcome']")
    MY_ACCOUNT_LONGED_IN = (By.CSS_SELECTOR, "div[class='panel header'] span[class='logged-in']")
    MSG_DISSAPPER = (By.CSS_SELECTOR, "div[class='panel header'] span[class='not-logged-in']")

    def __init__(self, driver):
        super().__init__(driver)

    # click on the login button
    def click_login(self):
        self.click(self.CLICK_LOGIN)
        return LoginPage(self.driver)

    def get_success_login(self):
        time.sleep(5)
        return self.get_text(self.MY_ACCOUNT_LONGED_IN)

    def wait_for_msg_dissaper(self):
        self.wait_for_element_invisibility(self.MSG_DISSAPPER)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BTN)
        return SignUpPage(self.driver)
