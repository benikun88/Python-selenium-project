from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.top_bar import TopBar


class TestCart:
    def test_initial_cart_state(self):
        top_bar = TopBar(self.driver)
        top_bar.click_cart_icon()
        assert TopBar.get_cart_empty_msg() == "You have no items in your shopping cart."

    def test_add_item_to_cart(self):
        productPage = ProductPage(self.driver)
        productPage.driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html#")
        productPage.choose_product_size("s")
        productPage.choose_product_color("black")
        productPage.click_add_to_cart()
        assert TopBar.get_cart_icon_Qty() == "1"
