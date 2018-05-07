# -*- coding: utf-8 -*-
from time import sleep
from unittest import TestCase
from appium import webdriver

from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium
from UIAutomation.Page.Mobile.iOS.CardListPage import CardList
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage

'''
    该任务为暂存任务,根据运单号获取到位置,根据更改位置判断该物品是否做到暂存需求;以及根据数据状态判断是否符合该需求场景
'''


class SitSprintFull001(TestCase):
    def setUp(self):
        self.admin = 10000214
        self.udid = get_ios_udid()
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone 6 Plus', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        LoginPage(self.driver).login(username=self.admin)  # 登录
        sleep(2)
        CardList(self.driver).click_long_task()  # 点击4个长期任务
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()

        pass

    def test_full(self):

        pass