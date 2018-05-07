# -*- coding:utf-8 -*-

import unittest

from appium import webdriver

from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.Sprint3Page.Sorting.SortingPage import SortingPage
from UIAutomation.Page.Mobile.iOS.Sprint3Page.WarehouseTask import WarehouseTask
from UIAutomation.TestCase.SIT.iOS.Sprint3.FunSorting001QSL import restore_sorting

__author__ = 'LiYu'
""" 功能：分拣"""


class FunSorting001(unittest.TestCase):

    def setUp(self):
        # 恢复分拣数据
        restore_sorting()
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=10000214, password=123456)
        pass

    def test_full2573(self):
        WarehouseTask(self.driver).click_sorting()
        SortingPage(self.driver).click_sorting_task()
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass
