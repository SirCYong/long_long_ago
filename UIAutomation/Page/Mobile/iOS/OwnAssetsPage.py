# -*- coding: utf-8 -*-
"""
Author: Caoyong
我要什么供应商页面
"""

from common.common_method.element.find_element import get_element
from selenium.common.exceptions import NoSuchWindowException
from common.common_method.configuration import log_write
from common.common_method.element.PageFactory import page_element_factory
from common.exception.IscsException import ParseXmlErrorException
from common.page.BasePage import BasePage


class OwnAssetsPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

        try:
            self.is_loaded()
            self.initial_element()
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

    def page_factory(self):
        namelist = ['AssetsTypeTitleText', 'AssetsOneBox', 'AssetsTwoBox', 'AssetsButton', 'AssetsThreeBox']
        ele_dic = page_element_factory(__file__, namelist)
        self.assets_type_title_text_locator = ele_dic['AssetsTypeTitleText']  # 选择类别框
        self.assets_one_box_locator = ele_dic['AssetsOneBox']
        self.assets_two_box_locator = ele_dic['AssetsTwoBox']
        self.assets_three_box_locator = ele_dic['AssetsThreeBox']
        self.assets_button_locator = ele_dic['AssetsButton']

    def is_loaded(self):
        pass

    def get_serve_type_title_text(self):
        return self.assets_type_title_text_locator

    def choose_assets(self):
        get_element(self.driver, self.assets_one_box_locator).click()
        get_element(self.driver, self.assets_two_box_locator).click()
        get_element(self.driver, self.assets_three_box_locator).click()
        get_element(self.driver, self.assets_button_locator).click()
        pass

