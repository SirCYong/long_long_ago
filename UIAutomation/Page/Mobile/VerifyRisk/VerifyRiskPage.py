# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Page.BasePage import BasePage
from UIAutomation.TestCase.SIT.Mobile.VerifyRisk.VerifyRisk_sql import get_verify_risk_info

__author__ = "xuwangchao"
__doc__ = "风险审核页面"


class VerifyRiskPage(BasePage):
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

    def is_loaded(self):
        pass

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
        name_list = ['login_button', 'user_name', 'password', 'long_task']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.login_button_locator = ele_dic['login_button']
        self.user_name_locator = ele_dic['user_name']
        self.password_locator = ele_dic['password']
        self.long_task_locator = ele_dic['long_task']

        # IOS独立的控件
        if self.is_run_ios():
            name_list = ['more_button',  'scan_logo', 'warn_logo', 'level_text', 'change_detail',
                         'red_flash_one', 'red_flash_two', 'red_flash_three', 'red_flash_four', 'red_flash_five',
                         'giver_name', 'receive_name', 'change_simple_text', 'time_text', 'know_button',
                         'page_number_text']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.more_button_locator = ele_dic['more_button']
            self.scan_logo_locator = ele_dic['scan_logo']
            self.level_text_locator = ele_dic['level_text']
            self.change_detail_locator = ele_dic['change_detail']
            self.giver_name_locator = ele_dic['giver_name']
            self.receive_name_locator = ele_dic['receive_name']
            self.change_simple_text_locator = ele_dic['change_simple_text']
            self.time_text_locator = ele_dic['time_text']
            self.know_button_locator = ele_dic['know_button']
            self.page_number_text_locator = ele_dic['page_number_text']

        # Android独立的控件
        if not self.is_run_ios():
            name_list = ['more_button', 'title_text', 'scan_logo', 'warn_logo', 'level_text', 'change_detail', 'red_flash_one',
                         'red_flash_two', 'red_flash_three', 'red_flash_four', 'red_flash_five', 'giver_name', 'receive_name',
                         'change_simple_text', 'time_text', 'know_button', 'page_number_text']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.more_button_locator = ele_dic['more_button']
            self.title_text_locator = ele_dic['title_text']
            self.scan_logo_locator = ele_dic['scan_logo']
            self.warn_logo_locator = ele_dic['warn_logo']
            self.level_text_locator = ele_dic['level_text']
            self.change_detail_locator = ele_dic['change_detail']
            self.red_flash_one_locator = ele_dic['red_flash_one']
            self.red_flash_two_locator = ele_dic['red_flash_two']
            self.red_flash_three_locator = ele_dic['red_flash_three']
            self.red_flash_four_locator = ele_dic['red_flash_four']
            self.red_flash_five_locator = ele_dic['red_flash_five']
            self.giver_name_locator = ele_dic['giver_name']
            self.receive_name_locator = ele_dic['receive_name']
            self.change_simple_text_locator = ele_dic['change_simple_text']
            self.time_text_locator = ele_dic['time_text']
            self.know_button_locator = ele_dic['know_button']
            self.page_number_text_locator = ele_dic['page_number_text']
        pass

    def assert_versify_risk(self, user_id):
        if self.is_run_ios():
            self._assert_versify_risk_ios(user_id)
        else:
            self._assert_versify_risk_android(user_id)
        pass

    def _assert_versify_risk_android(self, user_id):
        """
        android私有
        进入风险审核卡片后检测当前页面是否正确
        并点击知道了按钮检测下一个。。。
        """
        verify_risk_info = get_verify_risk_info(user_id)
        print('verify_risk_info--------------------->', verify_risk_info)
        for i in range(len(verify_risk_info)):
            print('这个是第', i, '张卡片了')
            print('这个是第', i, '张卡片了')
            print('这个是第', i, '张卡片了')
            print('这个是第', i, '张卡片了')
            print('这个是第', i, '张卡片了')
            time.sleep(2)
            a0 = self.action.is_element_present(self.more_button_locator)
            a1 = self.action.is_element_present(self.title_text_locator)
            a2= self.action.is_element_present(self.scan_logo_locator)
            a3 = self.action.is_element_present(self.warn_logo_locator)
            a4 = self.action.is_element_present(self.red_flash_one_locator)
            a5 = self.action.is_element_present(self.red_flash_two_locator)
            a6 = self.action.is_element_present(self.red_flash_three_locator)
            a7 = self.action.is_element_present(self.red_flash_four_locator)
            a8 = self.action.is_element_present(self.red_flash_five_locator)
            a9 = self.action.is_element_present(self.time_text_locator)
            a10 = self.action.is_element_present(self.know_button_locator)
            print(a0, a1, a3, a4, a5, a6, a7, a8, a9, a10)
            level_expect ='无影响或影响可以忽略'
            if verify_risk_info[i][1] == 2:
                level_expect = '可以承受'
            elif verify_risk_info[i][1] == 4:
                level_expect = '无法承受'
            print('level_expect---------------------->', level_expect)

            assert a0 and a1 and a2 and a3 and a4 and a5 and a6 and a7 and a8 and a9 and a10
            print(' a0 and a1 and a2 and a3 and a4 and a5 and a6 and a7 and a8 and a9 and a10')
            # assert self.action.text(self.level_text_locator) == level_expect
            print(self.action.text(self.level_text_locator))
            print(level_expect)
            print('1111111111111111111111111111111111111111111111111111111')
            # assert self.action.text(self.change_detail_locator) == verify_risk_info[i][5]
            print(self.action.text(self.change_detail_locator))
            print(verify_risk_info[i][5])
            print('2222222222222222222222222222222222222222222222222222')
            # assert self.action.text(self.giver_name_locator) == verify_risk_info[i][5][1:4]
            print(self.action.text(self.giver_name_locator))
            print(verify_risk_info[i][5][1:4])
            print('333333333333333333333333333333333333333333333333333333333')
            # assert self.action.text(self.receive_name_locator) == verify_risk_info[i][5][-4:-1]
            print('44444444444444444444444444444444444444444444444444444444444444')
            # assert self.action.text(self.change_simple_text_locator)[0:2] in verify_risk_info[i][5]
            print('55555555555555555555555555555555555555555555555555555555555555')
            # assert self.action.text(self.page_number_text_locator)[0] == str(i)
            print('666666666666666666666666666666666666666666666666')
            self.action.click(self.know_button_locator)
            print('7777777777777777777777777777777777777777777777777777777777777')
        self.action.is_element_present(('XPATH', "//*[@text='风险审核']"))
        pass

    def _assert_versify_risk_ios(self, user_id):
        """
        IOS私有
        进入风险审核卡片后检测当前页面是否正确
        并点击知道了按钮检测下一个。。。
        """
        verify_risk_info = get_verify_risk_info(user_id)
        print('verify_risk_info--------------------->', verify_risk_info)
        for i in range(len(verify_risk_info)):
            print('这个是第', i, '张卡片了')
            print('这个是第', i, '张卡片了')
            print('这个是第', i, '张卡片了')
            print('这个是第', i, '张卡片了')
            print('这个是第', i, '张卡片了')
            time.sleep(2)
            a0 = self.action.is_element_present(self.more_button_locator)
            a2 = self.action.is_element_present(self.scan_logo_locator)
            a9 = self.action.is_element_present(self.time_text_locator)
            a10 = self.action.is_element_present(self.know_button_locator)
            print(a0, a2, a9, a10)
            level_expect = '无影响或影响可以忽略'
            if verify_risk_info[i][1] == 2:
                level_expect = '可以承受'
            elif verify_risk_info[i][1] == 4:
                level_expect = '无法承受'
            print('level_expect---------------------->', level_expect)

            assert a0 and a2 and a9 and a10
            assert self.action.text(self.level_text_locator) == level_expect + ':'
            print(self.action.text(self.level_text_locator))
            print(level_expect + ':')
            print('1111111111111111111111111111111111111111111111111111111')
            assert self.action.text(self.change_detail_locator) == verify_risk_info[i][5]
            print(self.action.text(self.change_detail_locator))
            print(verify_risk_info[i][5])
            print('2222222222222222222222222222222222222222222222222222')
            assert self.action.text(self.giver_name_locator) == verify_risk_info[i][5][1:4]
            print(self.action.text(self.giver_name_locator))
            print(verify_risk_info[i][5][1:4])
            print('333333333333333333333333333333333333333333333333333333333')
            assert self.action.text(self.receive_name_locator) == verify_risk_info[i][5][-4:-1]
            self.action.click(self.know_button_locator)
        pass
















