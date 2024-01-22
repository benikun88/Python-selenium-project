import time

import allure
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.top_bar import TopBar


class TestLogin:

    @allure.description("""
        Test the login functionality with different data.

        Test data:
        - Valid username and empty password, expecting password error: "This is a required field."
        - Valid username and valid password, expecting no errors.
        - Invalid username and empty password, expecting email error: "Please enter a valid email address (Ex: johndoe@domain.com)."
    """)
    @pytest.mark.parametrize("username, password, expected_email_error, expected_password_error", [
        ("benikun88@gmail.com", "", None, "This is a required field."),
        ("benikun88@gmail.com", "1q2w3e4r!", None, None),  # No error expected for valid data
        ("benikun88", "", "Please enter a valid email address (Ex: johndoe@domain.com).", None),
    ])
    def test_login_with_different_data(self, setup, username, password, expected_email_error, expected_password_error):
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

    # def test_empty_password_error(self):
    #     global loginpage
    #     global topBarPage
    #     topBarPage = TopBar(self.driver)
    #     loginpage = topBarPage.click_login()
    #     loginpage.fill_info("benikun88@gmail.com", "")
    #     # print(loginpage.get_email_error())
    #     assert loginpage.get_password_error() == "This is a required field.", "Password error message is not as expected"
    #
    # def test_successful_login(self):
    #     global loginpage
    #     global topBarPage
    #     topBarPage = TopBar(self.driver)
    #     loginpage = topBarPage.click_login()
    #     loginpage.fill_info("benikun88@gmail.com", "1q2w3e4r!")
    #     time.sleep(7)
    #     assert topBarPage.get_success_login() == "Welcome, Benjamin Kun!", "Password error message is not as expected"
    #
    # def test_invalid_email_error(self):
    #     global loginpage
    #     global topBarPage
    #     topBarPage = TopBar(self.driver)
    #     loginpage = topBarPage.click_login()
    #     loginpage.fill_info("benikun88", "")
    #     time.sleep(7)
    #     assert loginpage.get_email_error() == "Please enter a valid email address (Ex: johndoe@domain.com).", "Password error message is not as expected"
