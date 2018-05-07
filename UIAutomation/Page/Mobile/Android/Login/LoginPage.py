# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.page import BasePage

__author__ ='yuetianzhuang'


class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
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
        name_list = ['login_button', 'userName_input', 'pwd_input', 'weiChat_login',
                     'go_weichat']
        ele_dic = page_element_factory(__file__, name_list)
        self.login_button_locator = ele_dic['login_button']
        self.user_name_locator = ele_dic['userName_input']
        self.password_locator = ele_dic['pwd_input']
        self.weiChat_login_locator = ele_dic['weiChat_login']
        self.go_weichat_locator = ele_dic['go_weichat']
        pass

    def is_loaded(self):
        pass

    # 输入用户名和密码登录
    def login(self, username=None, password=None):
        self.initial_element()
        self.action.send_keys(self.user_name_locator, username)
        get_element(self.driver, self.password_locator).set_text(password)
        self.action.click(self.login_button_locator)

    # 微信登录
    def WeiChat_login(self):
        self.initial_element()
        get_element(self.driver, self.weiChat_login_locator).click()

    # 前往微信界面
    def Go_WeiChat(self):
        self.initial_element()
        get_element(self.driver, self.go_weichat_locator).click()



