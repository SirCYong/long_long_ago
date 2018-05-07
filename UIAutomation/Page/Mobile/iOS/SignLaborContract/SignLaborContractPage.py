from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, get_elements, ParseXmlErrorException
from UIAutomation.Page import BasePage

__author__ = 'chenyanxiu'


class SignLaborContract(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.la_card_picking_locator = None
        self.la_card_shelve_locator = None
        self.la_card_packing_locator = None
        self.la_card_transfer_locator = None
        self.position_locator = None
        self.enter_for_locator = None
        self.la_line_locator = None
        self.return_map_locator = None
        self.la_card_locator = None
        self.la_type_locator = None
        self.la_no_locator = None
        self.la_unit_locator = None
        self.la_start_time_locator = None
        self.la_end_time_locator = None
        self.enter_me_locator = None
        self.la_line_num_locator = None
        self.all_ele = None
        self.think_locator = None
        try:
            self.is_loaded()
        except ParseXmlErrorException:
            assert False
        pass

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
        pass

    def page_factory(self):
        name_list = ['la_card_picking', 'la_card_shelve', 'la_card_packing', 'la_card_transfer', 'position', 'enter_for'
                     , 'la_line', 'return_map', 'la_card', 'la_type', 'la_no', 'la_unit', 'la_start_time', 'la_end_time',
                     'enter_me', 'la_line_num', 'all_ele', 'think']
        ele_dic = page_element_factory(__file__, name_list)
        self.la_card_picking_locator = ele_dic['la_card_picking']  # 拣选
        self.la_card_shelve_locator = ele_dic['la_card_shelve']  # 上架
        self.la_card_packing_locator = ele_dic['la_card_packing']  # 包装
        self.la_card_transfer_locator = ele_dic['la_card_transfer']  # 交接
        self.position_locator = ele_dic['position']  # 位置
        self.enter_for_locator = ele_dic['enter_for']  # 报名参加
        self.la_line_locator = ele_dic['la_line']  # 线
        self.return_map_locator = ele_dic['return_map']  # 返回
        self.la_card_locator = ele_dic['la_card']  # 拣选员
        self.la_type_locator = ele_dic['la_type']  # 第一个卡片的类型
        self.la_no_locator = ele_dic['la_no']  # 第一个卡片的数量
        self.la_unit_locator = ele_dic['la_unit']  # 第一个卡片的计量单位
        self.la_start_time_locator = ele_dic['la_start_time']  # 第一个卡片的开始时间
        self.la_end_time_locator = ele_dic['la_end_time']  # 第一个卡片的结束时间
        self.enter_me_locator = ele_dic['enter_me']  # 我参见
        self.la_line_num_locator = ele_dic['la_line_num']  # 线
        self.all_ele = ele_dic['all_ele']  # 详情页面所有元素
        self.think_locator = ele_dic['think']  # 再考虑
        pass

    def is_loaded(self):
        pass

    def click_the_first_labor_card(self, contract_type='包装'):
        """
        点击第一个卡片，判断里面的元素个数，如果不满足，就返回重新进
        :param contract_type:
        :param ele_no:
        """
        if contract_type == '包装':
            get_elements(self.driver, self.la_card_packing_locator)[0].click()  # 点击第一个劳务卡片
        pass

    def get_the_first_labor_detail_info(self):

        """
        获取劳务详情页面的数据

        """
        get_element(self.driver, self.la_type_locator).click()  # 详情

    def choice_amount_and_submit(self, is_choice=1):
        """
        is_select 为0时不滑动，为1时滑动

        :param is_choice: int
        :param proportion: float
        """
        # if is_choice == 1:
        #     la_line = get_element(self.driver, self.la_line_locator)
        #     la_line_size = la_line.size
        #     la_line_location = la_line.location
        #     TouchAction(self.driver).long_press(x=int(la_line_location['x']) + 1,
        #                                         y=int(la_line_location['y']) + 2).\
        #                                     move_to(x=int(la_line_size['width']), y=0).perform()

        get_element(self.driver, self.enter_for_locator).click()     #确认签订契约
        get_element(self.driver, self.enter_me_locator).click()     #我参加
        pass

    def think_more(self):
        get_element(self.driver, self.enter_for_locator).click()
        get_element(self.driver, self.think_locator).click()
