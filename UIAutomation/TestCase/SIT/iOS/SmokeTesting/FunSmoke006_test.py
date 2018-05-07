from time import sleep
from UIAutomation.Page.Mobile.ActivationDepot.ActivationDepotPage import ActivationDepotPage
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeLeft
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.iOS.Sprint1.SitSprint1Full001SQL import delete_depot_card
from UIAutomation.Utils import stop_android_appium, get_user_id
from UIAutomation.Utils.HttpWrapper import eject_logged_user

__author__ = 'CaoYong'


class FuncSmoke006(BaseTestCase):
    """
        激活仓库
    """
    def setUp(self):
        self.mobile = 18205010265
        self.admin = get_user_id(self.mobile)
        self.password = 123456
        BaseTestCase.setUp(self)
        sleep(3)
        delete_depot_card(self.admin)
        eject_logged_user(self.mobile, self.password)
        sleep(2)
        LoginPage(self.driver).login(self.mobile, self.password)  # 登录
        LongCardPage(self.driver).click_expected_card(self.admin, '激活仓库')

    def test_fun_smoke(self):
        # SwipeLeft(self.driver)
        ActivationDepotPage(self.driver).depot_input_information()
        sleep(10)
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)

        pass




