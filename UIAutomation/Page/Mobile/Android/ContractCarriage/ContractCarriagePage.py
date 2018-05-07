from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, get_element
from UIAutomation.Page import BasePage
__author__ = 'zhoujin'


class ContractCarriage(BasePage):
    """
    签订运输契约
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
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
        name_list = ['tr_card', 'tr_unit', 'tr_confirmation_contract', 'tr_line', 'tr_type', 'tr_no', 'tr_unit_one',
                     'tr_origin', 'tr_end', 'tr_line_num', 'confirm', 'all_ele']
        ele_dic = page_element_factory(__file__, name_list)
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

    def click_the_first_carriage_card(self, tr_card='发货量'):
        if tr_card == '发货量':
            self.action.click(self.tr_card_locator, locator_order=[0])

    def choice_amount_and_submit(self, proportion=1.0, is_choice=1):
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
