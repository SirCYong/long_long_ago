from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, initial_element_error_wrapper, sleep

"""
注销app
"""
__author__ = "CaoYong"
__package__ = 'IscsUIAutomation'


class ExitAppPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.click_nav_more_locator = None
        self.click_nav_me_locator = None
        self.click_logout_locator = None
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
        name_list = ('navMore', 'navMe', 'logout')
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.click_nav_more_locator = ele_dic['navMore']
        self.click_nav_me_locator = ele_dic['navMe']
        self.click_logout_locator = ele_dic['logout']
        pass

    def logout_app(self):
        if self.is_run_ios():
            self._logout_app_IOS()
        else:
            self._logout_app_android()
        pass

    def is_loaded(self):
        pass

    def _logout_app_IOS(self):
        self.action.click(self.click_nav_more_locator)
        self.action.click(self.click_nav_me_locator)
        sleep(2)
        self.action.click(self.click_logout_locator)
        sleep(2)
        pass

    def _logout_app_android(self):
        self.action.click(self.click_nav_more_locator)
        size_dic = self.action.get_window_size()
        start_x = size_dic['width'] * 0.6
        start_y = size_dic['height'] * 0.088
        self.driver.tap([(int(start_x), int(start_y))],)       # 点击（用户）坐标操作
        self.action.click(self.click_logout_locator)
        sleep(2)
        pass
