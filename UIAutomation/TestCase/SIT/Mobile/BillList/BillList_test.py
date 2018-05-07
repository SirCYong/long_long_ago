# coding=utf-8
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
import pytest
from UIAutomation.Page.Mobile.LoginPage.LoginPage import LoginPage
from UIAutomation.Page.Mobile.MyPage import MyPage
# from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.CardListPage import CardListPage
from UIAutomation.Page.Mobile.MoneyPocketPage import MoneyPocketPage
from UIAutomation.Page.Mobile.BillPage import BillPage
from UIAutomation.TestCase.SIT.Mobile.FunLogin_sql import release_labor_demand

__doc__ = "验证钱仓中未结算账单"
__author__ = "xuwangchao"


@pytest.mark.tryfirst
class FunLoginTest(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
        # 初始化数据
        self.username = '13788881111'
        self.password = '123456'
        # 恢复测试数据
        # release_labor_demand()
        # 初始化page
        self.login_page = LoginPage(self.driver)
        self.card_list_page = CardListPage(self.driver)
        self.my_page = MyPage(self.driver)
        self.money_pocket_page = MoneyPocketPage(self.driver)
        self.bill_page = BillPage(self.driver)
        pass

    def test_bill_list(self):
        """
        验证钱仓中未结算账单
        """
        self.login_page.login(self.username, self.password)
        self.card_list_page.click_more_button()
        self.card_list_page.click_my_button()
        self.my_page.click_my_monney()
        self.money_pocket_page.assert_my_monney()
        self.money_pocket_page.click_bill_unliquidated()
        self.bill_page.is_bill_page()
        self.bill_page.assert_bill()
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
