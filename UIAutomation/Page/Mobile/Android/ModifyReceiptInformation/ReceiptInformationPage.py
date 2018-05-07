# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage

# Author:zhongchangwei


class ReceiptInformationPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.is_loaded()
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
        name_list = ['c_name', 'phone', 'address', 'sddress_detail', 'zip_code', 'order_no', 'submit']
        ele_dic = page_element_factory(__file__, name_list)
        self.c_name_locator = ele_dic['c_name']  # 姓名
        self.phone_locator = ele_dic['phone']  # 手机号
        self.address_locator = ele_dic['address']  # 地址
        self.sddress_detail_locator = ele_dic['sddress_detail']  # 详细地址
        self.zip_code_locator = ele_dic['zip_code']  # 邮编
        self.order_no_locator = ele_dic['order_no']  # 订单号
        self.submit_locator = ele_dic['submit']  # 提交
        pass

    def is_loaded(self):
        # assert self.driver.current_activity == '.activity.orders.AlertOrdersActivity'
        pass
