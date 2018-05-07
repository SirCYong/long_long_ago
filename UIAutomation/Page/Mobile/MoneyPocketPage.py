# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.TestCase.SIT.Mobile.BillList.BillList_sql import get_bill_info
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException

__author__ = "xuwangchao"
__doc__ = "钱仓页面"


class MoneyPocketPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        if self.is_run_ios():
            self.xml_file = __file__[:__file__.rfind(".")] + "IOS.xml"
        else:
            self.xml_file = __file__[:__file__.rfind(".")] + "Android.xml"

        try:
            self.initial_element()
        except ParseXmlErrorException:
            # screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            # self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            # print("错误截图：")
            # print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            # run_info_log(u'XML解析失败.', GlobalVar.get_log_file())
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            print(u'控件不在当前页面上.')
            # screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            # self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            # print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            # run_info_log(u'控件不在当前页面上.', GlobalVar.get_log_file())
            raise
        pass

    def page_factory(self):
        """
        初始化页面控件
        """
        # 2端统一的控件
        # name_list = ['login_button', 'user_name', 'password']
        # ele_dic = page_element_factory(self.xml_file, name_list)
        # self.login_button_locator = ele_dic['login_button']
        # self.user_name_locator = ele_dic['user_name']
        # self.password_locator = ele_dic['password']

        # IOS独立的控件
        if self.is_run_ios():
            name_list = ['bound', 'long_task', 'manage_authorize']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.bound_locator = ele_dic['bound']
            self.long_task_locator = ele_dic['long_task']
            self.manage_authorize_locator = ele_dic['manage_authorize']

        # Android独立的控件
        if not self.is_run_ios():
            name_list = ['wallet_uncheckout_count', 'wallet_uncheckout_count_text',
                         'wallet_left_advance_text', 'wallet_left_advance',
                         'wallet_left_deposit_text', 'wallet_left_deposit']
            ele_dic = page_element_factory(self.xml_file, name_list)


            # 动态数字:账单数量
            self.wallet_uncheckout_count_locator = ele_dic['wallet_uncheckout_count']
            # 静态文字:份
            self.wallet_uncheckout_count_text_locator = ele_dic['wallet_uncheckout_count_text']


            # 静态文字:现存预付款
            self.wallet_left_advance_text_locator = ele_dic['wallet_left_advance_text']
            # 动态数字:现存预付款
            self.wallet_left_advance_locator = ele_dic['wallet_left_advance']


            # 静态文字:现存保证金
            self.wallet_left_deposit_text_locator = ele_dic['wallet_left_deposit_text']
            # 动态数字:现存保证金
            self.wallet_left_deposit_locator = ele_dic['wallet_left_deposit']

    def is_loaded(self):
        pass

    def click_bill_unliquidated(self):
        """
        在钱仓页面点击未结算的账单
        """
        if self.is_run_ios():
            print(u"在跑iOS的")
        else:
            self._click_bill_unliquidated_android()
        pass

    def assert_my_monney(self):
        print('验证钱仓中的页面元素')
        print('验证钱仓中的页面元素')
        print('验证钱仓中的页面元素')
        print('验证钱仓中的页面元素')
        print('验证钱仓中的页面元素')

        """
        验证钱仓中的页面元素
        """
        if self.is_run_ios():
            print(u"在跑iOS的")
        else:
            self._assert_my_monney_android()
        pass

    def _assert_my_monney_android(self):
        """
        android私有方法
        验证钱仓中的页面元素
        """
        print('_assert_my_monney_android')
        print('_assert_my_monney_android')
        print('_assert_my_monney_android')
        print('_assert_my_monney_android')
        print('_assert_my_monney_android')

        wallet_uncheckout_count_expect = self.action.text(self.wallet_uncheckout_count_locator)
        print('wallet_uncheckout_count_expect:', wallet_uncheckout_count_expect)
        wallet_left_advance_expect = self.action.text(self.wallet_left_advance_locator)
        print('wallet_left_advance_expect', wallet_left_advance_expect)
        wallet_left_deposit_expect = self.action.text(self.wallet_left_deposit_locator)
        print('wallet_left_deposit_expect', wallet_left_deposit_expect)

        ele_dic_my_monney = get_bill_info()
        print('ele_dic_my_monney', ele_dic_my_monney)

        wallet_uncheckout_count_real = ele_dic_my_monney['unliquidated_counts']
        print('wallet_uncheckout_count_real', wallet_uncheckout_count_real)
        wallet_left_advance_real = ele_dic_my_monney['wallet_left_advance']
        print('wallet_left_advance_real', wallet_left_advance_real)
        wallet_left_deposit_real = ele_dic_my_monney['wallet_left_deposit']
        print('wallet_left_deposit_real', wallet_left_deposit_real)

        assert wallet_uncheckout_count_expect == wallet_uncheckout_count_real
        assert wallet_left_advance_expect == wallet_left_advance_real
        assert wallet_left_deposit_expect == wallet_left_deposit_real
        pass

    def _click_bill_unliquidated_android(self):
        """
        android 私有方法
        在钱仓页面点击未结算的账单
        """
        self.action.click(self.wallet_uncheckout_count_locator)
        pass

