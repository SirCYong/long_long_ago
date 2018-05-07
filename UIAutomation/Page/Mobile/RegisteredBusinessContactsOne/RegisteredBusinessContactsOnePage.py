# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Utils import ParseXmlErrorException, sleep
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory

__author__ = "xuwangchao"
__doc__ = "注册联系人第一页"


class RegisteredBusinessContactsOnePage(BasePage):
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
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ['LongTaskCard']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.long_task_card_locator = ele_dic['LongTaskCard']


        # IOS独立控件
        if self.is_run_ios():
            name_list = ['business_name', 'duijieren', 'lianxiren', 'lianxiren_mobile', 'jiedanren', 'duizhangren',
                         'next_button', "choose_location", "location_edit_text", "location_text_first"]
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.business_name_locator = ele_dic['business_name']
            self.duijieren_locator = ele_dic['duijieren']
            self.lianxiren_locator = ele_dic['lianxiren']
            self.lianxiren_mobile_locator = ele_dic['lianxiren_mobile']
            self.jiedanren_locator = ele_dic['jiedanren']
            self.duizhangren_locator = ele_dic['duizhangren']
            self.next_button_locator = ele_dic['next_button']
            self.choose_location_locator = ele_dic['choose_location']
            self.location_edit_text_locator = ele_dic['location_edit_text']
            self.location_text_first_locator = ele_dic['location_text_first']
            pass
        # Android独立控件
        if not self.is_run_ios():
            name_list = ['business_name', 'duijieren', 'lianxiren', 'lianxiren_mobile', 'jiedanren', 'duizhangren', 'next_button', "location_warn_text", "choose_location", "location_edit_text", "location_text_first"]
            ele_dic = page_element_factory(self.xml_file, name_list)
            # self.business_name_locator = ele_dic['business_name']
            # self.duijieren_locator = ele_dic['duijieren']
            # self.lianxiren_locator = ele_dic['lianxiren']
            # self.lianxiren_mobile_locator = ele_dic['lianxiren_mobile']
            # self.jiedanren_locator = ele_dic['jiedanren']
            # self.duizhangren_locator = ele_dic['duizhangren']
            # self.next_button_locator = ele_dic['next_button']
            # self.location_warn_text_locator = ele_dic['location_warn_text']
            # self.choose_location_locator = ele_dic['choose_location']
            # self.location_edit_text_locator = ele_dic['location_edit_text']
            # self.location_text_first_locator = ele_dic['location_text_first']
            pass

    def assert_first_page(self):
        """
        判断有没有到第一页
        :return:
        """
        if self.is_run_ios():
            self._assert_first_page_ios()
        if not self.is_run_ios():
            self._assert_first_page_android()

    def is_loaded(self):
        pass
    
    def _assert_first_page_ios(self):
        """
        ios上的判断有没有到了第一个页面
        :return:
        """
        assert self.action.is_element_present(self.business_name_locator)
        assert self.action.is_element_present(self.duijieren_locator)
        assert self.action.is_element_present(self.lianxiren_locator)
        assert self.action.is_element_present(self.lianxiren_mobile_locator)
        assert self.action.is_element_present(self.jiedanren_locator)
        assert self.action.is_element_present(self.duizhangren_locator)
        assert self.action.is_element_present(self.next_button_locator)
        assert self.action.is_element_present(self.choose_location_locator)
        assert self.action.is_element_present(self.location_edit_text_locator)
        pass
    
    def _assert_first_page_ios(self):
        """
        ios上的判断有没有到了第一个页面
        :return:
        """
        LongCardPage(self.driver).click_long_task_card()

    def _assert_first_page_android(self):
        """
        android上的判断有没有到了第一个页面
        """
        assert self.action.is_element_present(self.business_name_locator)
        assert self.action.is_element_present(self.duijieren_locator)
        assert self.action.is_element_present(self.lianxiren_locator)
        assert self.action.is_element_present(self.lianxiren_mobile_locator)
        assert self.action.is_element_present(self.jiedanren_locator)
        assert self.action.is_element_present(self.duizhangren_locator)
        assert self.action.is_element_present(self.next_button_locator)
        assert self.action.is_element_present(self.location_warn_text_locator)
        assert self.action.is_element_present(self.choose_location_locator)
        assert self.action.is_element_present(self.location_edit_text_locator)
        pass

    def type_first_page(self):
        if self.is_run_ios():
            self._type_first_page_ios()
        else:
            self._type_first_page_android()
        pass

    def choose_location(self):
        if self.is_run_ios():
            self._choose_location_ios()
        else:
            self._choose_location_android()
        pass
    
    def _type_first_page_ios(self):
    #  	"""
    #      ios上在第一章卡片上输入完整信息
    #  	"""
        print("ios上在第一章卡片上输入完整信息")
        self.action.send_keys(self.business_name_locator, "公司名称好")
        self.action.send_keys(self.duijieren_locator, "对接人好")
        self.action.send_keys(self.lianxiren_locator, "联系人好")
        self.action.send_keys(self.lianxiren_mobile_locator, "12345678")
        self.action.send_keys(self.jiedanren_locator, "接单人好")
        self.action.send_keys(self.duizhangren_locator, "对账人好")
        sleep(5)
        self.driver.hide_keyboard()
        pass
    
    def _choose_location_ios(self):
        """
    	ios上在第一页点击选择地址进入地图页面，并选择第一个地址。
		"""
        self.action.click(self.choose_location_locator)
        time.sleep(5)
        self.action.click(self.location_text_first_locator)
        pass
    
    def _type_first_page_android(self):
        """
        android上在第一章卡片上输入完整信息
        """
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[0].clear()
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[0].send_keys(str("公司名称好"))
        # self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[1].clear()
        # self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[1].send_keys(str("详细地址好"))
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[2].clear()
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[2].send_keys(str("对接人好"))
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[3].clear()
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[3].send_keys(str("联系人好"))
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[4].clear()
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[4].send_keys(str("12345678"))
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[5].clear()
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[5].send_keys(str("接单人好"))
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[6].clear()
        self.driver.find_elements_by_id("com.iscs.mobilewcs:id/edit_text")[6].send_keys(str("对账人好"))
        pass


    def _choose_location_android(self):
        """
        android上在第一页点击选择地址进入地图页面，并选择第一个地址。
        """
        self.action.click(self.choose_location_locator)
        time.sleep(5)
        self.action.click(self.location_text_first_locator)
        # self.driver.find_elements_by_id("com.iscs.mobilewcs:id/active_entry_item_local_img")[0].click()
        pass


    def click_next_button(self):
        print("点击下一步的按钮")
        self.action.click(self.next_button_locator)
        pass




