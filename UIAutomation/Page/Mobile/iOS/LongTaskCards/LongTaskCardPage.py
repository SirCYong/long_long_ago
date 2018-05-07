# -*- coding: utf-8 -*-

"""
Author:liyu

长期任务卡片主界面

"""
from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException

from common.common_method.configuration import log_write
from common.common_method.element.PageFactory import page_element_factory
from common.exception.IscsException import ParseXmlErrorException
from common.page.BasePage import BasePage


class LongTaskCardPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

        try:
            self.is_loaded()
        except ParseXmlErrorException:
            log_write(ParseXmlErrorException(u'XML解析失败.'))
            assert False

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            log_write(NoSuchWindowException(u'不在当前页面', screen='page.png'))
            BasePage.screen_shot(self)
            assert False
        pass

    def is_loaded(self):
        pass

    def page_factory(self):
        name_list = ['Refresh', 'ReleaseLaborDemand', 'StorageUnloading', 'StorageHanDove', 'StoragePoint', 'StorageInventory']
        ele_dic = page_element_factory(__file__, name_list)
        self.refresh_locator = ele_dic['Refresh']
        self.releaselabordemand_locator = ele_dic['ReleaseLaborDemand']
        self.storageunloading_locator = ele_dic['StorageUnloading']
        self.storagehandove_locator = ele_dic['StorageHanDove']
        self.storagepoint_locator = ele_dic['StoragePoint']
        self.storageinventory_locator = ele_dic['StorageInventory']
        pass

    def click_release_labor_demand(self):
        """
        点击发布劳务需求

        """
        self.initial_element()
        self.action.click(self.releaselabordemand_locator)

    def click_storage_point(self):
        """
        点击入库扫码点数

        """
        self.initial_element()
        self.action.click(self.storagepoint_locator)

    def click_storage_inventory(self):
        """
        点击入库上架

        """
        self.initial_element()
        self.action.click(self.storageinventory_locator)

    def assert_long_card_page(self):
        """
        验证是否到长期卡片页面,找到'刷新'卡片

        """
        assert_that(self.action.is_element_present(self.refresh_locator), equal_to(True))
        pass

