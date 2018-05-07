# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class ActivationEntityShopPage(BasePage):
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
        name_list = ('entityShopName', 'entityShopMapChoice', 'entityShopAddress', 'entityShopArea',
                     'nextButton')
        ele_dic = page_element_factory(__file__, name_list)
        self.input_entity_name_locator = ele_dic['entityShopName']
        self.input_entity_address_locator = ele_dic['entityShopAddress']
        self.input_entity_area_locator = ele_dic['entityShopArea']
        self.click_map_locator = ele_dic['entityShopMapChoice']
        self.click_next_button_locator = ele_dic['nextButton']

    def is_loaded(self):

        pass

    def entity_shop_input_information(self):

        get_element(self.driver, self.input_entity_name_locator).send_keys(u'店大欺人')
        get_element(self.driver, self.input_entity_address_locator).send_keys(u'黄泉路')
        get_element(self.driver, self.input_entity_area_locator).send_keys(250)
        get_element(self.driver, self.click_map_locator).click()
        sleep(2)
        DepotMapPage(self.driver).map_first()
        get_element(self.driver, self.click_next_button_locator).click()
        pass
