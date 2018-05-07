# -*- coding: utf-8 -*-

# Author:liyu
from time import sleep

from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Utils import page_element_factory


class SelectTimePage(BasePage):
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
        name_list = ['SuccessfulImage', 'StartTime', 'OneYear', 'ImportInformation', 'SelectTime',
                     'ImportFailure', 'ReImport', 'ImportSuccess', 'Close']
        ele_dic = page_element_factory(__file__, name_list)
        self.success_fulImage_localtor = ele_dic['SuccessfulImage']
        self.start_time_localtor = ele_dic['StartTime']
        self.oneyear_localtor = ele_dic['OneYear']
        self.import_information_localtor = ele_dic['ImportInformation']
        self.select_time_localtor = ele_dic['SelectTime']
        self.importfailure_time_localtor = ele_dic['ImportFailure']
        self.reimport_localtor = ele_dic['ReImport']
        self.importsuccess_localtor = ele_dic['ImportSuccess']
        self.close_localtor = ele_dic['Close']
        pass

    def is_loaded(self):
        pass

    def click_start_time(self):
        """
        选择时间
        :return:
        """
        self.initial_element()
        self.action.click(self.start_time_localtor)
        sleep(2)
        # 时间选择框里的内容
        self.action.click(self.select_time_localtor)
        sleep(2)
        self.action.click(self.oneyear_localtor)
        sleep(2)
        # 点击开始导入
        self.action.click(self.import_information_localtor)

    def assert_import_information(self):
        """
        验证是否可以看到'开始导入'按钮
        :return:
        """
        self.initial_element()
        assert_that(self.action.is_element_present(self.import_information_localtor), equal_to(True))

    def click_re_import(self):
        """
        重新导入
        :return:
        """
        self.initial_element()
        self.action.click(self.reimport_localtor)

    def click_close(self):
        """
        关闭
        :return:
        """
        self.initial_element()
        self.action.click(self.close_localtor)

    def assert_jump_select_time(self):
        """
        验证是否跳转到选择时间页面，找到'开始导入信息'按钮
        :return:
        """
        self.initial_element()
        assert_that(self.action.is_element_present(self.import_information_localtor), equal_to(True))


