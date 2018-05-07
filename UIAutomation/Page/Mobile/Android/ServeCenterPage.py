from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage

class ServeCenterPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
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
        namelist = ["confirmButton", "fourButton"]
        ele_dic = page_element_factory(__file__, namelist)
        self.confirm_button_element = get_element(self.driver, ele_dic['confirmButton'])  # 选择类别框
        self.four_button_element = get_element(self.driver, ele_dic['fourButton'])  # 第四个选择框

    def is_loaded(self):
        pass

    def get_confirm_button(self):
        self.initial_element()
        return self.confirm_button_element

    def get_four_button(self):
        self.initial_element()
        return self.four_button_element