from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, get_elements, get_element, sleep, ParseXmlErrorException, \
    initial_element_error_wrapper
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
__author__ = 'zhongchangwei'


class SignedWarehousingSupplyContract(BasePage):
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

    def _page_factory_ios(self):
        name_list = ['cc_su_card_throughput', 'cc_supply_card_warehouse_area', 'star',
                     'cc_supply_submit_button', 'cc_supply_confirm_button', 'cc_supply_point', 'cc_supply_type',
                     'cc_supply_no', 'cc_supply_unit', 'cc_supply_cc_supply_start_time', 'cc_supply_cc_supply_end_time',
                     'cc_supply_name', 'cc_supply_detail_no', 'cc_supply_detail_unit',
                     'cc_supply_detail_cc_supply_start_time',
                     'cc_supply_detail_cc_supply_end_time', 'cc_supply_detail_price', 'cc_supply_detail_instury',
                     'cc_supply_detail_overdue_clause', 'cc_supply_detail_select_no', 'all_ele']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.cc_su_card_throughput_locator = ele_dic['cc_su_card_throughput']  # 吞吐量
        self.cc_supply_card_warehouse_area_locator = ele_dic['cc_supply_card_warehouse_area']  # 仓库面积
        self.cc_supply_submit_button_locator = ele_dic['cc_supply_submit_button']  # 确认签订契约
        self.cc_supply_confirm_button_locator = ele_dic['cc_supply_confirm_button']  # 确认签订
        self.star_locator = ele_dic['star']  # 星级
        self.cc_supply_point_locator = ele_dic['cc_supply_point']  # 线
        self.cc_supply_type_locator = ele_dic['cc_supply_type']  # 第一个卡片的类型
        self.cc_supply_no_locator = ele_dic['cc_supply_no']  # 第一个卡片的数量
        self.cc_supply_unit_locator = ele_dic['cc_supply_unit']  # 第一个卡片的计量单位
        self.cc_supply_start_time_locator = ele_dic['cc_supply_cc_supply_start_time']  # 第一个卡片的开始时间
        self.cc_supply_end_time_locator = ele_dic['cc_supply_cc_supply_end_time']  # 第一个卡片的开始时间
        self.cc_supply_name_locator = ele_dic['cc_supply_name']  # 发布者
        self.cc_supply_detail_no_locator = ele_dic['cc_supply_detail_no']  # 详情数量
        self.cc_supply_detail_unit_locator = ele_dic['cc_supply_detail_unit']  # 详情单位
        self.cc_supply_detail_start_time_locator = ele_dic['cc_supply_detail_cc_supply_start_time']  # 详情开始时间
        self.cc_supply_detail_end_time_locator = ele_dic['cc_supply_detail_cc_supply_end_time']  # 详情结束时间
        self.cc_supply_detail_price_locator = ele_dic['cc_supply_detail_price']  # 详情价格
        self.cc_supply_detail_instury_locator = ele_dic['cc_supply_detail_instury']  # 行业
        self.cc_supply_detail_overdue_clause_locator = ele_dic['cc_supply_detail_overdue_clause']  # 逾期条款
        self.cc_supply_detail_select_no_locator = ele_dic['cc_supply_detail_select_no']  # 选择的数量
        self.all_ele = ele_dic['all_ele']  # 详情页面所有元素
        pass

    def _page_factory_android(self):
        name_list = ['contract_name', 'contract_number', 'contract_units', 'start_time', 'end_time',
                     'detail_supply_name', 'swipe_button', 'swipe_button2', 'submit_button',
                     'submit_button2', 'confirm_button']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.contract_name_locator = ele_dic['contract_name']  # 类型
        self.contract_number_locator = ele_dic['contract_number']  # 数量
        self.contract_units_locator = ele_dic['contract_units']  # 计算单位
        self.start_time_locator = ele_dic['start_time']  # 开始时间
        self.end_time_locator = ele_dic['end_time']  # 结束时间
        self.detail_supply_name_locator = ele_dic['detail_supply_name']  # 发布者
        self.swipe_button_locator = ele_dic['swipe_button']  # 仓储供应滑块
        self.swipe_button_locator2 = ele_dic['swipe_button2']  # 仓储需求滑块
        self.submit_button_locator = ele_dic['submit_button']  # 仓储供应提交按钮
        self.submit_button_locator2 = ele_dic['submit_button2']  # 仓储需求提交按钮
        self.confirm_button_locator = ele_dic['confirm_button']  # 确认按钮

    def is_loaded(self):
        pass

    def page_factory(self):
        if self.is_run_ios():
            self._page_factory_ios()
        else:
            self._page_factory_android()

    def get_the_first_warehouse_card_info(self):
        if self.is_run_ios():
            self._get_the_first_warehouse_card_info_ios()

    def click_the_first_warehouse_card(self, contract_type='SUPPLY', rs_type='RE', ele_no=17):
        if self.is_run_ios():
            self._click_the_first_warehouse_card_ios(contract_type, rs_type, ele_no)
        else:
            self._click_the_first_warehouse_card_android()

    def get_the_first_warehouse_detail_info(self, warehouse_type='supply'):
        if self.is_run_ios():
            self._get_the_first_warehouse_detail_info_ios(warehouse_type)

    def choice_amount_and_submit(self, is_choice=1, proportion=1.0, contract_type='SUPPLY'):
        if self.is_run_ios():
            self._choice_amount_and_submit_ios(is_choice, proportion)
        else:
            self._choice_amount_and_submit_android(is_choice, proportion, contract_type)

    def _get_the_first_warehouse_card_info_ios(self):
        """
        获取仓储供应第一个卡片的内容
        """
        contract_type = self.action.text(self.cc_supply_type_locator)  # 任务类型
        amount = self.action.text(self.cc_supply_no_locator)  # 数量
        unit = self.action.text(self.cc_supply_unit_locator)  # 计算单位
        start_time = self.action.text(self.cc_supply_unit_locator)  # 判断开始时间
        end_time = self.action.text(self.cc_supply_end_time_locator)  # 判断结束时间
        return contract_type, amount, unit, start_time, end_time
        pass

    def _click_the_first_warehouse_card_ios(self, contract_type, rs_type, ele_no):
        """
        点击第一个卡片，判断里面的元素个数，如果不满足，就返回重新进
        :param rs_type:
        :param contract_type:
        :param ele_no:
        """
        if contract_type == 'DEMAND':
            ele_no = 16
        if rs_type == 'RE':
            self.action.click(self.cc_supply_card_warehouse_area_locator, locator_order=[0])  # 点击第一个仓库面积卡片
            i = 0
            while len(get_elements(self.driver, self.all_ele)) != ele_no:
                CardPage(self.driver).back()
                sleep(5)
                self.action.click(self.cc_supply_card_warehouse_area_locator, locator_order=[0])  # 点击第一个仓库面积卡片
                i += 1
                if i > 4:
                    break

        if rs_type == 'WA':
            self.action.click(self.cc_su_card_throughput_locator, locator_order=[0])  # 点击第一个吞吐量卡片
            i = 0
            while len(get_elements(self.driver, self.all_ele)) != ele_no:
                CardPage(self.driver).back()
                sleep(5)
                self.action.click(self.cc_su_card_throughput_locator, locator_order=[0])  # 点击第一个吞吐量卡片
                i += 1
                if i > 4:
                    break
        pass

    def _click_the_first_warehouse_card_android(self):
        self.action.click(self.contract_name_locator, locator_order=[0])  # 点击第一个卡片
        sleep(2)

    def _get_the_first_warehouse_detail_info_ios(self, warehouse_type):

        """
        获取仓储详情页面的数据

        """
        supply_name = self.action.text(self.cc_supply_name_locator)   # 发布者
        detail_amount = self.action.text(self.cc_supply_detail_no_locator)  # 详情数量
        detail_unit = self.action.text(self.cc_supply_detail_unit_locator)  # 详情单位
        detail_start_time = self.action.text(self.cc_supply_detail_start_time_locator)  # 详情开始时间
        detail_end_time = self.action.text(self.cc_supply_detail_end_time_locator)  # 详情结束时间
        detail_price = self.action.text(self.cc_supply_detail_price_locator)  # 价格
        detail_instury = self.action.text(self.cc_supply_detail_instury_locator)  # 行业
        detail_overdue_clause = self.action.text(self.cc_supply_detail_overdue_clause_locator)  # 逾期条款
        if warehouse_type == 'supply':
            star_amount = len(get_elements(self.driver, self.star_locator))  # 星级
            return supply_name, detail_amount, detail_unit, star_amount, detail_start_time, detail_end_time, \
                detail_price, detail_instury, detail_overdue_clause
        else:
            return supply_name, detail_amount, detail_unit, detail_start_time, detail_end_time, \
                   detail_price, detail_instury, detail_overdue_clause
        pass

    def _choice_amount_and_submit_ios(self, is_choice, proportion):
        """
        is_select 为0时不滑动，为1时滑动，proportion为滑动的比例，从0.1到1.0

        :param is_choice: int
        :param proportion: float
        """
        if is_choice == 1 and 0.1 <= proportion <= 1.0:
            point_ele = get_element(self.driver, self.cc_supply_point_locator)  # 获取滑块元素，并获取位置和大小
            locator_x = point_ele.location['x'] + point_ele.size['width'] / 2.0
            locator_y = point_ele.location['y'] + point_ele.size['height'] / 2.0
            button_ele = get_element(self.driver, self.cc_supply_submit_button_locator)  # 获取确定签订契约的元素，并获取位置和大小
            locator_x2 = (button_ele.location['x'] + button_ele.size['width'] - locator_x) * proportion
            TouchAction(self.driver).long_press(x=locator_x, y=locator_y).move_to(x=locator_x2,
                                                                                  y=0).release().perform()

        self.action.click(self.cc_supply_submit_button_locator)  # 点击确认签订契约
        self.action.click(self.cc_supply_confirm_button_locator)  # 点击确认签订
        pass

    def _choice_amount_and_submit_android(self, is_choice, proportion, contract_type):
        """
        is_select 为0时不滑动，为1时滑动，proportion为滑动的比例，从0.1到1.0
        :param is_choice: int
        :param proportion: float
        """
        if is_choice == 1 and 0.1 <= proportion <= 1.0:
            sleep(2)
            if contract_type == 'SUPPLY':
                point_ele = get_element(self.driver, self.submit_button_locator)  # 获取提交按钮元素，用来计算滑块长度
                swipe_button_ele = get_element(self.driver, self.swipe_button_locator)  # 获取滑块元素
            else:
                point_ele = get_element(self.driver, self.submit_button_locator2)  # 获取提交按钮元素，用来计算滑块长度
                swipe_button_ele = get_element(self.driver, self.swipe_button_locator2)  # 获取滑块元素
            locator_x = point_ele.size['width'] * proportion + point_ele.location['x'] + 10
            locator_y = swipe_button_ele.location['y'] + swipe_button_ele.size['height'] / 2
            TouchAction(self.driver).long_press(el=swipe_button_ele).\
                move_to(x=locator_x, y=locator_y).release().perform()
        sleep(3)
        if contract_type == 'SUPPLY':
            self.action.click(self.submit_button_locator)  # 点击确认签订契约
            self.action.click(self.confirm_button_locator)  # 点击确认签订
        else:
            self.action.click(self.submit_button_locator2)  # 点击确认签订契约
            self.action.click(self.confirm_button_locator)  # 点击确认签订
        pass
