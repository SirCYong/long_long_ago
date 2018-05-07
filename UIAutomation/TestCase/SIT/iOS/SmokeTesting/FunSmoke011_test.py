# -*- coding: utf-8  -*-
# language:zh-CN
"""
发布仓储需求
__author__= 'ytz'
"""
from time import sleep

from appium import webdriver

from UIAutomation.Page.Mobile.CardList.CommonCardPage import Common_Card_Page
from UIAutomation.Page.Mobile.PublishWarehouseDemand import PublishWarehouseDemandPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium, is_element_present
from .FunSmoke011SQL import FunSmoke011SQL


class FunSmoke011(BaseTestCase):

    def setUp(self):
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        FunSmoke011SQL()  # 恢复数据
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone 6 Plus',
                             'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal',
                             'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        # 登录
        LoginPage(self.driver).login(username=13311112222, password=123456)
        #  弹出确认绑定框
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '绑定')):
            PublishWarehouseDemandPage(self.driver).click_bd_btn()
        else:
            assert True
        # 登录后点击长期任务 滑动屏幕一次
        Common_Card_Page(self.driver).click_long_task()
        sleep(1)
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '发布仓储需求'))
        pass

    def test_fun_publish_ware_house_demand(self):

        Common_Card_Page(self.driver).click_ware_house_demand()
        sleep(1)
        # 点击'发发布仓储需求'卡片
        WareHouse = PublishWarehouseDemandPage(self.driver)
        # 点击选择行业、级别、日期、地点[包含在一个方法中]
        WareHouse.click_cross_border_button_ios()
        sleep(1)
        # 输入处理量和仓储面积
        WareHouse.click_processing_capacity_button_ios()
        sleep(1)
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '完成'))
        # 点击完成
        WareHouse.click_complete()
        pass

    def tearDown(self):
        stop_ios_appium()
        pass
