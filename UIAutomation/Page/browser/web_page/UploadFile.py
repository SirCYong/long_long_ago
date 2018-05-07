# -*- coding: utf-8 -*-

# Author:liyu
from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Utils import page_element_factory


class UploadFile(BasePage):
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
        name_list = ['Up_file', 'ImportSuccess', 'import_fail', 'select_time', 'close']
        ele_dic = page_element_factory(__file__, name_list)
        self.file_localtor = ele_dic['Up_file']
        self.import_success_localtor = ele_dic['ImportSuccess']
        self.import_fail_localtor = ele_dic['import_fail']
        self.select_time_localtor = ele_dic['select_time']
        self.close_localtor = ele_dic['close']
        pass

    def is_loaded(self):
        pass

    def click_file(self):
        """
        点击上传文件
        :return:
        """
        self.initial_element()
        self.action.click(self.file_localtor)

    def assert_select_time(self):
        """
        验证是否跳转到选择时间界面
        :return:
        """
        self.initial_element()
        assert_that(self.action.is_element_present(self.select_time_localtor), equal_to(True))

    def assert_import_success(self):
        """
        验证是否导入成功
        :return:
        """
        self.initial_element()
        assert_that(self.action.is_element_present(self.import_success_localtor), equal_to(True))

    def assert_import_fail(self):
        """
        验证是否导入失败
        :return:
        """
        self.initial_element()
        assert_that(self.action.is_element_present(self.import_fail_localtor), equal_to(True))

    def click_close(self):
        self.initial_element()
        self.action.click(self.close_localtor)




