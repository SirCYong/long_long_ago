from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Utils import page_element_factory

__author__ = "LiYu"
__doc__ = "锁定账号和解锁账号"


class LockAccountPage(BasePage):
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
        name_list = ['lockAccount_code', 'next_lock', 'lock_reason', 'determine_lock', 'confirm',
                     'unlockAccount_code', 'next_unlock', 'unlock_reason', 'determine_unlock', 'unconfirm']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.lockAccount_code_locator = ele_dic['lockAccount_code']  # 锁定
        self.next_lock_locator = ele_dic['next_lock']  # 锁定下一步
        self.lock_reason_locator = ele_dic['lock_reason']  # 锁定原因
        self.determine_lock_locator = ele_dic['determine_lock']  # 确认锁定
        self.confirm_locator = ele_dic['confirm']
        self.unlockAccount_code_locator = ele_dic['unlockAccount_code']  # 解锁
        self.next_unlock_locator = ele_dic['next_unlock']  # 解锁下一步
        self.unlock_reason_locator = ele_dic['unlock_reason']  # 解锁原因
        self.determine_unlock_locator = ele_dic['determine_unlock']  # 确认解锁
        self.unconfirm_locator = ele_dic['unconfirm']

    def click_lock(self):
        """
        锁定操作
        :return:
        """
        if self.is_run_ios():
            self._click_lock_ios()
        if not self.is_run_ios():
            self._click_lock_android()

    def click_unlock(self):
        """
        解锁操作
        :return:
        """
        if self.is_run_ios():
            self._click_unlock_ios()
        if not self.is_run_ios():
            self._click_unlock_android()

    def _click_lock_android(self):
        self.action.click(self.lockAccount_code_locator)
        self.action.send_keys(self.lockAccount_code_locator, value=18800001124)
        self.action.click(self.next_lock_locator)
        sleep(2)
        self.action.click(self.lock_reason_locator)
        self.action.send_keys(self.lock_reason_locator, value='锁定原因android')
        self.action.click(self.determine_lock_locator)
        self.action.click(self.confirm_locator)

    def _click_unlock_android(self):
        self.action.click(self.unlockAccount_code_locator)
        self.action.send_keys(self.unlockAccount_code_locator, value=18800001124)
        self.action.click(self.next_unlock_locator)
        sleep(2)
        self.action.click(self.unlock_reason_locator)
        self.action.send_keys(self.unlock_reason_locator, value='解锁原因android')
        self.action.click(self.determine_unlock_locator)
        self.action.click(self.unconfirm_locator)

    def _click_lock_ios(self):
        self.action.set_value(self.lockAccount_code_locator, value=18800001124)
        self.action.click(self.next_lock_locator)
        self.action.set_value(self.lock_reason_locator, value='锁定原因IOS')
        self.action.click(self.determine_lock_locator)
        self.action.click(self.confirm_locator)

    def _click_unlock_ios(self):
        self.action.set_value(self.unlockAccount_code_locator, value=18800001124)
        self.action.click(self.next_unlock_locator)
        self.action.set_value(self.unlock_reason_locator, value='解锁原因IOS')
        self.action.click(self.determine_unlock_locator)
        self.action.click(self.unconfirm_locator)

