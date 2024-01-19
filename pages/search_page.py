# Search bar.
# Search results based on user queries.
# High-quality images of the product.
# Product description, including details like size, color, and material.
# Price and available sizes.
# Add to cart and buy now options.
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    # Locators for elements on the page
    PRODUCT_NAME = (By.CSS_SELECTOR, "span[id='product-price-1812'] span[class='price']")
    NO_ITEM_RESULTS_IN_SERACH=(By.CSS_SELECTOR,".message.notice")
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
