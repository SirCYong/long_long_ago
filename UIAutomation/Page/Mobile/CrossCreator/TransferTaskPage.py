from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeDown
from UIAutomation.Utils import initial_element_error_wrapper, ParseXmlErrorException, page_element_factory, \
    is_element_present
from UIAutomation.tests.Utils.test_cmd import is_run_ios


class TransferTask(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_forward_locator = None
        self.click_sure_choice_locator = None
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
        name_list = ('forward', 'sureChoice')
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.click_forward_locator = ele_dic['forward']
        self.click_sure_choice_locator = ele_dic['sureChoice']

    def is_loaded(self):

        pass

    def operation_transfer_task(self):
        if self.is_run_ios():
            self._operation_transfer_task_ios()
        else:
            self._operation_transfer_task_Android()

        pass

    def _operation_transfer_task_ios(self):
        mobile_size = self.driver.get_window_size()
        width = mobile_size['width']
        height = mobile_size['height']
        h = 479 / 1280.0 * height
        w = width * (424 / 637)
        self.driver.tap([(w, h)], 100)
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '非服务认证')):
            a = self.driver.find_elements_by_accessibility_id('非服务认证')
            a[0].click()
        else:
            print('此号数据丢失')
            assert False
        SwipeDown(self.driver)
        sleep(5)
        self.action.click(self.click_forward_locator)
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '转发该任务')):
            self.driver.find_element_by_accessibility_id('转发该任务').click()
        a = self.driver.find_elements_by_accessibility_id('选择')
        a[0].click()
        print(len(a))
        self.action.click(self.click_sure_choice_locator)
        pass

    def _operation_transfer_task_Android(self):
        pass

    def operation_transfer_task1(self):
        if self.is_run_ios():
            self._operation_transfer_task1_ios()
        else:
            self._operation_transfer_task1_Android()
        pass

    def _operation_transfer_task1_ios(self):
        mobile_size = self.driver.get_window_size()
        width = mobile_size['width']
        height = mobile_size['height']
        h = 479 / 1280.0 * height
        w = width * (424 / 637)
        self.driver.tap([(w, h)], 100)
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '非服务认证')):
            a = self.driver.find_elements_by_accessibility_id('非服务认证')
            a[0].click()
            print('任务分配已经确认')
        else:
            print('分配未成功，或者其他原因')
            assert False
        SwipeDown(self.driver)
        self.action.click(self.click_forward_locator)
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '转发该任务')):
            self.driver.find_element_by_accessibility_id('转发该任务').click()
        a = self.driver.find_elements_by_accessibility_id('选择')
        a[1].click()
        print(len(a))
        self.action.click(self.click_sure_choice_locator)
        pass

    def _operation_transfer_task1_Android(self):
        pass