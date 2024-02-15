# configs/config_checkout.py

# Test data for checkout
VALID_DISCOUNT_CODE = "20poff"
INVALID_DISCOUNT_CODE = "20pof"

# Expected success and error messages for discount code
EXPECTED_SUCCESS_APPLY_CODE = "Your coupon was successfully applied."
EXPECTED_SUCCESS_REMOVE_CODE = "Your coupon was successfully removed."
EXPECTED_ERROR_INVALID_CODE = "The coupon code isn't valid. Verify the code and try again."

# Test URLs
CHECKOUT_PAGE_URL = "https://magento.softwaretestingboard.com/checkout"
URL_ITEM_TO_ADD = "https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html#"
MAIN_PAGE_URL = "https://magento.softwaretestingboard.com/"
# Other configurations
WAIT_TIME = 10  # Adjust this according to your needs
SIZE = "S"
COLOR = "Black"
