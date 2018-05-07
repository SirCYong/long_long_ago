# -*- coding: utf-8 -*-
# language:zh-CN

# Author:yuetianzhuang
import os
import unittest
from time import sleep
from selenium import webdriver

from common.common_method.element.is_element_present import is_element_present
from common.page.browser.PublishGoodsSupply.GoodsSupplyPage import GoodsSupplyPage
from common.page.browser.web_page.login import LoginPage



class FunSmoke012(unittest.TestCase):
    def setUp(self):
        sleep(10)
        # 恢复账号数据
        username ='13588880000'
        password = '123456'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://cit.iscs.com.cn")
        # 登录
        LoginPage(self.driver).login(username, password)
        pass

    def test_full(self):
        assert is_element_present(self.driver, ('XPATH', 'html/body/div[1]/div/ui-view/div/div/ul/div[2]/div/li[4]'))
        goods_supply = GoodsSupplyPage(self.driver)
        # 点击卡片
        goods_supply.card()
        sleep(2)
        # 调用写的exe文件
        os.system("F:\\TeseCase\\UploadFilesChrome.exe")
        sleep(3)
        # #判断输出条输出为导入成功还是导入失败
        dd = self.driver.find_element_by_xpath("html/body/div[1]/div/ui-view/div/div[2]/div/div[3]/div/div[4]/div/p").text
        if dd == u'导入失败':
            goods_supply.click_reImport()  # 点击重新导入
            sleep(2)
            goods_supply.click_re_upload_file()
            sleep(2)
            os.system("F:\\TeseCase\\Uploadturefile.exe")
            sleep(5)
        elif dd == u'导入成功':
            sleep(2)
            print("文件导入成功！")
            pass

    def tearDown(self):
        pass
