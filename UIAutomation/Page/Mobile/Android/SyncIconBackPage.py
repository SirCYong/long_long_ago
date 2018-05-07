# language  zh-CN
# Author: yue

from selenium.common.exceptions import NoSuchWindowException
from time import sleep
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage


class SyncIconBack(BasePage):
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

    def is_loaded(self):

        pass

    def page_factory(self):

        name_list = ['icon_back']
        element_metadata_dict = page_element_factory(__file__, name_list)

        print(element_metadata_dict)

        self.icon_back_element = get_element(self.driver, element_metadata_dict['icon_back'])

        pass

    def IconBack_Button(self):

        self.initial_element()

        self.icon_back_element.click()
        sleep(2)

        pass
