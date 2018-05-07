# coding=utf-8
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Page.Mobile.DemoPage.LoginPage import LoginPage
from UIAutomation.TestCase.SIT.Mobile.FunLogin_sql import release_labor_demand
import pytest

__doc__ = "登录用例，作为demo文件，勿删"
__author__ = "zzh"


@pytest.mark.tryfirst
class FunLoginTest(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)

        # 恢复测试数据
        # release_labor_demand()

        # 当前用户角色
        self.role = "login"
        self.driver.keyevent(4)

        # 初始化账号
        self.username = self.account_manage.get_account_by_role(self.role)["account"]
        self.password = self.account_manage.get_account_by_role(self.role)["password"]

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
