from pages.cart_page import CartPage
from pages.mini_cart_page import MiniCartPage
from pages.product_page import ProductPage
from pages.top_bar import TopBar


class TestCart:
    def test_initial_cart_state(self):
        top_bar = TopBar(self.driver)
        top_bar.click_cart_icon()
        assert top_bar.get_cart_empty_msg() == "You have no items in your shopping cart."

    def test_add_item_to_cart(self):
        top_bar = TopBar(self.driver)
        product_page = ProductPage(self.driver)
        product_page.driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html#")
        product_page.choose_product_size("S")
        product_page.choose_product_color("Black")
        product_page.click_add_to_cart()
        assert top_bar.get_cart_icon_qty() == "1"

    def test_remove_item_from_cart(self):
        top_bar = TopBar(self.driver)
        product_page = ProductPage(self.driver)
        product_page.driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html#")
        product_page.choose_product_size("S")
        product_page.choose_product_color("Black")
        product_page.click_add_to_cart()
        mini_cart_page = MiniCartPage(self.driver)
        top_bar.click_cart_icon()
        mini_cart_page.remove_item()
        assert top_bar.get_cart_empty_msg() == "You have no items in your shopping cart."

    def test_update_cart_qty(self):
        top_bar = TopBar(self.driver)
        product_page = ProductPage(self.driver)
        product_page.driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html#")
        product_page.choose_product_size("S")
        product_page.choose_product_color("Black")
        product_page.click_add_to_cart()
        assert top_bar.get_cart_icon_qty() == "1"
        product_page.click_add_to_cart()
        assert top_bar.get_cart_icon_qty() == "2"

    def test_sub_total_equal_total(self):
        top_bar = TopBar(self.driver)
        product_page = ProductPage(self.driver)
        product_page.driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html#")
        product_page.choose_product_size("S")
        product_page.choose_product_color("Black")
        product_page.set_product_quantity("5")
        product_page.click_add_to_cart()
        mini_cart = MiniCartPage(self.driver)
        top_bar.click_cart_icon()
        price = int(mini_cart.get_item_price()) * 5
        assert price == mini_cart.get_subtotal_price()
