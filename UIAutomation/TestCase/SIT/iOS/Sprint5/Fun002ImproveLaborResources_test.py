# -*- coding: utf-8 -*-
from appium import webdriver

from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium
from UIAutomation.Page.Mobile.LoginPage.LoginPage import LoginPage
from UIAutomation.Page.Mobile.MainPage.MainPage import MainPage
from UIAutomation.Page.Mobile.PublishLabour.PublishLabour import PublishLabour
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

__author__ = 'LiYu'

"""功能：完善劳务资源"""


class Fun002ImproveLaborResources(BaseTestCase):

    def setUp(self):
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        # 登录
        LoginPage(self.driver).login(username=18877777777, password=111111)
        pass

    def test_continue_release(self):
        # 登录后点击长期任务卡片
        main_page = MainPage(self.driver)
        main_page.select_page()
        publish_labour = PublishLabour(self.driver)
        publish_labour.click_public_labor()
        pass

    def tearDown(self):
        self.driver.close()
        stop_ios_appium()
        pass
