# -*- coding: utf-8 -*-

from UIAutomation.Page import BasePage
import time
from UIAutomation.Utils import ParseXmlErrorException, GlobalVar, run_info_log, page_element_factory
__author__ = "Yuetianzhuang"
__doc__ = "通用卡片List"


class CommonCardPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.select_logistics_brand_locator = None
        self.modify_receipt_information_locator = None
        self.open_order_download_locator = None
        self.non_service_certification_locator = None
        self.distribution_manager_and_supervisor_locator = None
        self.monitor_authorization_locator = None
        self.manager_authorization_locator = None
        self.contract_of_carriage_locator = None
        self.sign_labor_contract_locator = None
        self.sign_warehouse_supply_contract_locator = None
        self.sign_warehouse_demand_contract_locator = None
        self.f5_locator = None
        self.return1_locator = None
        self.CardOne_locator = None
        self.longCard_locator = None
        self.back_locator = None
        self.ware_house_demand_locator = None
        self.long_task_locator = None
        self.RegisterSupplier_locator = None
        self.purchase_orders_locator = None
        self.upload_delivery_order_locator = None
        self.set_promotional_template_locator = None
        self.release_storage_requirement_locator = None
        self.release_supply_locator = None

        try:
            self.initial_element()
        except ParseXmlErrorException:
            print(u'XML解析失败.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'XML解析失败.', GlobalVar.get_log_file())
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except Exception():
            print(u'控件不在当前页面上.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'控件不在当前页面上.', GlobalVar.get_log_file())
            raise
        pass

    def page_factory(self):
        # iOS and Android端统一的控件
        name_list = ['', '', '', '']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self._locator = ele_dic['']
        self._locator = ele_dic['']
        self._locator = ele_dic['']
        self._locator = ele_dic['']
        # IOS独立的控件
        if self.is_run_ios():
            name_list = ['purchase_orders', 'upload_delivery_order',
                         'set_promotional_template', 'release_storage_requirement',
                         'release_supply', 'RegisterSupplier',
                         'select_logistics_brand', 'modify_receipt_information',
                         'open_order_download', 'non_service_certification',
                         'distribution_manager_and_supervisor', 'monitor_authorization',
                         'manager_authorization', 'contract_of_carriage',
                         'sign_labor_contract', 'sign_warehouse_supply_contract',
                         'sign_warehouse_demand_contract', 'f5',
                         'return1', 'CardOne', 'longCard', 'back',
                         'ware_house_demand', 'long_task', 'RegisterSupplier']
            ele_dic = page_element_factory(__file__, name_list)
            self.select_logistics_brand_locator = ele_dic['select_logistics_brand']
            self.modify_receipt_information_locator = ele_dic['modify_receipt_information']
            self.open_order_download_locator = ele_dic['open_order_download']
            self.non_service_certification_locator = ele_dic['non_service_certification']
            self.distribution_manager_and_supervisor_locator = ele_dic['distribution_manager_and_supervisor']
            self.monitor_authorization_locator = ele_dic['monitor_authorization']
            self.manager_authorization_locator = ele_dic['manager_authorization']
            self.contract_of_carriage_locator = ele_dic['contract_of_carriage']
            self.sign_labor_contract_locator = ele_dic['sign_labor_contract']
            self.sign_warehouse_supply_contract_locator = ele_dic['sign_warehouse_supply_contract']
            self.sign_warehouse_demand_contract_locator = ele_dic['sign_warehouse_demand_contract']
            self.f5_locator = ele_dic['f5']
            self.return1_locator = ele_dic['return1']
            self.CardOne_locator = ele_dic['CardOne']
            self.longCard_locator = ele_dic['longCard']
            self.back_locator = ele_dic['back']
            self.ware_house_demand_locator = ele_dic['ware_house_demand']
            self.long_task_locator = ele_dic['long_task']
            self.RegisterSupplier_locator = ele_dic['RegisterSupplier']
            self.purchase_orders_locator = ele_dic['purchase_orders']
            self.upload_delivery_order_locator = ele_dic['upload_delivery_order']
            self.set_promotional_template_locator = ele_dic['set_promotional_template']
            self.release_storage_requirement_locator = ele_dic['release_storage_requirement']
            self.release_supply_locator = ele_dic['release_supply']
        # Android独立的控件
        if not self.is_run_ios():
            name_list = ['']
            ele_dic = page_element_factory(self.xml_file, name_list)
            # 左上角更多按钮
            self._locator = ele_dic['']
        pass

    def is_loaded(self):
        pass

    def click_select_logistics_brand_card(self):
        self.action.click(self.select_logistics_brand_locator)

    def click_modify_receipt_information_card(self):
        self.action.click(self.modify_receipt_information_locator)

    def open_order_download_card_text(self):
        open_order_download_card_text = self.action.text(self.open_order_download_locator)
        print (open_order_download_card_text)

    def click_open_order_download_card(self):
        self.action.click(self.open_order_download_locator)

    def click_non_service_certification_card(self):
        self.action.click(self.non_service_certification_locator)

    def distribution_manager_and_supervisor_card(self):
        self.action.click(self.distribution_manager_and_supervisor_locator)

    def monitor_authorization_card(self):
        self.action.click(self.monitor_authorization_locator)

    def manager_authorization_card(self):
        self.action.click(self.manager_authorization_locator)

    def drop_down(self):
        width = self.action.get_window_size()['width']
        height = self.action.get_window_size()['height']
        self.action.swipe(width / 2, height * 6 / 7, width / 2, -(height * 4 / 7), 1000)

    def click_select_service_scope(self):
        self.action.click(['ACCESSIBILITY_ID', '选择服务范围'])

    # 空白卡片
    def click_card_one(self):
        self.action.click(self.CardOne_locator)

    def contract_carriage_locator_card(self):
        self.action.click(self.contract_of_carriage_locator)

    def sign_labor_contract_locator_card(self):
        self.action.click(self.sign_labor_contract_locator)

    def sign_warehouse_supply_contract_card(self):
        self.action.click(self.sign_warehouse_supply_contract_locator)

    def sign_warehouse_demand_contract_card(self):
        self.action.click(self.sign_warehouse_demand_contract_locator)

    def click_f5(self):
        self.action.click(self.f5_locator)

    def back(self):
        self.action.click(self.back_locator)

    def click_ware_house_demand(self):
        self.action.click(self.ware_house_demand_locator)

    # 点击长期卡片
    def click_long_task(self):
        self.action.click(self.long_task_locator)

    # 注册供应商
    def click_register_supplier(self):
        self.action.click(self.RegisterSupplier_locator)

    # 选购下单
    def click_purchase_orders(self):
        self.action.click(self.purchase_orders_locator)

    # 上传送货单
    def click_upload_delivery(self):
        self.action.click(self.upload_delivery_order_locator)

    # 设置促销模板
    def click_set_promotional_template(self):
        self.action.click(self.set_promotional_template_locator)

    # 发布仓储需求
    def click_release_storage_requirement(self):
        self.action.click(self.release_storage_requirement_locator)

    # 发布供货供应
    def click_release_supply(self):
        self.action.click(self.release_supply_locator)





