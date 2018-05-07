# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, GlobalVar, run_info_log
from UIAutomation.Page import BasePage


__author__ = "xuwangchao"
__doc__ = "首页"

"""
操作长期卡片页面
"""

class CardListPage(BasePage):
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
            # print (u'控件不在当前页面上.')
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
            name_list = ['more_button', 'long_task']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.more_button_locator = ele_dic['more_button']  # xx左上角更多按钮
            self.long_task_locator = ele_dic['long_task']  # xx个长期任务

    def is_loaded(self):
        pass

    def click_more_button(self):
        """
       点击左上角更多按钮
        """
        if self.is_run_ios():
            print("在跑iOS的")
        else:
            self._click_more_button_android()
        pass

    def _click_more_button_android(self):
        """
        android私有方法
        点击左上角更多按钮
        """
        self.action.click(self.more_button_locator)
        pass

    def click_my_button(self):
        """
        点击我的
        """
        if self.is_run_ios():
            print(u"在跑iOS的")
        else:
            self._click_my_button_android()
        pass

    def _click_my_button_android(self):
        size_dic = self.action.get_window_size()
        start_x = size_dic['width'] * 0.6
        start_y = size_dic['height'] * 0.088
        self.action.tap_driver([(int(start_x), int(start_y))])
        pass

    def click_long_task(self):
        """
        点击xx个长期任务
        """
        if self.is_run_ios():
            print(u"在跑iOS的")
        else:
            self._click_long_task_android()
        pass

    def _click_long_task_android(self):
        """
        android私有
        点击xx个长期任务
        """
        self.action.click(self.long_task_locator)
        pass







