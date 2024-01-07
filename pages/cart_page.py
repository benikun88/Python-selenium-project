from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "button[data-role='proceed-to-checkout']")
    CART_SUBTOTAL_PRICE = (By.CSS_SELECTOR, "td[class='col subtotal'] span[class='price']")
    CART_ITEM_PRICE = (By.CSS_SELECTOR, "td[class='col price'] span[class='price']")
    PRODUCTS_ITEMS: list = (
        By.CSS_SELECTOR, "td[class='col item'] div[class='product-item-details'] a")
    EDIT_ITEM = (By.CSS_SELECTOR, "a[title='Edit item parameters']")
    REMOVE_ITEM = (By.CSS_SELECTOR, ".action.action-delete")
    ITEM_DETIELS = (By.CSS_SELECTOR, "span[role='tab']")
    UPDATE_QTY_BTN = (By.CSS_SELECTOR, "button[title='Update Shopping Cart'] span")
    QTY_TEXTBOX = (By.CSS_SELECTOR, ".item-qty.cart-item-qty")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".subtitle.empty")
    MOVE_TO_WISHLIST = (By.CSS_SELECTOR, "a[class='use-ajax action towishlist action-towishlist'] span")
    SHIPPING_PRICE = (By.CSS_SELECTOR, "span[data-th='Shipping']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_proceed_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BTN)
        return CartPage(self.driver)

    def get_item_price(self):
        return self.get_text(self.CART_ITEM_PRICE)

    def get_subtotal_price(self):
        return self.get_text(self.CART_SUBTOTAL_PRICE)

    def get_cart_empty_msg(self):
        return self.get_text(self.EMPTY_CART_MSG)

    def fill_quantity(self):
        self.fill_text(self.QTY_TEXTBOX)
        self.click(self.UPDATE_QTY_BTN)

    def remove_item(self):
        self.click(self.REMOVE_ITEM)
    def view_cart(self):
        self.click(self.REMOVE_ITEM)