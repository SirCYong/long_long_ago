# -*- coding: utf-8 -*-
# language:zh-CN
# Author:liyu
# 功能：导入库位库存
import os
from time import sleep
from selenium import webdriver

from UIAutomation.Page.browser.web_page.LoginPage import LoginPage
from UIAutomation.Page.browser.web_page.MainCard import MainCard
from UIAutomation.Page.browser.web_page.SelectTime import SelectTimePage
from UIAutomation.Page.browser.web_page.UploadFile import UploadFile
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Web.Sprint4.FunImportInventorySQL import release_import_inventory
from UIAutomation.TestCase.SIT.Web.Sprint6.FunImportINventorySQL import select_import_inventory


class FunImportInventory(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://192.168.6.32/login')
        # 登录
        LoginPage(self.driver).login(username='17767205508', password='123456')

    # 导入正确模板
    def test_right_template(self):
        MainCard(self.driver).click_import_inventory()
        sleep(2)
        up_file = UploadFile(self.driver)
        up_file.click_file()
        os.system("D:\\test\\importinventory.exe")
        sleep(2)
        up_file.assert_import_success()
        # 关闭操作
        SelectTimePage(self.driver).click_close()
        select_import_inventory()
        pass

    # 导入错误类型模板
    def test_wrong_template(self):
        MainCard(self.driver).click_import_inventory()
        sleep(2)
        up_file = UploadFile(self.driver)
        up_file.click_file()
        os.system("D:\\test\\test.exe")
        sleep(5)
        up_file.assert_import_fail()
        # 点击重新导入操作
        SelectTimePage(self.driver).click_re_import()
        self.test_right_template()

    def tearDown(self):
        self.driver.quit()
        pass
