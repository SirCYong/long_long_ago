# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import basic_sit
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory

__author__ = "LiYu"
__doc__ = "移动和交接页面"


class MovePage(BasePage):

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

    def page_factory(self):
        """
        初始化页面控件
        """
        name_list = ['move', 'handover', 'waybill_number', 'starting_position', 'target_location', 'complete',
                     'starting_entrust', 'target_entrust']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.move_locator = ele_dic['move']
        self.handover_locator = ele_dic['handover']
        self.waybill_number_locator = ele_dic['waybill_number']
        self.starting_position_locator = ele_dic['starting_position']
        self.target_location_locator = ele_dic['target_location']
        self.complete_locator = ele_dic['complete']
        self.starting_entrust_locator = ele_dic['starting_entrust']
        self.target_entrust_locator = ele_dic['target_entrust']

    def move(self):
        """
        移动
        :return:
        """
        if self.is_run_ios:
            self._click_move_ios()
        if not self.is_run_ios():
            self._click_move_android()

    def handover(self):
        """
        交接
        :return:
        """
        if self.is_run_ios:
            self._click_handover_ios()
        if not self.is_run_ios():
            self._click_handover_android()

    def select_code(self):
        """
        数据库查询快递单号
        :return:
        """
        self.code_list = []
        con, curs = basic_sit()
        try:
            sql = ['select  o.identify_code from xdw_app.cm_identify_relation_package o order by o.update_time desc']
            curs.execute(sql)
            result = curs.fetchone()
            for t in result:
                self.code_list.append(t[0])

        except Exception as e:
            print(e, '查询快递单号出错')

    def _click_move_ios(self):
        self.action.click(self.move_locator)
        self.action.set_value(self.waybill_number_locator, value=self.code_list[0])
        self.action.click(self.complete_locator)

    def _click_move_android(self):
        self.action.click(self.move_locator)
        self.action.send_keys(self.waybill_number_locator, value=self.code_list[0])
        self.action.click(self.complete_locator)

    def _click_handover_ios(self):
        self.action.click(self.handover_locator)
        self.action.set_value(self.waybill_number_locator, value=self.code_list[0])
        self.action.click(self.complete_locator)

    def _click_handover_android(self):
        self.action.click(self.handover_locator)
        self.action.send_keys(self.waybill_number_locator, value=self.code_list[0])
        self.action.click(self.complete_locator)






