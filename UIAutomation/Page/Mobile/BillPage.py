# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.TestCase.SIT.Mobile.BillList.BillList_sql import get_bill_list_detail_info
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException


__author__ = "xuwangchao"
__doc__ = "账单页面"


class BillPage(BasePage):
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
            name_list = ['week', 'day', 'sum', 'name', 'type', 'all', 'receivable', 'payable']
            ele_dic = page_element_factory(self.xml_file, name_list)
            # 动态文字日期:周几
            self.week_locator = ele_dic['week']
            # 动态数字日期:XX-XX
            self.day_locator = ele_dic['day']
            # 动态账单金额
            self.sum_locator = ele_dic['sum']
            # 动态用户名
            self.name_locator = ele_dic['name']
            # 动态款项是否结算
            self.type_locator = ele_dic['type']
            # fragment:全部
            self.all_locator = ele_dic['all']
            # fragment:应收
            self.receivable_locator = ele_dic['receivable']
            # fragment:应付
            self.payable_locator = ele_dic['payable']

    def is_loaded(self):
        pass

    def is_bill_page(self):
        """
        判断是否到达了账单页面
        """
        if self.is_run_ios():
            print(u"正在跑iOS")
        else:
            self._is_bill_page_android()

    def assert_bill(self):
        """
        通过账单页面的时间(周几/日期),账单金额,用户名,款项是否已经结算来判断
        """
        if self.is_run_ios():
            print(u"正在跑iOS")
        else:
            self._assert_bill_android()
        pass

    def _is_bill_page_android(self):
        """
        android私有方法
        判断是否到达了账单页面
        """
        week_locator_exists = self.action.is_element_present(self.week_locator)
        day_locator_exists = self.action.is_element_present(self.day_locator)
        sum_locator_exists = self.action.is_element_present(self.sum_locator)
        name_locator_exists = self.action.is_element_present(self.name_locator)
        type_locator_exists = self.action.is_element_present(self.type_locator)
        all_locator_exists = self.action.is_element_present(self.all_locator)
        receivable_locator_exists = self.action.is_element_present(self.receivable_locator)
        payable_locator_exists = self.action.is_element_present(self.payable_locator)
        assert week_locator_exists
        assert day_locator_exists
        assert sum_locator_exists
        assert name_locator_exists
        assert type_locator_exists
        assert all_locator_exists
        assert receivable_locator_exists
        assert payable_locator_exists

    def _assert_bill_android(self):
        """
        android私有方法
        通过账单页面的时间(周几/日期),账单金额,用户名,款项是否已经结算来判断
        """
        bill_detail_sql = get_bill_list_detail_info()
        print(bill_detail_sql)
        counts = len(bill_detail_sql)
        for i in range(counts):
            if i == 6:
                break
            bill_detail_dic = bill_detail_sql[i]
            print("第-------------------" + str(i) + "----------------------次")
            day_expect = (self.action.text(self.day_locator, i))
            sum_expect = (self.action.text(self.sum_locator, i))
            print('sum_expect', sum_expect)
            print('sum_expect', sum_expect)
            print('sum_expect', sum_expect)

            name_expect = (self.action.text(self.name_locator, i))
            if bill_detail_dic['bill_status'] == 0:
                type_expect = self.action.text(self.type_locator, i)
                assert type_expect == '款项未结算'
            if bill_detail_dic['bill_status'] == 100:
                if not self.action.is_element_present(self.type_locator):
                    pass
                else:
                    assert False

            sum_real = bill_detail_dic['bill_money']
            print('sum_real', sum_real)
            print('sum_real', sum_real)
            print('sum_real', sum_real)

            day_real_before = str(bill_detail_dic['create_time'])
            day_real = day_real_before[day_real_before.find('-') + 1:day_real_before.find(' ')]
            name_real = bill_detail_dic['user_name']
            print('开始单个判断了')
            print('开始单个判断了')
            print('开始单个判断了')
            print('开始单个判断了')
            print('开始单个判断了')
            print(sum_real == sum_expect)
            print(day_real == day_expect)
            print(name_expect == name_real)
            assert sum_real == sum_expect and day_real == day_expect and name_expect == name_real
            print('单个判断结束了')
            print('单个判断结束了')
            print('单个判断结束了')
            print('单个判断结束了')
            print('单个判断结束了')

            pass
