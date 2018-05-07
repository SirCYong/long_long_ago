# -*- coding: utf-8  -*-
"""
Author:Yuetianzhuang
注册供应商
"""
import unittest
from time import sleep

from appium import webdriver

from UIAutomation.Page.Mobile.RegisteredSuppliers import RegisterSuppliersPage
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium, is_element_present


class FunRegisterSuppliers001(unittest.TestCase):

    def setUp(self):
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone 6 Plus',
                             'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal',
                             'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        # 登录
        LoginPage(self.driver).login(username=13311112222, password=123456)
        # 登录后手机桌面空白卡片
        CardPage(self.driver).click_card_one()
        sleep(1)
        assert is_element_present(self.driver,('ACCESSIBILITY_ID', '注册供应商'))
        pass

    def test_FunRegisterSuppliers001(self):

        supplier_register = RegisterSuppliersPage(self.driver)
        # 注册供应商必要信息填写
        supplier_register.input_required()
        #  # 注册供应商选填信息——接单人
        supplier_register.single_person()
        #  # 注册供应商选填信息——对账人
        supplier_register.reconciliation()
        #  # 注册供应商选填信息——付款人
        supplier_register.pay_person()
        # 点击注册
        supplier_register.register()
        pass

    def tearDown(self):
        self.driver.close()
        stop_ios_appium()
        pass
