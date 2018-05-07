# -*- coding: utf-8 -*-
from appium import webdriver

from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.Page.Mobile.iOS.GenerateBill.GenerateBillPage import GenerateBillPage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Android.Sprint7.FUNGenerateBillSQL import resume_generate_bill

__author__ = 'XuWangchao'

""" 功能：生成应付账单 """


class Fun001StorageInventory(BaseTestCase):

    def setUp(self):
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        resume_generate_bill()
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=13544443600, password=123456)
        pass

    def test_generate_bill(self):
        CardPage(self.driver).click_generate_bill()
        GenerateBillPage(self.driver).get_element_from_sql()            # 根据SQL验证"生成账单"页面元素是否存在
        GenerateBillPage(self.driver).click_generate_bill_button()      # 点击"生成应付账单"按钮
        GenerateBillPage(self.driver).assert_generate_bill_result()     # 从SQL中验证结果
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass
