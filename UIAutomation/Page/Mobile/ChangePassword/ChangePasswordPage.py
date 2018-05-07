from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.TestCase.SIT.Mobile.ChangePassword.ChangePasswordSQL import get_test_code
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Utils import page_element_factory

__author__ = "LiYu"
__doc__ = "忘记密码"


class ChangePasswordPage(BasePage):
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
        except NoSuchWindowException():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ['forgot_password', 'mobile_code', 'TestGetCode', 'TestCode', 'next',
                     'new_password', 'confirm_password', 'submit', 'confirm', 'password_title']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.forgot_password_locator = ele_dic['forgot_password']  # 忘记密码
        self.mobile_code_locator = ele_dic['mobile_code']  # 手机号
        self.TestGetCode_locator = ele_dic['TestGetCode']  # 获取验证码
        self.TestCode_locator = ele_dic['TestCode']  # 验证码
        self.next_locator = ele_dic['next']  # 验证码
        self.new_password_locator = ele_dic['new_password']  # 新密码
        self.confirm_password_locator = ele_dic['confirm_password']  # 确认新密码
        self.submit_locator = ele_dic['submit']  # 提交
        self.confirm_locator = ele_dic['confirm']  # 修改密码成功确认按钮
        self.password_title_locator = ele_dic['password_title']

    def change_password(self):
        """
        忘记密码
        :return:
        """
        if self.is_run_ios():
            self._click_password_ios()
        if not self.is_run_ios():
            self._click_password_android()

    def _click_password_android(self):
        self.action.click(self.forgot_password_locator)
        self.action.click(self.mobile_code_locator)
        self.action.send_keys(self.mobile_code_locator, value=18800001124)
        self.action.click(self.TestGetCode_locator)
        line = get_test_code()
        self.action.send_keys(self.TestCode_locator, value=line)
        self.action.click(self.next_locator)
        a = self.action.is_element_present(self.password_title_locator)
        assert_that(a, equal_to(True), u'忘记密码')
        self.action.click(self.new_password_locator)
        self.action.send_keys(self.new_password_locator, value='wc123456')
        self.action.click(self.confirm_password_locator)
        self.action.send_keys(self.confirm_password_locator, value='wc123456')
        self.action.click(self.submit_locator)
        self.action.click(self.confirm_locator)

    def _click_password_ios(self):
        self.action.click(self.forgot_password_locator)
        self.action.set_value(self.mobile_code_locator, value=18800001124)
        self.action.click(self.TestGetCode_locator)
        line = get_test_code()
        self.action.set_value(self.TestCode_locator, value=line)
        self.action.click(self.next_locator)
        a = self.action.is_element_present(self.password_title_locator)
        assert_that(a, equal_to(True), u'忘记密码')
        self.action.set_value(self.new_password_locator, value='wc123456')
        self.action.set_value(self.confirm_password_locator, value='wc123456')
        self.action.click(self.submit_locator)
        self.action.click(self.confirm_locator)

