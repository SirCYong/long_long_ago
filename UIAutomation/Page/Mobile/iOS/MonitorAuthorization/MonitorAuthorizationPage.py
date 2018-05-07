# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchWindowException


# Author:zhongchangwei
from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, get_elements, get_element


class MonitorAuthorization(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

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
        name_list = ['take_container', 'picking_goods', 'quality_testing', 'print_receipt', 'purchase_order',
                     'procurement_planning', 'copy_jurisdiction', 'transfer_jurisdiction',
                     'do_not_want_to_assign_button', 'sure_assign_button']
        ele_dic = page_element_factory(__file__, name_list)
        self.take_container_locator = ele_dic['take_container']  # 拿取容器
        self.picking_goods_locator = ele_dic['picking_goods']  # 拣选商品
        self.quality_testing_locator = ele_dic['quality_testing']  # 质检
        self.print_receipt_locator = ele_dic['print_receipt']  # 打印入库单
        self.purchase_order_locator = ele_dic['purchase_order']  # 下采购单
        self.procurement_planning_locator = ele_dic['procurement_planning']  # 采购计划
        self.copy_jurisdiction_locator = ele_dic['copy_jurisdiction']  # 复制权限
        self.transfer_jurisdiction_locator = ele_dic['transfer_jurisdiction']  # 移交权限
        self.do_not_want_to_assign_button_locator = ele_dic['do_not_want_to_assign_button']  # 不想分配
        self.sure_assign_button_locator = ele_dic['sure_assign_button']  # 确认分配
        pass

    def is_loaded(self):
        pass

    def assign_permission(self, assign_type, user_name, permission_type1=None, permission_type2=None,
                          permission_type3=None, permission_type4=None, permission_type5=None, permission_type6=None):

        """
            选择权限，复制或者移交权限，搜索通讯录用户，分配权限，完成分配

        :param assign_type: 复制或者移交
        :param user_name:  通讯录名
        :param permission_type1:  权限
        :param permission_type2:  权限
        :param permission_type3:  权限
        :param permission_type4:  权限
        :param permission_type5:  权限
        :param permission_type6:  权限
        """
        self.initial_element()

        # 通讯录页面
        self.mail_list_instant = MailListPage(self.driver)
        self.mail_list_instant.page_factory()
        self.search_locator = self.mail_list_instant.search_locator  # 搜索
        self.assign_locator = self.mail_list_instant.assign_locator  # 分配

        if permission_type1:
            get_elements(self.driver, permission_type1)[-1].click()  # 选择权限
        if permission_type2:
            get_elements(self.driver, permission_type2)[-1].click()  # 选择权限
        if permission_type3:
            get_elements(self.driver, permission_type3)[-1].click()  # 选择权限
        if permission_type4:
            get_elements(self.driver, permission_type4)[-1].click()  # 选择权限
        if permission_type5:
            get_elements(self.driver, permission_type5)[-1].click()  # 选择权限
        if permission_type6:
            get_elements(self.driver, permission_type6)[-1].click()  # 选择权限

        get_element(self.driver, assign_type).click()   # 提交
        get_element(self.driver, self.search_locator).send_keys(user_name)  # 查询需要分配的用户
        get_element(self.driver, self.search_locator).click()
        sleep(1)
        get_elements(self.driver, self.assign_locator)[-1].click()  # 点击分配按钮

        get_elements(self.driver, self.sure_assign_button_locator)[-1].click()  # 确认分配页面，确认分配