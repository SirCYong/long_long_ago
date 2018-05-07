from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'zhoujin'


class ManagementBusinessUnit(BasePage):
    """
    管理业务单位
    假定已经创建过一个以及业务单位
    """
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
        name_list = ['province', 'city', 'county']
        ele_dic = page_element_factory(__file__, name_list)

        pass

    def is_loaded(self):
        pass