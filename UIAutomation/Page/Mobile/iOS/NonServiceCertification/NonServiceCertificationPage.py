# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, is_element_present
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke017SQL import reduction_select

__author__ = 'zhongchangwei'


class NonServiceCertification(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.pass_locator = None
        self.reject_locator = None
        self.error_prompt_icon_locator = None
        self.tip_locator = None
        self.not_him_locator = None
        self.name_error_locator = None
        self.photo_error_locator = None
        self.cancel_locator = None
        self.audit_pass_locator = None
        self.ta_locator = None
        self.only_one_locator = None

        try:
            self.is_loaded()
        except ParseXmlErrorException:
            assert False

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
        pass

    def page_factory(self):
        name_list = ['pass', 'reject', 'error_prompt_icon', 'tip', 'not_him',
                     'name_error', 'photo_error', 'cancel', 'audit_pass', 'ta', 'only_one']
        ele_dic = page_element_factory(__file__, name_list)
        self.pass_locator = ele_dic['pass']  # 通过
        self.reject_locator = ele_dic['reject']  # 驳回
        self.error_prompt_icon_locator = ele_dic['error_prompt_icon']  # 错误提示图标
        self.tip_locator = ele_dic['tip']  # 该号码与记录不一致
        self.not_him_locator = ele_dic['not_him']  # 不是TA
        self.name_error_locator = ele_dic['name_error']  # 姓名不符
        self.photo_error_locator = ele_dic['photo_error']  # 照片不符
        self.cancel_locator = ele_dic['cancel']  # 取消
        self.audit_pass_locator = ele_dic['audit_pass']  # 审核通过
        self.ta_locator = ele_dic['ta']  # 是TA
        self.only_one_locator = ele_dic['only_one']  # 是TA
        pass

    def is_loaded(self):
        pass

    def image_click(self, i):
        ele = get_element(self.driver,
                          ['XPATH', '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIACollectionView[1]'])
        width = ele.size['width']
        height = ele.size['height']
        print(width, height)
        height1 = height * (220 / 740.0 + 160.0 / (740 * 2))
        width1 = width * (45 / 410.0 + 160.0 / (410 * 2))
        height2 = height * (220 / 740.0 + 240.0 / 740)
        width2 = width * (45 / 410.0 + 240.0 / 410)
        if int(i) == 0:
            self.driver.tap([(width1, height1)], 100)
            print(width1, height1)
        if int(i) == 1:
            self.driver.tap([(width2, height1)], 100)
            print(width2, height1)
        if int(i) == 2:
            self.driver.tap([(width1, height2)], 100)
            print(width1, height2)
        if int(i) == 3:
            self.driver.tap([(width2, height2)], 100)
            print(width2, height2)

    def only_one(self, invitee_id):
        reduction_select(invitee_id)
        self.image_click(0)
        get_element(self.driver, self.ta_locator).click()
        sleep(2)
        for i in range(3):
            if is_element_present(self.driver, self.ta_locator):
                reduction_select(invitee_id)
                self.image_click(i + 1)
                get_element(self.driver, self.ta_locator).click()
                sleep(2)
            else:
                break

    def wrong_two(self):
        # self.initial_element()
        self.image_click(0)
        get_element(self.driver, self.ta_locator).click()
        sleep(2)
        # for i in range(3):
        if is_element_present(self.driver, self.audit_pass_locator):
            get_element(self.driver, ['ACCESSIBILITY_ID', 'icon back']).click()
            sleep(2)
            for i in range(2):
                self.image_click(1)
                get_element(self.driver, self.ta_locator).click()
                self.image_click(1)
                sleep(2)
        elif is_element_present(self.driver, self.ta_locator):
            self.image_click(0)
            sleep(1)
            # get_element(self.driver, self.ta_locator).click()
            self.image_click(0)
            get_element(self.driver, self.ta_locator).click()
            sleep(2)
        is_element_present(self.driver, ['ACCESSIBILITY_ID', '刷新'])
        print(u'两次审核失败')

    def submit(self):
        sleep(2)
        get_element(self.driver, self.audit_pass_locator).click()
        sleep(5)




