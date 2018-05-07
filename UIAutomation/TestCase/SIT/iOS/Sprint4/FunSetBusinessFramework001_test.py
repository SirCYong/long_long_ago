"""
业务架构任务
"""
import unittest
from time import sleep

from appium import webdriver

from UIAutomation.Page.Mobile.TaskCenter import TaskCenterPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeLeft
from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium

__author__ = 'caoyong'


class FunSetBusinessFramework001(unittest.TestCase):
    def setUp(self):
        self.user_id = 18888000070
        self.password = 123456
        self.admin = 10000959
        self.udid = get_ios_udid()
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone 6', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(self.user_id, self.password)
        # CardPage(self.driver).click_card_one()
        # 恢复数据（sql）
        # delete_business_framework(self.admin)
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass

    def test_FunSetBusinessFramework001(self):
        SwipeLeft(self.driver)
        TaskCenterPage(self.driver).task_business_framework()
        sleep(2)
        # self.driver.find_element_by_accessibility_id("业务框架任务").click()
        pass

