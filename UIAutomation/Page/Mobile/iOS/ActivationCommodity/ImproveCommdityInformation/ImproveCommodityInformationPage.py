from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, initial_element_error_wrapper
from UIAutomation.Page import BasePage

__author__ = 'caoyong'


class ImproveCommodityInformationPage(BasePage):
    """
    我要什么供应商页面
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_activation_depot_locator = None

        try:
            self.is_loaded()
            self.initial_element()
        except ParseXmlErrorException:
            initial_element_error_wrapper(self.driver)
            assert False

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            assert False
        pass

    def page_factory(self):
        namelist = ()
        ele_dic = page_element_factory(__file__, namelist)
        self.click_activation_depot_locator = ele_dic['activationDepot']

    def is_loaded(self):
        pass


