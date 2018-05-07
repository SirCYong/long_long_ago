# -*- coding: utf-8 -*-

# Author:liyu
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Utils import page_element_factory


class MainCard(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

        try:
            self.initial_element()
        except ParseXmlErrorException:
            initial_element_error_wrapper(self.driver)
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        name_list = ['AddButton', 'TransportContract', 'ImportInventory', 'perfect_warehousing_contract']
        ele_dic = page_element_factory(__file__, name_list)
        self.addbutton_localtor = ele_dic['AddButton']
        self.transportcontract_localtor = ele_dic['TransportContract']
        self.importinventory_localtor = ele_dic['ImportInventory']
        self.perfect_warehousing_contract_locator = ele_dic['perfect_warehousing_contract']
        pass

    def is_loaded(self):
        pass

    # 发布运输
    def click_button(self):
        self.initial_element()
        self.action.click(self.addbutton_localtor)

    # 导入运输契约
    def click_transport_contract(self):
        self.initial_element()
        self.action.click( self.transportcontract_localtor)

    # 导入库存
    def click_import_inventory(self):
        self.initial_element()
        self.action.click(self.importinventory_localtor)

    # 点击完善仓储契约
    def click_perfect_warehousing_contract(self):
        self.initial_element()
        self.action.click(self.perfect_warehousing_contract_locator)







