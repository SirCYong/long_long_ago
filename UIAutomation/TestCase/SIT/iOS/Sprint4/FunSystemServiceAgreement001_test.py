# -*- coding: utf-8 -*-
"""
功能：签订系统服务契约并提交保证金
"""
import unittest
from time import sleep
from appium import webdriver

from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium, get_element
from UIAutomation.Page.Mobile.iOS.LaborDemand.MagePage import MainPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.SubmitDeposit.SubmitDeposit import SubmitDeposit
from UIAutomation.Page.Mobile.iOS.SystemServiceAgreement.SystemServiceAgreement import SystemServiceAgreement
__auhtor__ = 'liyu'


class FunSystemServiceAgreement001(unittest.TestCase):

    def setUp(self):
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=10000214, password=123456)
        pass

    def test_full2573(self):
        MainPage(self.driver).click_system_service()
        sleep(2)
        SystemServiceAgreement(self.driver).click_agreement()
        sleep(2)
        MainPage(self.driver).click_deposit()
        sleep(2)
        SubmitDeposit(self.driver).click_union_pay()
        # CIT测试环境  银联测试账号支付
        get_element(self.driver, ['ACCESSIBILITY_ID', '下一步']).click()
        sleep(2)
        get_element(self.driver, ['ACCESSIBILITY_ID', '免费获取']).click()
        edit_elements = self.driver.find_elements_by_class_name('UIATextField')
        edit_elements[-1].set_value("123456")
        sleep(2)
        get_element(self.driver, ['ACCESSIBILITY_ID', '完成']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '确认付款']).click()
        sleep(5)
        get_element(self.driver, ['ACCESSIBILITY_ID', '返回商户']).click()

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass
