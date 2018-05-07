# -*- coding: utf-8 -*-

"""
Author:liyu
# 发布仓储供应选择时间页面
"""
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory


class SelectTime(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.confirm_locator = None
        try:
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
        name_list = ['Confirm']
        ele_dic = page_element_factory(__file__, name_list)
        self.confirm_locator = ele_dic['Confirm']   # 拣选
        pass

    def click_confirm(self):
        """
        选择时间确认按钮
        :return:
        """
        self.action.click(self.confirm_locator)

    def is_loaded(self):
        pass
