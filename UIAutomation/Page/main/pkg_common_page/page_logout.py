from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, initial_element_error_wrapper

__author__ = "zzh"
__package__ = 'IscsUIAutomation'


class PageLogout(BasePage):
    """
    注销登录
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

        try:
            self.is_loaded()
            self.initial_element()
        except ParseXmlErrorException:
            initial_element_error_wrapper(self.driver)
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        name_list = ["button_more",
                     "button_personal",
                     "button_logout"]
        ele_dic = page_element_factory(self.standard_xml_file, name_list)
        # 登录后的主界面：左上角...按钮
        self.button_more = ele_dic['button_more']
        # 登录后的主界面：左上角个人资料按钮
        self.button_personal = ele_dic['button_personal']
        # 个人资料页面：注销按钮
        self.button_logout = ele_dic['button_logout']
        pass

    def logout_app(self):
        if self.is_run_ios():
            self._logout_app_ios()
        else:
            self._logout_app_android()
        pass

    def is_loaded(self):
        pass

    def _logout_app_ios(self):
        self.action.click(self.button_more)
        self.action.click(self.button_personal)
        self.action.click(self.button_logout)
        pass

    def _logout_app_android(self):
        self.action.click(self.button_more)
        size_dic = self.action.get_window_size()
        start_x = size_dic['width'] * 0.6
        start_y = size_dic['height'] * 0.088
        self.driver.tap([(int(start_x), int(start_y))],)       # 点击（用户）坐标操作
        self.action.click(self.button_logout)
        pass
