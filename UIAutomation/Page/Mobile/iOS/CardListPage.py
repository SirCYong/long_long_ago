# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException


# Author:zhongchangwei
from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory


class CardPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

        try:
            self.is_loaded()
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
        name_list = ['select_logistics_brand',
                     'modify_receipt_information',
                     'OpenOrderDownload',
                     'non_service_certification',
                     'distribution_manager_and_supervisor',
                     'monitor_authorization',
                     'manager_authorization',
                     'select_service_scope',
                     'contract_of_carriage',
                     'sign_labor_contract',
                     'sign_warehouse_supply_contract',
                     'sign_warehouse_demand_contract',
                     'back', 'f5',
                     'CardOne', 'CardTwo', 'longCard',
                     'back',
                     'ware_house_demand',
                     'longTimeCard',
                     'twenty-six_long_task',
                     'generate_bill'
                     ]
        ele_dic = page_element_factory(__file__, name_list)
        self.select_logistics_brand_locator = ele_dic['select_logistics_brand']   # 选择物流品牌
        self.modify_receipt_information_locator = ele_dic['modify_receipt_information']  # 修改收货信息
        self.open_order_download_locator = ele_dic['OpenOrderDownload']  # 开启订单下载
        self.non_service_certification_locator = ele_dic['non_service_certification']  # 非服务认证
        self.distribution_manager_and_supervisor_locator = ele_dic['distribution_manager_and_supervisor']  # 分配管理者和监控者
        self.monitor_authorization_locator = ele_dic['monitor_authorization']  # 监控者授权
        self.manager_authorization_locator = ele_dic['manager_authorization']  # 管理者授权
        self.selectservicescope_locator = ele_dic['select_service_scope']  # 选择服务范围
        self.contract_of_carriage_locator = ele_dic['contract_of_carriage']  # 找运输供应
        self.sign_labor_contract_locator = ele_dic['sign_labor_contract']  # 找劳务需求
        self.sign_warehouse_supply_contract_locator = ele_dic['sign_warehouse_supply_contract']  # 生成找仓储供应的任务
        self.sign_warehouse_demand_contract_locator = ele_dic['sign_warehouse_demand_contract']  # 生成找仓储需求的任务
        self.f5_locator = ele_dic['f5']  # 刷新
        # 临时卡片,Sprint2临时出来一个长期卡片中心,点击进去卡片中心
        self.CardOne_locator = ele_dic['CardOne']  #
        self.CardTwo_locator = ele_dic['CardTwo']
        self.back_locator = ele_dic['back']
        self.ware_house_demand_locator = ele_dic['ware_house_demand']
        self.cilck_long_card_locator = ele_dic['longTimeCard']
        self.long_card_locator = ele_dic['longCard']
        self.twenty_six_long_task_locator = ele_dic['twenty-six_long_task']
        self.generate_bill_locator = ele_dic['generate_bill']
        pass

    def is_loaded(self):
        pass

    def click_generate_bill_card(self):
        """
        点击'生成账单'卡片
        """
        self.action.click(self.generate_bill_locator)

    def click_twenty_six_long_task_locator(self):
        """
        点击26个长期任务
        """
        self.action.click(self.twenty_six_long_task_locator)

    def flick_left_to_right(self):
        """
        长期任务中翻页直至"生成账单"
        """
        self.initial_element()
        size_dic = self.action.get_window_size()
        start_x = size_dic['width'] * 0.8
        start_y = size_dic['height'] * 0.5
        end_y = 0
        # print size_dic['width']
        # print size_dic['height']
        # sleep(3)
        for i in range(2):
            self.action.swipe(int(start_x), start_y, - int(start_x), end_y, 1500)
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
        # width = self.driver.get_window_size()['width']
        # height = self.driver.get_window_size()['height']
        self.action.swipe(width / 2, height * 6 / 7, width / 2, -(height * 4 / 7), 1000)
        # self.driver.swipe(width / 2, height * 6 / 7, width / 2, -(height * 4 / 7), 1000)

    def click_select_service_scope(self):
        self.action.click(['ACCESSIBILITY_ID', '选择服务范围'])
        # get_element(self.driver, ['ACCESSIBILITY_ID', '选择服务范围']).click()

    # 空白卡片
    def click_card_one(self):
        self.action.click(self.CardOne_locator)
        pass

    def click_card_two(self):
        self.action.click(self.CardTwo_locator)
        pass

    def click_long_card(self):

        self.action.click(self.long_card_locator)
        pass

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

    def click_long_time_card(self):
        self.action.click(self.cilck_long_card_locator)

    def click_generate_bill(self):
        """
        登陆后找到并点击"生成账单"卡片
        """
        self.click_twenty_six_long_task_locator()  # 登录后点击长期任务，进入长期任务卡片主界面
        self.card_page.flick_left_to_right()  # 从左往右滑动到"生成账单"卡片
        self.card_page.click_generate_bill_card()  # 点击"生成账单"卡片
        pass
