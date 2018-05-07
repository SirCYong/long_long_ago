# -*- coding: utf-8 -*-
# language:zh-CN
from time import sleep

from appium import webdriver

from common.common_method.appium.get_udid import get_android_udid
from common.common_method.appium.start_appium import start_android_appium
from common.page.Mobile.Android.Login.LoginPage import LoginPage


class SamSungMobile:

    def __init__(self):
        pass

    def setMobile(self):
        self.udid = get_android_udid()
        self.desired_caps = {
            'platformName': 'Android',
            'version': '5.1',
            'deviceName': '%s' % self.udid,
            'appPackage': 'com.iscs.mobilewcs',
            'appActivity': '.activity.test.TextActivity',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True'
        }
        start_android_appium(self.udid)
        self.driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', self.desired_caps)
        #  第一步，点击微信登录
        Login =  LoginPage(self.driver)
        #
        Login.WeiChat_login()
        sleep(1)
        self.driver.tap([(500, 990)], 500)
        sleep(1)
        #  跳转至前往微信登录界面
        Login.Go_WeiChat()
        sleep(1)
        # 点击第一个人
        self.driver.tap([(600, 315)], 500)
        sleep(1)
        # 点击邀请链接
        self.driver.tap([(450, 505)], 500)
        sleep(1)
        # 点击更多
        self.driver.tap([(1010, 135)], 500)
        sleep(1)
        # 在浏览器中打开
        self.driver.tap([(167, 1445)], 500)
        sleep(1)
        # 跳转至网仓App,并点击微信登录
        Login.WeiChat_login()
        sleep(1)
        self.driver.tap([(500, 990)], 500)
        sleep(1)
        pass