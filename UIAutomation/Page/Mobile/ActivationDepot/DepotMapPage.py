from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, initial_element_error_wrapper
from UIAutomation.Page import BasePage
__author__ = 'CaoYong'


class DepotMapPage(BasePage):
    """
    激活仓库（地图操作）
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.initial_element()
        except ParseXmlErrorException:
            initial_element_error_wrapper(self.driver)
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        name_list = ['mapFirst']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.get_map_first_locator = ele_dic['mapFirst']

    def is_loaded(self):

        pass

    def map_first(self):
        if self.is_run_ios():
            self._map_first_IOS()
        else:
            self._map_first_android()
        pass

    def _map_first_IOS(self):
        self.action.click(self.get_map_first_locator)
        pass

    def _map_first_android(self):
        self.action.click(self.get_map_first_locator, [1])
        # self.driver.find_element_by_xpath("//*[@resource-id='com.iscs.mobilewcs:id/actie_storehouse_recyclerview_id']")
        pass
