from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Page.Mobile.LoginPage.LoginPage import LoginPage


"""
Demo Test case for New project testcase.
"""
__author__ = "Yongli"
__package__ = 'IscsUIAutomation'


class DemoLoginTestCase(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)

        # 恢复测试数据
        # release_labor_demand()

        # 当前用户角色
        self.role = "login"

        # 初始化账号
        self.username = '13544443600'
        self.password = '123456'

        # 初始化page
        self.login_page = LoginPage(self.driver)
        pass

    def test_login_ok(self):
        """
        登录成功
        """

        self.login_page.login(self.username, self.password)
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
