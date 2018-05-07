# coding=utf-8
from time import sleep

from UIAutomation.Page.Mobile.VerifyRisk.VerifyRiskPage import VerifyRiskPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
import pytest
from UIAutomation.Page.Mobile.LoginPage.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage

__doc__ = "风险审核"
__author__ = "xuwangchao"


@pytest.mark.tryfirst
class FunVerifyRisk(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
        self.username = '13654541244'
        self.password = '123456'
        self.login_page = LoginPage(self.driver)
        self.long_task_page = LongCardPage(self.driver)
        self.verify_risk_page = VerifyRiskPage(self.driver)
        pass

    def test_bill_list(self):
        """
        风险审核
        """
        self.login_page.login(self.username, self.password) # 登陆
        self.long_task_page.click_expected_card(10001456, '风险审核') # 找到并点击风险审核卡片
        self.verify_risk_page.assert_versify_risk(10001456) # assert风险审核详情
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
