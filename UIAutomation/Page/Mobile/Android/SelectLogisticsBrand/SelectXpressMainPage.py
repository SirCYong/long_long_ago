# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage

# Author:zhongchangwei


class SelectXpressMainPage(BasePage):
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
        name_list = ['buyers_request_add_button',
                     'buyers_refused_add_button',
                     'buyers_request_text',
                     'buyers_refused_text',
                     'order_number',
                     'receipt_address',
                     'submit',
                     'confirm',
                     'selected_logistics_brands']
        ele_dic = page_element_factory(__file__, name_list)
        self.buyers_request_add_button_locator = ele_dic['buyers_request_add_button']  # 买家要求发,添加快递
        self.buyers_refused_add_button_locator = ele_dic['buyers_refused_add_button']  # 买家拒绝发,添加快递
        self.buyers_request_text_locator = ele_dic['buyers_request_text']  # 没有买家要求发的快递时的文案
        self.buyers_refused_text_locator = ele_dic['buyers_refused_text']  # 没有买家拒绝发的快递时的文案
        self.order_number_locator = ele_dic['order_number']  # 订单号
        self.receipt_address_locator = ele_dic['receipt_address']  # 收货地址
        self.submit_locator = ele_dic['submit']  # 按以上要求发货
        self.confirm_locator = ele_dic['confirm']   # 确定
        self.selected_logistics_brands_locator = ele_dic['selected_logistics_brands']  # 已选择的快递品牌
        pass

    def is_loaded(self):
        pass
