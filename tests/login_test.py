from selenium import webdriver
import allure
import pytest
from configs import config_login
from pages.login_page import LoginPage
from pages.top_bar import TopBar

@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("setup_login_test")
class TestLogin:
    @pytest.fixture
    # pre steps before starting each test
    def setup_login_test(self):
        global top_bar_page
        global login_page
        top_bar_page = TopBar(self.driver)
        login_page = top_bar_page.click_login()

    def test_page_loaded(self):
        assert login_page.is_page_loaded() == True

    @allure.description("""
        Test the login functionality with different data.

        Test data:
        - Valid username and empty password, expecting password error: "This is a required field."
        - Valid username and valid password, expecting no errors.
        - Invalid username and empty password, expecting email error: "Please enter a valid email address (Ex: johndoe@domain.com)."
    """)
    @pytest.mark.parametrize("username, password, expected_email_error, expected_password_error", [
        (config_login.VALID_USERNAME, config_login.VALID_PASSWORD, None, None),
        (config_login.VALID_USERNAME, config_login.EMPTY_PASSWORD, None, config_login.EXPECTED_PASSWORD_ERROR),
        (config_login.INVALID_USERNAME, config_login.EMPTY_PASSWORD, config_login.EXPECTED_EMAIL_ERROR, None)
    ])
    def test_login_with_different_data(self, setup, username, password, expected_email_error, expected_password_error):
        login_page.fill_info(username, password)

        if expected_email_error:
            assert login_page.get_email_error() == expected_email_error
        elif expected_password_error:
            assert login_page.get_password_error() == expected_password_error
        else:
            assert top_bar_page.get_success_login() == config_login.EXPECTED_SUCCESS_LOGIN

    @pytest.mark.parametrize("username, password", [
        (config_login.VALID_USERNAME, config_login.VALID_PASSWORD)])
    def test_login_consist_after_reload_page(self, username, password):
        login_page.fill_info(username, password)
        if top_bar_page.get_success_login() == config_login.EXPECTED_SUCCESS_LOGIN:
            self.driver.refresh()
            assert top_bar_page.get_success_login() == config_login.EXPECTED_SUCCESS_LOGIN
        else:
            assert top_bar_page.get_success_login() == config_login.EXPECTED_SUCCESS_LOGIN

    # sign out test
    @pytest.mark.parametrize("username, password", [
        (config_login.VALID_USERNAME, config_login.VALID_PASSWORD)])
    def test_sign_out(self, username, password):
        login_page.fill_info(username, password)
        top_bar_page.click_switch_dropdown_list_my_account()
        top_bar_page.click_sign_out()
        assert top_bar_page.get_success_logout_msg() == config_login.EXPECTED_SUCCESS_LOGOUT_MSG

    # Sign in- password recovery tests
    def test_password_recovery(self):
        login_page.click_forgot_password()
        login_page.fill_email_address_reset("Benikun88@gmail.com")
        login_page.click_reset_password()
        assert login_page.get_reset_msg_process() == "If there is an account associated with Benikun88@gmail.com you will receive an email with a link to reset your password."
