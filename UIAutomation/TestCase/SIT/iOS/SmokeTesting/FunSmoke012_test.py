import os
import unittest
from time import sleep
from selenium import webdriver

from UIAutomation.Page.browser.LoginPage import BrowserLoginPage
from UIAutomation.Page.browser.PublishGoodsSupply.GoodsSupplyPage import GoodsSupplyPage
from UIAutomation.TestCase.SIT.Web.Sprint2.FUN_GoodsSupply import RestoreSQL
__author__ = 'yuetianzhuang'


class FunSmoke012(unittest.TestCase):
    """
    PC 端发布供货供应
    """
    def setUp(self):
        self.username = 100188
        self.password = 123
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        RestoreSQL()  # 还原数据
        self.driver.get("http://192.168.6.31/login")
        sleep(1)
        BrowserLoginPage(self.driver).login('199265', '1')
        pass

    def test_full(self):
        goods_supply = GoodsSupplyPage(self.driver)
        # 点击卡片
        goods_supply.card()
        sleep(2)
        # 调用写的exe文件
        os.system("F:\\TeseCase\\UploadFilesChrome.exe")
        sleep(3)
        # #判断输出条输出为导入成功还是导入失败
        dd = self.driver.find_element_by_xpath("html/body/div[2]/div/ui-view/div/div[2]/div/div[3]/div/div[4]/div/p").text
        if dd == u'导入失败':
            goods_supply.click_reImport()  # 点击重新上传
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
        self.driver.quit()
        pass
