# -*- coding: utf-8 -*-

# Author:xuwangchao
from selenium.common.exceptions import NoSuchWindowException
from common.common_method.element.PageFactory import page_element_factory
from common.exception.IscsException import ParseXmlErrorException
from common.page.BasePage import BasePage
from common.common_method.util import logger
from common.common_method.global_var import GlobalVar
import time


class PerfectWarehousingContract(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.login_button_locator = None
        self.userName_input_locator = None
        self.pwd_input_locator = None
        self.weiChat_login_locator = None
        self.go_weichat_locator = None

        try:
            self.initial_element()
        except ParseXmlErrorException:
            print (u'XML解析失败.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print "错误截图："
            print '<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />'
            logger.run_info_log(u'XML解析失败.', GlobalVar.get_log_file())
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            print (u'控件不在当前页面上.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print "错误截图："
            print '<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />'
            logger.run_info_log(u'控件不在当前页面上.', GlobalVar.get_log_file())
            raise
        pass

    def page_factory(self):
        name_list = ['choose_upload_file', 'import_success']
        ele_dic = page_element_factory(__file__, name_list)
        self.choose_upload_file_locator = ele_dic['choose_upload_file']
        self.import_success_locator = ele_dic['import_success']
        print(self.choose_upload_file_locator, self.import_success_locator)
        pass

    def is_loaded(self):
        pass

    def is_success(self):
        """
        判断是否导入成功
        """
        self.initial_element()
        expect_str = u'导入成功'
        real_str = self.action.text(self.import_success_locator)
        assert expect_str == real_str
        print "导入成功"





