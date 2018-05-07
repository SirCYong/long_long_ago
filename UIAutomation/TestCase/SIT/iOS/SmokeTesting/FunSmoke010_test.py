# -*- coding: utf-8 -*-
# language:zh-CN
"""
Author:liyu
"""
# 功能：发布运输供应
import os
from time import sleep
from selenium import webdriver

from UIAutomation.Page.browser.web_page.LoginPage import LoginPage
from UIAutomation.Page.browser.web_page.MainCard import MainCard
from UIAutomation.Page.browser.web_page.SelectTime import SelectTimePage
from UIAutomation.Page.browser.web_page.UploadFile import UploadFile
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

from .FunSmoke010SQL import release_transport_supply, select_transport_supply


class FunSmoke010(BaseTestCase):
    def setUp(self):
        sleep(10)
        # 恢复账号数据
        release_transport_supply()
        username = '18722236521'  # user=199161
        password = '123456'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://cit.iscs.com.cn")
        # 登录
        LoginPage(self.driver).login(username=username, password=password)
        pass

    def test_full(self):
        MainCard(self.driver).click_button()
        sleep(2)
        up_flile = UploadFile(self.driver)
        up_flile.click_file()
        sleep(2)
        # 通过AutoIt操作导入
        os.system("D:\\test\\test.exe")
        sleep(5)
        select_time = SelectTimePage(self.driver)
        select_time.click_start_time()
        select_time.assert_import_information()
        sleep(2)
        select_time.click_close()
        # 校验数据库
        select_transport_supply()
        sleep(5)

    def tearDown(self):
        self.driver.quit()
        pass
