from time import sleep
from unittest import TestCase
from appium import webdriver

from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium, is_element_present
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
__author__ = 'chenyanxiu'


class FUNLogin2_007(TestCase):
    """
    登陆密码错误
    """
    def setUp(self):
        self.user_id = 199357
        self.passwdus = 17444445555
        self.udid = get_ios_udid()
        print(self.udid)
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)

        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass

    def test_Login2_007(self):
        LoginPage(self.driver).login(username=self.passwdus, password=1236555)  # 登录
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '登录'))

