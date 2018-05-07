# -*- coding: utf-8  -*-
"""
增加银行卡
"""
import unittest
from time import sleep

from appium import webdriver

from UIAutomation.Page.Mobile.TaskCenter import TaskCenterPage
from UIAutomation.Page.Mobile.iOS.BindBankCard.BindBankCardPage import BindBankCardPage
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium

__author__ = 'caoyong'


class FunSetBusinessFramework001(unittest.TestCase):
    def setUp(self):
        self.user_id = 13712345678
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
        CardPage(self.driver).click_long_card()
        # 恢复数据（sql）

        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass

    def test_operation_bind_bank(self):
        TaskCenterPage(self.driver).task_bind_bank_card()
        a = BindBankCardPage(self.driver)
        a.operation_bank_payment()
        a.operation_bank_verification(self.admin)
        pass
