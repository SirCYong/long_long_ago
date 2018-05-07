# coding=utf-8
from time import sleep
from unittest import TestCase
from selenium import webdriver

from UIAutomation.Page.Mobile.LoginPage import LoginPage


class Test(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    def test_activation_commodity_web(self, user_id=18888000002, password=123456):
        self.driver = webdriver.Firefox()
        self.driver.get("http://cit.iscs.com.cn/login")
        self.driver.maximize_window()
        LoginPage(self.driver).login(user_id, password)
        sleep(3)
        a = self.driver.find_elements_by_xpath("//p[contains(text(),'激活商品')]")
        print (type(a))
        print (len(a))
        print (a[0].text)
        a[0].click()
        sleep(5)
        # print (a[1].text)
        # print (a[2].text)

        pass