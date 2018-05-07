# -*- coding: utf-8  -*-
"""
Author:liyu
"""
import unittest
from time import sleep
from appium import webdriver

from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium, is_element_present

from UIAutomation.Page.Mobile.iOS.LaborDemand.MagePage import MainPage
from UIAutomation.Page.Mobile.iOS.LaborDemand.SelectTime import SelectTime
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.ReleaseWarehouseSupplies.ReleaseWarehouseSupplies import ReleaseWarehouse
from UIAutomation.TestCase.SIT.iOS.Sprint2.FunStorageSupply001SQL import release_storage_supply


class FunStorageSupply001(unittest.TestCase):

    def setUp(self):
        # 测试数据恢复
        release_storage_supply()
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        # 登录
        LoginPage(self.driver).login(username=199164)
        # 登录后手机桌面空白卡片
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAScrollView[1]/UIACollectionView[1]/UIACollectionCell[2]").click()
        sleep(2)
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '发布仓储供应'))
        pass

    def test_full2246(self):
        # 点击发布仓储供应的任务
        MainPage(self.driver).click_release_warehouse()
        # 选择行业，吞吐量，价格，面积
        warehouse = ReleaseWarehouse(self.driver)
        warehouse.click_storage_supply()
        # 选择时间
        SelectTime(self.driver).click_confirm()
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '立即发布'))
        # 点击立即发布
        warehouse.click_immediately_release()
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass
