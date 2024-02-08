import time

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.signup_page import SignUpPage


class TopBar(BasePage):
    # Locators for elements on the page
    CLICK_LOGIN = (By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
    CART_ICON_BTN = (By.CSS_SELECTOR, ".action.showcart")
    CART_LOADING = (By.CSS_SELECTOR, "._block-content-loading")
    CART_COUNTER = (By.CSS_SELECTOR, ".counter-number")
    CART_COUNTER_EMPTY = (By.CSS_SELECTOR, ".counter.qty.empty .counter-number")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".subtitle.empty")
    SEARCH_TEXT_BOX = (By.CSS_SELECTOR, "#search")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[title='Search']")
    TOP_BAR_ITEMS = (By.CSS_SELECTOR, ".level-top.ui-corner-all")
    # MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "div[class='panel header'] li[class='greet welcome']")
    MY_ACCOUNT_LOGGED_IN = (By.CSS_SELECTOR, "div[class='panel header'] span[class='logged-in']")
    MSG_DISSAPPER = (By.CSS_SELECTOR, "div[class='panel header'] span[class='not-logged-in']")
    SWITCH_DROP_LIST_BTN = (By.CSS_SELECTOR, "div[class='panel header'] button[type='button']")
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, "div[class='panel wrapper'] li:nth-child(1) a:nth-child(1)")
    SIGN_OUT_BTN = (By.CSS_SELECTOR, "div[aria-hidden='false'] li[data-label='or'] a")
    SIGN_OUT_SUCCESS_MSG = (By.CSS_SELECTOR, ".base")
    SITE_LOGO = (By.CSS_SELECTOR,
                 "img[src='https://magento.softwaretestingboard.com/pub/static/version1695896754/frontend/Magento/luma/en_US/images/logo.svg']")

    def __init__(self, driver):
        super().__init__(driver)

    # Clicks on the login button and returns a LoginPage instance
    @allure.step("Click on the login button")
    def click_login(self):
        self.click(self.CLICK_LOGIN)
        return LoginPage(self.driver)

    # Waits for a success login message to appear and returns the text
    @allure.step("Wait for a success login message to appear")
    def get_success_login(self):
        time.sleep(5)  # This sleep may not be the best practice, consider using WebDriverWait instead
        return self.get_text(self.MY_ACCOUNT_LOGGED_IN)

    # Waits for the login message to disappear
    @allure.step("Wait for the login message to disappear")
    def wait_for_msg_dissaper(self):
        self.wait_for_element_invisibility(self.MSG_DISSAPPER)

    # Clicks on the "Create an Account" button and returns a SignUpPage instance
    @allure.step("Click on the 'Create an Account' button")
    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BTN)
        return SignUpPage(self.driver)

    # Clicks on the shopping cart icon
    @allure.step("Click on the shopping cart icon")
    def click_cart_icon(self):
        self.wait_for_element_invisibility(*self.CART_LOADING)
        self.click(self.CART_ICON_BTN)

    # Enters a search query in the search text box and clicks the search button
    @allure.step("Search for item: {search_query}")
    def search_for_item(self, search_query):
        self.fill_text(self.SEARCH_TEXT_BOX, search_query)
        self.click(self.SEARCH_BTN)

    # Clicks on the switch dropdown list button
    @allure.step("Click on the switch dropdown list button")
    def click_switch_dropdown_list_my_account(self):
        time.sleep(5)
        self.click(self.SWITCH_DROP_LIST_BTN)

    # Clicks on the "My Account" button
    @allure.step("Click on the 'My Account' button")
    def click_my_account(self):
        self.click(self.MY_ACCOUNT_BTN)

    # Clicks on the "Sign Out" button
    @allure.step("Click on the 'Sign Out' button")
    def click_sign_out(self):
        self.click(self.SIGN_OUT_BTN)

    # Enter a search query and submit the search form.
    @allure.step("Perform search for query: {query}")
    def perform_search(self, query):
        self.fill_text(self.SEARCH_TEXT_BOX, query)  # Assuming you have a fill method in BasePage

    # Click on the search button to initiate the search.
    @allure.step("Click on the search button")
    def click_search_button(self):
        self.click(self.SEARCH_TEXT_BOX)
        return SearchPage(self.driver)

    @allure.step("Get success logout message")
    def get_success_logout_msg(self):
        return self.get_text(self.SIGN_OUT_SUCCESS_MSG)

    @allure.step("Check if the site logo is visible")
    def is_logo_visible(self):
        return self.is_elements_exist(self.SITE_LOGO)

    @allure.step("Check if the top bar with product types is visible")
    def is_top_bar_visible(self):
        return self.is_elements_exist(self.TOP_BAR_ITEMS)

    @allure.step("Navigate to the home page")
    def go_to_home_page(self):
        self.driver.get("https://magento.softwaretestingboard.com/")

    @allure.step("Check if the search bar is visible")
    def is_search_bar_visible(self):
        return self.is_elements_exist(self.SEARCH_TEXT_BOX)

    def get_cart_empty_msg(self):
        return self.get_text(self.EMPTY_CART_MSG)

    def get_cart_icon_qty(self):
        self.wait_for_element_invisibility(*self.CART_LOADING)
        return self.get_text(self.CART_COUNTER)

