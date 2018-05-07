from time import sleep
from UIAutomation.Page import BasePage
from UIAutomation.Page.BasePage import platform, compatible
from UIAutomation.Page.main.pkg_common_page.page_logout import PageLogout
from UIAutomation.Page.main.pkg_common_page.page_long_card import PageLongCard
from UIAutomation.Page.main.pkg_common_page.page_logout import PageLogout
from UIAutomation.Utils import initial_element_error_wrapper, ParseXmlErrorException, page_element_factory

__author__ = "zzh"


class PageLogin(BasePage):
    """
    登录Page
    """
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
        except Exception():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ["input_user_name",
                     "input_password",
                     "button_login",
                     "button_wechat",
                     "button_bound",
                     "button_circle_progress_view",
                     "button_long_task",
                     "button_more",
                     "button_personal",
                     "button_logout",
                     "button_login_alert_confirm",
                     "button_update_later"]

        ele_dic = page_element_factory(self.standard_xml_file, name_list)

        # 手机号/身份证号输入框
        self.input_user_name = ele_dic['input_user_name']
        # 密码输入框
        self.input_password = ele_dic['input_password']
        # 登录按钮
        self.button_login = ele_dic['button_login']
        # 微信登录按钮
        self.button_wechat = ele_dic['button_wechat']
        # 登录后如果出现是否绑定新设备弹框： 绑定按钮
        self.button_bound = ele_dic["button_bound"]
        # 登录后的主界面：圆圈控件
        self.button_circle_progress_view = ele_dic['button_circle_progress_view']
        # 登录后的主界面：长期任务
        self.button_long_task = ele_dic['button_long_task']
        # 登录后的主界面：左上角...按钮
        self.button_more = ele_dic['button_more']
        # 登录后的主界面：左上角个人资料按钮
        self.button_personal = ele_dic['button_personal']
        # 个人资料页面：注销按钮
        self.button_logout = ele_dic['button_logout']
        # 当登录App时被顶下来的提示请登录界面确定按钮
        self.button_login_alert_confirm = ele_dic['button_login_alert_confirm']
        # 版本更新页面：稍后更新按钮
        self.button_update_later = ele_dic['button_update_later']

    def is_loaded(self):
        pass

    def login(self, username, password, logout=1):
        """
        公用：登录
        :param username:
        :param password:
        :param logout: 1 需要重新登录， 0 不需要重新登录
        :return:
        """
        self.login_ios(username, password, logout)

    @platform("ios")
    def login_ios(self, username=None, password=None, logout=1):
        """
        ios登录
        :param username: 用户名
        :param password: 密码
        :return:
        """
        # if not is_element_present(self.driver, ('ACCESSIBILITY_ID', '微信登录')):
        #     ExitAppPage(self.driver).logout_app()
        # if is_element_present(self.driver, ('ACCESSIBILITY_ID', '微信登录')):
        #     if username:
        #         print(self.user_name_locator)
        #         self.action.set_value(self.user_name_locator, username)
        #         sleep(1)
        #     if password:
        #         self.action.set_value(self.password_locator, password)
        #         if is_element_present(self.driver, ('ACCESSIBILITY_ID', '完成')):
        #             sleep(1)
        #             self.action.click(('ACCESSIBILITY_ID', '完成'))
        #     self.action.click(self.login_button_locator)
        #     sleep(2)
        #     if is_element_present(self.driver, ('ACCESSIBILITY_ID', '绑定')):
        #         sleep(4)
        #         self.action.click(('ACCESSIBILITY_ID', '绑定'))
        pass

    @platform("android")
    def login_android(self, username=None, password=None, logout=1):
        """
        android登录
        :param username:
        :param password:
        :param logout:
        :return:
        Update Cy
        """
        # 存在更新页面
        if self.action.is_element_present(self.button_update_later):
            self.action.click(self.button_update_later)
        # 存在登录App时被顶下来的提示请登录界面
        if self.action.is_element_present(self.button_login_alert_confirm):
            self.action.click(self.button_login_alert_confirm)
        # 已经登录过且不需要重新登录
        if self.action.is_element_present(self.button_circle_progress_view) and not logout:
            pass
        # 需要登录或重新登录
        else:
            # 不在登录页面上，说明需要注销再重新登录
            if not self.action.is_element_present(self.button_login):
                self.page_logout = PageLogout(self.driver)
                self.page_logout.logout_app()
            # 输入用户名
            self.action.send_keys(self.input_user_name, username)
            # 输入密码
            self.action.send_keys(self.input_password)
            # 点击登录按钮
            self.action.click(self.button_login)

            # 登录后如果出现是否绑定新设备弹框，点击绑定按钮
            if self.action.is_element_present(self.button_bound):
                self.action.click(self.button_bound)
