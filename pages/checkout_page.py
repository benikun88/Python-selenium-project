from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    SHIPPING_ADDRESS_SECTION = (By.CSS_SELECTOR, ".shipping-address-item.selected-item")
    NEW_ADDRESS_BTN = (By.CSS_SELECTOR,".action.action-show-popup")
    # Shipping Address
    FIRST_NAME_TEXT_BOX=(By.CSS_SELECTOR,"#NEYKSU8")
    LAST_NAME_TEXT_BOX = (By.CSS_SELECTOR, "#CEQDYY0")
    STREET_ADDRESS_TEXT_BOX = (By.CSS_SELECTOR, "#QQBO9IB")
    CITY_TEXT_BOX = (By.CSS_SELECTOR, "#N6MGM0Y")
    COUNTRY_DROP_LIST = (By.CSS_SELECTOR, "#DVWFUC5")
    PHONE_NUMBER_TEXT_BOX = (By.CSS_SELECTOR, "#UI1F719")
    SHIP_HERE_BTN = (By.CSS_SELECTOR, "button[class='action primary action-save-address'] span")
    NEXT_BTN = (By.CSS_SELECTOR, ".button.action.continue.primary")

    def __init__(self, driver):
        super().__init__(driver)