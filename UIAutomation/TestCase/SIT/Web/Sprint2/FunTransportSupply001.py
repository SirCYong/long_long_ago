# -*- coding: utf-8 -*-
# language:zh-CN
import os
import unittest
from time import sleep
from selenium import webdriver

from UIAutomation.Page.browser.web_page.LoginPage import LoginPage
from UIAutomation.Page.browser.web_page.MainCard import MainCard
from UIAutomation.Page.browser.web_page.SelectTime import SelectTimePage
from UIAutomation.Page.browser.web_page.UploadFile import UploadFile
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke010SQL import release_transport_supply

__author__ = 'LiYu'
""" 功能：发布运输供应"""


class FunTransportSupply001(BaseTestCase):
    def setUp(self):
        self.username = 17767205508
        self.password = 123456
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://192.168.6.32")
        # 登录
        LoginPage(self.driver).login(self.username, self.password)

    def test_full(self):
        MainCard(self.driver).click_button()
        sleep(2)
        up_file = UploadFile(self.driver)
        up_file.click_file()
        sleep(2)
        # 通过AutoIt操作导入
        os.system("D:\\test\\test.exe")
        sleep(5)
        select_time_page = SelectTimePage(self.driver)
        # 跳转
        select_time_page.assert_import_information()
        # 选择时间
        select_time_page.click_start_time()

    def tearDown(self):
        self.driver.quit()
        pass
