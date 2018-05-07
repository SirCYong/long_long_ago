from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.MainPage.MainPage import MainPage
from UIAutomation.Page.Mobile.PublishWarehouseSupply.ContractualObligation import ContractualObligation
from UIAutomation.Page.Mobile.PublishWarehouseSupply.PublishWarehouseSupply import PublishWarehouseSupply
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.PublishSupply.PublishSupply_sql import assert_publish_supply
from UIAutomation.Utils.HttpWrapper import eject_logged_user

__author__ = 'LiYu'
""" 功能：发布仓储供应+建立契约义务项 """


class PublishSupply(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        eject_logged_user(account=17767205508, password=123456)
        login_page = LoginPage(self.driver)
        login_page.login(username=17767205508, password=123456)
        pass

    def tearDown(self):
        # 注销app
        exit_app = ExitAppPage(self.driver)
        exit_app.logout_app()
        sleep(2)
        BaseTestCase.tearDown(self)

    def test_publish_supply_full(self):
        main_page = MainPage(self.driver)
        main_page.select_page()
        test_public_supply = PublishWarehouseSupply(self.driver)
        test_public_supply.click_publish_warehouse_supply()
        # 建立契约义务项.
        test_contractual_obligation = ContractualObligation(self.driver)
        test_contractual_obligation.service_contract()
        assert_publish_supply()

