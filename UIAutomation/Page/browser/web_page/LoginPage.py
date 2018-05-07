# -*- coding: utf-8 -*-

# Author:liyu
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, sleep
from UIAutomation.Utils import get_element
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Utils import page_element_factory


class LoginPage(BasePage):
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

    def page_factory(self):
        name_list = ['userName', 'password', 'login-submit']
        ele_dic = page_element_factory(__file__, name_list)
        self.username_locator = ele_dic['userName']
        self.password_locator = ele_dic['password']
        self.login_submit_locator = ele_dic['login-submit']
        pass

    def is_loaded(self):

        pass

    def login(self, username=None, password=None):
        self.initial_element()
        if username:
            get_element(self.driver, self.username_locator).send_keys(username)
        if password:
            get_element(self.driver, self.password_locator).send_keys(password)
        sleep(2)
        get_element(self.driver, self.login_submit_locator).click()

