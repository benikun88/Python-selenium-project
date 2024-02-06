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
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-item-link")
    NO_ITEM_RESULTS_IN_SERACH_MSG = (By.CSS_SELECTOR, ".message.notice")
    SEARCH_RESULT_PAGE_TITLE = (By.CSS_SELECTOR, ".base")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_names(self):
        # Get the names of products listed on the search page.
        return self.get_text(self.PRODUCT_NAME)

    def get_no_item_results_message(self):
        # Get the message displayed when there are no search results.
        return self.get_text(self.NO_ITEM_RESULTS_IN_SERACH_MSG)

    def get_search_result_page_title(self):
        # Get the title of the search result page.
        return self.get_text(self.SEARCH_RESULT_PAGE_TITLE)
