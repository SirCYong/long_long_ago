# -*- coding: utf-8 -*-
"""
Author: CaoYong

"""
from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.ActivationDepot.ActivationDepotPage import ActivationDepotPage
from UIAutomation.Page.Mobile.iOS.BindBankCard.BindBankCardPage import BindBankCardPage
from UIAutomation.Page.Mobile.iOS.BusinessFrameworkTask.BusinessFrameworkTaskPage import BusinessFrameworkTaskPage
from UIAutomation.Page.Mobile.iOS.CustomerChoosePage import CustomerChoosePage
from UIAutomation.Page.Mobile.iOS.TaskCenter.URLSQLPage import activation_depot_status
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException


class TaskCenterPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_activation_depot_locator = None
        self.click_activation_entity_shop_locator = None
        self.click_choice_service_type_locator = None
        self.click_activation_commodity_locator = None
        self.click_business_framework_locator = None
        self.click_bind_bank_locator = None
        self.click_commodity_shows_card_locator = None
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
        namelist = ('activationDepot', 'activationEntityShop', 'choiceServiceType', 'activationCommodity',
                    'businessFramework', 'bindBankCard', 'CommodityShows')
        ele_dic = page_element_factory(__file__, namelist)
        self.click_activation_depot_locator = ele_dic['activationDepot']
        self.click_activation_entity_shop_locator = ele_dic['activationEntityShop']
        self.click_choice_service_type_locator = ele_dic['choiceServiceType']
        self.click_activation_commodity_locator = ele_dic['activationCommodity']
        self.click_business_framework_locator = ele_dic['businessFramework']
        self.click_bind_bank_locator = ele_dic['bindBankCard']
        self.click_commodity_shows_card_locator = ele_dic['CommodityShows']

    def is_loaded(self):
        pass

    def activation_depot(self, admin=None):
        self.action.click(self.click_activation_depot_locator)
        ActivationDepotPage(self.driver).depot_input_information()
        sleep(5)
        activation_depot_status(admin)

        pass

    def activation_commodity(self):
        self.action.click(self.click_activation_commodity_locator)
        pass

    def activation_entity_shop(self):
        self.action.click(self.click_activation_entity_shop_locator)
        pass

    def task_business_framework(self):
        self.action.click(self.click_business_framework_locator)
        BusinessFrameworkTaskPage(self.driver).operation_business_framework_task()
        pass

    def click_service_type(self):
        self.action.click(self.click_choice_service_type_locator)
        customer = CustomerChoosePage(self.driver)
        customer.main_warehouse_customer()  # 激活仓储服务
        customer.main_transport_service_customer()  # 激活运输服务
        customer.main_supply_service()  # 激活供给服务
        pass

    def task_bind_bank_card(self):
        self.action.click(self.click_bind_bank_locator)
        a = BindBankCardPage(self.driver)
        a.operation_bind_bank_card()
        pass

    def task_commodity_show(self):
        self.action.click(self.click_commodity_shows_card_locator)
        pass

