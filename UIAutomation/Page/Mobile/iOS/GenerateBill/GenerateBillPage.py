# -*- coding: utf-8 -*-
from time import sleep, time
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory,  ParseXmlErrorException, GlobalVar, run_info_log
from UIAutomation.Page import BasePage
from UIAutomation.TestCase.SIT.iOS.Sprint7.FUNGenerateBillSQL import get_bill_info, get_generate_bill_result

__author__ = "xuwangchao"


class GenerateBillPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.initial_element()
        except ParseXmlErrorException:
            print (u'XML解析失败.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time()) + "_screenshot.png"
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
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'控件不在当前页面上.', GlobalVar.get_log_file())
            raise
        pass

    def page_factory(self):
        name_list = ['generate_bill_name', 'generate_bill_total', 'generate_bill_button', 'generate_bill_time',
                     'traffic_bill', 'storage_bill']
        ele_dic = page_element_factory(__file__, name_list)
        self.generate_bill_name_locator = ele_dic['generate_bill_name']
        self.generate_bill_total_locator = ele_dic['generate_bill_total']
        self.generate_bill_button_locator = ele_dic['generate_bill_button']
        self.generate_bill_time_locator = ele_dic['generate_bill_time']
        self.traffic_bill_locator = ele_dic['traffic_bill']
        self.storage_bill_locator = ele_dic['storage_bill']
        pass

    def is_loaded(self):
        pass

    def get_element_from_sql(self):
        """
        验证生成账单页面元素
        """
        self.initial_element()
        ele_bill_sql = get_bill_info()
        print(ele_bill_sql)
        expect_title = u"给".encode('utf-8') + ele_bill_sql['name'] + u"的账单".encode('utf-8')
        expect_start_time = ele_bill_sql['start_time']
        expect_end_time = ele_bill_sql['end_time']
        expect_time = expect_start_time + " ~ " + expect_end_time
        expect_time = expect_time.replace("-", ".")

        print(expect_start_time)
        print(expect_end_time)
        print(expect_time)

        expect_total = u'合计: ¥'.encode('utf-8') + str(ele_bill_sql['total'])
        if 'WA' in ele_bill_sql.iterkeys():
            wa_price = '¥' + str(ele_bill_sql['WA'])
            assert self.action.is_element_present(('ACCESSIBILITY_ID', u'仓储契约'))
            assert self.action.is_element_present(('ACCESSIBILITY_ID', wa_price))
        if 'TR' in ele_bill_sql.iterkeys():
            tr_price = '¥' + str(ele_bill_sql['TR'])
            assert self.action.is_element_present(('ACCESSIBILITY_ID', u'运输契约'))
            assert self.action.is_element_present(('ACCESSIBILITY_ID', tr_price))
        assert self.action.is_element_present(('ACCESSIBILITY_ID', expect_title))
        assert self.action.is_element_present(('ACCESSIBILITY_ID', expect_time))
        assert self.action.is_element_present(('ACCESSIBILITY_ID', expect_total))

    def click_generate_bill_button(self):
        """
        点击"生成应付账单"按钮
        """
        self.initial_element()
        self.action.click(self.generate_bill_button_locator)
        sleep(2)
        pass

    @staticmethod
    def assert_generate_bill_result():
        """
        点击"生成应付账单"后验证SQL结果
        """
        ele_generate_bill_sql = get_generate_bill_result()
        fee_no = ele_generate_bill_sql["fee_no"]
        bill_no = ele_generate_bill_sql["bill_no"]
        record_no = ele_generate_bill_sql["record_no"]
        # operation_no = ele_generate_bill_sql["operation_no"]
        # card_no = ele_generate_bill_sql["card_no"]
        assert fee_no == 0 and bill_no == 1 and record_no == 2
        pass


