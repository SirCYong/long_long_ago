from time import sleep
from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Utils import initial_element_error_wrapper, ParseXmlErrorException, is_element_present, \
    page_element_factory
__author__ = "LiYu"
__doc__ = "登录"


class LoginPage(BasePage):
    def __init__(self, driver):

        self.user_name_locator = None
        self.password_locator = None
        self.login_button_locator = None
        self.more_button_locator = None
        self.personal_button_locator = None
        self.logout_button_locator = None

        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.user_name_locator = None
        self.password_locator = None
        self.login_button_locator = None
        self.more_button_locator = None
        self.personal_button_locator = None
        self.logout_button_locator = None
        self.bound_locator = None
        try:
            self.initial_element()
        except ParseXmlErrorException:
            initial_element_error_wrapper(self.driver)
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except Exception():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ['user_name', 'password', 'login_button', 'more_button', 'personal_button', 'logout_button']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.user_name_locator = ele_dic['user_name']
        self.password_locator = ele_dic['password']
        self.login_button_locator = ele_dic['login_button']
        self.more_button_locator = ele_dic['more_button']
        self.personal_button_locator = ele_dic['personal_button']
        self.logout_button_locator = ele_dic['logout_button']

    def is_loaded(self):
        pass

    def login(self, username, password):
        """
        公用：登录
        :param username:
        :param password:
        :return:
        """

        if self.is_run_ios():
            self._login_ios(username, password)
        else:
            self._login_android(username, password)

    def _login_ios(self, username=None, password=None):
        """
        ios登录
        :param username: 用户名
        :param password: 密码
        :return:
        """
        if not is_element_present(self.driver, ('ACCESSIBILITY_ID', '微信登录')):
            ExitAppPage(self.driver).logout_app()
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '微信登录')):
            if username:
                print(self.user_name_locator)
                self.action.set_value(self.user_name_locator, username)
                sleep(1)
            if password:
                self.action.set_value(self.password_locator, password)
                if is_element_present(self.driver, ('ACCESSIBILITY_ID', '完成')):
                    sleep(1)
                    self.action.click(('ACCESSIBILITY_ID', '完成'))
            self.action.click(self.login_button_locator)
            sleep(2)
            if is_element_present(self.driver, ('ACCESSIBILITY_ID', '绑定')):
                sleep(4)
                self.action.click(('ACCESSIBILITY_ID', '绑定'))

    def _login_android(self, username=None, password=None):
        """
        android登录
        :param username:
        :param password:
        :return:
        Update Cy
        """
        if is_element_present(self.driver, ("XPATH", "//*[@resource-id='android:id/message' and @text='请登陆']")):
            sleep(4)
            self.action.click(("XPATH", "//*[@resource-id='android:id/button1' and @text='确定']"))
            pass
        if not is_element_present(self.driver, ('ID', 'btn_login_wechat')):
            ExitAppPage(self.driver).logout_app()
        if is_element_present(self.driver, ('ID', 'btn_login_wechat')):
            if username:
                print(self.user_name_locator)
                self.action.send_keys(self.user_name_locator, username)
                sleep(1)
            if password:
                self.action.send_keys(self.password_locator, password)
            self.action.click(self.login_button_locator)
            sleep(2)
            if is_element_present(self.driver, ("XPATH", "//*[@resource-id='android:id/message' and @text='是否绑定新设备']")):
                sleep(4)
                self.action.click(('XPATH', "//*[@resource-id='android:id/button1' and @text='绑定']"))
                pass

        # if self.action.is_element_present(self.more_button_locator):
        #     self.action.click(self.more_button_locator)
        #     self.action.tap_element(self.personal_button_locator, 588, 140)
        #     self.action.click(self.logout_button_locator)
        # self.action.send_keys(self.user_name_locator, username)
        # self.action.send_keys(self.password_locator, password)
        # self.action.click(self.login_button_locator)
