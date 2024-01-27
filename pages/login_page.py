import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators for elements on the page
    LOGIN_PAGE_LOAD_TITLE = (By.CSS_SELECTOR, ".base")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    PASSWORD_FIELD = (By.NAME, "login[password]")
    CLICK_BTN = (By.CSS_SELECTOR, ".action.login.primary")
    CLICK_LOGIN = (By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
    EMAIL_FIELD_ERROR = (By.CSS_SELECTOR, "#email-error")
    PASSWORD_FIELD_ERROR = (By.CSS_SELECTOR, "#pass-error")
    WRONG_SIGNIN_ERROR = (By.CSS_SELECTOR, ".message-error.error.message")
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "div[class='panel header'] li[class='greet welcome']")
    FORGOT_PASSWORD_BTN = (By.CSS_SELECTOR, "a[class='action remind'] span")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Fill login information - Email: {email}, Password: {password}")
    def fill_info(self, email, password):
        # Fill email field
        self.fill_text(self.EMAIL_FIELD, email)
        # Fill password field
        self.fill_text(self.PASSWORD_FIELD, password)
        # Click the login button
        self.click(self.CLICK_BTN)

    @allure.step("Retrieve email error message")
    def get_email_error(self):
        # Return the text of the email error element
        return self.get_text(self.EMAIL_FIELD_ERROR)

    @allure.step("Retrieve password error message")
    def get_password_error(self):
        # Return the text of the password error element
        return self.get_text(self.PASSWORD_FIELD_ERROR)

    @allure.step("Retrieve success login message")
    def get_success_login(self):
        # Return the text of the my account button (indicating a successful login)
        return self.get_text(self.MY_ACCOUNT_BTN)

    @allure.step("Check if LoginPage is loaded")
    def is_page_loaded(self):
        return self.is_elements_exist(self.LOGIN_PAGE_LOAD_TITLE)
    @allure.step("enter to forgot password")
    def click_forgot_password(self):
        return self.click(self.FORGOT_PASSWORD_BTN)
