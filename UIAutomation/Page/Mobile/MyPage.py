# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, GlobalVar, run_info_log
from UIAutomation.Page import BasePage
# from UIAutomation.Utils import GlobalVar
# from UIAutomation.Utils import run_info_log

__author__ = "xuwangchao"
__doc__ = "我的页面"


class MyPage(BasePage):
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
            # print(u'控件不在当前页面上.')
            # screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            # self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            # print("错误截图：")
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
            print(' # Android独立的控件')
            name_list = ['my_monney', 'notify', 'setting', 'logout']
            ele_dic = page_element_factory(self.xml_file, name_list)
            # 钱仓
            self.my_monney_locator = ele_dic['my_monney']
            # 通知
            self.notify_locator = ele_dic['notify']
            # 设置
            self.setting_locator = ele_dic['setting']
            # 注销
            self.logout_locator = ele_dic['logout']

    def is_loaded(self):
        pass

    def click_my_monney(self):
        print('点击钱仓按钮')
        """
       点击钱仓按钮
        """
        if self.is_run_ios():
            print(u"在跑iOS的")
        else:
            self._click_my_monney_android()
        pass

    def _click_my_monney_android(self):
        print('android私有方法')
        """
        android私有方法
        点击钱仓
        """
        self.action.click(self.my_monney_locator)
        pass










