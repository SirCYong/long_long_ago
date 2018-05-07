from time import sleep
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.MainPage.MainPage import MainPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.VerifyRisk import VerifyRiskPage
from UIAutomation.Page.Mobile.RegisteredBusinessContactsOne.RegisteredBusinessContactsOnePage import RegisteredBusinessContactsOnePage
from UIAutomation.Page.Mobile.RegisteredBusinessContactsTwo.RegisteredBusinessContactsTwoPage import RegisteredBusinessContactsTwoPage
from UIAutomation.Page.Mobile.PublishWarehouseSupply.ContractualObligation import ContractualObligation
from UIAutomation.Page.Mobile.PublishWarehouseSupply.PublishWarehouseSupply import PublishWarehouseSupply
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils.HttpWrapper import eject_logged_user
from UIAutomation.TestCase.SIT.Mobile.RegisteredBusinessContacts.RegisteredBusinessContacts_sql import clear_first_sql, clear_second_sql
__author__ = 'xuwangchao'
""" 功能：完善注册业务关系人 """


class RegisteredBusinessContacts(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        clear_first_sql()
        clear_second_sql()
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.exit_app = ExitAppPage(self.driver)
        self.longcard_page = LongCardPage(self.driver)
        self.registerd_bussiness_first_page_first = RegisteredBusinessContactsOnePage(self.driver)
        self.registerd_bussiness_second_page =RegisteredBusinessContactsTwoPage(self.driver)
        self.login_page.login(username=18267990494, password=123456)
        pass

    def test_publish_supply_full(self):
        self.longcard_page.click_expected_card(10001475, '注册业务关系人')
        self.registerd_bussiness_first_page_first.assert_first_page()
        self.registerd_bussiness_first_page_first.choose_location()
        self.registerd_bussiness_first_page_first.type_first_page()
        self.registerd_bussiness_first_page_first.click_next_button()
        self.registerd_bussiness_second_page.assert_second_page()
        self.registerd_bussiness_second_page.type_second_page()
        self.registerd_bussiness_second_page.click_ok_button()
        self.registerd_bussiness_second_page.assert_sql()
        pass

    def tearDown(self):
        # 注销app
        self.exit_app.logout_app()
        sleep(2)
        BaseTestCase.tearDown(self)
        pass




