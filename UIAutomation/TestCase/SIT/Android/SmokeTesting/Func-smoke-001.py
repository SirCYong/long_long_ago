# -*- coding: utf-8 -*-
# language:zh-CN
import unittest
from appium import webdriver

from UIAutomation.Utils import stop_android_appium, start_android_appium, get_android_udid
from UIAutomation.Page.Mobile.Android.StartLoginPage import StartLogin
from UIAutomation.Page.Mobile.Android.TaskCenterPage import SelectTypeBox


class FuncSmoke001(unittest.TestCase):
    def setUp(self):
        self.user_id = 199289
        self.password = 1
        stop_android_appium()
        self.udid = get_android_udid()
        print(self.udid)
        self.desired_caps = {}
        self.desired_caps = dict(platformName='Android', version='5.1.1', deviceName='%s' % self.udid,
                                 appPackage='com.iscs.mobilewcs', appActivity='.activity.test.TextActivity',
                                 unicodeKeyboard='True', resetKeyboard='True')
        start_android_appium(self.udid)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        StartLogin(self.driver).get_start_login(self.user_id, self.password)

    def tearDown(self):
        self.driver.quit()
        stop_android_appium()

        pass

    def test_fun_smoke(self):
        SelectTypeBox(self.driver).activation_depot()
        pass

if __name__ == '__main__':
    unittest.main()
