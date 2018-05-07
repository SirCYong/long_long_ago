
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, is_element_present, sleep
from UIAutomation.Page import BasePage
__author__ = 'zhoujin'


class SignLaborContract(BasePage):
    """
    签订劳务契约
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.no_hour = '29'
        self.no_piece = '0.95'
        self.no = '2'
        self.type = '包装'
        self.shift = '白班'
        self.unit_hour1 = '元/小时'
        self.unit_hour = '计时 (元/小时)'
        self.unit_piece = '计件 (元/件)'
        self.position = '海南省三沙市中沙群岛的岛礁及其海域'
        self.start_time = '2018/12/23'
        self.end_time = '2018/12/23'
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
        self.think_locator = None
        self.all_ele = None
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
                     , 'return_map', 'la_card', 'la_type', 'la_no', 'la_unit', 'la_start_time', 'la_end_time',
                     'enter_me', 'all_ele', 'think', 'yuan_hour', 'yuan_peace', 'work', 'address', 'start_time',
                     'end_time', 'msg_text']

        ele_dic = page_element_factory(__file__, name_list)
        self.la_card_picking_locator = ele_dic['la_card_picking']  # 拣选
        self.la_card_shelve_locator = ele_dic['la_card_shelve']  # 上架
        self.la_card_packing_locator = ele_dic['la_card_packing']  # 包装
        self.la_card_transfer_locator = ele_dic['la_card_transfer']  # 交接
        self.position_locator = ele_dic['position']  # 位置
        self.enter_for_locator = ele_dic['enter_for']  # 报名参加
        self.return_map_locator = ele_dic['return_map']  # 返回
        self.la_card_locator = ele_dic['la_card']  # 拣选员
        self.la_type_locator = ele_dic['la_type']  # 第一个卡片的类型
        self.la_no_locator = ele_dic['la_no']  # 第一个卡片的数量
        self.la_unit_locator = ele_dic['la_unit']  # 第一个卡片的计量单位
        self.la_start_time_locator = ele_dic['la_start_time']  # 第一个卡片的开始时间
        self.la_end_time_locator = ele_dic['la_end_time']  # 第一个卡片的结束时间
        self.enter_me_locator = ele_dic['enter_me']  # 我参加
        self.all_ele = ele_dic['all_ele']  # 详情页面所有元素
        self.end_time_locator = ele_dic['end_time']  # 结束时间

        self.yuan_hour_locator = ele_dic['yuan_hour']
        self.yuan_peace_locator = ele_dic['yuan_peace']
        self.work_locator = ele_dic['work']  # 工作时间
        self.address_locator = ele_dic['address']  # 详细地址
        self.start_time_locator = ele_dic['start_time']  # 开始时间
        self.think_locator = ele_dic['think']  # 再考虑
        self.msg_text_locator = ele_dic['msg_text']  # 再考虑
        # if self.is_run_ios():
        #     self._page_factory_ios()
        # else:
        #     self._page_factory_android()

    def is_loaded(self):
        pass

    def click_the_first_labor_card(self, contract_type='包装'):
        if contract_type == '包装':
            self.action.click(self.la_card_packing_locator, locator_order=[0])

    def click_the_first_labor_card_twice(self):
        sleep(5)
        self.action.click(self.la_start_time_locator, locator_order=[0])
        if is_element_present(self.driver, self.msg_text_locator):
            self.driver.keyevent(4)
            # self.driver.back()
            sleep(5)
        self.action.click(self.la_start_time_locator, locator_order=[0])

    def get_the_first_labor_detail_info(self):
        """
        获取劳务详情页面的数据
        """
        get_element(self.driver, self.la_type_locator).click()  # 详情

    def choice_amount_and_submit(self):
        """
        :param is_choice: int
        :param proportion: float
        """
        get_element(self.driver, self.enter_for_locator).click()     # 报名参加
        get_element(self.driver, self.enter_me_locator).click()     # 确认报名
        pass

    def think_more(self):
        """
            再考虑
        """
        get_element(self.driver, self.enter_for_locator).click()
        get_element(self.driver, self.think_locator).click()

    def assert_la(self):
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.no]).text == self.no  # 判断数量
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.no_hour]).text == self.no_hour
        # 判断时间价钱
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.no_piece]).text == self.no_piece
        # 判断件价钱
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.unit_hour]).text == self.unit_hour
        # 判断时间单位
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.unit_piece]).text == self.unit_piece
        # 判断件单位
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.type]).text == self.type  # 判断工种
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.shift]).text == self.shift  # 判断班次
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.position]).text == self.position
        # 判断地址
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.start_time]).text == self.start_time
        # 判断开始时间
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.end_time]).text == self.end_time
        # 判断结束时间
