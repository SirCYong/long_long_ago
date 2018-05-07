# -*- coding: utf-8 -*-
"""
Author:liyu
"""
from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class ChoosePayPage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver, __file__)
        self.driver = driver

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
        name_list = ['ALIPAY','UnionPay','AgreedDeposit','ToPay']
        ele_dic = page_element_factory(__file__, name_list)
        self.ALIPAY_element = get_element(self.driver, ele_dic['ALIPAY'])     #支付宝
        self.UnionPay_element = get_element(self.driver, ele_dic['UnionPay'])     #银联
        self.AgreedDeposit_element = get_element(self.driver, ele_dic['AgreedDeposit'])     #同意保证金
        self.ToPay_element = get_element(self.driver, ele_dic['ToPay'])     #去支付
        pass

    def click_alipay(self):
        self.initial_element()
        self.ALIPAY_element.click()
        sleep(1)
        self.ToPay_element.click()
        pass

    def click_unionpay(self):
        self.initial_element()
        self.UnionPay_element.click()
        sleep(1)
        self.ToPay_element.click()
        pass

    def click_agreeddeposit(self):
        self.AgreedDeposit_element.click()
        pass

    # def click_topay(self):
    #
    #     self.ToPay_element.click()

    def is_loaded(self):
        pass
