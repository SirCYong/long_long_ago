# -*- coding: utf-8 -*-
"""
Author: Yongli
"""
from common.common_method.element.PageFactory import page_element_factory
from common.common_method.element.find_element import get_element
from common.page.BasePage import BasePage


class RegisterPrintPage(BasePage):
    def __init__(self, web_driver):
        BasePage.__init__(self,web_driver)
        self.driver = web_driver

    def is_loaded(self):
        pass

    def initial_element(self):
        self.page_factory()
        pass

    def page_factory(self):
        name_list = ['ip_address', 'port', 'print_type', 'type_to_print', 'location', 'submit']
        element_metadata_dict = page_element_factory(__file__, name_list)
        self.ip_address_input_box_element = get_element(self.driver, element_metadata_dict['ip_address'])
        self.port_input_box_element = get_element(self.driver, element_metadata_dict['port'])
        self.choose_priter_type_element = get_element(self.driver, element_metadata_dict['print_type'])
        self.choose_to_print_type_element = get_element(self.driver, element_metadata_dict['type_to_print'])
        self.choose_location_element = get_element(self.driver, element_metadata_dict['location'])
        self.submit_element = get_element(self.driver, element_metadata_dict['submit'])

        pass

    def register_print_method(self, ip_address, port):
        self.initial_element()
        self.ip_address_input_box_element.sendkeys(ip_address)
        self.port_input_box_element.sendkeys(port)
        self.submit_element.click()



