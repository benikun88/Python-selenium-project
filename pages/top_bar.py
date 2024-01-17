import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage


class TopBar(BasePage):
    # Locators for elements on the page
    CLICK_LOGIN = (By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
    CART_ICON_BTN = (By.CSS_SELECTOR, ".action.showcart")
    SEARCH_TEXT_BOX = (By.CSS_SELECTOR, "#search")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[title='Search']")
    TOP_BAR_ITEMS = (By.CSS_SELECTOR, ".level-top.ui-corner-all")
    # MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "div[class='panel header'] li[class='greet welcome']")
    MY_ACCOUNT_LOGGED_IN = (By.CSS_SELECTOR, "div[class='panel header'] span[class='logged-in']")
    MSG_DISSAPPER = (By.CSS_SELECTOR, "div[class='panel header'] span[class='not-logged-in']")
    SWITCH_DROP_LIST_BTN = (By.CSS_SELECTOR, "div[class='panel header'] button[type='button']")
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "div[class='panel wrapper'] li:nth-child(1) a:nth-child(1)")
    SIGN_OUT_BTN = (By.CSS_SELECTOR, "div[class='panel wrapper'] li:nth-child(1) a:nth-child(1)")

    def __init__(self, driver):
        super().__init__(driver)

    # Clicks on the login button and returns a LoginPage instance
    def click_login(self):
        self.click(self.CLICK_LOGIN)
        return LoginPage(self.driver)

    # Waits for a success login message to appear and returns the text
    def get_success_login(self):
        time.sleep(5)  # This sleep may not be the best practice, consider using WebDriverWait instead
        return self.get_text(self.MY_ACCOUNT_LOGGED_IN)

    # Waits for the login message to disappear
    def wait_for_msg_dissaper(self):
        self.wait_for_element_invisibility(self.MSG_DISSAPPER)

    # Clicks on the "Create an Account" button and returns a SignUpPage instance
    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BTN)
        return SignUpPage(self.driver)

    # Clicks on the shopping cart icon
    def click_cart_icon(self):
        self.click(self.CART_ICON_BTN)

    # Enters a search query in the search text box and clicks the search button
    def search_for_item(self, search_query):
        self.fill_text(self.SEARCH_TEXT_BOX, search_query)
        self.click(self.SEARCH_BTN)

    # Clicks on the switch dropdown list button
    def click_switch_dropdown_list(self):
        self.click(self.SWITCH_DROP_LIST_BTN)

    # Clicks on the "My Account" button
    def click_my_account(self):
        self.click(self.MY_ACCOUNT_BTN)

    # Clicks on the "Sign Out" button
    def click_sign_out(self):
        self.click(self.SIGN_OUT_BTN)
