from time import sleep


from appium import webdriver as app_web_driver
from selenium import webdriver as browser_web_driver

from UIAutomation.Page.Mobile.ActivationEntityShop.ActivationEntityShopButtonPage import ActivationEntityShopButtonPage
from UIAutomation.Page.Mobile.ActivationEntityShop.ActivationEntityShopPage import ActivationEntityShopPage
from UIAutomation.Page.Mobile.ActivationEntityShop.ImportHistoricalOrderPage import ImportHistoricalOrderPage
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.iOS.ActivationCommodity.ActivationCommodityPage import ActivationCommodityPage
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeLeft
from UIAutomation.Page.browser.ActivationEntityShopWeb.ActivationEntityShopWebPage import ActivationEntityShopWebPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke004SQL import delete_entity_shop
from UIAutomation.Utils import stop_android_appium, get_user_id

__author__ = 'CaoYong'


class FuncSmoke005(BaseTestCase):
    """
        激活实体店
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        self.mobile = 18888000130
        self.admin = get_user_id(self.mobile)
        self.password = 123456
        # self.path = '/Users/cy/Downloads/test1107.xlsx'
        self.path = "F:/test1107.xlsx"
        # if is_run_ios()
        #     self.path = '/Users/cy/Downloads/test1107.xlsx'
        # else:
        #     self.path = 'c:/'

        sleep(2)
        # 浏览器的Driver
        self.browser = browser_web_driver.Firefox()
        sleep(1)
        # delete_entity_shop(self.admin)
        sleep(2)
        # LoginPage(self.driver).login(self.mobile, self.password)  # 登录
        # LongCardPage(self.driver).click_expected_card(self.admin, '激活实体店')

    def tearDown(self):
        self.browser.quit()
        ExitAppPage(self.driver).logout_app()
        stop_android_appium()

        pass

    def test_fun_smoke(self):
        # ActivationEntityShopPage(self.driver).entity_shop_input_information()
        # sleep(1)
        # ActivationEntityShopButtonPage(self.driver).go_import()
        ImportHistoricalOrderPage(self.browser).web_historical_order(self.mobile, self.password)
        sleep(3)
        ActivationEntityShopWebPage(self.browser).web_input_activation_entity_shop(self.path)
        sleep(2)

        pass


