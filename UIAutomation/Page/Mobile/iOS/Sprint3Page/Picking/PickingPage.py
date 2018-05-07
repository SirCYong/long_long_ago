# -*- coding: utf-8 -*-

"""
Author:liyu
"""
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class PickingPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.starting_position_locator = None
        self.target_position_locator = None
        self.starting_carrier_locator = None
        self.target_carrier_locator = None
        self.complete_button_locator = None
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

    def is_loaded(self):
        pass

    def page_factory(self):
        name_list = ['starting_position', 'target_position', 'starting_carrier', 'target_carrier', 'complete_button']
        ele_dic = page_element_factory(__file__, name_list)
        self.starting_position_locator = ele_dic['starting_position']
        self.target_position_locator = ele_dic['target_position']
        self.starting_carrier_locator = ele_dic['starting_carrier']
        self.target_carrier_locator = ele_dic['target_carrier']
        self.complete_button_locator = ele_dic['complete_button']
        pass

    def click_picking_task(self):
        self.initial_element()
        get_element(self.driver, self.starting_position_locator).send_keys('')
        get_element(self.driver, self.target_position_locator).send_keys('')
        get_element(self.driver, self.starting_carrier_locator).send_keys('')
        get_element(self.driver, self.target_carrier_locator).send_keys('')
        get_element(self.driver, self.complete_button_locator).click()
        pass
