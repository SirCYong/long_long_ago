# -*- coding: utf-8 -*-
# language  zh-CN
# Author: Cy
from time import sleep
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, get_element
from UIAutomation.Page import BasePage
from UIAutomation.page.Mobile.iOS.IosStartLogin.TransitionPage import IosTransitionPage


class IosStartLoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
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
        namelist = ('startLogin', 'userID', 'password', 'go')
        ele_dic = page_element_factory(__file__, namelist)
        self.start_login_locator = ele_dic['startLogin']  # 登录按钮
        self.input_userID_locator = ele_dic['userID']
        self.input_password_locaror = ele_dic['password']
        self.click_go_locator = ele_dic['go']

    def is_loaded(self):
        pass

    def get_start_login(self, user_id=None, password=None):
        get_element(self.driver, self.input_userID_locator).set_value(user_id)
        get_element(self.driver, self.input_password_locaror).set_value(password)
        get_element(self.driver, self.click_go_locator).click()
        sleep(2)
        IosTransitionPage(self.driver).click_first()

        pass

