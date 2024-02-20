import os
from urllib import request

import pytest
from selenium.webdriver.chrome.options import Options
import allure
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")
    yield
    driver.quit()


def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


def pytest_sessionfinish() -> None:
    environment_properties = {
        'browser': driver.name,
        'driver_version': driver.capabilities['browserVersion']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)
