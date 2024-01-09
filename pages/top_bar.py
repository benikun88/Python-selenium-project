from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage


class TopBar(BasePage):
    CLICK_LOGIN = (By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, "header[class='page-header'] li:nth-child(3) a:nth-child(1)")
    CART_ICON_BTN = (By.CSS_SELECTOR, ".action.showcart")
    SEARCH_TEXT_BOX = (By.CSS_SELECTOR, "#search")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[title='Search']")
    TOP_BAR_ITEMS = (By.CSS_SELECTOR, ".level-top.ui-corner-all")
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "div[class='panel header'] li[class='greet welcome']")
    MSG_DISSAPPER = (By.CSS_SELECTOR, "div[class='panel header'] span[class='not-logged-in']")

    def __init__(self, driver):
        super().__init__(driver)

    # click on the login button
    def click_login(self):
        self.click(self.CLICK_LOGIN)
        return LoginPage(self.driver)

    def get_success_login(self):
        return self.get_text(self.MY_ACCOUNT_BTN)
    def wait_for_msg_dissaper(self):
        self.wait_for_element_invisibility(self.MSG_DISSAPPER)