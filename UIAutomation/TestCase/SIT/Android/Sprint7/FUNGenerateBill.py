# -*- coding: utf-8 -*-
# language:zh-CN
import unittest
from appium import webdriver

from UIAutomation.Utils import get_android_udid, stop_android_appium, start_android_appium
from UIAutomation.Page.Mobile.Android.GenerateBill.GenerateBillPage import GenerateBillPage
from UIAutomation.Page.Mobile.Android.Login.LoginPage import LoginPage
from UIAutomation.Page.Mobile.Android.CardListPage import CardPage
from UIAutomation.TestCase.SIT.Android.Sprint7.FUNGenerateBillSQL import resume_generate_bill
__author__ = "xuwangchao"


class FunSmokeLogin(unittest.TestCase):
    def setUp(self):
        stop_android_appium()
        self.udid = get_android_udid()
        # resume_generate_bill()
        print(self.udid)
        self.desired_caps = {
            'platformName': 'Android',
            'version': '5.1.1',
            'deviceName': '%s' % self.udid,
            'appPackage': 'com.iscs.mobilewcs',
            'appActivity': 'com.iscs.mobilewcs.activity.base.LauncherActivity',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True'
        }
        start_android_appium(self.udid)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        pass

    def test_next_step_five(self):
        LoginPage(self.driver).login(username='13544443600', password='123456')
        CardPage(self.driver).click_long_task()     # 登录后点击长期任务，进入长期任务卡片主界面
        CardPage(self.driver).flick_top_to_bottom()     # 从左往右滑动到"生成账单"卡片
        CardPage(self.driver).click_generate_bill()     # 点击"生成账单"卡片
        GenerateBillPage(self.driver).assert_generate_bill_sql()    # 根据SQL验证"生成账单"页面元素是否存在
        GenerateBillPage(self.driver).click_generate_bill_button()  # 点击"生成应付账单"按钮
        GenerateBillPage(self.driver).get_generate_bill_result_sql()    # 从SQL中验证结果
        pass

    def tearDown(self):
        self.driver.quit()
        stop_android_appium()
        print("释放资源~")
        pass
