import time

import allure
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.top_bar import TopBar


class TestLogin:
    def test_page_loaded(self):
        top_bar_page = TopBar(self.driver)
        login_page = top_bar_page.click_login()
        assert login_page.is_page_loaded() == True

    @allure.description("""
        Test the login functionality with different data.

        Test data:
        - Valid username and empty password, expecting password error: "This is a required field."
        - Valid username and valid password, expecting no errors.
        - Invalid username and empty password, expecting email error: "Please enter a valid email address (Ex: johndoe@domain.com)."
    """)
    @pytest.mark.parametrize("test_data", [
        {"username": "benikun88@gmail.com", "password": "1q2w3e4r!", "expected_email_error": None,
         "expected_password_error": None},
        {"username": "benikun88@gmail.com", "password": "", "expected_email_error": None,
         "expected_password_error": "This is a required field."},
        {"username": "benikun88", "password": "",
         "expected_email_error": "Please enter a valid email address (Ex: johndoe@domain.com).",
         "expected_password_error": None}
    ])
    def test_login_with_different_data(self, setup, test_data):
        username = test_data["username"]
        password = test_data["password"]
        expected_email_error = test_data["expected_email_error"]
        expected_password_error = test_data["expected_password_error"]

        top_bar_page = TopBar(self.driver)
        login_page = top_bar_page.click_login()
        login_page.fill_info(username, password)

        if expected_email_error:
            assert login_page.get_email_error() == expected_email_error
        elif expected_password_error:
            assert login_page.get_password_error() == expected_password_error
        else:
            # Add other assertions for successful login
            assert top_bar_page.get_success_login() == "Welcome, Benjamin Kun!"
            # Add additional assertions for successful login if needed


