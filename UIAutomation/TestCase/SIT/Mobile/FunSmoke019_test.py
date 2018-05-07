from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.ManageAddress.ManageAddressPage import ManageAddressPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.FunSmoke019SQL import delete_address
from UIAutomation.Utils import get_user_id

__author__ = 'CaoYong'


class FuncSmoke019(BaseTestCase):
    """
        激活仓库
    """
    def setUp(self):
        self.mobile = 18888000131
        self.admin = get_user_id(self.mobile)
        self.password = 123456
        BaseTestCase.setUp(self)
        sleep(3)
        delete_address(self.admin)
        LoginPage(self.driver).login(self.mobile, self.password)  # 登录
        LongCardPage(self.driver).click_expected_card(self.admin, '管理收货地址')

    def test_fun_smoke(self):
        ManageAddressPage(self.driver).address_input_information()
        sleep(10)
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)

        pass




