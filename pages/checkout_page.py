from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_PAGE_LOAD_TITLE = (By.CSS_SELECTOR, ".base")
    SHIPPING_ADDRESS_SECTION_BTN = (By.CSS_SELECTOR, ".shipping-address-item.selected-item")
    NEW_ADDRESS_BTN = (By.CSS_SELECTOR,".action.action-show-popup")
    # Shipping Address
    FIRST_NAME_TEXT_BOX=(By.CSS_SELECTOR,"#NEYKSU8")
    LAST_NAME_TEXT_BOX = (By.CSS_SELECTOR, "#CEQDYY0")
    STREET_ADDRESS_TEXT_BOX = (By.CSS_SELECTOR, "#QQBO9IB")
    CITY_TEXT_BOX = (By.CSS_SELECTOR, "#N6MGM0Y")
    COUNTRY_DROP_LIST = (By.CSS_SELECTOR, "#DVWFUC5")
    PHONE_NUMBER_TEXT_BOX = (By.CSS_SELECTOR, "#UI1F719")
    SHIP_HERE_BTN = (By.CSS_SELECTOR, "button[class='action primary action-save-address'] span")
    NEXT_BTN = (By.CSS_SELECTOR, ".button.action.continue.primary")
    PLACE_ORDER_BTN = (By.CSS_SELECTOR, "button[title='Place Order']")
    REVEL_DISCOUNT_CODE_BTN = (By.CSS_SELECTOR, "#block-discount-heading")
    DISCOUNT_CODE_TEXT_BOX = (By.CSS_SELECTOR, "#coupon_code")
    APPLY_DISCOUNT_BTN = (By.CSS_SELECTOR, "button[value='Apply Discount'] span")
    CANCEL_DISCOUNT_COUPON_BTN = (By.CSS_SELECTOR, "button[value='Cancel'] span span")
    DISCOUNT_COUPON_SUCCSES_MSG = (By.CSS_SELECTOR, "div[data-ui-id='checkout-cart-validationmessages-message-success']")
    DISCOUNT_COUPON_ERROR_MSG = (By.CSS_SELECTOR, "div[data-ui-id='checkout-cart-validationmessages-message-error']")

    def __init__(self, driver):
        super().__init__(driver)

    def select_shipping_address_section(self):
        self.click(self.SHIPPING_ADDRESS_SECTION_BTN)

    # Method to click on the "New Address" button
    def click_new_address_button(self):
        self.click(self.NEW_ADDRESS_BTN)

    # Method to fill shipping address information
    def fill_shipping_address(self, first_name, last_name, street_address, city, country, phone_number):
        self.fill_text(self.FIRST_NAME_TEXT_BOX, first_name)
        self.fill_text(self.LAST_NAME_TEXT_BOX, last_name)
        self.fill_text(self.STREET_ADDRESS_TEXT_BOX, street_address)
        self.fill_text(self.CITY_TEXT_BOX, city)
        self.select_by_value(self.COUNTRY_DROP_LIST, country)
        self.fill_text(self.PHONE_NUMBER_TEXT_BOX, phone_number)

    # Method to click on the "Ship Here" button
    def click_ship_here_button(self):
        self.click(self.SHIP_HERE_BTN)

    # Method to click on the "Next" button
    def click_next_button(self):
        self.click(self.NEXT_BTN)

    # Method to place the order
    def place_order(self):
        self.click(self.PLACE_ORDER_BTN)

    def is_page_loaded(self):
        return self.is_elements_exist(self.CHECKOUT_PAGE_LOAD_TITLE)

    # Reveals the discount code section
    def reveal_discount_code_section(self):
        self.click(self.REVEL_DISCOUNT_CODE_BTN)

    # Applies a discount code in the cart
    def apply_discount_code(self, discount_code):
        self.fill_text(self.DISCOUNT_CODE_TEXT_BOX, discount_code)
        self.click(self.APPLY_DISCOUNT_BTN)

    # Cancels the applied discount code
    def cancel_discount_code(self):
        self.click(self.CANCEL_DISCOUNT_COUPON_BTN)

    # Checks if the success message for applying a discount code is visible
    def is_discount_code_applied_successfully(self):
        return self.is_element_visible(self.DISCOUNT_COUPON_SUCCESS_MSG)