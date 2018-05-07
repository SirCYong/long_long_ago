# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException
from common.common_method.configuration import log_write
from common.common_method.element.PageFactory import page_element_factory
from common.exception.IscsException import ParseXmlErrorException
from common.page.BasePage import BasePage

# Author:zhongchangwei


class ReceiptInformationPage(BasePage):
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
        name_list = ['c_name', 'phone', 'address', 'sddress_detail', 'zip_code', 'order_no',
                     'submit', 'blank', 'card_type', 'task_create_time']
        ele_dic = page_element_factory(__file__, name_list)
        self.c_name_locator = ele_dic['c_name']  # 名字
        self.phone_locator = ele_dic['phone']  # 电话
        self.address_locator = ele_dic['address']  # 地址
        self.sddress_detail_locator = ele_dic['sddress_detail']  # 详细地址
        self.zip_code_locator = ele_dic['zip_code']  # 邮编
        self.order_no_locator = ele_dic['order_no']  # 订单号
        self.submit_locator = ele_dic['submit']  # 提交
        self.blank_locator = ele_dic['blank']  # 空白
        self.card_type_locator = ele_dic['card_type']  # 卡片类型
        self.task_create_time_locator = ele_dic['task_create_time']  # 任务创建时间
        pass

    def is_loaded(self):
        pass