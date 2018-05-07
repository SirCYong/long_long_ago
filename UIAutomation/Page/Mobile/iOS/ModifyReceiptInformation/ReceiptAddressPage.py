# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException
from common.common_method.configuration import log_write
from common.common_method.element.PageFactory import page_element_factory
from common.exception.IscsException import ParseXmlErrorException
from common.page.BasePage import BasePage

# Author:zhongchangwei


class ReceiptAddressPage(BasePage):
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

    def page_factory(self):
        name_list = ['province', 'city', 'county']
        ele_dic = page_element_factory(__file__, name_list)
        self.province_locator = ele_dic['province']  # 省
        self.city_locator = ele_dic['city']  # 市
        self.county_locator = ele_dic['county']  # 县
        pass

    def is_loaded(self):
        pass