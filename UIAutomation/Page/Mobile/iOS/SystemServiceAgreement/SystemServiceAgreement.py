# -*- coding: utf-8 -*-
"""
Author:liyu
功能：签订系统服务契约
"""

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element,ParseXmlErrorException
from UIAutomation.Page import BasePage


class SystemServiceAgreement(BasePage):
    def is_loaded(self):
        pass

    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.agreement_locator = None
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
        name_list = ['Agreement']
        ele_dic = page_element_factory(__file__, name_list)
        self.agreement_locator = ele_dic['Agreement']
        pass

    # 同意服务契约
    def click_agreement(self):
        self.initial_element()
        get_element(self.driver, self.agreement_locator).click()

