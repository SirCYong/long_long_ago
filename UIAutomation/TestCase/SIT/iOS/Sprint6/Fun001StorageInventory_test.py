# -*- coding: utf-8 -*-

from time import sleep
from appium import webdriver
from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium
from UIAutomation.Page.Mobile.iOS.LaborDemand.MagePage import MainPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.LongTaskCards.LongTaskCardPage import LongTaskCardPage
from UIAutomation.Page.Mobile.iOS.StorageInventory.StorageInventoryPage import StorageInventoryPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

__author__ = 'LiYu'

""" 功能：入库上架 """


class Fun001StorageInventory(BaseTestCase):

    def setUp(self):
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS', \
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=17676769090, password=123456)
        pass

    def test_storage_inventory(self):
        # 登录后点击长期任务，进入长期任务卡片主界面
        main_page = MainPage(self.driver)
        main_page.click_long_card()
        sleep(15)
        long_task_page = LongTaskCardPage(self.driver)
        # 验证是否到长期任务主页面
        long_task_page.assert_long_card_page()
        # 点击入库上架
        w = ['PL00006', 'tz3228747110', '150', 'GS01005', 'tx7719tx7719010100', '100', 'GS01006']
        long_task_page.click_storage_inventory()
        storage_inventory = StorageInventoryPage(self.driver)
        storage_inventory.click_carton(carton=w[0])
        storage_inventory.click_inventory(outer_box_code=w[0], commodity_code=w[1], amount=w[2],\
                                          storage_code=w[3])
        storage_inventory.click_inventory(outer_box_code=w[0], commodity_code=w[4], amount=w[5],\
                                          storage_code=w[6])
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass
