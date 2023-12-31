from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class Top_Bar(BasePage):
    CLICK_LOGIN = (By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
    CREATE_ACCOUNT_BTN=(By.CSS_SELECTOR, "header[class='page-header'] li:nth-child(3) a:nth-child(1)")
    CART_ICON_BTN=(By.CSS_SELECTOR, ".action.showcart")
    SEARCH_TEXT_BOX=(By.CSS_SELECTOR, "#search")
    SEARCH_BTN=(By.CSS_SELECTOR, "button[title='Search']")
    TOP_BAR_ITEMS=(By.CSS_SELECTOR, ".level-top.ui-corner-all")

    def __init__(self, driver):
        super().__init__(driver)

    # def select_product_type(self,name):
