from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    CLOSE_MINI_CART_BTN = (By.CSS_SELECTOR, "#btn-minicart-close")
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "#top-cart-btn-checkout")
    CART_SUBTOTAL_PRICE = (By.CSS_SELECTOR, "span[data-bind='html: cart().subtotal_excl_tax'] span[class='price']")
    PRODUCTS_MINICART_ITEMS: list = (By.CSS_SELECTOR,".minicart-items .item.product.product-item .product-item-details .product-item-name")
    EDIT_ITEM = (By.CSS_SELECTOR, "a[title='Edit item']")
    REMOVE_ITEM = (By.CSS_SELECTOR,"a[title='Remove item']")
    ITEM_DETIELS = (By.CSS_SELECTOR,"span[role='tab']")
    NUMBER_OF_ITEMS_IN_CART = (By.CSS_SELECTOR,".count")
    MINI_CART_CLOSE_BTN = (By.CSS_SELECTOR,"#btn-minicart-close")
    VIEW_EDIT_BTN = (By.CSS_SELECTOR,".action.viewcart")
    SUCCESSFUL_RESTORATION=(By.CSS_SELECTOR,"div[data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_successful_registration_text_msg(self):
        return self.get_text(self.SUCCESSFUL_RESTORATION)