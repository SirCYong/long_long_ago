from time import sleep
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, \
    initial_element_error_wrapper

__author__ = 'zhongchangwei'


class BoundPrinter(BasePage):
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

    def _page_factory_ios(self):
        name_list = ['to_bound_button', 'back', 'code_text_box', 'bound_button', 're_print_express_button',
                     'complete_button']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.to_bound_button_locator = ele_dic['to_bound_button']  # 去绑定
        self.back_locator = ele_dic['back']  # 返回
        self.code_text_box_locator = ele_dic['code_text_box']  # 条码文本框
        self.bound_button_locator = ele_dic['bound_button']  # 绑定按钮
        self.re_print_express_button_locator = ele_dic['re_print_express_button']  # 补打快递单按钮
        self.complete_button_locator = ele_dic['complete_button']  # 完成
        pass

    def _page_factory_android(self):
        name_list = ['to_bound_button', 'code_text_box', 'bound_button', 're_print_express_button']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.to_bound_button_locator = ele_dic['to_bound_button']  # 去绑定
        self.code_text_box_locator = ele_dic['code_text_box']  # 条码文本框
        self.bound_button_locator = ele_dic['bound_button']  # 绑定按钮
        self.re_print_express_button_locator = ele_dic['re_print_express_button']  # 补打快递单按钮
        pass

    def is_loaded(self):
        pass

    def page_factory(self):
        if self.is_run_ios():
            self._page_factory_ios()
        else:
            self._page_factory_android()

    def bound_printer(self, code):
        if self.is_run_ios():
            self._bound_printer_ios(code)
        else:
            self._bound_printer_android(code)

    def _bound_printer_android(self, code):
        self.action.click(self.to_bound_button_locator)
        self.driver.back()
        self.action.send_keys(self.code_text_box_locator, code)
        sleep(1)
        self.action.click(self.bound_button_locator)
        sleep(5)
        assert self.action.is_element_present(self.re_print_express_button_locator)

    def _bound_printer_ios(self, code):
        self.action.click(self.to_bound_button_locator)
        self.action.click(self.back_locator)
        self.action.send_keys(self.code_text_box_locator, code)
        self.action.click(self.complete_button_locator)
        sleep(1)
        self.action.click(self.bound_button_locator)
        sleep(5)
        assert self.action.is_element_present(self.re_print_express_button_locator)
