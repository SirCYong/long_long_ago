# -*- coding: utf-8 -*-
# language:zh-CN
import unittest
import requests
from time import sleep
from appium import webdriver

from UIAutomation.Utils import get_android_udid, start_android_appium, stop_android_appium
from UIAutomation.Page.Mobile.Android.Login.LoginPage import LoginPage
from UIAutomation.Page.Mobile.Android.Register.RegisterPage import RegisterPage


class FunSmokeLogin(unittest.TestCase):
    def setUp(self):
        stop_android_appium()
        self.udid = get_android_udid()
        print(self.udid)
        start_android_appium(self.udid)
        self.desired_caps = {
            'platformName': 'Android',
            'version': '4.4.2',
            'deviceName': '%s' % self.udid,
            'appPackage': 'com.iscs.mobilewcs',
            'appActivity': '.com.iscs.mobilewcs.activity.base.LauncherActivity',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities={})
        self.driver.wait_activity('com.iscs.mobilewcs.activity.base.LauncherActivity', 10)


        #  第一步，点击微信登录
        # Login = LoginPage(self.driver)
        LoginPage(self.driver).WeiChat_login()
        sleep(1)
        self.driver.tap([(500, 990)], 500)
        sleep(1)
        #  跳转至前往微信登录界面
        LoginPage(self.driver).Go_WeiChat()
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
        LoginPage(self.driver).WeiChat_login()
        sleep(1)
        self.driver.tap([(500, 990)], 500)
        sleep(1)
        pass

    def tearDown(self):
        stop_android_appium()
        print("释放资源！")
        pass

    def testNextStepFive(self):

        RegisterPage(self.driver).Click_WebChatLoginBtn_element()
        #  微信登录
        sleep(2)
        self.driver.tap([(500, 990)], 500)
        sleep(2)
        # 点击获取国家表码
        Page_Register = RegisterPage(self.driver)
        Page_Register.Click_ChooseCountryCodeBtn_element()

        Page_Register.Click_NameTextInput_element()  # 真实姓名：
        sleep(2)
        Page_Register.Click_IDCardNumText_element()  # 输入身份证
        sleep(2)
        Page_Register.Click_PhotographBtn_element()  # 点击拍照认证
        sleep(2)
        # 点击照相按钮
        self.driver.tap([(550, 1660)], 500)
        sleep(1)
        self.driver.tap([(1012, 72)], 500)
        # 完成
        self.driver.tap([(813, 137)], 500)
        sleep(2)
        Page_Register.Click_DoneBtn_element()
        sleep(1)
        Page_Register.Click_NextStepBtn1_element()
        sleep(1)
        Page_Register.Click_MobilePhoneInputText_element()  # 输入手机号
        sleep(3)
        Page_Register.Click_VerifyBtn_element()  # 点击获取验证码
        sleep(1)
        try:
            self.url = "http://192.168.200.136:8080/base/register/verifyCodeSms"  # 调用接口，返回数据进行判断
            parameter = {"mobile": "15268509694"}
            self.request = requests.post(self.url, json=parameter)
            self.values = self.request.json()
            if self.values['code'] == '0':
                # 在验证码栏位中输入错误验证码
                Page_Register.Click_VerifyCodeText_element_Error()
                print("Testing:输入错误验证码！")
                Page_Register.Click_NestStepBtn2_element()  # 点击下一步
                sleep(3)
            # 点击获取验证码按钮
            else:
                print("Testing:接口出错，无法发出json请求！")
                Page_Register.Click_VerifyBtn_element()  # 点击再次获取验证码
                print("系统提示无网络")
                # 当完善信息完成后，开始对下一步细节开始对接
                # 编写sql 查看用户是否已经对
        except Exception as e:
            print(e)
        pass


if __name__ == '__main__':
    unittest.main()


