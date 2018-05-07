# 管理收货地址
#  Cy
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.ActivationDepot.DepotMapPage import DepotMapPage
from UIAutomation.Utils import ParseXmlErrorException, GlobalVar, logger, page_element_factory, sleep, \
    is_element_present, initial_element_error_wrapper


class ManageAddressPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_add_address_locator = None
        self.input_nike_name_locator = None
        self.input_name_locator = None
        self.click_mobile_locator = None
        self.click_choice_locator = None
        self.click_save_locator = None
        try:
            self.is_loaded()
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
        name_list = ('addAddress', 'addressNikeName', 'name', 'mobile', 'clickChoice', 'save')
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.click_add_address_locator = ele_dic['addAddress']
        self.input_nike_name_locator = ele_dic['addressNikeName']
        self.input_name_locator = ele_dic['name']
        self.click_mobile_locator = ele_dic['mobile']
        self.click_choice_locator = ele_dic['clickChoice']
        self.click_save_locator = ele_dic['save']

    def is_loaded(self):

        pass

    def address_input_information(self):
        if self.is_run_ios():
            self._address_input_information_ios()
        else:
            self._address_input_information_android()
        pass

    def _address_input_information_ios(self):
        self.action.click(self.click_add_address_locator)
        # self.driver.find_element_by_accessibility_id('添加地址').click()
        # sleep(1)
        self.action.set_value(self.input_nike_name_locator, 'pd')
        # self.driver.find_element_by_xpath(
        #     '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]').set_value(
        #     'pd')
        # sleep(1)
        self.action.set_value(self.input_name_locator, '冯二婷')
        # self.driver.find_element_by_xpath(
        #     '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]/UIATextField[1]').set_value(
        #     '故事')
        # sleep(1)
        self.action.set_value(self.click_mobile_locator, '18888000131')
        # self.driver.find_element_by_xpath(
        #     '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[3]/UIATextField[1]').set_value(
        #     '18888000131')
        # sleep(1)
        self.action.click(self.click_choice_locator)
        DepotMapPage(self.driver).map_first()
        self.action.click(self.click_save_locator)
        pass

    def _address_input_information_android(self):
        self.action.click(self.click_add_address_locator)
        self.action.send_keys(self.input_nike_name_locator, 'pd')
        self.action.send_keys(self.input_name_locator, '冯二婷')
        self.action.send_keys(self.click_mobile_locator, '18888000131')
        self.action.click(self.click_choice_locator)
        DepotMapPage(self.driver).map_first()
        self.action.click(self.click_save_locator)
        pass
