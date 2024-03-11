import time
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span[id='product-price-1812'] span[class='price']")
    PRODUCT_SIZE_LIST = (By.CSS_SELECTOR, ".swatch-option.text")
    PRODUCT_COLOR_LIST = (By.CSS_SELECTOR, ".swatch-option.color")
    PRODUCT_QTY = (By.CSS_SELECTOR, "#qty")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#product-addtocart-button")
    CHOSEN_SIZE = (By.CSS_SELECTOR, "div[class='swatch-attribute size'] span[class='swatch-attribute-selected-option']")
    ADD_TO_COMPARE_LOGO = (By.CSS_SELECTOR, "div[class='product-addto-links'] a[class='action tocompare']")
    ADD_TO_WISH_LIST_LOGO = (By.CSS_SELECTOR, "div[class='product-addto-links'] a[class='action towishlist']")
    CHOSEN_COLOR = (
    By.CSS_SELECTOR, "div[class='swatch-attribute color'] span[class='swatch-attribute-selected-option']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get product price")
    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    @allure.step("Choose product size")
    def choose_product_size(self, size):
        size_elements = self.wait_for_elements_visibility(*self.PRODUCT_SIZE_LIST)
        for size_element in size_elements:
            if size_element.get_attribute("option-label") == size:
                size_element.click()
                return

    @allure.step("Choose product color")
    def choose_product_color(self, color):
        color_elements = self.wait_for_elements_visibility(*self.PRODUCT_COLOR_LIST)
        for color_element in color_elements:
            if color_element.get_attribute("option-label") == color:
                color_element.click()
                return

    @allure.step("Set product quantity")
    def set_product_quantity(self, quantity):
        self.fill_text(self.PRODUCT_QTY, str(quantity))

    @allure.step("Click add to cart")
    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        time.sleep(2)

    @allure.step("Get chosen size")
    def get_chosen_size(self):
        return self.get_text(self.CHOSEN_SIZE)

    @allure.step("Get chosen color")
    def get_chosen_color(self):
        return self.get_text(self.CHOSEN_COLOR)

    @allure.step("Get compare logo")
    def get_compare_logo(self):
        return self.wait_for_element_visibility(*self.ADD_TO_COMPARE_LOGO)

    @allure.step("Get wish list logo")
    def get_wish_list_logo(self):
        return self.wait_for_element_visibility(*self.ADD_TO_WISH_LIST_LOGO)
