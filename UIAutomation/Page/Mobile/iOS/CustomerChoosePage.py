# -*- coding: utf-8 -*-
"""
Author: Caoyong
我要什么供应商页面
"""
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory


class CustomerChoosePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

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
        namelist = ('CustomerTypeTitleText', 'CustomerOneBox', 'CustomerTwoBox', 'CustomerButton', 'CustomerThreeBox',
                    'warehouseService', 'transportService', 'CustomerFourBox', 'CustomerFiveBox', 'CustomerSixBox',
                    'CustomerSevenBox', 'CustomerEightBox', 'CustomerNineBox', 'CustomerTenBox', 'oneSupplyService',
                    'twoSupplyService', 'threeSupplyService')
        ele_dic = page_element_factory(__file__, namelist)
        self.customer_type_title_text_locator = ele_dic['CustomerTypeTitleText']  # 选择类别框
        self.customer_one_box_locator = ele_dic['CustomerOneBox']
        self.customer_two_box_locator = ele_dic['CustomerTwoBox']
        self.customer_three_box_locator = ele_dic['CustomerThreeBox']
        self.four_box_locator = ele_dic['CustomerFourBox']
        self.five_box_locator = ele_dic['CustomerFiveBox']
        self.six_box_locator = ele_dic['CustomerSixBox']
        self.seven_box_locator = ele_dic['CustomerSevenBox']
        self.eight_box_locator = ele_dic['CustomerEightBox']
        self.nine_box_locator = ele_dic['CustomerNineBox']
        self.ten_box_locator = ele_dic['CustomerTenBox']
        self.customer_button_locator = ele_dic['CustomerButton']
        self.warehouse_service_locator = ele_dic['warehouseService']
        self.transport_service_locator = ele_dic['transportService']
        self.one_supply_locator = ele_dic['oneSupplyService']
        self.two_supply_locator = ele_dic['twoSupplyService']
        self.three_supply_locator = ele_dic['threeSupplyService']

    def is_loaded(self):
        pass

    def get_customer_type_title_text(self):
        return self.customer_type_title_text_locator

    def choose_customer(self):  # 全选
        self.action.click(self.customer_one_box_locator)
        self.action.click(self.customer_two_box_locator)
        self.action.click(self.customer_three_box_locator)
        self.action.click(self.four_box_locator)
        self.action.click(self.five_box_locator)
        self.action.click(self.six_box_locator)
        self.action.click(self.seven_box_locator)
        self.action.click(self.eight_box_locator)
        self.action.click(self.nine_box_locator)
        self.action.click(self.ten_box_locator)
        self.action.click(self.customer_button_locator)
        pass

    def main_warehouse_customer(self):  # 仓储服务
        self.action.click(self.warehouse_service_locator)
        self.action.click(self.customer_button_locator)
        pass

    def main_transport_service_customer(self):  # 传输服务
        self.action.click(self.transport_service_locator)
        self.action.click(self.customer_button_locator)
        pass

    def main_supply_service(self):  # 发布供货供给
        self.action.click(self.one_supply_locator)
        self.action.click(self.two_supply_locator)
        self.action.click(self.three_supply_locator)
        self.action.click(self.customer_button_locator)
        pass













