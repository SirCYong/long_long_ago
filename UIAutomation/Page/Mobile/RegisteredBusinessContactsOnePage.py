# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory

__author__ = "xuwangchao"
__doc__ = "注册联系人第一页"


class MainPage(BasePage):
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
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ['LongTaskCard']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.long_task_card_locator = ele_dic['LongTaskCard']


        # IOS独立控件
        if self.is_run_ios():
            name_list = ['Release_labor_demand', 'Release_warehouse', 'System_service_agreement', 'Submit_deposit',
                         'Empty_card', 'Sorting_clerk', 'Location', 'LongTaskCard', 'Release_Long_labor_demand',
                         'card_layout', 'long_card_supply']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.release_labor_demand_locator = ele_dic['Release_labor_demand']
            self.release_warehouse_locator = ele_dic['Release_warehouse']
            self.system_service_agreement_locator = ele_dic['System_service_agreement']
            self.submit_deposit_locator = ele_dic['Submit_deposit']
            self.empty_card_locator = ele_dic['Empty_card']
            self.sorting_clerk_locator = ele_dic['Sorting_clerk']
            self.location_locator = ele_dic['Location']
            self.long_task_card_locator = ele_dic['LongTaskCard']
            self.long_labor_locator = ele_dic['card_layout']
            self.long_supply_locator = ele_dic['long_card_supply']
            pass
        # Android独立控件
        if not self.is_run_ios():
            name_list = ['business_name', 'duijieren', 'lianxiren', 'lianxiren_mobile', 'duidanren', 'duizhangren', 'next_button']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.business_name_locator = ele_dic['business_name']
            self.duijieren_locator = ele_dic['duijieren']
            self.lianxiren_locator = ele_dic['lianxiren']
            self.lianxiren_mobile_locator = ele_dic['lianxiren_mobile']
            self.duidanren_locator = ele_dic['duidanren']
            self.duizhangren_locator = ele_dic['duizhangren']
            self.next_button_locator = ele_dic['next_button']
            pass

    def assert_first_page(self):
        """
        点击长期任务卡片
        :return:
        """
        if self.is_run_ios():
            self._long_task_card_ios()

        if not self.is_run_ios():
            self._assert_first_page_android()

    def is_loaded(self):
        pass

    def _assert_first_page_ios(self):
        """
        ios上的判断有没有到了第一个页面
        :return:
        """
        LongCardPage(self.driver).click_long_task_card()

    def _assert_first_page_android(self):
        """
        android上的判断有没有到了第一个页面
        """
        assert self.action.is_element_present(self.business_name_locator)
        assert self.action.is_element_present(self.duijieren_locator)
        assert self.action.is_element_present(self.lianxiren_locator)
        assert self.action.is_element_present(self.lianxiren_mobile_locator)
        assert self.action.is_element_present(self.duidanren_locator)
        assert self.action.is_element_present(self.duizhangren_locator)
        assert self.action.is_element_present(self.next_button_locator)
        pass


