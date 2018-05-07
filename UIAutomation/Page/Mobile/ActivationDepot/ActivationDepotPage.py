# -*- coding: utf-8 -*-
# 激活仓库
#  Cy
import time

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.ActivationDepot.DepotMapPage import DepotMapPage
from UIAutomation.Utils import ParseXmlErrorException, GlobalVar, page_element_factory, sleep, \
    is_element_present, initial_element_error_wrapper


class ActivationDepotPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
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
        name_list = ('depotName', 'depotAddress', 'depotAreaButton', 'depotAreaText', 'depotRentButton', 'depotRentText',
                     'depotRentAdd', 'depotMap', 'depotActivation', 'finishButton', 'ok', 'inputDepotRent')
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.input_depot_name_locator = ele_dic['depotName']
        self.input_depot_address_locator = ele_dic['depotAddress']
        self.input_depot_area_button_locator = ele_dic['depotAreaButton']
        self.input_depot_area_text_locator = ele_dic['depotAreaText']
        self.click_depot_rent_locator = ele_dic['depotRentButton']
        self.input_depot_rent_locator = ele_dic['depotRentText']
        self.click_depot_rent_add_locator = ele_dic['depotRentAdd']
        self.click_map_locator = ele_dic['depotMap']
        self.click_depot_activation_locator = ele_dic['depotActivation']
        self.click_finish_button_locator = ele_dic['finishButton']
        self.click_ok_locator = ele_dic['ok']

    def is_loaded(self):

        pass

    def depot_input_information(self):
        if self.is_run_ios():
            self._depot_input_information_ios()
        else:
            self._depot_input_information_android()
        pass

    def _depot_input_information_ios(self):
        self.action.set_value(self.input_depot_name_locator, u'起的隆冬强1')
        self.action.set_value(self.input_depot_address_locator, '下沙')
        self.action.set_value(self.click_depot_rent_locator, 346)
        self.action.set_value(self.input_depot_area_text_locator, 56515)
        self.action.click(self.click_map_locator)
        sleep(2)
        DepotMapPage(self.driver).map_first()
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '完成')):
            sleep(1)
            self.action.click(self.click_finish_button_locator)
        sleep(1)
        self.action.click(self.click_depot_activation_locator)
        sleep(3)
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '激活成功'))
        self.action.click(self.click_ok_locator)
        pass

    def _depot_input_information_android(self):
        self.action.click(self.click_map_locator)
        sleep(2)
        DepotMapPage(self.driver).map_first()
        self.action.send_keys(self.input_depot_name_locator, u'起的隆冬强1')
        self.action.send_keys(self.input_depot_address_locator, '下沙')
        # self.action.send_keys(self.input_depot_area_locator, '56515')
        # get_element(self.driver, self.input_depot_area_locator).send_keys(56515)
        self.action.click(self.input_depot_area_button_locator)
        self.action.send_keys(self.input_depot_area_text_locator, '56515')
        self.action.click(self.click_depot_rent_locator)
        # self.action.send_keys(self.input_depot_rent_locator, '123')
        self.action.clear(self.input_depot_rent_locator)
        self.action.send_keys(self.input_depot_rent_locator, '123')
        self.action.click(self.click_depot_rent_add_locator, [4])

        # self.driver.find_element_by_xpath("//*[@resource-id='active_entry_map_title' and @text='科技园路']").click()
        # self.action.click(self.click_depot_activation_locator)
        self.action.click(self.click_ok_locator)
        assert is_element_present(self.driver, ("XPATH", "//*[@resource-id='com.iscs.mobilewcs:id/"
                                                         "iv_active_goods_ok_txt' and @text='成功激活']"))
        pass

