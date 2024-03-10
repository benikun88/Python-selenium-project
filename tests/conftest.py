import os
from urllib import request

import pytest
from _pytest.config import Config
from selenium.webdriver.chrome.options import Options
import allure
from selenium import webdriver
from applitools.selenium import Eyes
from applitools.common import MatchLevel

@pytest.fixture(autouse=True)
def setup(request):
    if "api" not in request.node.keywords:
        global driver
        options = Options()
        options.add_experimental_option("detach", True)
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        request.cls.driver = driver
        driver.maximize_window()
        driver.get("https://magento.softwaretestingboard.com/")
        yield
        driver.quit()
    else:
        yield None


def pytest_exception_interact(report):
    if report.failed:
        if "api" not in report.keywords:
            # Attach screenshot for non-API tests
            allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)


def pytest_configure(config: Config) -> None:
    config.option.allure_report_dir = "allure-results"


@pytest.fixture()
def eyes():
    eyes = Eyes()
    eyes.api_key = 'yQZoWxzsvOfSFbrd3YGmcSpl1061UWFGuNz6dXPWMQvXA110'  # Set your Applitools API key here
    yield eyes
    eyes.abort_async()  # Make sure to abort the session to handle any exceptions

# def pytest_sessionfinish() -> None:
#     environment_properties = {
#      'browser': driver.name,
#      'driver_version': driver.capabilities['browserVersion']
#     }
#     allure_env_path = os.path.join("allure-results", 'environment.properties')
#     with open(allure_env_path, 'w') as f:
#         data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
#         f.write(data)
