# -*- coding: utf-8 -*-
# language  zh-CN
# Author: yue


from selenium.common.exceptions import NoSuchWindowException

from time import sleep

from common.common_method.configuration import log_write
from common.common_method.element.PageFactory import page_element_factory
from common.common_method.element.find_element import get_element
from common.exception.IscsException import ParseXmlErrorException
from common.page.BasePage import BasePage


class ClosesyButtonPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

        try:
            self.is_loaded()
        except ParseXmlErrorException:
            log_write(ParseXmlErrorException(u'XML解析失败.'))
            assert False

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            log_write(NoSuchWindowException(u'不在当前页面', screen='page.png'))
            BasePage.screen_shot(self)
            assert False

        pass

    def page_factory(self):

        name_list = ['Closesy_Button']
        element_metadata_dict = page_element_factory(__file__, name_list)
        self.Closesy_Button_element = get_element(self.driver, element_metadata_dict['Closesy_Button'])

        pass

    def click_closesy_button(self):

        self.initial_element()
        self.Closesy_Button_element.click()

        sleep(2)
        pass

    def is_loaded(self):

        pass