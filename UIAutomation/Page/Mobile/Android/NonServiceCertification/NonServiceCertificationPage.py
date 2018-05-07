from time import sleep
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeDown
from UIAutomation.Utils import page_element_factory, get_element, is_element_present, GlobalVar,\
    ParseXmlErrorException, run_info_log
from UIAutomation.Page import BasePage
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke017SQL import reduction_select

__author__ = "ZJ"
__doc__ = "非服务认证"


class NonServiceCertification(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.non_service_locator = None
        self.more_locator = None
        self.transfer_locator = None
        self.find_locator = None
        self.number_locator = None
        self.first_photo_locator = None
        self.second_photo_locator = None
        self.third_photo_locator = None
        self.four_photo_locator = None
        self.ta_locator = None
        self.tip_pass_locator = None
        self.audit_locator = None
        self.front_locator = None
        self.back_locator = None
        self.cancel_locator = None
        self.pass_locator = None
        self.only_one_locator = None
        self.back_locator = None
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
        name_list = ['non_service', 'more',  'transfer', 'find', 'number', 'first_photo', 'second_photo',
                     'third_photo', 'four_photo', 'ta', 'tip', 'audit', 'front', 'back', 'cancel', 'pass', 'only_one',
                     'back']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.non_service_locator = ele_dic['non_service']  # 非服务认证
        self.more_locator = ele_dic['more']
        self.transfer_locator = ele_dic['transfer']      # 移交任务
        self.find_locator = ele_dic['find']  # 请找出某某
        self.number_locator = ele_dic['number']  # 手机号
        self.first_photo_locator = ele_dic['first_photo']  # 第一张照片
        self.second_photo_locator = ele_dic['second_photo']  # 第二张照片
        self.third_photo_locator = ele_dic['third_photo']  # 第三张照片
        self.four_photo_locator = ele_dic['four_photo']  # 第四张照片
        self.ta_locator = ele_dic['ta']  # 是他
        self.tip_pass_locator = ele_dic['tip']  # 该号码与记录不一致
        self.audit_locator = ele_dic['audit']   # 审核xx的身份证
        self.front_locator = ele_dic['front']   # 身份证正面
        self.back_locator = ele_dic['back']   # 身份证反面
        self.cancel_locator = ele_dic['cancel']  # 驳回
        self.pass_locator = ele_dic['pass']   # 审核通过
        self.only_one_locator = ele_dic['only_one']
        self.back_locator = ele_dic['back']  # 返回
        pass

    def is_loaded(self):
        pass

    def image_click(self, i):
        if self.is_run_ios():
            self._image_click_IOS(i)
        else:
            self._image_click_android(i)
            pass

    def _image_click_IOS(self, i):
        # ele = get_element(self.driver,
        #                   ['XPATH',"//*[@resource-id='com.iscs.mobilewcs:id/tv_show_examine_title' and @text='请找出授权"])
        # width = ele.size['width']
        # height = ele.size['height']
        # print(width, height)
        # height1 = height * (220 / 740.0 + 160.0 / (740 * 2))
        # width1 = width * (45 / 410.0 + 160.0 / (410 * 2))
        # height2 = height * (220 / 740.0 + 240.0 / 740)
        # width2 = width * (45 / 410.0 + 240.0 / 410)
        # if int(i) == 0:
        #     self.driver.tap([(width1, height1)], 100)
        #     print(width1, height1)
        # if int(i) == 1:
        #     self.driver.tap([(width2, height1)], 100)
        # print(width2, height1)
        # if int(i) == 2:
        #     self.driver.tap([(width1, height2)], 100)
        #     print(width1, height2)
        # if int(i) == 3:
        #     self.driver.tap([(width2, height2)], 100)
        #     print(width2, height2)
            pass

    def _image_click_android(self, i):
        if is_element_present(self.driver, ("XPATH", "//*[@resource-id='com.iscs.mobilewcs:id/tv_show_examine_title' and @text='请找出授权']")):
            SwipeDown(self.driver)
            self.driver.find_element_by_id("com.iscs.mobilewcs:id/yijiao_bt").click()
            self.driver.find_element_by_XPATH("//*[@resource-id='com.iscs.mobilewcs:id/tv_show_examine_title' and @text='转发']").click()
        pass

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
        self.image_click(0)
        get_element(self.driver, self.ta_locator).click()
        sleep(2)
        if is_element_present(self.driver, self.pass_locator):
            get_element(self.driver, ['ID', 'back']).click()
            sleep(2)
            for i in range(2):
                self.image_click(1)
                get_element(self.driver, self.ta_locator).click()
                self.image_click(1)
                sleep(2)
        elif is_element_present(self.driver, self.ta_locator):
            self.image_click(0)
            sleep(1)
            self.image_click(0)
            get_element(self.driver, self.ta_locator).click()
            sleep(2)
        print(u'两次审核失败')

    def submit(self):
        sleep(2)
        get_element(self.driver, self.pass_locator).click()
        sleep(5)




