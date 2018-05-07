# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Utils import ParseXmlErrorException, sleep
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory
from UIAutomation.TestCase.SIT.Mobile.RegisteredBusinessContacts.RegisteredBusinessContacts_sql import get_first_info, get_second_info, clear_first_sql, clear_second_sql, get_second_empty_info

__author__ = "xuwangchao"
__doc__ = "注册联系人第2页"


class RegisteredBusinessContactsTwoPage(BasePage):
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
            name_list = ['faren', 'tongyishehui', 'yingyezhizhao', 'zuzhijigoudaima', 'suiwudengjihao', 'ok_button']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.faren_locator = ele_dic['faren']
            self.tongyishehui_locator = ele_dic['tongyishehui']
            self.yingyezhizhao_locator = ele_dic['yingyezhizhao']
            self.zuzhijigoudaima_locator = ele_dic['zuzhijigoudaima']
            self.suiwudengjihao_locator = ele_dic['suiwudengjihao']
            self.ok_button_locator = ele_dic['ok_button']
            pass
        # Android独立控件
        if not self.is_run_ios():
            name_list = ['faren', 'tongyishehui', 'yingyezhizhao', 'zuzhijigoudaima', 'suiwudengjihao', 'ok_button']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.faren_locator = ele_dic['faren']
            self.tongyishehui_locator = ele_dic['tongyishehui']
            self.yingyezhizhao_locator = ele_dic['yingyezhizhao']
            self.zuzhijigoudaima_locator = ele_dic['zuzhijigoudaima']
            self.suiwudengjihao_locator = ele_dic['suiwudengjihao']
            self.ok_button_locator = ele_dic['ok_button']
            pass

    def is_loaded(self):
        pass

    def assert_sql(self):
        if self.is_run_ios():
            self.assert_sql_empty()
            pass
        if not self.is_run_ios():
            list_one = get_first_info()
            set_two = get_second_info()
            print(list_one)
            print(set_two)
            lianxiren_mobile_expect = list_one["lianxiren_mobile"]
            duijieren_expect = list_one["duijieren"]
            lianxiren_expect = list_one["lianxiren"]
            location_expect = list_one["location"]
            duizhangren_expect =list_one["duizhangren"]
            jiedanren_expect = list_one["jiedanren"]
            print("开始assert")
            assert "123456789012345" in set_two
            assert "公司名称好" in set_two
            print("开始继续assert")
            assert lianxiren_mobile_expect == '12345678'
            assert duijieren_expect == '对接人好'
            assert lianxiren_expect == '联系人好'
            assert location_expect == '浙江省杭州市江干区白杨街道科技园路新加坡科技园2号楼'
            assert duizhangren_expect == '对账人好'
            assert jiedanren_expect == '接单人好'
            pass

    def assert_sql_empty(self):
        empty_set = get_second_empty_info()
        assert "公司名称好" in empty_set
        pass

    def assert_second_page(self):
        """
        判断是不是在第二章卡片了
        :return:
        """
        if self.is_run_ios():
            self._assert_second_page_ios()
        if not self.is_run_ios():
            self._assert_second_page_android()
        pass

    def type_second_page(self):
        """
        在第二章卡片中输入
        :return:
        """
        if self.is_run_ios():
            print("ios上第二页搞不定hide_keyboard")
        if not self.is_run_ios():
            self._type_second_android()
        pass

    def click_ok_button(self):
        """
        点击完成按钮
        """
        self.action.click(self.ok_button_locator)
        pass

    def haha(self):
        self.driver.set_connecttu
        pass
    
    def _assert_second_page_ios(self):
        """
        ios上的判断有没有到了第2个页面
        :return:
        """
        assert self.action.is_element_present(self.faren_locator)
        assert self.action.is_element_present(self.tongyishehui_locator)
        assert self.action.is_element_present(self.yingyezhizhao_locator)
        assert self.action.is_element_present(self.zuzhijigoudaima_locator)
        assert self.action.is_element_present(self.suiwudengjihao_locator)
        assert self.action.is_element_present(self.ok_button_locator)
        pass
    
    def _assert_second_page_android(self):
        """
        android上的判断有没有到了第2个页面
        """
        assert self.action.is_element_present(self.faren_locator)
        assert self.action.is_element_present(self.tongyishehui_locator)
        assert self.action.is_element_present(self.yingyezhizhao_locator)
        assert self.action.is_element_present(self.zuzhijigoudaima_locator)
        assert self.action.is_element_present(self.suiwudengjihao_locator)
        assert self.action.is_element_present(self.ok_button_locator)
        assert self.action.is_element_present(self.btn_license_locator)
        pass

    def _type_second_page_ios(self):
        self.action.send_keys(self.tongyishehui_locator, "1234567890123")
        self.action.send_keys(self.yingyezhizhao_locator, "1234567890")
        self.action.send_keys(self.zuzhijigoudaima_locator, "123456789012345")
        self.action.send_keys(self.suiwudengjihao_locator, "123456789012345")
        self.action.send_keys(self.faren_locator, "公司法人好")
        sleep(5)
        self.driver.hide_keyboard()
        # self.driver.hide_keyboard()
        # self.driver.hide_keyboard()
        pass

    def _type_second_page_android(self):
        """
        android的第二个页面输入
        """
        self.driver.find_element_by_xpath("//*[@text='税务登记号']").send_keys(str("123456789012345"))
        # self.driver.find_element_by_xpath("//*[@text='组织机构代码']")[-1].send_keys(str("123456789012345"))
        # self.driver.find_element_by_xpath("//*[@text='营业执照注册号']")[-2].send_keys(str("1234567890"))
        # self.driver.find_element_by_xpath("//*[@text='统一社会信用代码']")[-3].send_keys(str("1234567890123"))
        # self.driver.find_element_by_xpath("//*[@text='公司法人']")[-4].send_keys(str("123456789012345678"))
        pass





