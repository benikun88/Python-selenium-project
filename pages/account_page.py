from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    EDIT_BTN = (By.CSS_SELECTOR, "div[class='box box-information'] a[class='action edit']")
    CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, "#top-cart-btn-checkout")
    MANAGE_ADDRESS_BTN = (By.CSS_SELECTOR, "body > div:nth-child(5) > main:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1)")
    STATUS_COL: list = (By.CSS_SELECTOR,".col.status")
    VIEW_ORDER: list = (By.CSS_SELECTOR,".action.view")
    REORDER_ORDER: list = (By.CSS_SELECTOR,".action.order")
    FIRST_NAME_TEXT_BOX = (By.CSS_SELECTOR, "#firstname")
    LAST_NAME_TEXT_BOX = (By.CSS_SELECTOR, "#lastname")
    EMAIL_TEXT_BOX = (By.CSS_SELECTOR, "#email")
    CURRENT_PASSWORD_TEXT_BOX = (By.CSS_SELECTOR, "#current-password")
    NEW_PASSWORD_TEXT_BOX = (By.CSS_SELECTOR, "#password")
    CONFIRM_NEW_PASSWORD_TEXT_BOX = (By.CSS_SELECTOR, "#password-confirmation")
    EMAIL_CHANGE_CHECK_BOX = (By.CSS_SELECTOR,"#change-email")
    PASSWORD_CHANGE_CHECK_BOX = (By.CSS_SELECTOR,"#change-password")
    SAVE_CHNAGE_BTN = (By.CSS_SELECTOR,"button[title='Save']")
    MY_ORDERS_SECTION = (By.CSS_SELECTOR,"div[class='sidebar sidebar-main'] li:nth-child(2) a:nth-child(1)")

    def __init__(self, driver):
        super().__init__(driver)

