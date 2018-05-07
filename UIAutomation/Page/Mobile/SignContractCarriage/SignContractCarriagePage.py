# coding: utf-8
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.TestCase.SIT.iOS.Sprint2.FunSignTransportContrectSQL import get_transport_contract_ukid, \
    get_transport_contract_item_ukid, get_transport_contract_info
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, get_elements, get_element, \
    initial_element_error_wrapper
from UIAutomation.Page import BasePage
__author__ = 'chenyanxiu'


class SignContractCarriage(BasePage):
    """
    签订运输契约
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.user_id = 10001476
        self.tr_participant_ukid = 10001476
        self.origin = '杭州'
        self.end = '浙江、安徽、上海'
        self.no = '3088'
        self.num = '3'
        self.weight = '0-10'
        self.type = '发货量'
        self.express = '韵达速递'
        self.unit_hour = '单'
        self.express_type = '标准快递'
        self.position = '江干区、下城区、上城区'
        self.start_time = '2020-12-23'
        self.end_time = '2025-12-23'
        self.driver = driver
        self.tr_card_locator = None
        self.tr_unit_locator = None
        self.tr_confirmation_contract_locator = None
        self.tr_line_locator = None
        self.tr_type_locator = None
        self.tr_no_locator = None
        self.tr_unit_one_locator = None
        self.tr_origin_locator = None
        self.tr_end_locator = None
        self.confirm_locator = None
        self.tr_line_num_locator = None
        self.all_ele = None
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
            BasePage.screen_shot(self)
            assert False
        pass

    def _page_factory_ios(self):
        name_list = ['tr_card', 'tr_unit', 'tr_confirmation_contract', 'tr_line', 'tr_type', 'tr_no', 'tr_unit_one',
                     'tr_origin', 'tr_end', 'tr_line_num', 'confirm', 'all_ele']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.tr_card_locator = ele_dic['tr_card']  # 发货量
        self.tr_unit_locator = ele_dic['tr_unit']  # 单位
        self.tr_confirmation_contract_locator = ele_dic['tr_confirmation_contract']  # 确认签订契约
        self.tr_line_locator = ele_dic['tr_line']  # 线
        self.tr_type_locator = ele_dic['tr_type']  # 第一个卡片的类型
        self.tr_no_locator = ele_dic['tr_no']  # 第一个卡片的数量
        self.tr_unit_one_locator = ele_dic['tr_unit_one']  # 第一个卡片的计量单位
        self.tr_origin_locator = ele_dic['tr_origin']  # 第一个卡片的开始时间
        self.tr_end_locator = ele_dic['tr_end']  # 第一个卡片的结束时间
        self.confirm_locator = ele_dic['confirm']  # 确定
        self.tr_line_num_locator = ele_dic['tr_line_num']  # 线
        self.all_ele = ele_dic['all_ele']  # 详情页面所有元素
        pass

    def _page_factory_android(self):
        name_list = ['tr_card', 'tr_unit', 'tr_confirmation_contract', 'tr_line', 'tr_type', 'tr_no', 'tr_unit_one',
                     'tr_origin', 'tr_end', 'tr_line_num', 'confirm', 'all_ele']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.tr_card_locator = ele_dic['tr_card']  # 发货量
        self.tr_unit_locator = ele_dic['tr_unit']  # 单位
        self.tr_confirmation_contract_locator = ele_dic['tr_confirmation_contract']  # 确认签订契约
        self.tr_line_locator = ele_dic['tr_line']  # 线
        self.tr_type_locator = ele_dic['tr_type']  # 第一个卡片的类型
        self.tr_no_locator = ele_dic['tr_no']  # 第一个卡片的数量
        self.tr_unit_one_locator = ele_dic['tr_unit_one']  # 第一个卡片的计量单位
        self.tr_origin_locator = ele_dic['tr_origin']  # 第一个卡片的开始时间
        self.tr_end_locator = ele_dic['tr_end']  # 第一个卡片的结束时间
        self.confirm_locator = ele_dic['confirm']  # 确认签订
        self.tr_line_num_locator = ele_dic['tr_line_num']  # 线
        self.all_ele = ele_dic['all_ele']  # 详情页面所有元素
        pass

    def is_loaded(self):
        pass

    def page_factory(self):
        if self.is_run_ios():
            self._page_factory_ios()
        else:
            self._page_factory_android()

    def click_the_first_carriage_card(self):
        if self.is_run_ios():
            self._click_the_first_carriage_card_ios()
        else:
            self._click_the_first_carriage_card_android()

    def _click_the_first_carriage_card_android(self):
        self.action.click(self.tr_card_locator, locator_order=[0])

    def _click_the_first_carriage_card_ios(self):
        get_elements(self.driver, self.tr_type_locator)[0].click()  # 点击第一个运输卡片

    def assert_tr(self):
        if self.is_run_ios():
            self._assert_tr_ios()
        else:
            self._assert_tr_android()

    def choice_amount_and_submit(self, proportion=1.0, is_choice=1):
        if self.is_run_ios():
            self._choice_amount_and_submit_ios(is_choice)
        else:
            self._choice_amount_and_submit_android(proportion, is_choice)

    def _choice_amount_and_submit_ios(self, is_choice=1):
        """
        is_select 为0时不滑动，为1时滑动

        :param is_choice: int
        :param proportion: float
        """
        if is_choice == 1:
            tr_line = get_element(self.driver, self.tr_line_locator)
            tr_line_size = tr_line.size
            tr_line_location = tr_line.location
            TouchAction(self.driver).long_press(x=int(tr_line_location['x']) + 1,
                                                y=int(tr_line_location['y']) + 2). \
                move_to(x=int(tr_line_size['width']), y=0).perform()

        get_element(self.driver, self.tr_confirmation_contract_locator).click()  # 确认签订契约
        get_element(self.driver, self.confirm_locator).click()  # 我参加
        pass

    def _choice_amount_and_submit_android(self, proportion=1.0, is_choice=1):
        """
        is_select 为0时不滑动，为1时滑动, proportion为滑动的比例，从0.1到1.0
        :param is_choice: int
        :param proportion: float
        """
        if is_choice == 1 and 0.1 <= proportion <= 1.0:
            point_ele = get_element(self.driver, self.tr_confirmation_contract_locator)  # 获取提交按钮元素，用来计算滑块长度
            tr_line_ele = get_element(self.driver, self.tr_line_locator)  # 获取滑块元素
            locator_x = point_ele.size['width'] * proportion + point_ele.location['x'] + 10
            locator_y = tr_line_ele.location['y'] + tr_line_ele.size['height'] / 2
            TouchAction(self.driver).long_press(el=tr_line_ele). \
                move_to(x=locator_x, y=locator_y).release().perform()

        get_element(self.driver, self.tr_confirmation_contract_locator).click()  # 确认签订契约
        get_element(self.driver, self.confirm_locator).click()    # 确认签订
        pass

    def _assert_tr_ios(self):
        # 判断第一个卡片的信息
        transport_contract_ukid = get_transport_contract_ukid(self.tr_participant_ukid)  # 获取第一个契约id
        transport_contract_item_ukid = get_transport_contract_item_ukid(transport_contract_ukid)  # 获取第一个契约ITEM_ukid
        print(transport_contract_ukid, transport_contract_item_ukid)
        transport_contract_info = get_transport_contract_info(self.user_id, transport_contract_ukid,
                                                              transport_contract_item_ukid)
        DEPARTURE = str(transport_contract_info['DEPARTURE'])
        DESTINATIONS = str(transport_contract_info['DESTINATIONS'])
        DEPARTURE2 = '始发地:' + DEPARTURE
        DESTINATIONS2 = '目的地:' + DESTINATIONS
        assert get_element(self.driver, self.tr_type_locator).text == self.type  # 判断工种
        assert get_element(self.driver, self.tr_no_locator).text == self.no  # 判断数量
        assert get_element(self.driver, self.tr_unit_one_locator).text == self.unit_hour  # 判断计算单位
        assert get_element(self.driver, self.tr_origin_locator).text == DEPARTURE2  # 判断开始时间
        assert get_element(self.driver, self.tr_end_locator).text == DESTINATIONS2  # 判断结束时间

    def _assert_tr_android(self):

        pass

    def _tr_judgment_ios(self):
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.express]).text == self.express  # 判断数量
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.no]).text == self.no  # 判断数量
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.num]).text == self.num  # 判断价钱
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.unit_hour]).text == self.unit_hour
        # 判断单位
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.start_time]).text == self.start_time
        # 判断开始时间
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.end_time]).text == self.end_time
        # 判断结束时间
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.origin]).text == self.origin  # 判断始发地
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.end]).text== self.end  # 判断目的地
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.express_type]).text == \
               self.express_type  # 判断快递类型
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.weight]).text == self.weight  # 判断重量
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.position]).text == self.position

