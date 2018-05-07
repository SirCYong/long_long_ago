# -*- coding: utf-8 -*-
# language:zh-CN
# 功能：完善仓储契约
import os
import unittest
from time import sleep
from selenium import webdriver

from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.browser.web_page.MainCard import MainCard
from UIAutomation.Page.browser.web_page.PerfectWarehousingContract import PerfectWarehousingContract
from UIAutomation.Page.browser.web_page.UploadFile import UploadFile
from UIAutomation.TestCase.SIT.Web.Sprint6.PerfectWarehousingContractSQL import resume_perfect_warehousing_contract, \
    get_perfect_warehousing_contract_result

__author__ = "xuwangchao"


class FunImportInventory(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://cit.iscs.com.cn')
        resume_perfect_warehousing_contract()
        # 登录
        LoginPage(self.driver).login(username='13788881111', password='123456')

    def test_right_template(self):
        MainCard(self.driver).click_perfect_warehousing_contract()
        sleep(2)
        UploadFile(self.driver).click_file()
        os.system("C:\\uploadFile\\uploadWaContractTemplate.exe")
        sleep(2)
        PerfectWarehousingContract(self.driver).is_success()
        assert get_perfect_warehousing_contract_result() == 30
        pass

    def tearDown(self):
        self.driver.quit()

        pass
