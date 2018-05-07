# -*- coding: utf-8 -*-
# language  zh-CN
# Author: Cy
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, get_element
from UIAutomation.Page import BasePage


class IosTransitionPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

        try:
            self.is_loaded()
            self.initial_element()
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
        namelist = ['first']
        ele_dic = page_element_factory(__file__, namelist)
        self.click_first_locator = ele_dic['first']  #

    def is_loaded(self):
        pass

    def click_first(self):
        get_element(self.driver, self.click_first_locator).click()

        pass
