import time
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import initial_element_error_wrapper, ParseXmlErrorException, page_element_factory

__author__ = 'zzh'
__package__ = 'IscsUIAutomation'


class PageLongCard(BasePage):
    """
    长期卡片操作Page
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.initial_element()
        except ParseXmlErrorException:
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            raise
        pass

    def is_loaded(self):
        pass

    def page_factory(self):
        # 2端统一的控件
        name_list = ["button_long_task"]

        ele_dic = page_element_factory(self.standard_xml_file, name_list)

        # 登录后的主界面：长期任务
        self.button_long_task = ele_dic['button_long_task']

    def click_button_long_card_by_card_name(self, card_name):
        """
        根据卡片名称点击长期卡片
        :param card_name: 卡片名称
        :return:
        """
        # 点击主页面的长期任务按钮
        self.click_button_long_task()

        locator = ("XPATH", "//*[@text='" + card_name + "']")
        if self.action.is_element_present(locator):
            self.action.click(locator)
        else:
            i = 1
            while i < 10:
                width = self.action.get_window_size()["width"]
                height = self.action.get_window_size()["height"]
                start_x = width / 2
                start_y = height / 2
                end_x = width / 5
                end_y = height / 2
                self.action.swipe(start_x, start_y, end_x, end_y)
                time.sleep(2)
                if self.action.is_element_present(locator):
                    self.action.click(locator)
                    break

    def click_button_long_task(self):
        """
        点击xx个长期任务
        """
        if self.is_run_ios():
            mobile_size = self.action.get_window_size()
            print(mobile_size)
            width = mobile_size['width']
            height = mobile_size['height']
            h = 479 / 1280.0 * height
            w = width * 0.32
            self.driver.tap([(w, h)], 100)
        else:
            self.action.click(self.button_long_task)
        pass




