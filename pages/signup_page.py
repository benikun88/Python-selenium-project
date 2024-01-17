from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.base_page import BasePage


class SignUpPage(BasePage):
    # Page Load Title
    SING_UP_PAGE_LOAD_TITLE = (By.CSS_SELECTOR, ".base")

    # Form field locators
    FIRST_NAME_TEXT_BOX = (By.CSS_SELECTOR, "#firstname")
    LAST_NAME_TEXT_BOX = (By.CSS_SELECTOR, "#lastname")
    EMAIL_TEXT_BOX = (By.CSS_SELECTOR, "#email_address")
    PASSWORD_TEXT_BOX = (By.CSS_SELECTOR, "#password")
    PASSWORD_CONFIRMATION_TEXT_BOX = (By.CSS_SELECTOR, "#password-confirmation")
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button[title='Create an Account'] span")

    # Error message locators
    FIRST_NAME_TEXT_BOX_ERROR = (By.CSS_SELECTOR, "#firstname-error")
    LAST_NAME_TEXT_BOX_ERROR = (By.CSS_SELECTOR, "#lastname-error")
    EMAIL_TEXT_BOX_ERROR = (By.CSS_SELECTOR, "#email_address-error")
    PASSWORD_TEXT_BOX_ERROR = (By.CSS_SELECTOR, "#password-error")
    PASSWORD_CONFIRMATION_TEXT_BOX_ERROR = (By.CSS_SELECTOR, "#password-confirmation-error")
    EXITING_USER_OR_EMAIL_RECOVER_ERROR_MSG = (By.CSS_SELECTOR, "div[data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    # Minimum length of this field must be equal or greater than 8 symbols.
    # Leading and trailing spaces will be ignored.
    # Please enter a valid email address (Ex: johndoe@domain.com).

    def __init__(self, driver):
        super().__init__(driver)

    # Method to fill a text box with the specified text
    def fill_text(self, locator, txt: str) -> None:
        super().fill_text(locator, txt)

    # Method to sign up with the provided user details
    def sign_up(self, first_name, last_name, email, password, repeat_password):
        self.fill_text(self.FIRST_NAME_TEXT_BOX, first_name)
        self.fill_text(self.LAST_NAME_TEXT_BOX, last_name)
        self.fill_text(self.EMAIL_TEXT_BOX, email)
        self.fill_text(self.PASSWORD_TEXT_BOX, password)
        self.fill_text(self.PASSWORD_CONFIRMATION_TEXT_BOX, repeat_password)
        self.click(self.CREATE_ACCOUNT_BTN)
        return AccountPage(self.driver)

    # Method to get the error message for an existing user or during email recovery
    def get_existing_user_error(self):
        return self.get_text(self.EXITING_USER_OR_EMAIL_RECOVER_ERROR_MSG)

    # Additional method to check if the SignUpPage is loaded
    def is_page_loaded(self):
        # Checking if the page load title element is present on the page
        return self.is_elements_exist(self.SING_UP_PAGE_LOAD_TITLE)

    # Additional method to get the error messages for each field (if any)
    def get_field_errors(self):
        errors = {}
        fields = {
            "first_name": self.FIRST_NAME_TEXT_BOX_ERROR,
            "last_name": self.LAST_NAME_TEXT_BOX_ERROR,
            "email": self.EMAIL_TEXT_BOX_ERROR,
            "password": self.PASSWORD_TEXT_BOX_ERROR,
            "password_confirmation": self.PASSWORD_CONFIRMATION_TEXT_BOX_ERROR,
        }

        for field, locator in fields.items():
            try:
                errors[field] = self.get_text(locator)
            except NoSuchElementException:
                # Handle the case when the element is not present
                errors[field] = f"{field.capitalize()} element not found on the page."

        return errors
