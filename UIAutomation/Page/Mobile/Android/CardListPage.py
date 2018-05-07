# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, get_elements
from UIAutomation.Page import BasePage

__author__ = 'zhongchangwei'


class CardPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.select_logistics_brand_locator = None
        self.modify_receipt_information_locator = None
        self.open_order_download_locator = None
        self.OpenSyncCardBtn_element = None
        self.close_order_download_locator = None
        self.long_task_locator = None
        self.generate_labor_demand_locator = None
        self.generate_bill_locator = None
        self.CardOne_locator = None
        self.CardTwo_locator = None
        self.sign_labor_contract_locator = None
        self.sign_warehouse_supply_contract_locator = None
        self.sign_warehouse_demand_contract_locator = None
        self.f5_locator = None
        self.non_service_certification_locator = None
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
        name_list = ['select_logistics_brand', 'modify_receipt_information', 'OpenOrderDownload', 'OpenSyncCardBtn',
                     'close_order_download', 'long_task', 'generate_labor_demand', 'generate_bill']
        ele_dic = page_element_factory(__file__, name_list)
        self.select_logistics_brand_locator = ele_dic['select_logistics_brand']   # 选择物流品牌
        self.modify_receipt_information_locator = ele_dic['modify_receipt_information']  # 修改收货信息
        self.open_order_download_locator = ele_dic['OpenOrderDownload']  # 开启订单下载
        self.OpenSyncCardBtn_element = ele_dic['OpenSyncCardBtn']
        self.close_order_download_locator = ele_dic['close_order_download']  # 关闭订单下载
        self.long_task_locator = ele_dic['long_task']  # XX个长期任务
        self.generate_labor_demand_locator = ele_dic['generate_labor_demand']  # 生成找劳务需求的任务
        self.generate_bill_locator = ele_dic['generate_bill']  # 生成账单
        self.CardOne_locator = ele_dic['CardOne']  # 非服务认证卡片
        self.sign_labor_contract_locator = ele_dic['sign_labor_contract']  # 生成找劳务需求的任务
        self.sign_warehouse_supply_contract_locator = ele_dic['sign_warehouse_supply_contract']  # 生成找仓储供应的任务
        self.sign_warehouse_demand_contract_locator = ele_dic['sign_warehouse_demand_contract']  # 生成找仓储需求的任务
        self.CardTwo_locator = ele_dic['CardTwo']
        self.f5_locator = ele_dic['f5']  # 刷新
        self.non_service_certification_locator = ele_dic['non_service_certification']  # 非服务认证
        pass

    def is_loaded(self):
        pass

    def click_f5(self):
        self.action.click(self.f5_locator)

    def click_non_service_certification_card(self):
        self.action.click(self.non_service_certification_locator)

    def click_card_one(self):
        self.action.click(self.CardOne_locator)
        pass

    def sign_labor_contract_locator_card(self):
        self.action.click(self.sign_labor_contract_locator)

    def click_select_logistics_brand_card(self):
        self.initial_element()
        get_element(self.driver, self.select_logistics_brand_locator).click()

    def click_modify_receipt_information_card(self):
        self.initial_element()
        get_element(self.driver, self.modify_receipt_information_locator).click()

    def open_order_download_card_text(self):
        self.initial_element()
        open_order_download_card_text = get_elements(self.driver, self.open_order_download_locator)[2].text
        print (open_order_download_card_text)

    def click_open_order_download_card(self):
        self.initial_element()
        get_elements(self.driver, self.open_order_download_locator)[2].click()

    def click_select_SyncOpenCard(self):
        self.initial_element()
        get_element(self.driver, self.OpenSyncCardBtn_element).click()

    def click_close_order_download_card(self):
        self.initial_element()
        get_element(self.driver, self.close_order_download_locator).click()

    def click_long_task(self):
        self.initial_element()
        self.action.click(self.long_task_locator)

    def flick_top_to_bottom(self):
        self.initial_element()
        size_dic = self.action.get_window_size()
        start_x = size_dic['width'] / 2
        start_y = size_dic['height'] * 0.9
        end_x = size_dic['width'] / 2
        end_y = size_dic['height'] * 0.4
        for i in range(3):
            sleep(2)
            self.action.swipe(int(start_x), int(start_y), int(end_x), int(end_y), 1500)
        pass

    def click_generate_labor_demand(self):
        self.initial_element()
        self.driver.find_element_by_android_uiautomator("new UiSelector().textContains(\"生成找劳务需求的任务\")").click()
        self.action.click(self.generate_labor_demand_locator)

    def click_generate_bill(self):
        self.initial_element()
        self.action.click(self.generate_bill_locator)




