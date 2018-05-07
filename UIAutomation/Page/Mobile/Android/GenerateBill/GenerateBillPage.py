# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, GlobalVar, ParseXmlErrorException, run_info_log
from UIAutomation.page import BasePage
from UIAutomation.TestCase.SIT.Android.Sprint7.FUNGenerateBillSQL import get_bill_info, get_generate_bill_result

__author__ = "xuwangchao"


class GenerateBillPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.generate_bill_name_locator = None
        self.generate_bill_total_locator = None
        self.generate_bill_button_locator = None
        self.generate_bill_time_locator = None
        self.traffic_type_locator = None
        self.bill_type_locator = None
        try:
            self.initial_element()
        except ParseXmlErrorException:
            print (u'XML解析失败.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'XML解析失败.', GlobalVar.get_log_file())
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            print (u'控件不在当前页面上.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'控件不在当前页面上.', GlobalVar.get_log_file())
            raise
        pass

    def page_factory(self):
        name_list = ['generate_bill_name', 'generate_bill_total',
                     'generate_bill_button', 'generate_bill_time',
                     'traffic_type', 'bill_type ']
        ele_dic = page_element_factory(__file__, name_list)
        self.generate_bill_name_locator = ele_dic['generate_bill_name']
        self.generate_bill_total_locator = ele_dic['generate_bill_total']
        self.generate_bill_button_locator = ele_dic['generate_bill_button']
        self.generate_bill_time_locator = ele_dic['generate_bill_time']
        # self.traffic_bill_locator = ele_dic['traffic_bill']
        # self.storage_bill_locator = ele_dic['storage_bill']
        self.traffic_type_locator = ele_dic['traffic_type']
        self.bill_type_locator = ele_dic['bill_type']
        pass

    def is_loaded(self):
        pass

    def assert_generate_bill_sql(self):
        """
        验证生成账单页面元素
        """
        self.initial_element()
        ele_bill_sql = get_bill_info()
        expect_title_name = ele_bill_sql['name']
        expect_start_time = ele_bill_sql['start_time']
        expect_end_time = ele_bill_sql['end_time']
        expect_time = expect_start_time + " ~ " + expect_end_time
        expect_total = ele_bill_sql['total']
        real_title = self.action.text(self.generate_bill_name_locator)
        real_title_name = real_title[2: len(real_title) - 4]
        real_time = self.action.text(self.generate_bill_time_locator)
        real_total = self.action.text(self.generate_bill_total_locator)
        # real_traffic_bill = self.action.text(self.traffic_bill_locator)
        # real_storage_bill = self.action.text(self.storage_bill_locator)
        print(expect_title_name + ' ' + expect_time + " " + expect_total)
        print(type(expect_title_name))
        print(type(expect_time))
        print(type(expect_total))
        print(type(real_title_name.encode('utf-8')))
        print(type(real_time))
        print(type(real_total))
        assert real_title_name.encode('utf-8') == expect_title_name
        assert real_time.encode('utf-8') == expect_time
        assert real_total.encode('utf-8') == expect_total
        # if 'WA' in ele_bill_sql.iterkeys():
        #     wa_price = str(ele_bill_sql['WA'])
        # if 'TR' in ele_bill_sql.iterkeys():
        #     tr_price = str(ele_bill_sql['TR'])
        pass

    def get_generate_bill_result_sql(self):
        """
        点击"生成应付账单"后验证SQL结果
        """
        self.initial_element()
        ele_bill_result_sql = get_generate_bill_result()
        fee_no = ele_bill_result_sql["fee_no"]
        bill_no = ele_bill_result_sql["bill_no"]
        record_no = ele_bill_result_sql["record_no"]
        assert fee_no == 0 and bill_no == 1 and record_no == 2
        pass

    def click_generate_bill_button(self):
        """
        点击生成账单按钮
        """
        self.initial_element()
        self.action.click(self.generate_bill_button_locator)






