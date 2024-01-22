from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage

class MiniCartPage(BasePage):
    # Locator for the close button in the mini cart
    CLOSE_MINI_CART_BTN = (By.CSS_SELECTOR, "#btn-minicart-close")

    # Locators for elements on the page
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "#top-cart-btn-checkout")
    CART_SUBTOTAL_PRICE = (By.CSS_SELECTOR, "span[data-bind='html: cart().subtotal_excl_tax'] span[class='price']")
    CART_ITEM_PRICE = (By.CSS_SELECTOR, "span[class='minicart-price'] span[class='price']")
    PRODUCTS_MINI_CART_ITEMS: list = (
        By.CSS_SELECTOR, ".minicart-items .item.product.product-item .product-item-details .product-item-name")
    EDIT_ITEM = (By.CSS_SELECTOR, "a[title='Edit item']")
    REMOVE_ITEM = (By.CSS_SELECTOR, "a[title='Remove item']")
    ITEM_DETAILS = (By.CSS_SELECTOR, "span[role='tab']")
    NUMBER_OF_ITEMS_IN_CART = (By.CSS_SELECTOR, ".count")
    MINI_CART_CLOSE_BTN = (By.CSS_SELECTOR, "#btn-minicart-close")
    VIEW_EDIT_BTN = (By.CSS_SELECTOR, ".action.viewcart")
    UPDATE_BTN = (By.CSS_SELECTOR, ".update-cart-item")
    QTY_TEXTBOX = (By.CSS_SELECTOR, ".item-qty.cart-item-qty")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".subtitle.empty")

    def __init__(self, driver):
        super().__init__(driver)

    # Clicks the "Proceed to Checkout" button in the mini cart and returns a new CartPage instance
    def click_proceed_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BTN)
        return CartPage(self.driver)

    # Retrieves the item price from the mini cart
    def get_item_price(self):
        return self.get_text(self.CART_ITEM_PRICE)

    # Retrieves the subtotal price from the mini cart
    def get_subtotal_price(self):
        return self.get_text(self.CART_SUBTOTAL_PRICE)

    # Retrieves the empty cart message from the mini cart
    def get_cart_empty_msg(self):
        return self.get_text(self.EMPTY_CART_MSG)

    # Fills the quantity in the mini cart and updates it
    def fill_quantity(self):
        self.fill_text(self.QTY_TEXTBOX)
        self.click(self.UPDATE_BTN)

    # Removes an item from the mini cart
    def remove_item(self):
        self.click(self.REMOVE_ITEM)

    # Views the cart in the mini cart (Note: The method name suggests removing an item, but the code clicks the remove item button)
    def view_cart(self):
        self.click(self.REMOVE_ITEM)

    # Clicks the "Close Mini Cart" button
    def close_mini_cart(self):
        self.click(self.CLOSE_MINI_CART_BTN)
