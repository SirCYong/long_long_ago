# -*- coding: utf-8 -*-

"""
Author:liyu
"""


from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, get_element


class SelectAddressCity(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
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
        name_list = ['Provinces_city']
        ele_dic = page_element_factory(__file__, name_list)
        self.provinces_cities_locator = ele_dic['Provinces_city']
        pass

    def select_province_city(self):
        self.initial_element()
        get_element(self.driver, self.provinces_cities_locator).click()
        pass

    def is_loaded(self):
        pass
