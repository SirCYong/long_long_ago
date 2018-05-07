# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException
from common.common_method.configuration import log_write
from common.common_method.element.PageFactory import page_element_factory
from common.common_method.element.find_element import get_element
from common.exception.IscsException import ParseXmlErrorException
from common.page.BasePage import BasePage
"""
Author:zhongchangwei
"""


class MainPage(BasePage):
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

    def is_loaded(self):
        pass

    def page_factory(self):
        name_list = ['team3', 'Main_Forecast_review_button']
        ele_dic = page_element_factory(__file__, name_list)
        self.team3_locator = ele_dic['team3']
        self.Main_Forecast_review_button_element = get_element(self.driver, ele_dic['Main_Forecast_review_button'])  # 主页面预测审核按钮
        pass

    def run_click(self):
        self.initial_element()
        self.Main_Forecast_review_button_element.click()
        pass

    def click_team3(self, username=None, password=None):
        self.initial_element()
        get_element(self.driver, self.team3_locator).click()
        pass

