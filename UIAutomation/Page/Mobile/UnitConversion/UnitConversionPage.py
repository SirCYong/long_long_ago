# coding: utf-8
from time import sleep

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, initial_element_error_wrapper
from UIAutomation.Page import BasePage
__author__ = 'chenyanxiu'


class UnitConversionPage(BasePage):
    """
    单位转换
    """

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
        name_list = ['add_unit', 'et_add', 'bt_add', 'search', 'unit_name', 'unit_edit', 'unit_del', 'input_edit',
                     'next', 'before_count', 'before_unit', 'later_count', 'later_name', 'manage_unit', 'confirm',
                     'convert', 'convert_unit', 'card', 'back']

        ele_dic = page_element_factory(self.xml_file, name_list)
        self.add_unit_locator = ele_dic['add_unit']  # 添加单位
        self.et_add_locator = ele_dic['et_add']  # 输入
        self.bt_add_locator = ele_dic['bt_add']  # 确定
        self.search_locator = ele_dic['search']
        self.unit_name_locator = ele_dic['unit_name']
        self.unit_edit_contract_locator = ele_dic['unit_edit']  # 编辑单位
        self.unit_del_locator = ele_dic['unit_del']  # 删除单位
        self.input_edit_locator = ele_dic['input_edit']  # 输入商品
        self.next_locator = ele_dic['next']
        self.before_count_locator = ele_dic['before_count']  # 数量
        self.before_unit_locator = ele_dic['before_unit']  # 数量单位
        self.later_count_locator = ele_dic['later_count']
        self.later_name_locator = ele_dic['later_name']
        self.manage_unit_locator = ele_dic['manage_unit']  # 管理单位
        self.confirm_locator = ele_dic['confirm']  # 确定
        self.convert_locator = ele_dic['convert']  # 转换
        self.convert_unit_locator = ele_dic['convert_unit']  # 转换
        self.card_locator = ele_dic['card']
        self.back_locator = ele_dic['back']
        pass

    def _page_factory_android(self):
        name_list = ['add_unit', 'et_add', 'bt_add', 'search', 'unit_name', 'unit_edit', 'unit_del', 'input_edit',
                     'next', 'search_1', 'before_count', 'before_unit', 'later_count', 'later_name', 'manage_unit',
                     'confirm', 'convert', 'edit', 'delete', 'convert_later', 'convert_before', 'lanya', 'button1',
                     'card']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.add_unit_locator = ele_dic['add_unit']  # 添加单位
        self.et_add_locator = ele_dic['et_add']  # 输入
        self.bt_add_locator = ele_dic['bt_add']  # 确定
        self.search_locator = ele_dic['search']
        self.unit_name_locator = ele_dic['unit_name']
        self.unit_edit_contract_locator = ele_dic['unit_edit']  # 编辑单位
        self.unit_del_locator = ele_dic['unit_del']  # 删除单位
        self.input_edit_locator = ele_dic['input_edit']  # 输入商品
        self.next_locator = ele_dic['next']
        self.search_1_locator = ele_dic['search_1']
        self.before_count_locator = ele_dic['before_count']  # 数量
        self.before_unit_locator = ele_dic['before_unit']  # 数量单位
        self.later_count_locator = ele_dic['later_count']
        self.later_name_locator = ele_dic['later_name']
        self.manage_unit_locator = ele_dic['manage_unit']  # 管理单位
        self.confirm_locator = ele_dic['confirm']  # 确定
        self.convert_locator = ele_dic['convert']  # 转换
        self.edit_locator = ele_dic['edit']  # 编辑转换
        self.delete_locator = ele_dic['delete']
        self.convert_later_locator = ele_dic['convert_later']  # 转换后
        self.convert_before_locator = ele_dic['convert_before']  # 转换前
        self.lanya_locator = ele_dic['lanya']  # 转换前
        self.button1_locator = ele_dic['button1']
        self.card_locator = ele_dic['card']
        pass

    def is_loaded(self):
        pass

    def page_factory(self):
        if self.is_run_ios():
            self._page_factory_ios()
        else:
            self._page_factory_android()

    def add_unit(self, unit):
        if self.is_run_ios():
            self._add_unit_ios(unit)
        else:
            self._add_unit_android(unit)

    def unit_convert(self, unit, goods):
        if self.is_run_ios():
            self._unit_convert_ios(unit, goods)
        else:
            self._unit_convert_android(unit, goods)

    def _add_unit_ios(self, unit):
        """
        添加单位
        """
        self.action.click(self.add_unit_locator)  # 添加单位
        self.action.send_keys(self.et_add_locator, unit)
        self.action.click(self.bt_add_locator)  # 确定
        sleep(4)
        self.action.click(self.back_locator)
        sleep(2)
        while self.action.is_element_present(self.card_locator) != 1:
            self.action.click(self.back_locator)
        pass

    def _add_unit_android(self, unit):
        """
        添加单位
        """
        self.action.click(self.add_unit_locator)  # 添加单位
        self.action.set_value(self.et_add_locator, unit)
        self.action.click(self.bt_add_locator)  # 确定
        # self.action.click(self.search_locator)  # 搜索
        # self.action.send_keys(self.search_locator, unit)
        # self.action.is_element_present(self.unit_name_locator, locator_order=[0])  # 判断单位是否添加成功
        sleep(4)
        self.driver.keyevent(4)
        sleep(2)
        while self.action.is_element_present(self.card_locator) != 1:
            self.driver.keyevent(4)
        # assert self.action.text(self.unit_name_locator, locator_order=[0]) == unit
        pass

    def _unit_convert_ios(self, unit, goods, num1=12, num2=1):
        """
            单位转换
            """
        self.action.set_value(self.input_edit_locator, goods)
        self.action.click(self.next_locator)  # 下一步
        self.action.set_value(self.before_count_locator, num1)
        self.action.set_value(self.later_count_locator, num2)
        self.action.click(self.later_name_locator)
        self.action.click(self.confirm_locator)  # 选择该单位
        # self.action.is_element_present(self.unit_name_locator, locator_order=[0])  # 判断单位是否添加成功
        assert self.action.text(self.later_name_locator) == unit
        self.action.click(self.convert_locator)
        sleep(2)
        before_unit = self.action.text(self.before_unit_locator)
        convert_unit = ' 1' + unit + ' 12' + before_unit
        print(convert_unit)
        assert self.action.text(self.convert_unit_locator) == convert_unit
        pass

    def _unit_convert_android(self, unit, goods, num1=12, num2=1):
        """
        单位转换
        """
        if self.action.is_element_present(self.button1_locator):
            self.action.click(self.button1_locator)  # 确定
            self.driver.keyevent(4)
        elif self.action.is_element_present(self.lanya_locator):
            self.driver.keyevent(4)
        self.action.send_keys(self.input_edit_locator, goods)
        self.action.click(self.next_locator)  # 下一步
        self.action.send_keys(self.before_count_locator, num1)
        self.action.send_keys(self.later_count_locator, num2)
        self.action.click(self.later_name_locator)
        self.action.click(self.confirm_locator)  # 选择该单位
        # self.action.is_element_present(self.unit_name_locator, locator_order=[0])  # 判断单位是否添加成功
        assert self.action.text(self.later_name_locator) == unit
        self.action.click(self.convert_locator)
        sleep(2)
        assert self.action.text(self.convert_later_locator) == unit
        pass

