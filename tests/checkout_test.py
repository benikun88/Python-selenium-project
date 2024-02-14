from selenium import webdriver
import allure
import pytest
from configs import config_login
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.mini_cart_page import MiniCartPage
from pages.product_page import ProductPage
from pages.top_bar import TopBar
from configs import config_login


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("setup_checkout_test")
class TestLogin:
    @pytest.fixture
    def setup_checkout_test(self):
        global top_bar_page
        global login_page
        top_bar_page = TopBar(self.driver)
        login_page = top_bar_page.click_login()
        login_page.fill_info(config_login.VALID_USERNAME, config_login.VALID_PASSWORD)
        product_page = ProductPage(self.driver)
        product_page.driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html#")
        product_page.choose_product_size("S")
        product_page.choose_product_color("Black")
        product_page.click_add_to_cart()
        top_bar = TopBar(self.driver)
        top_bar.click_cart_icon()
        mini_cart = MiniCartPage(self.driver)
        mini_cart.click_proceed_checkout()

    def test_adresss_loaded(self):
        checkout_page = CheckoutPage(self.driver)
        assert checkout_page.is_shipping_address_section_exist() == True

    def test_discount(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.click_next_button()
        item_price_str = checkout_page.get_total_price()
        item_price = checkout_page.convert_price_to_float(item_price_str)
        item_price = item_price * 0.8
        print(item_price)
        checkout_page.reveal_discount_code_section()
        checkout_page.apply_discount_code("20poff")
        assert checkout_page.get_total_price() == item_price
