from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class ServeTypeTitleText(BasePage):
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
        namelist = ["serveTypeTitleText"]
        ele_dic = page_element_factory(__file__, namelist)
        self.serve_type_title_text_element = get_element(self.driver, ele_dic['serveTypeTitleText'])  # 选择类别框

    def is_loaded(self):
        pass

    def get_serve_type_title_text(self):
        self.initial_element()
        return self.serve_type_title_text_element