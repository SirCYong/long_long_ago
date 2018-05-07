# coding:utf-8
from time import sleep
from unittest import TestCase

from appium import webdriver

from UIAutomation.Utils import start_ios_appium, get_ios_udid, stop_ios_appium
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.page.Mobile.iOS.LoginPage import LoginPage


class AllProcess(TestCase):
    def setUp(self):
        self.user_id = 10000237
        self.invitee_id = 1111111003
        # 用户账号从10000297变为428, 从迭代二数据结构变化导致的老账号失效
        self.admin = 10000428
        sleep(3)
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        #self.get_ui_locator(self.driver)
        LoginPage(self.driver).login(username=self.admin)  # 登录
        CardPage(self.driver).click_card_one()  # 登入卡片一

        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass

    def test_step_by_step_valid(self):
        # 找劳务需求
        # 劳务领薪
        # 劳务收入确认
        # 找运输供应
        # 仓储需求
        # 劳务收入确认
        # 找仓储供应
        # 激活仓库
        # 激活实体店

        pass