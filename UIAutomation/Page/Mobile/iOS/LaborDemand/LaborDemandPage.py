# -*- coding: utf-8 -*-

from time import sleep

from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.iOS.LaborDemand.SelectAddress.SelectAddressPage import SelectAddressPage
from UIAutomation.Page.Mobile.iOS.LaborDemand.SelectAddress.SelectCity import SelectAddressCity
from UIAutomation.Page.Mobile.iOS.LaborDemand.SelectAddress.SelectCityArea import SelectAddressCityArea
from UIAutomation.Page.Mobile.iOS.LaborDemand.SelectTime import SelectTime
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory

__author__ = "LiYu"
"""发布劳务需求页面"""





class LaborDemandPage(BasePage):
    def is_loaded(self):
        pass

    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.picking_locator = None
        self.packaging_locator = None
        self.handover_locator = None
        self.shelves_locator = None
        self.icon_cut_locator = None
        self.icon_add_locator = None
        self.day_shift_locator = None
        self.night_locator = None
        self.select_date_locator = None
        self.select_address_locator = None
        self.location_locator = None
        self.complete_locator = None
        self.continue_release_locator = None

        try:
            self.initial_element()
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
        name_list = ['Please_select', 'Picking', 'Packaging', 'Handover', 'Shelves', 'icon_cut', 'icon_add',
                     'DayShift', 'Night', 'SelectDate', 'SelectAddress', 'Location', 'Complete',
                     'ContinueRelease', 'Province', 'Provinces_city', 'Provinces_cities_area']
        ele_dic = page_element_factory(__file__, name_list)
        self.picking_locator = ele_dic['Picking']  # 拣选
        self.packaging_locator = ele_dic['Packaging']     # 包装
        self.handover_locator = ele_dic['Handover']   # 交接
        self.shelves_locator = ele_dic['Shelves']     # 上架
        self.icon_cut_locator = ele_dic['icon_cut']  # 人数 -
        self.icon_add_locator = ele_dic['icon_add']  # 人数 +
        self.day_shift_locator = ele_dic['DayShift']   # 白班
        self.night_locator = ele_dic['Night']     # 晚班
        self.select_date_locator = ele_dic['SelectDate']  # 选择时间
        self.select_address_locator = ele_dic['SelectAddress']  # 选择地址
        self.location_locator = ele_dic['Location']
        self.complete_locator = ele_dic['Complete']  # 完成
        self.continue_release_locator = ele_dic['ContinueRelease']  # 继续发布
        self.please_select_locator = ele_dic['Please_select']  # 请选择
        self.province_locator = ele_dic['Province']  # 省
        self.provinces_city_locator = ele_dic['Provinces_city']  # 市
        self.provinces_cities_area_locator = ele_dic['Provinces_cities_area']  # 区
        self.confirm_locator = ele_dic['confirm']  # 确定
        pass

    def assert_picking_locator_present(self):
        """
        判断拣选员存在
        :return:
        """
        assert_that(self.action.is_element_present(self.picking_locator), equal_to(True))

    def assert_location_present(self):
        """
        判断控件浙江省 杭州市 西湖区存在
        :return:
        """
        assert_that(self.action.is_element_present(self.location_locator), equal_to(True))

    def click_please_select(self):
        """
        点击请选择操作
        :return:
        """
        self.action.click(self.please_select_locator)

    def click_packing(self):
        """
        选择拣选、包装、分拣、交接
        :return:
        """
        self.action.click(self.packaging_locator)
        self.action.click(self.handover_locator)
        self.action.click(self.shelves_locator)
        self.action.click(self.packaging_locator)
        self.action.click(self.confirm_locator)
        sleep(2)
        self.action.click(self.day_shift_locator)
        self.action.click(self.icon_cut_locator)
        pass

    def click_select_time(self):
        """
        选择时间
        :return:
        """
        self.action.click(self.select_date_locator)
        SelectTime(self.driver).click_confirm()
        pass

    def click_select_address(self):
        """
        选择地址
        :return:
        """
        self.action.click(self.select_address_locator)

        SelectAddressPage(self.driver).select_province()

        SelectAddressCity(self.driver).select_province_city()

        SelectAddressCityArea(self.driver).select_province_city_area()
        pass

    def click_complete(self):
        """
        点击完成操作
        :return:
        """
        self.action.click(self.complete_locator)

    def click_continue_release(self):
        """
        点击继续发布
        :return:
        """
        self.action.click(self.continue_release_locator)

    def assert_please_select_address(self):
        """
        判断是否存在请选择地址
        :return:
        """
        assert_that(self.action.is_element_present(self.select_address_locator), equal_to(True))
