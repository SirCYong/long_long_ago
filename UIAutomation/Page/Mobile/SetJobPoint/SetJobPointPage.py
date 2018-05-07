from time import sleep
from hamcrest import *
from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.CommonPage.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.CommonPage.LongCardPage import LongCardPage
from UIAutomation.Utils import initial_element_error_wrapper, ParseXmlErrorException, is_element_present, \
    page_element_factory
__author__ = "zzh"
__doc__ = "维护工作点"


class SetJobPointPage(BasePage):
    """
    维护工作点
    """
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
        except Exception():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ['scanner_number', 'job_point_name', 'wheel_vendor', 'btn_confirm', 'finish']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.scanner_number_locator = ele_dic['scanner_number']
        self.job_point_name_locator = ele_dic['job_point_name']
        self.wheel_vendor_locator = ele_dic['wheel_vendor']
        self.btn_confirm_locator = ele_dic['btn_confirm']
        self.finish_locator = ele_dic['finish']

    def is_loaded(self):
        pass

    def input_job_point_code(self, code):
        """
        输入工作点条码
        """
        self.action.send_keys(self.scanner_number_locator, code)
        engines = self.driver.available_ime_engines
        engines.remove(u'io.appium.android.ime/.UnicodeIME')
        self.driver.activate_ime_engine(engines[0])
        self.action.keyevent(66)

    def click_job_point_name(self):
        """
        点击工作点类型
        :return:
        """
        self.action.click(self.job_point_name_locator)

    def check_job_point_name_exist(self):
        """
        检查工作点类型控件存在
        :return:
        """
        assert_that(self.action.is_element_present(self.job_point_name_locator), equal_to("True"))

    def swipe_wheel_vendor(self):
        """
        选择一个工作点类型
        :return:
        """
        # self.action.swipe()
        pass

    def click_btn_confirm(self):
        """
        点击选择工作点类型的确定按钮
        :return:
        """
        self.action.click(self.btn_confirm_locator)

    def click_btn_finish(self):
        """
        点击完成按钮
        :return:
        """
        self.action.click(self.finish_locator)


