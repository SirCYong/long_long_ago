from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory,  ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'caoyong'


class MyCustomerPage(BasePage):
    """
    我的客户(点击按钮)
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_my_customer_locator = None
        self.click_retail_shop_locator = None
        self.click_depot_locator = None
        self.click_wholesale_shop_locator = None
        self.click_finished_product_locator = None
        self.click_material_factory_locator = None
        self.click_transport_locator = None
        self.click_confirm_button_locator = None
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
        name_list = ('myCustomer', 'retailShop', 'depot', 'wholesaleShop', 'finishedProduct', 'materialFactory',
                     'transport', 'confirmButton')
        ele_dic = page_element_factory(__file__, name_list)
        self.click_my_customer_locator = ele_dic['myCustomer']
        self.click_retail_shop_locator = ele_dic['retailShop']
        self.click_depot_locator = ele_dic['depot']
        self.click_wholesale_shop_locator = ele_dic['wholesaleShop']
        self.click_finished_product_locator = ele_dic['finishedProduct']
        self.click_material_factory_locator = ele_dic['materialFactory']
        self.click_transport_locator = ele_dic['transport']
        self.click_confirm_button_locator = ele_dic['confirmButton']

    def is_loaded(self):

        pass

    def task_click_my_customer_title(self):
        self.action.click(self.click_my_customer_locator)
        MyCustomerPage(self.driver).operation_my_customer()
        pass

    def operation_my_customer(self):
        self.action.click(self.click_retail_shop_locator)
        self.action.click(self.click_depot_locator)
        self.action.click(self.click_wholesale_shop_locator)
        self.action.click(self.click_finished_product_locator)
        self.action.click(self.click_material_factory_locator)
        self.action.click(self.click_transport_locator)
        self.action.click(self.click_confirm_button_locator)
        pass