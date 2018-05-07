"""
跨创造者分配权限
管理者、监控者权限授权
CY
"""
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_user_id


class AssignPermissions(BaseTestCase):
    def setUp(self):
        self.mobile1 = 15355945533
        self.mobile2 = 15355945534
        self.user1_id = get_user_id(self.mobile1)
        self.user2_id = get_user_id(self.mobile2)
        self.password = 123456
        LoginPage(self.driver).login(self.mobile1, self.password)
        LongCardPage(self.driver).click_expected_card(self.user1_id, '管理者权限')
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        pass

    def test_assignPermissions(self):

        pass