import os
from time import sleep
from selenium import webdriver
from UIAutomation.Page.browser.web_page.LoginPage import LoginPage
from UIAutomation.Page.browser.web_page.MainCard import MainCard
from UIAutomation.Page.browser.web_page.SelectTime import SelectTimePage
from UIAutomation.Page.browser.web_page.UploadFile import UploadFile
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

__author__ = 'LiYu'
""" 功能：完善运输契约 """


class FunTransportContract(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://192.168.6.32/login")
        LoginPage(self.driver).login(username='17767205508', password='123456')

    def test_import_contract(self):
        # 点击完善运输契约长期卡片
        MainCard(self.driver).click_transport_contract()
        sleep(2)
        # 点击请选择上传文件
        up_file = UploadFile(self.driver)
        up_file.click_file()
        os.system("D:\\test\\完善运输契约_圆通2.exe")
        sleep(5)
        up_file.assert_import_success()
        # 点击关闭操作
        sleep(10)
        up_file.click_close()
        pass

    def tearDown(self):
        self.driver.quit()
        pass
