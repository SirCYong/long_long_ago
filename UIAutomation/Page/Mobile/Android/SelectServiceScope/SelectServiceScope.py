# -*- coding: utf-8 -*-
"""
Author:liyu
"""
from selenium.common.exceptions import NoSuchWindowException


from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, get_elements
from UIAutomation.Page import BasePage


class SelectServiceScope(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver, __file__)
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
        name_list = ['ManageWarehouse','Paydeposit']
        ele_dic = page_element_factory(__file__, name_list)
        self.managewarehouse_elements = get_elements(self.driver, ("ID","tv_name"))
        self.paydeposit_element = get_element(self.driver,ele_dic['Paydeposit'])#缴纳保证金
        return self.managewarehouse_elements

        #self.paydeposit_element = get_element(self.driver,ele_dic['Paydeposit'])
        pass

    # def click_managewarehouse(self):
    #     self.initial_element()
    #     self.ManageWarehouse_element.click()
    #     pass
    #
    # def click_sellprods(self):
    #     #self.initial_element()
    #     self.Sellprods_element.click()
    #     pass
    #
    # def click_managelabor(self):
    #     #self.initial_element()
    #     self.ManageLabor_element.click()
    #     pass
    #
    # def click_freight(self):
    #     #self.initial_element()
    #     self.Freight_element.click()
    #     pass
    #
    # def click_makeproduction(self):
    #     #self.initial_element()
    #     self.
    #
    #     pass

    def click_paydeposit(self):
        self.initial_element()
        self.paydeposit_element.click()
        pass

    def is_loaded(self):
        pass
