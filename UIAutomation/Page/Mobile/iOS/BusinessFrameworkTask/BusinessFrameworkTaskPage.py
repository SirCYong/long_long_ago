# -*- coding: utf-8 -*-
#
#  Cy
from time import sleep

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, is_element_present
from UIAutomation.Page import BasePage
from .MyCustomerPage import MyCustomerPage
from .MySupplierPage import MySupplierPage
from .WhatIHavePage import WhatIHavePage
__author__ = 'caoyong'


class BusinessFrameworkTaskPage(BasePage):
    """
    激活实体店(点击按钮)
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_who_am_I_locator = None
        self.click_wholesale_locator = None
        self.click_transport_locator = None
        self.click_warehouse_locator = None
        self.click_Labor_dispatch = None
        self.click_confirm_button = None
        self.click_last_confirm_button_locator = None
        try:
            self.is_loaded()
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
        name_list = ('whoAmI', 'wholesale', 'transportation', 'warehouse', 'LaborDispatch', 'ConfirmButton',
                     'lastConfirmButton')
        ele_dic = page_element_factory(__file__, name_list)
        self.click_who_am_I_locator = ele_dic['whoAmI']
        self.click_wholesale_locator = ele_dic['wholesale']
        self.click_transport_locator = ele_dic['transportation']
        self.click_warehouse_locator = ele_dic['warehouse']
        self.click_Labor_dispatch = ele_dic['LaborDispatch']
        self.click_confirm_button = ele_dic['ConfirmButton']
        self.click_last_confirm_button_locator = ele_dic['lastConfirmButton']
        pass

    def is_loaded(self):

        pass

    def operation_business_framework_task(self):
        self.action.click(self.click_who_am_I_locator)
        BusinessFrameworkTaskPage(self.driver).operation_who_i_business_framework_click()
        WhatIHavePage(self.driver).click_what_i_have_title()
        sleep(2)
        MySupplierPage(self.driver).click_my_supplier()
        MyCustomerPage(self.driver).task_click_my_customer_title()
        self.action.click(self.click_last_confirm_button_locator)
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '签订系统供应契约'))
        pass

    def operation_business_framework_click(self):
        self.action.click(self.click_wholesale_locator)
        self.action.click(self.click_transport_locator)
        self.action.click(self.click_warehouse_locator)
        self.action.click(self.click_Labor_dispatch)

    def operation_who_i_business_framework_click(self):
        self.action.click(self.click_wholesale_locator)
        self.action.click(self.click_transport_locator)
        self.action.click(self.click_warehouse_locator)
        get_element(self.driver, self.click_Labor_dispatch).click()
        get_element(self.driver, self.click_confirm_button).click()
        pass
