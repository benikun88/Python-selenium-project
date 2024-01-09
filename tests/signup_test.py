import time

from pages.top_bar import TopBar


class TestSignUp:

    def test_01(self):
        url = "https://magento.softwaretestingboard.com/customer/account/"
        global create_account
        topBarPage = TopBar(self.driver)
        create_account=topBarPage.click_create_account()
        create_account.sign_up("test","test2","b888@mail.com","1q2w3e4r!","1q2w3e4r!")
        # print(loginpage.get_email_error())
        time.sleep(5)
        assert create_account.driver.current_url == url