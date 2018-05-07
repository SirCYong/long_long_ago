import requests
import sys
from time import sleep
from UIAutomation.Utils import GetCardListFailureException, Action, parse_cfg, get_setting_configuration
from UIAutomation.Utils.HttpWrapper import get_request_post_head_parameters, eject_logged_user
from UIAutomation.Page.BasePage import BasePage

__author__ = 'Yong_li'
__package__ = 'IscsUIAutomation'
"""
操作临时卡片请使用这个方法，只要输入你拥有的卡片名称就可以了.
"""


class PageTempCard(BasePage):
    """
    临时卡片操作Page
    """
    def __init__(self, driver, username, password, card_list_index):
        """

        :param driver: Appium driver
        :type driver:
        :param username: cellphone number
        :type username: str
        :param password:
        :type password:
        """
        BasePage.__init__(driver, __file__)
        self.screen_shot_name = __name__
        self.driver = driver
        self.action = Action(driver)
        self.username = username
        self.password = password
        self.card_list_index = card_list_index

    def click_expected_card(self, card_name):
        """
        如果想要点击自己期望的那个卡片，传入卡片的中文名字就可以了．
        :param card_name:
        :type card_name:
        :return:
        :rtype:
        """
        position = self.get_card_position(card_name)
        w, h = self.get_abs_width_height(position)
        swip_times = self.swap_times(position)
        if swip_times:
            swip_times_int = int(swip_times)
            for i in range(swip_times_int):
                self.swipe_card()
        self.driver.tap([(h, w)], 200)
        # self.action.tap_driver([(w, h)], 1000)

    def get_abs_width_height(self, position):
        mobile_size = self.action.get_window_size()
        width = mobile_size['width']
        height = mobile_size['height']
        w = 0
        h = 0
        sleep(5)
        if position <= 6:
            if position == 1:
                h = 671 / 1280.0 * height
                w = 138 / 752.0 * width
                return h, w
            if position == 2:
                h = 671 / 1280.0 * height
                w = 376 / 752.0 * width
                return h, w
            if position == 3:
                h = 671 / 1280.0 * height
                w = 612 / 752.0 * width
                return h,w
            if position == 4:
                h = 1017 / 1280.0 * height
                w = 138 / 752.0 * width
                return h, w
            if position == 5:
                h = 1017 / 1280.0 * height
                w = 376 / 752.0 * width
                return h, w
            if position == 6:
                h = 1017 / 1280.0 * height
                w = 612 / 752.0 * width
                return h, w
        if position > 6:
            locator_number = (position - 6) % 9
            if locator_number == 0:
                raise ValueError
            if locator_number == 1:
                h = 325 / 1280.0 * height
                w = 138 / 752.0 * width
                return h, w
            if locator_number == 2:
                h = 325 / 1280.0 * height
                w = 376 / 752.0 * width
                return h, w
            if locator_number == 3:
                h = 325 / 1280.0 * height
                w = 612 / 752.0 * width
                return h, w
            if locator_number == 4:
                h = 671 / 1280.0 * height
                w = 138 / 752.0 * width
                return h, w
            if locator_number == 5:
                h = 671 / 1280.0 * height
                w = 376 / 752.0 * width
                return h, w
            if locator_number == 6:
                h = 671 / 1280.0 * height
                w = 612 / 752.0 * width
                return h, w
            if locator_number == 7:
                h = 1017 / 1280.0 * height
                w = 138 / 752.0 * width
                return h, w
            if locator_number == 8:
                h = 1017 / 1280.0 * height
                w = 376 / 752.0 * width
                return h, w
            if locator_number == 9:
                h = 1017 / 1280.0 * height
                w = 612 / 752.0 * width
                return h, w
        else:
            raise ValueError

    def get_card_position(self, card_name):
        # 系统发送post请求
        try:
            result = self.card_list_index
            card_list = []
            for r in result:
                card_list.append(r['cardName'])
            try:
                position = card_list.index(card_name) + 1
                # print card_list
            except Exception as e:
                print(e, 'Get Card List fail.')
                raise GetCardListFailureException
            return position

        except Exception as e:
            print(e)

    @staticmethod
    def __get_username_password():
        """
        去获取使用哪个用户名和密码去进行接口操作
        :return:
        :rtype:
        """
        setting = parse_cfg("setting", "cit_setting")
        return setting['username'], setting['password'], setting['host']

    def swipe_card(self):
        width = self.action.get_window_size()['width']
        height = self.action.get_window_size()['height']
        if self.is_run_ios():
            self.action.swipe(width * 5 / 7, height / 2, -(width * 3 / 7), height / 2, 200)
            sleep(1)
        else:
            sleep(2)
            self.action.swipe(0.9*width, 0.5*height, 0.1*width, 0.5*height, 250)

        # self.action.swipe(width * 5 / 7, height / 2, -(width * 3 / 7), height / 2, 100)
        # sleep(3)
        pass

    @staticmethod
    def swap_times(position):
        if position <=6:
            return None
        else:
            swap_times = (position - 6) / 9 + 1
            return swap_times
        pass

