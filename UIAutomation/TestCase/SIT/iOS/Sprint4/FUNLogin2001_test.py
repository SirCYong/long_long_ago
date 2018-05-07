# -*- coding: utf-8 -*-
# author:chenyanxiu
# 登陆主流程
from time import sleep
from unittest import TestCase
from appium import webdriver

from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.TestCase.SIT.iOS.Sprint4.FUNLogin2SQL import login_state
__author__ = 'chenyanxiu'


class FUNLogin2_001(TestCase):
    def setUp(self):
        self.user_id = 199357
        self.passwdus = 17444445555
        self.udid = get_ios_udid()
        print(self.udid)
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)

        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass

    def test_Login2_001(self):
        LoginPage(self.driver).login(username=self.passwdus, password=123456)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        assert login_state(self.passwdus) == True
