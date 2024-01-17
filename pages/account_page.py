from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):
    # Locators for elements on the page
    EDIT_BTN = (By.CSS_SELECTOR, "div[class='box box-information'] a[class='action edit']")
    CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, "#top-cart-btn-checkout")
    MANAGE_ADDRESS_BTN = (By.CSS_SELECTOR,
                          "body > div:nth-child(5) > main:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1)")
    ORDER_STATUS_COL: list = (By.CSS_SELECTOR, ".col.status")
    VIEW_ORDER: list = (By.CSS_SELECTOR, ".action.view")
    REORDER_ORDER: list = (By.CSS_SELECTOR, ".action.order")
    FIRST_NAME_TEXT_BOX = (By.CSS_SELECTOR, "#firstname")
    LAST_NAME_TEXT_BOX = (By.CSS_SELECTOR, "#lastname")
    EMAIL_TEXT_BOX = (By.CSS_SELECTOR, "#email")
    CURRENT_PASSWORD_TEXT_BOX = (By.CSS_SELECTOR, "#current-password")
    NEW_PASSWORD_TEXT_BOX = (By.CSS_SELECTOR, "#password")
    CONFIRM_NEW_PASSWORD_TEXT_BOX = (By.CSS_SELECTOR, "#password-confirmation")
    EMAIL_CHANGE_CHECK_BOX = (By.CSS_SELECTOR, "#change-email")
    PASSWORD_CHANGE_CHECK_BOX = (By.CSS_SELECTOR, "#change-password")
    SAVE_CHNAGE_BTN = (By.CSS_SELECTOR, "button[title='Save']")
    MY_ORDERS_SECTION = (By.CSS_SELECTOR, "div[class='sidebar sidebar-main'] li:nth-child(2) a:nth-child(1)")
    ACCOUNT_UPDATE_INFO_MSG = (By.CSS_SELECTOR, ".message-success.success.message")

    def __init__(self, driver):
        super().__init__(driver)

    # Clicks the "Edit" button
    def click_edit_btn(self):
        self.click(self.EDIT_BTN)

    # Clicks the "Change Password" button
    def click_change_password_btn(self):
        self.click(self.CHANGE_PASSWORD_BTN)

    # Clicks the "Manage Address" button
    def click_manage_address_btn(self):
        self.click(self.MANAGE_ADDRESS_BTN)

    # Fills the first name in the form
    def fill_name(self, first_name):
        self.fill_text(self.FIRST_NAME_TEXT_BOX, first_name)

    # Fills the last name in the form
    def fill_last_name(self, last_name):
        self.fill_text(self.LAST_NAME_TEXT_BOX, last_name)

    # Fills the current password in the form
    def fill_current_password(self, current_pass):
        self.fill_text(self.CURRENT_PASSWORD_TEXT_BOX, current_pass)

    # Fills the new password in the form
    def fill_new_password(self, new_pass):
        self.fill_text(self.NEW_PASSWORD_TEXT_BOX, new_pass)

    # Fills the confirmation of the new password in the form
    def fill_confirm_new_password(self, confirm_pass):
        self.fill_text(self.CONFIRM_NEW_PASSWORD_TEXT_BOX, confirm_pass)

    # Checks the "Change Email" checkbox
    def check_email_change_checkbox(self):
        self.click(self.EMAIL_CHANGE_CHECK_BOX)

    # Fills the email in the form
    def fill_email(self, email):
        self.fill_text(self.EMAIL_TEXT_BOX, email)

    # Checks the "Change Password" checkbox
    def check_password_change_checkbox(self):
        self.click(self.PASSWORD_CHANGE_CHECK_BOX)

    # Clicks the "Save Changes" button
    def click_save_change(self):
        self.click(self.SAVE_CHNAGE_BTN)

    # Retrieves the success change message
    def get_success_change_msg(self):
        return self.get_text(self.ACCOUNT_UPDATE_INFO_MSG)
