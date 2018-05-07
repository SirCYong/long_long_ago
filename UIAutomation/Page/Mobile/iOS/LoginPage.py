from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, is_element_present

__author__ = 'zhongchangwei'
#__updateauthor__ = 'chenyanxiu'
# Context: changed login method


class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.login_button_locator = None
        self.user_name_locator = None
        self.password_locator = None
        self.bound_locator = None

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
        name_list = ['login_button', 'user_name', 'password', 'bound']
        ele_dic = page_element_factory(__file__, name_list)
        self.login_button_locator = ele_dic['login_button']
        self.user_name_locator = ele_dic['user_name']
        self.password_locator = ele_dic['password']
        self.bound_locator = ele_dic['bound']
        pass

    def is_loaded(self):
        pass

    def login(self, username=None, password=None):
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '微信登录')):
            if username:
                self.action.set_value(self.user_name_locator, username)
                sleep(1)
            if password:
                self.action.set_value(self.password_locator, password)
                if is_element_present(self.driver, ('ACCESSIBILITY_ID', '完成')):
                    sleep(1)
                    self.action.click(('ACCESSIBILITY_ID', '完成'))
            self.action.click(self.login_button_locator)
            sleep(2)
            if is_element_present(self.driver, ('ACCESSIBILITY_ID', '绑定')):
                sleep(4)
                self.action.click(('ACCESSIBILITY_ID', '绑定'))
            pass
        # self.initial_element()
        # if username:
        #     self.action.set_value(self.user_name_locator, username)
        #     sleep(1)
        # if password:
        #     self.action.set_value(self.password_locator, password)
        #     if is_element_present(self.driver, ('ACCESSIBILITY_ID', '完成')):
        #         sleep(1)
        #         self.action.click(('ACCESSIBILITY_ID', '完成'))
        # self.action.click(self.login_button_locator)
        # sleep(2)
        # if is_element_present(self.driver, ('ACCESSIBILITY_ID', '绑定')):
        #     sleep(4)
        #     self.action.click(('ACCESSIBILITY_ID', '绑定'))




