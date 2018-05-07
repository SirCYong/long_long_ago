# -*- coding: utf-8  -*-


from time import sleep
from appium import webdriver
from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium
from UIAutomation.Page.Mobile.iOS.LaborDemand.MagePage import MainPage
from UIAutomation.Page.Mobile.iOS.LaborDemand.SelectTime import SelectTime
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.ReleaseWarehouseSupplies.ReleaseWarehouseSupplies import ReleaseWarehouse
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke009SQL import release_storage_supply, select_storage_supply
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
__author__ = 'LiYu'
""" 功能：发布仓储供应"""


class FunSmoke009(BaseTestCase):

    def setUp(self):
        username = 15399999999  # user=199310
        password = 123456
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
        LoginPage(self.driver).login(username=username, password=password)
        main_page = MainPage(self.driver)
        # 登录后手机桌面空白卡片
        main_page.click_empty_card()
        main_page.assert_release_warehouse()
        pass

    def test_full2246(self):
        # 点击发布仓储供应的任务
        MainPage(self.driver).click_release_warehouse()
        # 选择行业，吞吐量，价格，面积
        warehouse = ReleaseWarehouse(self.driver)
        warehouse.click_storage_supply()
        # 选择时间
        SelectTime(self.driver).click_confirm()
        warehouse.assert_immediately_release()
        # 点击立即发布
        warehouse.click_immediately_release()
        select_storage_supply()
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass
