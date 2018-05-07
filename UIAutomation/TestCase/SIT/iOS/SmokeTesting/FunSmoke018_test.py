# -*- coding: utf-8 -*-
"""
Description:注册供应商
__author__ = 'ytz'
"""
from time import sleep
from unittest import TestCase

from appium import webdriver

from UIAutomation.Page.Mobile.CardList.CommonCardPage import Common_Card_Page
from UIAutomation.Page.Mobile.RegisteredSuppliers import RegisterSuppliersPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke018SQL import Restore_RegisterSupplier_SQL
from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium, is_element_present


class FuncSmoke018(TestCase):
    def setUp(self):

        self.usr = 15511112222
        self.pwd = 123456
        # 删除数据
        Restore_RegisterSupplier_SQL()
        self.udid = get_ios_udid()
        print(self.udid)
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone6 Plus', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        LoginPage(self.driver).login(username=self.usr, password=self.pwd)  # 登录
        # 长期卡片
        Common_Card_Page(self.driver).click_long_task()
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '注册供应商'))

        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass

    def test_register_supplier(self):
        RegisterSupplier = RegisterSuppliersPage(self.driver)
        # 输入必填项
        RegisterSupplier.input_required()
        sleep(1)
        # 选填项--接单人
        RegisterSupplier.single_person()
        # 选填项--对账人
        RegisterSupplier.reconciliation()
        # 选填项--付款人
        RegisterSupplier.pay_person()
        # 点击付款
        assert is_element_present(self.driver, ['ACCESSIBILITY_ID', '注册'])
        RegisterSupplier.register()
        pass

