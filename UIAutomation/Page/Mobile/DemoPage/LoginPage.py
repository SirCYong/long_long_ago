import time
from hamcrest import *
from UIAutomation.Utils import page_element_factory, GlobalVar, run_info_log
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Page.BasePage import BasePage

__author__ = "zzh"
__doc__ = "登录页面，作为demo文件，勿删"


class LoginPage(BasePage):

    def __init__(self, driver):
        self.login_button_locator = None
        self.user_name_locator = None
        self.password_locator = None
        self.long_task_locator = None

        BasePage.__init__(self, driver)
        self.driver = driver
        if self.is_run_ios():
            self.xml_file = __file__[:__file__.rfind(".")] + "IOS.xml"
        else:
            self.xml_file = __file__[:__file__.rfind(".")] + "Android.xml"

        try:
            self.initial_element()
        except ParseXmlErrorException:
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
        except Exception:
            print(u'控件不在当前页面上.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'控件不在当前页面上.', GlobalVar.get_log_file())
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
            name_list = ['bound', 'manage_authorize']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.bound_locator = ele_dic['bound']
            self.manage_authorize_locator = ele_dic['manage_authorize']

        # Android独立的控件
        if not self.is_run_ios():
            name_list = ['circle_progress_view', 'card_layout', 'show_home', 'order_button']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.circle_progress_view_locator = ele_dic['circle_progress_view']
            self.card_layout_locator = ele_dic['card_layout']
            self.show_home_locator = ele_dic['show_home']
            self.order_button_locator = ele_dic['order_button']

    def is_loaded(self):
        pass

    def login(self, username, password):
        """
        登录操作
        :param username: 用户名
        :param password: 密码
        :return:
        """
        if self.is_run_ios():
            self._login_ios(username, password)
        else:
            self._login_android(username, password)

    def _login_ios(self, username=None, password=None):
        """
        ios登录操作，私有方法
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.action.set_value(self.user_name_locator, username)
        self.action.set_value(self.password_locator, password)
        self.action.click(self.login_button_locator)
        ret = self.action.is_element_present(self.long_task_locator)
        assert_that(ret, equal_to(True), u"登录失败")

    def _login_android(self, username=None, password=None):
        """
        android登录操作，私有方法
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.action.send_keys(self.user_name_locator, username)
        self.action.send_keys(self.password_locator, password)
        self.action.click(self.login_button_locator)
        ret = self.action.is_element_present(self.circle_progress_view_locator)
        assert_that(ret, equal_to(True), u"登录失败")
        pass






