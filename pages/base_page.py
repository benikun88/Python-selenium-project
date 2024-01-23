from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import random
import string


class BasePage:
    """ Wrapper for selenium operations """

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 30)  # Set your desired timeout

    def wait_for_element_presence(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_for_element_visibility(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_elements_visibility(self, by, value):
        """Wait for the visibility of multiple elements."""
        return self.wait.until(EC.visibility_of_all_elements_located((by, value)))

    def wait_for_element_invisibility(self, by, value):
        return self.wait.until(EC.invisibility_of_element((by, value)))

    def wait_for_element_clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def click(self, locator) -> None:
        el: WebElement = self.wait_for_element_clickable(*locator)
        self.driver.execute_script("arguments[0].setAttribute('style', 'border: 1px solid blue;');", el)
        #
        el.click()

    def fill_text(self, locator, txt: str) -> None:
        el: WebElement = self.wait_for_element_clickable(*locator)
        self.wait_for_element_visibility(*locator)
        self.driver.execute_script("arguments[0].setAttribute('style', 'border: 1px solid blue;');", el)
        el.clear()
        el.send_keys(txt)

    def get_text(self, locator) -> str:
        el: WebElement = self.wait_for_element_visibility(*locator)
        return el.text

    def hover(self, locator) -> str:
        el: WebElement = self.wait_for_element_visibility(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(el)

    # //need to be in utils app
    def generate_random_email(self) -> object:
        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        domain = "gmail.com"
        email = f"{username}@{domain}"
        return email

    def select_by_value(self, locator, value):
        select = Select(*locator)
        select.select_by_value(value)

    def select_by_text(self, locator, text):
        select = Select(*locator)
        select.select_by_visible_text(text)

    def select_by_index(self, locator, index):
        select = Select(*locator)
        select.select_by_index(index)

    def is_elements_exist(self, locator):
        try:
            element = self.wait_for_element_visibility(*locator)
            return element.is_displayed()
        except WebDriverException as e:
            return False

    def navigate_to(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)
