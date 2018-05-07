# -*- coding: utf-8 -*-
"""
Author:liyu
"""
from selenium.common.exceptions import NoSuchWindowException


from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class ForecastPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver,__file__)
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
        name_list = ['Forecast_review_button']
        ele_dic = page_element_factory(__file__, name_list)
        self.Forecast_review_button_element = get_element(self.driver, ele_dic['Forecast_review_button'])  # 预测审核按钮

        pass

    def run_click(self):
        self.initial_element()
        self.Forecast_review_button_element.click()
        pass

    def is_loaded(self):
        pass
