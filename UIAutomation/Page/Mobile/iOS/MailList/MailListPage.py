# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException


# Author:zhongchangwei
from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory


class MailListPage(BasePage):
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
        name_list = ['search', 'assign', 'invite_and_assign']
        ele_dic = page_element_factory(__file__, name_list)
        self.search_locator = ele_dic['search']  # 搜索
        self.assign_locator = ele_dic['assign']  # 分配
        self.invite_and_assign_locator = ele_dic['invite_and_assign']  # 邀请并分配
        pass

    def is_loaded(self):
        pass
