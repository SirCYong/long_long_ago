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


class ChooseSupplierPage(BasePage):
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
        namelist = ('serveTypeTitleText', 'serveOneBox', 'serveTwoBox', 'serveButton', 'serveThreeBox', 'serveFourBox',
                    'serveFiveBox', 'serveSixBox', 'serveSevenBox', 'serveEightBox', 'serveNineBox', 'serveTenBox',
                    'warehouse', 'labourService', 'notService')
        ele_dic = page_element_factory(__file__, namelist)
        self.serve_type_title_text_locator = ele_dic['serveTypeTitleText']  # 选择类别框
        self.serve_one_box_locator = ele_dic['serveOneBox']
        self.serve_two_box_locator = ele_dic['serveTwoBox']
        self.serve_three_locator = ele_dic['serveThreeBox']
        self.serve_four_locator = ele_dic['serveFourBox']
        self.serve_five_locator = ele_dic['serveFiveBox']
        self.serve_six_locator = ele_dic['serveSixBox']
        self.serve_seven_locator = ele_dic['serveSevenBox']
        self.serve_eight_locator = ele_dic['serveEightBox']
        self.serve_nine_locator = ele_dic['serveNineBox']
        self.serve_ten_locator = ele_dic['serveTenBox']
        self.serve_button_locator = ele_dic['serveButton']
        self.warehouse_locator = ele_dic['warehouse']
        self.labour_service_locator = ele_dic['labourService']
        self.not_service_locator = ele_dic['notService']

    def is_loaded(self):
        pass

    def get_serve_type_title_text(self):
        return self.serve_type_title_text_locator

    def choose_all_default(self):   # 全选
        get_element(self.driver, self.serve_one_box_locator).click()
        get_element(self.driver, self.serve_two_box_locator).click()
        get_element(self.driver, self.serve_three_locator).click()
        get_element(self.driver, self.serve_four_locator).click()
        get_element(self.driver, self.serve_five_locator).click()
        get_element(self.driver, self.serve_six_locator).click()
        get_element(self.driver, self.serve_seven_locator).click()
        get_element(self.driver, self.serve_eight_locator).click()
        get_element(self.driver, self.serve_nine_locator).click()
        get_element(self.driver, self.serve_ten_locator).click()
        get_element(self.driver, self.serve_button_locator).click()
        pass

    def main_choose_warehouse(self):    # 发布仓储需求
        get_element(self.driver, self.warehouse_locator).click()
        get_element(self.driver, self.serve_button_locator).click()
        pass

    def main_choice_labour_service(self):   # 发布劳务需求
        get_element(self.driver, self.labour_service_locator).click()
        get_element(self.driver, self.serve_button_locator).click()
        pass

    def main_not_service(self):   # 不选服务
        get_element(self.driver, self.not_service_locator).click()
        get_element(self.driver, self.serve_button_locator).click()
        pass








    # def choose_server_scope(driver, *type_list):
    #     创建一个列表，把所有合法类型定义了
        # list = ['', '', '']
        # 如果判断是空，则调用default
        # if(len(type_list)):
        #     def choosedefualt():
        #         click()
        # 如果不为空，则要判断是不是合法的
        # elif(type_list not in list):
        #     print('')
        #     assert False
        # list_ele = []
        # 点击用户要求的
        # else:
        #     for  element in type_list:
        #         list_ele.append( (driver, ['accessbility_id', element]))
        #
        # for ele in list_ele:
        #     ele.click()








