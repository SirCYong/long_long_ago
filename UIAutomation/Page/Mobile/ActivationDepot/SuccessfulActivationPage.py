from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, is_element_present, ParseXmlErrorException, \
    initial_element_error_wrapper
from UIAutomation.Page import BasePage
__author__ = 'CaoYong'


class SuccessfulActivationPage(BasePage):
    """
    成功激活仓库判断（地图操作）
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.get_success_activation_locator = None
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
        name_list = ['successActivation']
        ele_dic = page_element_factory(__file__, name_list)
        self.get_success_activation_locator = ele_dic['successActivation']

    def is_loaded(self):

        pass

    def map_first(self):
        if self.is_run_ios():
            self._map_first_ios()
        else:
            self._map_first_android()
        pass

    def _map_first_ios(self):
        assert is_element_present(self.driver, self.get_success_activation_locator)
        pass

    def _map_first_android(self):
        pass
