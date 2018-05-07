# -*- coding: utf-8 -*-

# Author:YueTianZhuang
# Up Cy
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class BrowserLoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.username_locator = None
        self.password_locator = None
        self.login_submit_locator = None
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
        name_list = ['LoginInput', 'PwdInput', 'LoginBtn']
        ele_dic = page_element_factory(__file__, name_list)
        self.username_locator = ele_dic['LoginInput']
        self.password_locator = ele_dic['PwdInput']
        self.login_submit_locator = ele_dic['LoginBtn']
        pass

    def is_loaded(self):

        pass

    def login(self, username=None, password=None):
        self.initial_element()
        if username:
            get_element(self.driver, self.username_locator).send_keys(username)
        if password:
            get_element(self.driver, self.password_locator).send_keys(password)

        get_element(self.driver, self.login_submit_locator).click()
