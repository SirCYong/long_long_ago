# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class PromptBoxPage(BasePage):
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
        namelist = ["promptBox", "rejectButton"]
        ele_dic = page_element_factory(__file__, namelist)
        self.prompt_box_element = get_element(self.driver, ele_dic['promptBox'])  # 选择类别框
        self.reject_button_element = get_element(self.driver, ele_dic['rejectButton'])  # 选择类别框

    def is_loaded(self):
        pass

    def get_prompt_box_title(self):
        self.initial_element()
        return self.prompt_box_element

    def get_reject_button(self):
        self.initial_element()
        return self.reject_button_element
