from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.ManagementBusinessUnit.ManagementBusinessUnitPage import ManagementBusinessUnit
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_user_id
from .ManagementBusinessUnitSQL import delete_business_unit, get_new_business_unit
__author__ = 'zhoujin'


class ManagementBusinessUnitTest(BaseTestCase):
    """
        管理业务单位
        先生成过一个一级业务单位
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        mobile = 15624301115
        password = 123456
        self.user_id = get_user_id(mobile)
        delete_business_unit(self.user_id)  # 删除管理业务单位
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_management_business_unit(self):
        LongCardPage(self.driver).click_expected_card(self.user_id, '管理业务单位')
        sleep(3)
        ManagementBusinessUnit(self.driver).management_business_unit()
        ManagementBusinessUnit(self.driver).submit()
        sleep(3)
        get_new_business_unit()
        print("管理业务单位成功")

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

