# -*- coding: utf-8  -*-
"""
Author:Cy
增加银行卡
"""
from time import sleep

from appium import webdriver

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeLeft
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium


class FunSetBusinessFramework001(BaseTestCase):
    def setUp(self):
        self.user_id = 18888000071
        self.password = 123456
        self.admin = 199795
        self.udid = get_ios_udid()
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone 6', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(self.user_id, self.password)
        print (self.driver.page_source)
        print(self.driver.current_context)
        # CardPage(self.driver).click_long_card()
        # 恢复数据（sql）

        pass

    def tearDown(self):
        # self.driver.quit()
        stop_ios_appium()
        pass

    def test_commodity_shows(self):
        SwipeLeft(self.driver)
        ExitAppPage(self.driver).logout_app()
        # TaskCenterPage(self.driver).task_commodity_show()
        pass

