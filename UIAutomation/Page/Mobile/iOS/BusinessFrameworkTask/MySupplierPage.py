from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage
___author__ = 'caoyong'


class MySupplierPage(BasePage):
    """
    我有什么(点击按钮)
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_my_supplier_locator = None
        self.click_my_finished_factory_locator = None
        self.click_material_factory_locator = None
        self.click_staff_locator = None
        self.click_wholesale_shop_locator = None
        self.click_tool_locator = None
        self.click_depot_locator = None
        self.click_transport_locator = None
        self.confirm_button_locator = None
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
        name_list = ('mySupplier', 'finishedFactory', 'materialFactory', 'staff', 'wholesaleShop', 'tool', 'depot',
                     'transport', 'confirmButton')
        ele_dic = page_element_factory(__file__, name_list)
        self.click_my_supplier_locator = ele_dic['mySupplier']
        self.click_my_finished_factory_locator = ele_dic['finishedFactory']
        self.click_material_factory_locator = ele_dic['materialFactory']
        self.click_staff_locator = ele_dic['staff']
        self.click_wholesale_shop_locator = ele_dic['wholesaleShop']
        self.click_tool_locator = ele_dic['tool']
        self.click_depot_locator = ele_dic['depot']
        self.click_transport_locator = ele_dic['transport']
        self.confirm_button_locator = ele_dic['confirmButton']
        pass

    def is_loaded(self):

        pass

    def click_my_supplier(self):
        self.action.click(self.click_my_supplier_locator)
        MySupplierPage(self.driver).operation_my_supplier()
        pass

    def operation_my_supplier(self):
        get_element(self.driver, self.click_my_finished_factory_locator).click()
        get_element(self.driver, self.click_material_factory_locator).click()
        get_element(self.driver, self.click_staff_locator).click()
        get_element(self.driver, self.click_wholesale_shop_locator).click()
        get_element(self.driver, self.click_tool_locator).click()
        get_element(self.driver, self.click_depot_locator).click()
        get_element(self.driver, self.click_transport_locator).click()
        # self.action.click(self.confirm_button_locator)
        get_element(self.driver, self.confirm_button_locator).click()
        pass