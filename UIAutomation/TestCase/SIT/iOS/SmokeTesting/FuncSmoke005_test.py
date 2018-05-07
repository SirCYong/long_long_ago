from time import sleep

from appium import webdriver as app_web_driver
from selenium import webdriver as browser_web_driver

from UIAutomation.Page.Mobile.ActivationEntityShop.ActivationEntityShopButtonPage import \
    ActivationEntityShopButtonPage
from UIAutomation.Page.Mobile.Android.ActivationEntityShop import ActivationEntityShopPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.TaskCenter import TaskCenterPage
from UIAutomation.Page.Mobile.iOS.ActivationCommodity.ActivationCommodityPage import ActivationCommodityPage
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeLeft
from UIAutomation.Page.browser.ActivationEntityShopWeb.ActivationEntityShopWebPage import ActivationEntityShopWebPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke004SQL import delete_entity_shop
from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium, stop_android_appium

__author__ = 'caoyong'


class FuncSmoke005(BaseTestCase):
    """
        激活实体店
    """
    def setUp(self):
        self.user_id = 18888000003
        self.admin = 199289
        self.password = 123456
        self.path = '/Users/cy/Downloads/test1107.xlsx'
        self.udid = get_ios_udid()
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = app_web_driver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(2)
        # 浏览器的Driver
        self.browser = browser_web_driver.Firefox()
        sleep(1)
        delete_entity_shop(self.admin)
        sleep(2)
        LoginPage(self.driver).login(self.user_id, self.password)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1

    def tearDown(self):
        self.browser.quit()
        self.driver.quit()
        stop_android_appium()

        pass

    def test_fun_smoke(self):
        SwipeLeft(self.driver)
        TaskCenterPage(self.driver).activation_entity_shop()
        ActivationEntityShopPage(self.driver).entity_shop_input_information()
        sleep(1)
        self.browser.get("http://192.168.6.31/login")
        self.browser.maximize_window()
        ActivationEntityShopButtonPage(self.driver).go_import()
        # browser_login_page(self.browser).login(self.user_id, self.password)
        sleep(3)
        ActivationEntityShopWebPage(self.browser).web_input_activation_entity_shop(self.path)
        sleep(2)
        ActivationCommodityPage(self.driver).import_commodity()
        sleep(20)
        pass


