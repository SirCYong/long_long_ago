# -*- coding: utf-8 -*-
"""
Author:liyu

# 功能：提交保证金

"""
from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element,ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'liyu'


class SubmitDeposit(BasePage):
    def is_loaded(self):
        pass

    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.alipay_locator = None
        self.wechat_locator = None
        self.unionpay_locator = None
        self.paybutton_locator = None
        try:
            self.is_loaded()
        except ParseXmlErrorException:
            assert False

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
            pass

    def page_factory(self):
        name_list = ['AliPay', 'WeChat', 'UnionPay', 'PayButton']
        ele_dic = page_element_factory(__file__, name_list)
        self.alipay_locator = ele_dic['AliPay']
        self.wechat_locator = ele_dic['WeChat']
        self.unionpay_locator = ele_dic['UnionPay']
        self.paybutton_locator = ele_dic['PayButton']
        pass

    # 选择支付宝支付方式
    def click_ali_pay(self):
        self.initial_element()
        get_element(self.driver, self.alipay_locator).click()
        sleep(1)
        get_element(self.driver, self.paybutton_locator).click()

    # 选择微信支付方式
    def click_we_chat(self):
        self.initial_element()
        get_element(self.driver, self.wechat_locator).click()
        sleep(1)
        get_element(self.driver, self.paybutton_locator).click()

    # 选择银联支付方式
    def click_union_pay(self):
        self.initial_element()
        get_element(self.driver, self.unionpay_locator).click()
        sleep(1)
        get_element(self.driver, self.paybutton_locator).click()
