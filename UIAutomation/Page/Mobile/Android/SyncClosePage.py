# language: zh_CN

# Author: yue
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage

class CloseSyncPage(BasePage):

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
        
        name_list = ['CloseSyncBtn']
        element_metadata_dict = page_element_factory(__file__, name_list)
        self.CloseSyncBtn_element = get_element(self.driver, element_metadata_dict['CloseSyncBtn'])
        pass
        
    def click_CloseSyncBtn(self):

        self.initial_element()
        self.CloseSyncBtn_element.click()
        pass 

