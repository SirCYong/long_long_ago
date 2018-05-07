# language  zh-CN
# Author: Cy
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class SelectTypeBox(BasePage):
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
        namelist = ["selectTypeBox"]
        ele_dic = page_element_factory(__file__, namelist)
        self.select_type_box_element = get_element(self.driver, ele_dic['selectTypeBox'])  # 登录按钮

    def is_loaded(self):
        pass

    def get_select_type_box(self):
        self.initial_element()
        return self.select_type_box_element