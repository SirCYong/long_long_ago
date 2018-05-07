from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.MainPage.MainPage import MainPage
from UIAutomation.Page.Mobile.PublishLabour.PublishLabour import PublishLabour
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils.HttpWrapper import eject_logged_user

__author__ = 'LiYu'
""" 功能：发布劳务需求 """


class PublicLabour(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        login_page = LoginPage(self.driver)
        login_page.login(username=17767205508, password=123456)
        sleep(2)
        pass

    def tearDown(self):
        # 注销app
        exit_app = ExitAppPage(self.driver)
        exit_app.logout_app()
        BaseTestCase.tearDown(self)
        pass

    def test_public_full(self):
        main_page = MainPage(self.driver)
        main_page.select_page()
        test_public_labour = PublishLabour(self.driver)
        test_public_labour.click_public_labor()
        pass


