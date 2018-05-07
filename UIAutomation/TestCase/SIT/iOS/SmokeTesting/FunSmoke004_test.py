from time import sleep

from appium import webdriver as app_web_driver
from selenium import webdriver as browser_web_driver

from UIAutomation.Page.Mobile.iOS.ActivationCommodity.ActivationCommodityPage import ActivationCommodityPage
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeLeft
from UIAutomation.Page.browser.ActivationCommodityWeb.ActivationCommodityWebPage import ActivationCommodityWebPage
from UIAutomation.Page.browser.LoginPage.BrowserLoginPage import BrowserLoginPage
from UIAutomation.Page.browser.web_page.LoginPage import LoginPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.iOS.Sprint1.SitSprint1Full001SQL import delete_commodity
from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_android_appium, stop_ios_appium

__author__ = 'caoyong'


class FuncSmoke004(BaseTestCase):
    """
        激活商品
    """
    def setUp(self):
        self.user_id = 18888000161
        self.password = 123456
        self.path = '/Users/cy/Downloads/correct-test07.zip'
        # self.path = '/Users/cy/Downloads/test001.zip'
        self.udid = get_ios_udid()
        # sleep(3)
        # stop_ios_appium()
        # sleep(2)
        # start_ios_appium(self.udid)
        # 连接ios设备
        # self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone 6', 'device': 'iOS',
        #                      'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        # self.driver = app_web_driver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        # 浏览器的Driver
        self.browser = browser_web_driver.Firefox()

        # sleep(3)
        # delete_commodity(self.admin)

        # LoginPage(self.driver).login(self.user_id, self.password)  # 登录
        # sleep(2)
        # CardPage(self.driver).click_card_one()  # 卡片1

    def tearDown(self):
        # self.driver.quit()
        self.browser.quit()
        # stop_android_appium()
        pass

    def test_fun_smoke(self):
        # SwipeLeft(self.driver)
        # TaskCenterPage(self.driver).activation_commodity()
        self.browser.get("http://192.168.6.31/login")
        self.browser.maximize_window()
        BrowserLoginPage(self.browser).login(self.user_id, self.password)
        sleep(3)
        # ActivationCommodityWebPage(self.browser).web_input_activation_commodity(self.path)
        sleep(5)
        # ActivationCommodityPage(self.driver).import_commodity()
        pass


