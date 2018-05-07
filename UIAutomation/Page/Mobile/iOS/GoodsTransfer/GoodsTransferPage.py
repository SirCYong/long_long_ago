# -*- coding: utf-8 -*-
"""
Author:Ytz
"""
from time import sleep

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, get_element
from UIAutomation.Page import BasePage


class LaborDemandPage(BasePage):
    def is_loaded(self):
        pass

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
        name_list = ['scan_input', 'start_location', 'target_location', 'complete_btn']
        ele_dic = page_element_factory(__file__, name_list)
        self.scan_input_element = get_element(self.driver, ele_dic['scan_input'])
        self.start_location_element = get_element(self.driver, ele_dic['start_location'])
        self.target_location_element = get_element(self.driver, ele_dic['target_location'])
        self.complete_btn_element = get_element(self.driver, ele_dic['complete_btn'])
        pass

    def click_transfer(self):
        self.initial_element()
        self.scan_input_element.send_keys('')
        sleep(2)
        self.start_location_element.send_keys('')
        sleep(2)
        self.target_location_element.send_keys('')
        sleep(2)
        self.complete_btn_element.send_keys('')
