from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'liyu'


class SelectServiceScope(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.ManageWarehouse_locator = None
        self.Sellprods_locator = None
        self.ManageLabor_locator = None
        self.Freight_locator = None
        self.MakeProduction_locator = None
        self.Paydeposit_locator = None
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
        name_list = ['ManageWarehouse', 'Sellprods', 'ManageLabor', 'Freight',' MakeProduction', 'Paydeposit']
        ele_dic = page_element_factory(__file__, name_list)
        self.ManageWarehouse_locator = ele_dic['ManageWarehouse']      # 管仓库
        self.Sellprods_locator = ele_dic['Sellprods']     # 卖货
        self.ManageLabor_locator = ele_dic['ManageLabor']     # 管劳务
        self.Freight_locator = ele_dic['Freight']     # 运货
        self.MakeProduction_locator = ele_dic['MakeProduction']       # 搞生产
        self.Paydeposit_locator = ele_dic['Paydeposit']       # 去交纳保证金
        pass

    def click_manage_warehouse(self):
        get_element(self.driver, self.ManageWarehouse_locator).click()
        pass

    def click_sell_prods(self):
        get_element(self.driver, self.Sellprods_locator).click()
        pass

    def click_manage_labor(self):
        get_element(self.driver, self.ManageLabor_locator).click()
        pass

    def click_freight(self):
        get_element(self.driver, self.Freight_locator).click()
        pass

    def click_make_production(self):
        get_element(self.driver, self.MakeProduction_locator).click()
        pass

    def click_pay_deposit(self):
        get_element(self.driver, self.Paydeposit_locator).click()
        pass

    def is_loaded(self):
        pass



