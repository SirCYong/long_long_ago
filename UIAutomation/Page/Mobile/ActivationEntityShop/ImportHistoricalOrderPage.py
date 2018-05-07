from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'CaoYong'


class ImportHistoricalOrderPage(BasePage):
    """
    激活里面的地图选择
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.browser = driver
        self.input_name_locator = None
        self.input_password_locator = None
        self.confirm_button_locator = None
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
        name_list = ('inputUserId', 'inputPassword', 'confirmButton')
        ele_dic = page_element_factory(__file__, name_list)
        self.input_name_locator = ele_dic['inputUserId']
        self.input_password_locator = ele_dic['inputPassword']
        self.confirm_button_locator = ele_dic['confirmButton']
        pass

    def is_loaded(self):

        pass

    def web_historical_order(self, admin=None, password=None):
        self.browser.get('http://192.168.6.32/login')
        self.browser.maximize_window()
        get_element(self.driver, self.input_name_locator).send_keys(admin)
        get_element(self.driver, self.input_password_locator).send_keys(password)
        get_element(self.driver, self.confirm_button_locator).click()
        pass
