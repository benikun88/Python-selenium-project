import time

import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.top_bar import TopBar


class TestLogin:

    def test01(self):
        global loginpage
        global topBarPage
        topBarPage = TopBar(self.driver)
        loginpage=topBarPage.click_login()
        loginpage.fill_info("benikun88@gmail.com","")
        # print(loginpage.get_email_error())
        assert loginpage.get_password_error() == "This is a required field."

    def test02(self):
        # loginpage = login(self.driver)
        loginpage.fill_info("benikun88@gmail.com", "1q2w3e4r!")
        time.sleep(7)
        assert topBarPage.get_success_login() == "Welcome, Benjamin Kun!"
