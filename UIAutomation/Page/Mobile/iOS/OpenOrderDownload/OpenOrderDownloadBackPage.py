# -*- coding: utf-8 -*-
# 说明
# Author
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage


class OpenOrderDownloadBackPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.interface_open_locator = None
        self.task_creation_time_locator = None
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
        name_list = ['interface_open',
                     'task_creation_time']
        ele_dic = page_element_factory(__file__, name_list)
        self.interface_open_locator = ele_dic['interface_open']  # 接口开启
        self.task_creation_time_locator = ele_dic['task_creation_time']  # 年
        pass

    def is_loaded(self):
        pass