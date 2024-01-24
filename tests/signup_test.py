import time

import allure

import pages.base_page
from pages.top_bar import TopBar


class TestSignUp:
    # test change
    @allure.description("""
        Test successful user signup.

        Steps:
        1. Click on the 'Create Account' link.
        2. Fill in the signup form with valid data.
        3. Verify successful registration message.
    """)
    def test_successful_signup(self):
        url = "https://magento.softwaretestingboard.com/customer/account/"
        top_bar_page = TopBar(self.driver)
        create_account = top_bar_page.click_create_account()
        account_page = create_account.sign_up("test", "test2", create_account.generate_random_email(), "1q2w3e4r!",
                                              "1q2w3e4r!")
        time.sleep(5)
        assert account_page.get_successful_registration_text_msg() == "Thank you for registering with Main Website Store."
    # test existing user

    @allure.description("""
        Test user signup with an existing email address.

        Steps:
        1. Click on the 'Create Account' link.
        2. Fill in the signup form with an email address that already exists.
        3. Verify the error message indicating the existing user.
    """)
    def test_existing_user_signup(self):
        url = "https://magento.softwaretestingboard.com/customer/account/"
        top_bar_page = TopBar(self.driver)
        create_account = top_bar_page.click_create_account()
        create_account.sign_up("test", "test2", "bk88@gmail.com", "1q2w3e4r!", "1q2w3e4r!")
        time.sleep(5)
        assert create_account.get_existing_user_error() == "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."
