# High-quality images of the product.
# Product description, including details like size, color, and material.
# Price and available sizes.
# Add to cart and buy now options.
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locators for elements on the page
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span[id='product-price-1812'] span[class='price']")
    PRODUCT_SIZE_LIST = (By.CSS_SELECTOR, ".swatch-option.text")
    PRODUCT_COLOR_LIST = (By.CSS_SELECTOR, ".swatch-option.color")
    PRODUCT_QTY = (By.CSS_SELECTOR, "#qty")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#product-addtocart-button")
    CHOSEN_SIZE = (By.CSS_SELECTOR, "div[class='swatch-attribute size'] span[class='swatch-attribute-selected-option']")
    CHOSEN_COLOR = (
        By.CSS_SELECTOR, "div[class='swatch-attribute color'] span[class='swatch-attribute-selected-option']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_price(self):
        # Return the price of the product.
        return self.get_text(self.PRODUCT_PRICE)

    def choose_product_size(self, size):
        """Choose the product size on the page."""
        size_elements = self.wait_for_elements_visibility(*self.PRODUCT_SIZE_LIST)

        for size_element in size_elements:
            if size_element.get_attribute("option-label") == size:
                size_element.click()
                return

    def choose_product_color(self, color):
        # Choose the product color on the page.
        color_elements = self.wait_for_elements_visibility(*self.PRODUCT_COLOR_LIST)

        for color_element in color_elements:
            if color_element.get_attribute("option-label") == color:
                color_element.click()
                return

    def set_product_quantity(self, quantity):
        # Set the quantity of the product.
        self.fill_text(self.PRODUCT_QTY, str(quantity))

    def click_add_to_cart(self):
        # Click the 'Add to Cart' button.
        self.click(self.ADD_TO_CART_BTN)
        time.sleep(1)

    def get_chosen_size(self):
        # Get the text of the chosen size element.
        return self.get_text(self.CHOSEN_SIZE)

    def get_chosen_color(self):
        # Get the text of the chosen color element.
        return self.get_text(self.CHOSEN_COLOR)
