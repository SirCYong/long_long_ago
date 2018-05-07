from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, is_element_present, ParseXmlErrorException
from UIAutomation.Page import BasePage

__author__ = 'caoyong'


class ActivationCommodityPage(BasePage):
    """
    激活商品
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.assert_import_locator = None

        try:
            self.is_loaded()
            self.initial_element()
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
        name_list = ['successActivation']
        ele_dic = page_element_factory(__file__, name_list)
        self.assert_import_locator = ele_dic['successActivation']
        pass

    def is_loaded(self):

        pass

    def import_commodity(self):
        assert is_element_present(self.driver, self.assert_import_locator)
        pass
