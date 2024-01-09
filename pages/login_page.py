from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    PASSWORD_FIELD = (By.NAME,"login[password]")
    CLICK_BTN = (By.CSS_SELECTOR, ".action.login.primary")
    CLICK_LOGIN = (By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
    EMAIL_FIELD_ERROR = (By.CSS_SELECTOR, "#email-error")
    PASSWORD_FIELD_ERROR = (By.CSS_SELECTOR, "#pass-error")
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "div[class='panel header'] li[class='greet welcome']")

    def __init__(self, driver):
        super().__init__(driver)

    # fill the login credentials
    def fill_info(self, email, password):
        self.fill_text(self.EMAIL_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.CLICK_BTN)


    # def click_login(self):
    #     self.click(self.CLICK_LOGIN)

    def get_email_error(self):
        return self.get_text(self.EMAIL_FIELD_ERROR)

    def get_password_error(self):
        return self.get_text(self.PASSWORD_FIELD_ERROR)

    def get_success_login(self):
        return self.get_text(self.MY_ACCOUNT_BTN)
