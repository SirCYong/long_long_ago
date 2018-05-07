# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory

__author__ = "LiYu"
__doc__ = "登录进入主界面"


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
            name_list = ['packing', 're_packing', 'LongTaskCard', 'card_layout', 'long_card_supply']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.packing_locator = ele_dic['packing']
            self.re_packing_locator = ele_dic['re_packing']
            self.long_task_card_locator = ele_dic['LongTaskCard']
            self.long_labor_locator = ele_dic['card_layout']
            self.long_supply_locator = ele_dic['long_card_supply']
            pass

    def select_page(self):
        """
        点击长期任务卡片
        :return:
        """
        if self.is_run_ios():
            self._long_task_card_ios()

        if not self.is_run_ios():
            self._long_task_card_android()

    def is_loaded(self):
        pass

    def _long_task_card_ios(self):
        """
        ios 长期任务卡片
        :return:
        """
        LongCardPage(self.driver).click_long_task_card()

    def _long_task_card_android(self):
        self.action.click(self.long_task_card_locator)

    def _packing_android(self):
        time.sleep(10)
        self.action.click(self.packing_locator)
        time.sleep(5)
        self.action.click(self.re_packing_locator)

    def click_publish_labor_ios(self):
        """
        ios:发布劳务需求
        :return:
        """
        self.action.click(self.long_labor_locator)

    def click_publish_supply_ios(self):
        """
        ios:发布仓储供应
        :return:
        """
        self.action.click(self.long_supply_locator)

    def click_publish_labor_android(self):
        """
        android:发布劳务需求
        :return:
        """
        self.action.click(self.long_labor_locator)

    def click_publish_supply_android(self):
        """
        android:发布仓储供应
        :return:
        """
        self.action.click(self.long_supply_locator)

    def click_packing_ios(self):
        self.action.click(self.packing_locator)

    def click_packing_android(self):
        self.action.click(self.packing_locator)







