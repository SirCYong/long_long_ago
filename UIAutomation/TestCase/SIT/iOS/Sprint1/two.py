# -*- coding: utf-8 -*-
from time import sleep
from unittest import TestCase

from nose.tools import assert_equal
from selenium import webdriver

from common.page.browser.web_page.login import LoginPage


def activation_commodity_web(admin=None, password=None):
    browser = webdriver.Firefox()
    browser.get("http://cit.iscs.com.cn/login")
    browser.maximize_window()
    LoginPage(browser).login(admin, password)
    sleep(3)
    try:
        a = browser.find_elements_by_xpath("//p[contains(text(),'激活商品')]")
        a[0].click()
        sleep(3)
        browser.find_element_by_xpath("//*[@id='data-ng-app']/body/div[1]/div/ui-view/div/div[2]/div/div[3]/div"
                                     "/div[1]/div[1]/div[1]/a/input").send_keys('/Users/cy/Downloads/correct-test07.zip')
        sleep(5)
        browser.find_elements_by_xpath("//p[contains(text(),'导入成功')]")
        browser.quit()
    except Exception as e:
        print (e)
        assert False, u'导入失败\n'

    pass


def test_play(admin=18888000003, password=123456):
    driver = webdriver.Firefox()
    driver.get("http://cit.iscs.com.cn/login")
    driver.maximize_window()
    LoginPage(driver).login(admin, password)
    sleep(3)



def test_run(self):
    # a = 'test001'+'.zip'
    # path = '\\/Users/cy/Downloads/' + a

    self.driver.find_element_by_xpath(".//*[@id='login-form']/aside/div/ul[1]/div[2]/input").send_keys(self.admin)
    self.driver.find_element_by_xpath(".//*[@id='login-form']/aside/div/ul[1]/div[3]/input").send_keys(self.password)
    self.driver.find_element_by_id("login-submit").click()
    sleep(5)
    # self.driver.find_element_by_xpath(".//*[@id='data-ng-app']/body/div[1]/div/ui-view/div/div/ul/div[2]"
    #                                   "/div/li[4]/p").click()
    self.driver.find_element_by_link_text("激活商品").click()
    sleep(3)
    self.driver.find_element_by_xpath(".//*[@id='data-ng-app']/body/div[1]/div/ui-view/div/div[2]/div/div[3]"
                                      "/div/div/div[1]/div[1]/a"
                                      "/input").send_keys('/Users/cy/Downloads/11748400000141000.xlsx')
    sleep(20)
    # self.driver.find_element_by_xpath("").send_keys('D:\\selenium_use_case\upload_file.txt')
    pass
