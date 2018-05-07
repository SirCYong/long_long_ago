# -*- coding: utf-8 -*-
# language:zh-CN
import unittest
import requests
from time import sleep
from appium import webdriver

from UIAutomation.Utils import get_android_udid, start_android_appium, stop_android_appium, get_elements
from UIAutomation.Page.Mobile.Android.Register.follow import FollowPage
from UIAutomation.Page.Mobile.Android.Register.RegisterPage import RegisterPage
from UIAutomation.TestCase.SIT.Android.Sprint1.sql import setFirstOne, setSQlDelete_common

"""
    注意：此脚本适用于华为手机，型号，P8-Max
    Android全流程：
        1.前期(App已下载)Team3流程介入：发送注册链接至Michael.stack微信上

        点击微信链接，进入App，开始进行注册信息录入

        2.流程：当用户打开App后，通过点击微信登录，进入微信后，点击授权登录，之后，进入完善信息界面
       跑完善信息流程
"""
class FUNC1845(unittest.TestCase):
    def setUp(self):
        stop_android_appium()
        self.udid = get_android_udid()
        print(self.udid)
        self.desired_caps = {
            'platformName': 'Android',
            'version': '5.1.1',
            'deviceName': '%s'% self.udid,
            'appPackage': 'com.iscs.mobilewcs',
            'appActivity': 'com.iscs.mobilewcs.activity.base.LauncherActivity',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True'
        }
        start_android_appium(self.udid)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(30)

        setFirstOne()  # 还原task库注册信息
        sleep(1)
        setSQlDelete_common()  # 还原BASIC库注册信息
        '''
                Team3组开始
                进行授权服务邀请：进入App后，点击伟大的三组button，进入界面后，输入10000243;点击登录
                进入界面，点击服务认证邀请，进入邀请好友界面，点击选择好友BUTTON，选择张三，点击邀请button,
                跳入微信，选择折耳喵，点击分享，点击返回网仓三号，点击退出。完成
            '''
        PageFollow = FollowPage(self.driver)
        PageFollow.click_team_three_btn_element()  # 点击伟大的三组button
        sleep(1)
        PageFollow.click_login_input_element()  # 进入界面后，输入10000243
        sleep(1)
        PageFollow.click_login_btn_element()  # 点击登录
        # 服务认证邀请
        LinearLayout = get_elements(self.driver, ("CLASS_NAME", "android.widget.LinearLayout"))
        LinearLayout[3].click()
        PageFollow.click_select_friend_btn_element()  # 选择好友
        sleep(1)
        # 选择测试账号
        Invite_Button = get_elements(self.driver, ("CLASS_NAME", "android.widget.Button"))
        Invite_Button[1].click()
        sleep(2)
        # 跳转至微信界并点击人物
        self.driver.tap([(240, 590)], 500)
        sleep(2)
        # 点击分享按钮
        self.driver.tap([(870, 1190)], 500)
        sleep(4)
        # 留在微信
        self.driver.tap([(820, 1155)], 500)
        sleep(2)
        # 点击测试账号
        self.driver.tap([(540, 260)], 500)
        sleep(3)
        # 点击邀请链接
        self.driver.tap([(561, 403)], 500)
        sleep(5)
        # 点击下载客户端右边按钮 105
        self.driver.tap([(1015, 120)], 100)
        sleep(2)
        # 点击在浏览器中打开 -->跳入网仓三号
        self.driver.tap([(900, 700)], 500)
        sleep(2)
        pass

    """
    当手机有网络时，用户点击本国国家标码中国，输入手机号，点击获取验证码按钮且输入收到验证码，点击下一步进入待审核页面
    """

    def test_login_three_NextStepFive(self):
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

    def tearDown(self):
        stop_android_appium()
        print("释放资源！")
        pass

    """
    当手机处于在有网状态时，用户点击美国标码，输入中国手机号，点击获取验证码按钮，验证码无法收到，提示手机号码与国标不匹配
    """
    def test_login_three_NextStep(self):
        RegisterPage(self.driver).Click_WebChatLoginBtn_element()
        #  微信登录
        sleep(2)
        self.driver.tap([(500, 990)], 500)
        sleep(2)
        Page_Register = RegisterPage(self.driver)
        Page_Register.Click_NameTextInput_element()  # 真实姓名：
        sleep(2)
        Page_Register.Click_IDCardNumText_element()  # 输入身份证
        sleep(2)
        Page_Register.Click_PhotographBtn_element()  # 点击拍照认证
        image_views = get_elements(self.driver, ("CLASS_NAME", "android.widget.ImageView"))   # 点击照相按钮
        image_views[7].click()
        sleep(2)
        self.driver.tap([(965, 15)], 500)  # 点击勾
        sleep(1)
        Page_Register.Click_DoneBtn_element() # 点击应用该头像
        sleep(1)
        Page_Register.Click_NextStepBtn1_element() # 点击下一步
        sleep(1)
        Page_Register.Click_ChooseCountryCodeBtn_element() # 点击国家标码
        self.driver.tap([(530, 1220)], 500)  # 点击 USA 码
        Page_Register.Click_MobilePhoneInputText_element()  # 输入手机号152-6850-9694
        sleep(1)
        Page_Register.Click_VerifyBtn_element()  # 点击获取验证码
        sleep(1)
        try:
            # 调用接口，返回数据进行判断
            self.url = "http://192.168.200.136:8080/base/register/verifyCodeSms"
            parameter = {"mobile": "15268509694"}
            self.request = requests.post(self.url, json=parameter)
            self.values = self.request.json()
            if self.values['code'] == '0':
                # 在验证码栏位中输入错误验证码
                Page_Register.Click_VerifyCodeText_element_Error()
                print("Testing:短信已收到，输入错误验证码！")
                Page_Register.Click_NestStepBtn2_element()  # 点击下一步
                sleep(1)
            # 点击获取验证码按钮
            else:
                print("Testing:接口出错，无法发出json请求！")
        except Exception as e:
            print(e)
            pass
    """
    当手机处于无网状态时，用户对其进行点击时，提示无网络
    """
    def test_login_three_NextStepTwo(self):
        RegisterPage(self.driver).Click_WebChatLoginBtn_element()
        #  微信登录
        sleep(2)
        self.driver.tap([(500, 990)], 500)
        sleep(2)
        Page_Register = RegisterPage(self.driver)
        self.driver.mobile.set_network_connection(self.driver.mobile.AIRPLANE_MODE)
        sleep(5)
        Page_Register.Click_NameTextInput_element()  # 真实姓名：
        sleep(1)
        Page_Register.Click_IDCardNumText_element()  # 输入身份证
        sleep(1)
        Page_Register.Click_PhotographBtn_element()   # 点击拍照认证
        sleep(1)
        #  摄像头按钮
        image_views = get_elements(self.driver, ("CLASS_NAME", "android.widget.ImageView"))
        image_views[7].click()
        sleep(1)
        self.driver.tap([(965, 15)], 500)   # 点击勾
        sleep(1)
        Page_Register.Click_DoneBtn_element()
        sleep(1)
        Page_Register.Click_NextStepBtn1_element()
        #  提示无网络
        pass
    """
     当手机无网络时，用户点击本国国家标码中国，输入手机号，点击获取验证码按钮且验证码无法收到，再次点击获取验证码，提示无网络
    """
    def test_login_three_NextStepFore(self):
        RegisterPage(self.driver).Click_WebChatLoginBtn_element()
        #  微信登录
        sleep(2)
        self.driver.tap([(500, 990)], 500)
        sleep(2)

        Page_Register = RegisterPage(self.driver)
        Page_Register.Click_ChooseCountryCodeBtn_element()  # 点击获取国家表码
        self.driver.tap([(690, 860)], 500)  # 点击中国码
        Page_Register.Click_NameTextInput_element()  # 真实姓名：
        sleep(2)
        Page_Register.Click_IDCardNumText_element()  # 输入身份证
        sleep(2)
        Page_Register.Click_PhotographBtn_element()  # 点击拍照认证
        sleep(1)
        # 点击照相按钮
        self.driver.tap([(550, 1660)], 500)
        sleep(1)
        self.driver.tap([(1012, 72)], 500)
        # 完成
        sleep(2)
        self.driver.tap([(813, 137)], 500)
        sleep(2)
        Page_Register.Click_DoneBtn_element()
        sleep(1)
        Page_Register.Click_NextStepBtn1_element()
        sleep(1)
        # 输入手机号
        Page_Register.Click_MobilePhoneInputText_element()
        sleep(1)
        # 点击获取验证码
        Page_Register.Click_VerifyBtn_element()
        sleep(1)
        # 调用接口，返回数据进行判断
        try:
            self.url = "http://192.168.200.136:8080/base/register/verifyCodeSms"
            parameter = {"mobile": "15268509694"}
            self.request = requests.post(self.url, json=parameter)
            self.values = self.request.json()
            if self.values['code'] == '0':
                # 在验证码栏位中输入错误验证码
                Page_Register.Click_VerifyCodeText_element_Error()
                print("Testing:短信已收到，输入错误验证码！")
                Page_Register.Click_NestStepBtn2_element()  # 点击下一步
                sleep(1)
            else:
                print("Testing:接口出错，无法发出json请求！")
                Page_Register.Click_VerifyBtn_element()  # 点击再次获取验证码
                print("系统提示无网络")
        except Exception as e:
            print(e)
        pass

