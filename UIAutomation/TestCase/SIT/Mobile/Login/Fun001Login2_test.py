# coding=utf-8
from UIAutomation.TestCase import BaseTestCase
import pytest
from UIAutomation.Page.Mobile.DemoPage.LoginPage import LoginPage
from .Fun001Login2_sql import login_state

__doc__ = "登录用例，作为demo文件，勿删"
__author__ = "zzh"


@pytest.mark.tryfirst
class Fun001Login2(BaseTestCase):
    def setUp(self):
        super(Fun001Login2).setUp(self)

        # 初始化数据
        self.username = '12012345678'
        self.password = '123456'

        # 恢复测试数据
        login_state(self.username)

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
        super(Fun001Login2).tearDown(self)
        pass