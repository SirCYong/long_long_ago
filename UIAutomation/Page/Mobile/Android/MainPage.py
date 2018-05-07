# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage

# Author:yuetianzhuang


class MainPage(BasePage):
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
        name_list = ['Improve_InformationBtn']
        ele_dic = page_element_factory(__file__, name_list)
        self.Improve_InformationBtn_element = ele_dic['Improve_InformationBtn']

        pass

    def is_loaded(self):

        pass

    def click_Improve_InformationBtn(self):
        self.initial_element()
        get_element(self.driver, self.Improve_InformationBtn_element).click()


