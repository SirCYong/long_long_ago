# -*- coding: utf-8 -*-
# 激活实体店(PC端)
#  Cy

from time import sleep
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, get_elements, get_element


class ActivationEntityShopWebPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_activation_locator = None
        self.import_commodity_file_locator = None

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
        name_list = ('clickActivationEntityShop', 'inputFile')
        ele_dic = page_element_factory(__file__, name_list)
        self.click_activation_locator = ele_dic['clickActivationEntityShop']
        self.import_commodity_file_locator = ele_dic['inputFile']
        pass

    def is_loaded(self):

        pass

    def web_input_activation_entity_shop(self, path=None):
        a = get_elements(self.driver, self.click_activation_locator)
        a[0].click()
        # elem = self.driver.find_element_by_css_selector(".position-abs")
        # try:
        #     script =  'document.getElementsByClassName("position-abs")[0].click()'
        #     ret = self.driver.execute_script(script)
        #     alert = self.driver.switchTo().alert()
        #     alert.sendKeys(path)
        #     c =  get_element(self.driver, self.import_commodity_file_locator)
        #     script = '$(".position-abs").click()'
        #     ret = self.driver.execute_script(script)
        # except Exception as e:
        #     raise e
        get_element(self.driver, self.import_commodity_file_locator).send_keys(path)
        sleep(3)

        pass
