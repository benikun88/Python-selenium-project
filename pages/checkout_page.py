from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_PAGE_LOAD_TITLE = (By.CSS_SELECTOR, ".base")
    ORDER_TOTAL = (By.CSS_SELECTOR, "span[data-th='Cart Subtotal']")
    DISCOUNT_PRICE = (By.CSS_SELECTOR, "tr[class='totals discount'] td[class='amount']")
    SHIPPING_ADDRESS_SECTION_BTN = (By.CSS_SELECTOR, ".shipping-address-item.selected-item")
    NEW_ADDRESS_BTN = (By.CSS_SELECTOR, ".action.action-show-popup")
    # Shipping Address
    FIRST_NAME_TEXT_BOX = (By.NAME, "firstname")
    LAST_NAME_TEXT_BOX = (By.NAME, "lastname")
    STREET_ADDRESS_TEXT_BOX = (By.NAME, "street[0]")
    CITY_TEXT_BOX = (By.NAME, "city")
    COUNTRY_DROP_LIST = (By.NAME, "region_id")
    PHONE_NUMBER_TEXT_BOX = (By.NAME, "telephone")
    SHIP_HERE_BTN = (By.CSS_SELECTOR, "button[class='action primary action-save-address'] span")
    NEXT_BTN = (By.CSS_SELECTOR, ".button.action.continue.primary")
    PLACE_ORDER_BTN = (By.CSS_SELECTOR, "button[title='Place Order']")
    REVEL_DISCOUNT_CODE_BTN = (By.CSS_SELECTOR, "#block-discount-heading")
    DISCOUNT_CODE_TEXT_BOX = (By.CSS_SELECTOR, "#discount-code")
    APPLY_DISCOUNT_BTN = (By.CSS_SELECTOR, "button[value='Apply Discount'] span")
    CANCEL_DISCOUNT_COUPON_BTN = (By.CSS_SELECTOR, "button[value='Cancel'] span span")
    DISCOUNT_COUPON_SUCCSES_MSG = (
        By.CSS_SELECTOR, "div[data-ui-id='checkout-cart-validationmessages-message-success']")
    DISCOUNT_COUPON_ERROR_MSG = (By.CSS_SELECTOR, "div[data-ui-id='checkout-cart-validationmessages-message-error']")
    CHECKOUT_PAGE_LOADER = (By.CSS_SELECTOR, "img[alt='Loading...']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Check if the shipping address section exists")
    def is_shipping_address_section_exist(self):
        return self.is_elements_exist(self.SHIPPING_ADDRESS_SECTION_BTN)

    @allure.step("Click on the 'New Address' button")
    def click_new_address_button(self):
        self.click(self.NEW_ADDRESS_BTN)

    @allure.step("Fill shipping address information")
    def fill_shipping_address(self, first_name, last_name, street_address, city, country, phone_number):
        self.fill_text(self.FIRST_NAME_TEXT_BOX, first_name)
        self.fill_text(self.LAST_NAME_TEXT_BOX, last_name)
        self.fill_text(self.STREET_ADDRESS_TEXT_BOX, street_address)
        self.fill_text(self.CITY_TEXT_BOX, city)
        self.select_by_value(self.COUNTRY_DROP_LIST, country)
        self.fill_text(self.PHONE_NUMBER_TEXT_BOX, phone_number)

    @allure.step("Click on the 'Ship Here' button")
    def click_ship_here_button(self):
        self.click(self.SHIP_HERE_BTN)

    @allure.step("Click on the 'Next' button")
    def click_next_button(self):
        self.wait_for_element_invisibility(*self.CHECKOUT_PAGE_LOADER)
        self.click(self.NEXT_BTN)

    @allure.step("Place the order")
    def place_order(self):
        self.click(self.PLACE_ORDER_BTN)

    @allure.step("Check if the page is loaded")
    def is_page_loaded(self):
        return self.is_elements_exist(self.CHECKOUT_PAGE_LOAD_TITLE)

    @allure.step("Reveal the discount code section")
    def reveal_discount_code_section(self):
        self.wait_for_element_invisibility(*self.CHECKOUT_PAGE_LOADER)
        self.click(self.REVEL_DISCOUNT_CODE_BTN)

    @allure.step("Apply a discount code: {discount_code}")
    def apply_discount_code(self, discount_code):
        self.fill_text(self.DISCOUNT_CODE_TEXT_BOX, discount_code)
        self.click(self.APPLY_DISCOUNT_BTN)

    @allure.step("Cancel the applied discount code")
    def cancel_discount_code(self):
        self.click(self.CANCEL_DISCOUNT_COUPON_BTN)

    @allure.step("Check if the discount code is applied successfully")
    def is_discount_code_applied_successfully(self):
        return self.is_elements_exist(self.DISCOUNT_COUPON_SUCCSES_MSG)

    @allure.step("Convert price string to float: {price_str}")
    def convert_price_to_float(self, price_str):
        """
        Convert a price string to a floating-point number with only two digits after the decimal point.
        Assumes the price string is formatted as '$xxx.xx'.
        """
        price_str = price_str.replace('$', '')
        # If there are more than 2 digits after the decimal point, round to 2 decimal places
        if '.' in price_str:
            integer_part, decimal_part = price_str.split('.')
            decimal_part = decimal_part[:2]  # Take only the first two digits after the decimal point
            price_str = f"{integer_part}.{decimal_part}"
        return float(price_str)

    @allure.step("Get the total price")
    def get_total_price(self):
        self.wait_for_element_invisibility(*self.CHECKOUT_PAGE_LOADER)
        return self.get_text(self.ORDER_TOTAL)

    @allure.step("Get the total price")
    def get_discount_amount(self):
        self.wait_for_element_invisibility(*self.CHECKOUT_PAGE_LOADER)
        return self.get_text(self.DISCOUNT_PRICE)
