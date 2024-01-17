from selenium.webdriver.common.by import By

# ... (your existing imports and code)

class ProductPage(BasePage):
    # ... (your existing locators)

    # ...

    def get_product_price(self):
        """Return the price of the product."""
        return self.get_text(self.PRODUCT_PRICE)

    def choose_product_size(self, size):
        # Choose a specific size from the available options.
        try:
            size_option = self.find_element((By.XPATH, f"//div[@class='swatch-attribute size']//div[@class='swatch-option text' and contains(text(),'{size}')]"))
            size_option.click()
            return True
        except Exception as e:
            print(f"Error choosing product size: {e}")
            return False

    def choose_product_color(self, color):
        """Choose a specific color from the available options."""
        try:
            color_option = self.find_element((By.XPATH, f"//div[@class='swatch-attribute color']//div[@class='swatch-option color' and contains(text(),'{color}')]"))
            color_option.click()
            return True
        except Exception as e:
            print(f"Error choosing product color: {e}")
            return False

    def set_product_quantity(self, quantity):
        """Set the quantity of the product."""
        self.fill_text(self.PRODUCT_QTY, str(quantity))

    def click_add_to_cart(self):
        """Click the 'Add to Cart' button."""
        self.click(self.ADD_TO_CART_BTN)

    def click_buy_now(self):
        """Click the 'Buy Now' button."""
        # Implement the logic for the "Buy Now" button click if available on the page
        pass
