import pytest

from infra.browser import Browser

from logic.pages.youtube_page import YTPage
from tests.test_base import TestBase
from infra.config.config_provider import configuration


class TestClass(TestBase):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_10007_(self):
        page: YTPage = self.browser.navigate("https://web.eos.bnk-il.com/auth", YTPage)
        page.click_side_menu()
        print('past playwright')

    @pytest.mark.smoke
    def test_10008_(self):
        assert True is False



    @pytest.mark.smoke
    def test_10008_(self):
        assert True is False

