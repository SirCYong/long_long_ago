# -*- coding: utf-8 -*-
import unittest

from appium import webdriver

from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.Sprint3Page.Picking.PickingPage import PickingPage
from UIAutomation.Page.Mobile.iOS.Sprint3Page.WarehouseTask import WarehouseTask
from UIAutomation.TestCase.SIT.iOS.Sprint3.FunPicking001SQL import restore_picking

__author__ = 'LiYu'
""" 功能：拣选"""


class FunPicking001(unittest.TestCase):

    def setUp(self):
        # 恢复拣选数据
        restore_picking()
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
        WarehouseTask(self.driver).click_picking()
        PickingPage(self.driver).click_picking_task()

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass
