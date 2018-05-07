# -*- coding: utf-8 -*-

from time import sleep
from appium import webdriver
from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium
from UIAutomation.Page.Mobile.iOS.LaborDemand.MagePage import MainPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.LongTaskCards.LongTaskCardPage import LongTaskCardPage
from UIAutomation.Page.Mobile.iOS.StoragePoint.StoragePointPage import StoragePointPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

__author__ = 'LiYu'
""" 功能：入库扫码点数 """


class Fun004StoragePoint(BaseTestCase):

    def setUp(self):
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=17676769090, password=123456)
        pass

    def test_tor_age_point(self):
        # 登录后点击长期任务，进入长期任务卡片主界面
        main_page = MainPage(self.driver)
        main_page.click_long_card()
        sleep(15)
        long_task_page = LongTaskCardPage(self.driver)
        long_task_page.assert_long_card_page()
        long_task_page.click_storage_point()
        storage_point = StoragePointPage(self.driver)
        # 扫码点数(无批次)
        q = ['PL00005', 'tz3228747110', 'tx7719tx7719010100', 1, 20160803]
        storage_point.click_storage_point_step(carton=q[0], commodity_code=q[1], amount=q[3])
        # 点击检查下一个
        storage_point.click_check_next()
        # 扫码点数(有批次号)
        storage_point.click_storage_point_batch(commodity_code=q[2], product_batch=q[4], amount=q[3])
        # 点击检查下一个
        storage_point.click_check_next()
        # 点击'完成检查'
        storage_point.click_complete_inspection()
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass
