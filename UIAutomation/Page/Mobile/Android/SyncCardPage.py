# language  zh-CN
# Author: yuetianzhuang


from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class SyncCardPage(BasePage):

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

    def is_loaded(self):
        pass

    def page_factory(self):

        name_list = ['syncOpenBtn']
        try:
            element_metadata_dict = page_element_factory(__file__, name_list)
            self.syncOpenBtn_element = get_element(self.driver, element_metadata_dict['syncOpenBtn'])

        except Exception as e:
            assert False
            pass

    def ClickSyncOpenBtn(self):

        self.initial_element()
        self.syncOpenBtn_element.click()
        pass