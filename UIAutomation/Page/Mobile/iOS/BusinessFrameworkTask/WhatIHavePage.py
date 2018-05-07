from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, get_elements
from UIAutomation.Page import BasePage
__author__ = 'caoyong'


class WhatIHavePage(BasePage):
    """
    我有什么(点击按钮)
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_who_I_have_locator = None
        self.click_online_retail_locator = None
        self.click_my_transport_locator = None
        self.click_car_locator = None
        self.click_my_staff_locator = None
        self.click_goods_locator = None
        self.click_entity_retail_locator = None
        self.click_material_factory_locator = None
        self.click_transport_supplier_locator = None
        self.click_depot_locator = None
        self.click_service_provider_locator = None
        self.click_finish_factory_locator = None
        self.click_storage_equipment_locator = None
        self.click_online_shop_locator = None
        self.click_entity_shop_locator = None
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
        name_list = ('whatIHave', 'onlineRetail', 'myselfTransportation', 'car', 'myselfStaff', 'goods', 'entityRetail',
                     'materialFactory', 'transportSupplier', 'depot', 'serviceProvider', 'finishedFactory',
                     'storageEquipment', 'onlineShop', 'entityShop', 'confirmButton')
        ele_dic = page_element_factory(__file__, name_list)
        self.click_who_I_have_locator = ele_dic['whatIHave']
        self.click_online_retail_locator = ele_dic['onlineRetail']
        self.click_my_transport_locator = ele_dic['myselfTransportation']
        self.click_car_locator = ele_dic['car']
        self.click_my_staff_locator = ele_dic['myselfStaff']
        self.click_goods_locator = ele_dic['goods']
        self.click_entity_retail_locator = ele_dic['entityRetail']
        self.click_material_factory_locator = ele_dic['materialFactory']
        self.click_transport_supplier_locator = ele_dic['transportSupplier']
        self.click_depot_locator = ele_dic['depot']
        self.click_service_provider_locator = ele_dic['serviceProvider']
        self.click_finish_factory_locator = ele_dic['finishedFactory']
        self.click_storage_equipment_locator = ele_dic['storageEquipment']
        self.click_online_shop_locator = ele_dic['onlineShop']
        self.click_entity_shop_locator = ele_dic['entityShop']
        self.click_confirm_button_locator = ele_dic['confirmButton']
        pass

    def is_loaded(self):

        pass

    def click_what_i_have_title(self):
        get_element(self.driver, self.click_who_I_have_locator).click()
        WhatIHavePage(self.driver).operation_what_i_have()

        pass

    def operation_what_i_have(self):
        get_element(self.driver, self.click_online_retail_locator).click()
        get_element(self.driver, self.click_my_transport_locator).click()
        get_element(self.driver, self.click_car_locator).click()
        get_element(self.driver, self.click_my_staff_locator).click()
        get_element(self.driver, self.click_goods_locator).click()
        get_element(self.driver, self.click_entity_retail_locator).click()
        get_element(self.driver, self.click_material_factory_locator).click()
        get_element(self.driver, self.click_transport_supplier_locator).click()
        get_element(self.driver, self.click_depot_locator).click()
        get_element(self.driver, self.click_service_provider_locator).click()
        get_element(self.driver, self.click_finish_factory_locator).click()
        get_element(self.driver, self.click_storage_equipment_locator).click()
        get_element(self.driver, self.click_online_shop_locator).click()
        get_element(self.driver, self.click_entity_shop_locator).click()
        get_elements(self.driver, self.click_confirm_button_locator)[0].click()
        pass

