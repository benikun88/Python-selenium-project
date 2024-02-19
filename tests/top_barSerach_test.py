import pytest

from pages.top_bar import TopBar


class TestTopBar:
    def test_logo_visibility(self):
        top_bar = TopBar(self.driver)
        assert top_bar.is_logo_visible(), "The site logo is not present or visible."

    def test_top_bar_persists(self):
        top_bar = TopBar(self.driver)
        pages_to_visit = ["/customer/account/login", "/customer/account/create/", "/sale.html"]
        for page in pages_to_visit:
            self.driver.get(f"https://magento.softwaretestingboard.com{page}")
            assert top_bar.is_top_bar_visible(), f"The top bar is not visible on the {page} page."

    def test_search_bar_persists(self):
        top_bar = TopBar(self.driver)
        pages_to_visit = ["/customer/account/login", "/customer/account/create/", "/sale.html"]
        for page in pages_to_visit:
            self.driver.get(f"https://magento.softwaretestingboard.com{page}")
            assert top_bar.is_search_bar_visible(), f"The search bar is not visible on the {page} page."
