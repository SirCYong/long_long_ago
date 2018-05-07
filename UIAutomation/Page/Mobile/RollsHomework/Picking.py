# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page.Mobile.MainPage.MainPage import MainPage
from UIAutomation.Page.Mobile.PublishLabour.PublishLabour import PublishLabour
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper

from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory

__author__ = "LiYu"
__doc__ = "拣选页面功能"


class PickingPage(BasePage):
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
        name_list = ['picking', 'location', 'commodity', 'amount', 'confirm', 'carrier', 'select_unit',
                     'position']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.picking_locator = ele_dic['picking']
        self.location_locator = ele_dic['location']
        self.commodity_locator = ele_dic['commodity']
        self.amount_locator = ele_dic['amount']
        self.confirm_locator = ele_dic['confirm']
        self.carrier_locator = ele_dic['carrier']
        self.select_unit_locator = ele_dic['select_unit']
        self.position_locator = ele_dic['position']

    def select_packing(self):
        """
        拣选
        :return:
        """
        w = ['KW001', 'sjbm1175w', 1, 'GOK01001', 'GOK01002']
        if self.is_run_ios():
            MainPage(self.driver).click_packing_ios()
            # 拣选1
            self._temporary_task_packing_ios(location=w[0], commodity=w[1], amount=w[2], carrier=w[3])
        if not self.is_run_ios():
            MainPage(self.driver).click_packing_android()
            # 拣选1
            self._temporary_task_packing_android(location=w[0], commodity=w[1], amount=w[2], carrier=w[3])

    def is_loaded(self):
        pass

    def _temporary_task_packing_ios(self, location=None, commodity=None, amount=None, carrier=None):
        """
        ios拣选
        :return:
        """
        self.action.set_value(self.location_locator, location)
        self.action.set_value(self.commodity_locator, commodity)
        self.action.set_value(self.amount_locator, amount)
        self._selection_unit_ios()
        self.action.set_value(self.carrier_locator, carrier)

    def _selection_unit_ios(self):
        """
        ios:选择单位
        :return:
        """
        self.action.click(self.select_unit_locator)
        # 滑动
        test_up = PublishLabour(self.driver)
        test_up.click_swipe_up(x1=1/2, y1=1, x2=1/2, y2=2/9, time=2000)
        self.action.click(self.confirm_locator)
        pass

    def _temporary_task_packing_android(self, location=None, commodity=None, amount=None, carrier=None):
        """
        android拣选
        :return:
        """
        self.action.send_keys(self.location_locator, location)
        self.action.send_keys(self.commodity_locator, commodity)
        self.action.send_keys(self.amount_locator, amount)
        self._selection_unit_android()
        self.action.send_keys(self.carrier_locator, carrier)
        # 无法点击键盘完成按钮，点击‘位置’
        self.action.click(self.position_locator)

    def _selection_unit_android(self):
        """
        android:选择单位
        :return:
        """
        self.action.click(self.select_unit_locator)
        # 滑动
        test_up = PublishLabour(self.driver)
        test_up.click_swipe_up(x1=1/2, y1=1, x2=1/2, y2=2/9, time=2000)
        self.action.click(self.confirm_locator)
        pass





