import time
import allure
import pytest
from selenium import webdriver
from configs import config_cart
from pages.product_page import ProductPage
from pages.top_bar import TopBar


@pytest.mark.usefixtures("eyes")
@allure.feature("UI Applitools")
class TestVisual:
    @allure.description("This test validates UI using Applitools")
    def test_applitools_integration(self, eyes):
        try:
            eyes.open(self.driver, "magento.softwaretestingboard python project", "test_applitools_integration")
            eyes.check_window("Initial Window")
            test_results = eyes.close(False)
            assert test_results.is_passed, "Visual validation failed"
        finally:
            eyes.abort_async()

    @allure.description("This test validates the UI of the sign-in page")
    def test_sign_in_page_ui(self, eyes):
        try:
            top_bar_page = TopBar(self.driver)
            login_page = top_bar_page.click_login()
            eyes.open(self.driver, "magento.softwaretestingboard python project", "test_sign_in_page_ui")
            eyes.check_window("Customer Login")
            test_results = eyes.close(False)
            assert test_results.is_passed, "Visual validation failed"
        finally:
            eyes.abort_async()

    @allure.description("This test validates the UI of the sign-up page")
    def test_sign_up_page_ui(self, eyes):
        try:
            top_bar_page = TopBar(self.driver)
            create_account = top_bar_page.click_create_account()
            eyes.open(self.driver, "magento.softwaretestingboard python project", "test_sign_up_page_ui")
            eyes.check_window("Customer sign up")
            test_results = eyes.close(False)
            assert test_results.is_passed, "Visual validation failed"
        finally:
            eyes.abort_async()

    @allure.description("This test validates the UI of the search result page")
    def test_search_result_ui(self, eyes):
        try:
            top_bar_page = TopBar(self.driver)
            top_bar_page.search_for_item("ELISA")
            eyes.open(self.driver, "magento.softwaretestingboard python project", "test_search_result_ui")
            eyes.check_window("search result")
            test_results = eyes.close(False)
            assert test_results.is_passed, "Visual validation failed"
        finally:
            eyes.abort_async()

    @allure.description("This test validates the UI of the mini cart")
    def test_mini_cart_ui(self, eyes):
        try:
            global top_bar
            global product_page
            top_bar = TopBar(self.driver)
            product_page = ProductPage(self.driver)
            product_page.driver.get(config_cart.PRODUCT_PAGE_URL)
            product_page.choose_product_size(config_cart.PRODUCT_SIZE)
            product_page.choose_product_color(config_cart.PRODUCT_COLOR)
            product_page.click_add_to_cart()
            top_bar.click_cart_icon()
            top_bar.driver.execute_script("window.scrollTo(0, 0);")
            eyes.open(self.driver, "magento.softwaretestingboard python project", "test_mini_cart_ui")
            eyes.check_element(top_bar.get_cart_section(), "mini cart")
            test_results = eyes.close(False)
            assert test_results.is_passed, "Visual validation failed"
        finally:
            eyes.abort_async()
