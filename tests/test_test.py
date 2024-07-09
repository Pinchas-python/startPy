import pytest
from logic.pages.login_page import LogInPage
from tests.test_base import TestBase
from infra.config.config_provider import configuration
expected_result_email = 'Enter a valid email address'
expected_result_pass = 'Password cannot be empty'
expected_result_welcoome = ''
class TestClass(TestBase):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_with_login_without_email(self):
        page: LogInPage = self.browser.navigate("https://web.eos.bnk-il.com/auth", LogInPage)
        page.click_log_in()
        actual_result =  page.get_text()
        assert actual_result == expected_result_email

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_with_login_without_pass(self):
        page: LogInPage = self.browser.navigate("https://web.eos.bnk-il.com/auth", LogInPage)
        page.inser_email()
        page.click_log_in()
        actual_result = page.get_text_pass()
        assert actual_result == expected_result_pass

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_with_login_isvalid(self):
        page: LogInPage = self.browser.navigate("https://web.eos.bnk-il.com/auth", LogInPage)
        page.inser_email()
        page.inser_pass()
        page.click_log_in()
        actual_result = page.get_text()
        assert actual_result == expected_result_welcoome



    @pytest.mark.smoke
    def test_10008_(self):
        assert True is False

