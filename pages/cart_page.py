import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # CSS selectors for elements on the page
    CART_PAGE_LOAD_TITLE = (By.CSS_SELECTOR, ".base")
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "button[data-role='proceed-to-checkout']")
    CART_SUBTOTAL_PRICE = (By.CSS_SELECTOR, "td[class='col subtotal'] span[class='price']")
    CART_ITEM_PRICE = (By.CSS_SELECTOR, "td[class='col price'] span[class='price']")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".subtitle.empty")
    REMOVE_ITEM = (By.CSS_SELECTOR, ".action.action-delete")
    UPDATE_QTY_BTN = (By.CSS_SELECTOR, "button[title='Update Shopping Cart'] span")
    QTY_TEXTBOX = (By.CSS_SELECTOR, ".item-qty.cart-item-qty")
    DISCOUNT_CODE_TEXT_BOX = (By.CSS_SELECTOR, "#coupon_code")
    APPLY_DISCOUNT_BTN = (By.CSS_SELECTOR, "button[value='Apply Discount'] span")
    CANCEL_DISCOUNT_COUPON_BTN = (By.CSS_SELECTOR, "button[value='Cancel'] span span")
    DISCOUNT_COUPON_SUCCSES_MSG = (
        By.CSS_SELECTOR, "div[data-ui-id='checkout-cart-validationmessages-message-success']")
    CART_ERROR_MSG = (By.CSS_SELECTOR, ".message-error.error.message")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Clicks the "Proceed to Checkout" button and returns a new CartPage instance
    @allure.step("Click 'Proceed to Checkout' button")
    def click_proceed_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BTN)
        return CartPage(self.driver)

    # Retrieves the item price from the cart
    @allure.step("Get item price from the cart")
    def get_item_price(self):
        return self.get_text(self.CART_ITEM_PRICE)

    # Retrieves the subtotal price from the cart
    @allure.step("Get subtotal price from the cart")
    def get_subtotal_price(self):
        return self.get_text(self.CART_SUBTOTAL_PRICE)

    # Retrieves the empty cart message
    @allure.step("Get empty cart message")
    def get_cart_empty_msg(self):
        return self.get_text(self.EMPTY_CART_MSG)

    # Fills the quantity in the cart and updates it
    @allure.step("Fill quantity '{qty}' in the cart and update it")
    def fill_quantity(self, qty):
        self.fill_text(self.QTY_TEXTBOX, qty)
        self.click(self.UPDATE_QTY_BTN)

    # Removes an item from the cart
    @allure.step("Remove an item from the cart")
    def remove_item(self):
        self.click(self.REMOVE_ITEM)

    # Views the cart
    @allure.step("View the cart")
    def view_cart(self):
        self.click(self.REMOVE_ITEM)

    # Checking if the page load title element is present on the page
    @allure.step("Check if the page is loaded")
    def is_page_loaded(self):
        return self.is_elements_exist(self.CART_PAGE_LOAD_TITLE)

    # Reveals the discount code section
    @allure.step("Reveal the discount code section")
    def reveal_discount_code_section(self):
        self.click(self.REVEL_DISCOUNT_CODE_BTN)

    # Applies a discount code in the cart
    @allure.step("Apply discount code '{discount_code}'")
    def apply_discount_code(self, discount_code):
        self.fill_text(self.DISCOUNT_CODE_TEXT_BOX, discount_code)
        self.click(self.APPLY_DISCOUNT_BTN)

    # Cancels the applied discount code
    @allure.step("Cancel the applied discount code")
    def cancel_discount_code(self):
        self.click(self.CANCEL_DISCOUNT_COUPON_BTN)

    # Checks if the success message for applying a discount code is visible
    @allure.step("Check if the success message for applying a discount code is visible")
    def discount_code_msg(self):
        return self.get_text(self.DISCOUNT_COUPON_SUCCSES_MSG)

    # Retrieves the error message from the cart
    @allure.step("Get error message from the cart")
    def get_error_cart_msg(self):
        return self.get_text(self.CART_ERROR_MSG)
