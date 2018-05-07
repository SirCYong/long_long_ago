import unittest
from time import sleep

from appium import webdriver

from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.TestCase.SIT.iOS.Sprint1.SitSprint1Full001SQL import delete_depot_card
from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium

__author__ = 'caoyong'


class TestDepot(unittest.TestCase):
    """
        激活仓库
    """
    def setUp(self):
        self.admin = 199289
        self.udid = get_ios_udid()
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone 6', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        delete_depot_card(self.admin)
        LoginPage(self.driver).login(username=self.admin)  # 登录

        pass

    def tearDown(self):
        stop_ios_appium()
        pass

    def test_fun001(self):
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAScrollView[1]"
                                          "/UIACollectionView[1]/UIACollectionCell[2]").click()
        sleep(2)
        pass


