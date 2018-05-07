# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage

# Author:zhongchangwei


class ReceiptAddressPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.submit_button_locator =None
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
        name_list = ['submit_button']
        ele_dic = page_element_factory(__file__, name_list)
        self.submit_button_locator = ele_dic['submit_button']  # 提交
        pass

    def is_loaded(self):
        pass
