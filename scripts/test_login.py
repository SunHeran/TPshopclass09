from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page
import pytest


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    def test_login(self, args):
        phone = args["phone"]
        password = args["password"]
        expect = args["expect"]

        self.page.home.click_mine()
        self.page.mine.click_login_and_signup()
        self.page.login.input_phone(phone)
        self.page.login.input_password(password)
        self.page.login.click_login()
        assert self.page.login.is_toast_exits(expect)

    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login_miss_part"))
    def test_login_miss_part(self, args):
        phone = args["phone"]
        password = args["password"]

        self.page.home.click_mine()
        self.page.mine.click_login_and_signup()
        self.page.login.input_phone(phone)
        self.page.login.input_password(password)

        assert not self.page.login.is_login_button_enabled()