# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException


class ImportHistoricalOrderPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

        try:
            self.is_loaded()
            self.initial_element()
        except ParseXmlErrorException:
            log_write(ParseXmlErrorException(u'XML解析失败.'))
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
        name_list = ('inputUserId', 'inputPassword', 'confirmButton')
        ele_dic = page_element_factory(__file__, name_list)
        self.input_name_locator = ele_dic['inputUserId']
        self.input_passwd_loactor = ele_dic['inputPassword']
        self.confirm_button_loactor = ele_dic['confirmButton']
        pass

    def is_loaded(self):

        pass

    def web_historical_order(self, admin=199260):
        self.driver = webdriver.Firefox()
        self.driver.get('http://cit.iscs.com.cn/login')
        self.driver.maximize_window()
        get_element(self.driver, self.input_name_locator).send_keys(admin)
        get_element(self.driver, self.input_passwd_loactor).send_keys('as')
        get_element(self.driver, self.confirm_button_loactor).click()
        pass
