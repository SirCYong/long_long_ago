# -*- coding: utf-8 -*-


# 激活商品（PC端）
#  Cy
from time import sleep
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, get_elements, get_element


class ActivationCommodityWebPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

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
        name_list = ('clickActivationCommodity', 'inputFile', 'successActivation')
        ele_dic = page_element_factory(__file__, name_list)
        self.click_activation_locator = ele_dic['clickActivationCommodity']
        self.import_commodity_file_locator = ele_dic['inputFile']
        self.judge_avtivation_locator = ele_dic['successActivation']
        pass

    def is_loaded(self):

        pass

    def web_input_activation_commodity(self, path=None):
        a = get_elements(self.driver, self.click_activation_locator)
        a[0].click()
        get_element(self.driver, self.import_commodity_file_locator).send_keys(path)
        sleep(3)

        pass
