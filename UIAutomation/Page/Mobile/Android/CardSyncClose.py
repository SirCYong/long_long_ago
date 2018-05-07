# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage

class SyncCloseCd(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
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
        name_list = ['select_SyncCloseCard']
        ele_dic = page_element_factory(__file__, name_list)
        print(ele_dic)
        self.select_SyncCloseCard_element =get_element(self.driver, ele_dic['select_SyncCloseCard'])
        pass

    def is_loaded(self):
        pass

    def click_select_SyncCloseCard(self):
        self.initial_element()
        self.select_SyncCloseCard_element.click()
        pass

