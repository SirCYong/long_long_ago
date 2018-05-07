"""
Author:liyu
"""
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, get_element


class SelectAddressPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.is_loaded()
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
        name_list = ['Province']
        ele_dic = page_element_factory(__file__, name_list)
        self.province_locator = ele_dic['Province']
        pass

    def select_province(self):
        self.initial_element()
        get_element(self.driver, self.province_locator).click()
        pass

    def is_loaded(self):
        pass
