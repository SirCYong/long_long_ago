from time import sleep

from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.PublishLabour.PublishLabour import PublishLabour
from UIAutomation.Utils import ParseXmlErrorException, initial_element_error_wrapper, page_element_factory


__author__ = "LiYu"
__doc__ = "建立契约义务项"


class ContractualObligation(BasePage):
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
        except NoSuchWindowException:
            initial_element_error_wrapper(self.driver)
            raise

    def page_factory(self):
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ['add_obligations', 'without_add_obligations', 'service_type',
                     'invoice_amount', 'confirm', 'start_time', 'end_time', 'quantity_ceiling', 'type',
                     'lower_number', 'origin', 'tolerate', 'resource_discount', 'complete', 'continue_add',
                     'all_compulsory_items', 'swipe_year', 'select_time_confirm', 'close']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.add_obligations_locator = ele_dic['add_obligations']
        self.without_add_obligations_locator = ele_dic['without_add_obligations']
        self.invoice_amount_locator = ele_dic['invoice_amount']
        self.service_type_locator = ele_dic['service_type']
        self.start_time_locator = ele_dic['start_time']
        self.end_time_locator = ele_dic['end_time']
        self.type_locator = ele_dic['type']
        self.confirm_locator = ele_dic['confirm']
        self.quantity_ceiling_locator = ele_dic['quantity_ceiling']   # 上限
        self.lower_number_locator = ele_dic['lower_number']     # 下限
        self.origin_locator = ele_dic['origin']
        self.tolerate_locator = ele_dic['tolerate']    # 容忍
        self.resource_discount_locator = ele_dic['resource_discount']  # 折扣
        self.complete_locator = ele_dic['complete']
        self.continue_add_locator = ele_dic['continue_add']
        self.all_compulsory_items_locator = ele_dic['all_compulsory_items']
        self.swipe_year_locator = ele_dic['swipe_year']
        self.select_time_confirm_locator = ele_dic['select_time_confirm']
        self.close_locator = ele_dic['close']

    def is_loaded(self):
        pass

    def service_contract(self):
        """
        建立契约义务项：仓储服务契约
        :return:
        """
        if self.is_run_ios():
            self._service_contract_ios()
            self._continue_add_ios()
            self._invoice_amount_ios()
            self._complete_ios()
            self._assert_continue_ios()
            # self._all_compulsory_ios()
        if not self.is_run_ios():
            self._service_contract_android()
            self._continue_add_android()
            self._invoice_amount_android()
            self._complete_android()
            self._all_compulsory_android()

    def _service_contract_ios(self):
        """
        ios:添加义务项(服务星级)
        :return:
        """
        # 点击添加义务项
        self.action.click(self.add_obligations_locator)
        # 点击类型
        self.action.click(self.type_locator)
        # 点击服务星级
        self.action.click(self.service_type_locator)
        # 点击确认
        self.action.click(self.confirm_locator)
        # 折扣
        self.action.set_value(self.resource_discount_locator, value=9)
        # 点击开始时间
        self.action.click(self.start_time_locator)
        self.action.click(self.start_time_locator)
        # 点击确认
        self.action.click(self.confirm_locator)
        # 上限
        self.action.set_value(self.quantity_ceiling_locator, value=18888)
        self.close()
        # 下限
        self.action.set_value(self.lower_number_locator, value=100)
        self.close()

    def _continue_add_ios(self):
        """
        ios:继续添加
        :return:
        """
        self.action.click(self.continue_add_locator)
        sleep(2)

    def _all_compulsory_ios(self):
        """
        ios:点击已添加所有义务项
        :return:
        """
        self.action.click(self.all_compulsory_items_locator)

    def _complete_ios(self):
        """
        ios:点击完成
        :return:
        """
        self.action.click(self.complete_locator)

    def _invoice_amount_ios(self):
        """
        服务契约义务项(发货单量)
        :return:
        """
        # 点击类型
        self.action.click(self.type_locator)
        # 发货单量
        self.action.click(self.invoice_amount_locator)
        # 确认
        self.action.click(self.confirm_locator)
        # 结束时间
        self.action.click(self.end_time_locator)
        # 确认
        self.action.click(self.confirm_locator)
        # 上限
        self.action.send_keys(self.quantity_ceiling_locator, value=99999)
        self.close()
        # 下限
        self.action.send_keys(self.lower_number_locator, value=100)
        self.close()
        # 容忍
        self.action.click(self.tolerate_locator)

    def _service_contract_android(self):
        """
        android:添加义务项(服务星级)
        :return:
        """
        # 点击添加义务项
        sleep(20)
        self.action.click(self.add_obligations_locator)
        # 点击类型
        self.action.click(self.type_locator)
        # 点击服务星级
        self.action.click(self.service_type_locator)
        # 点击确认
        self.action.click(self.confirm_locator)
        # 折扣
        self.action.send_keys(self.resource_discount_locator, value=9)
        # 点击开始时间
        self.action.click(self.start_time_locator)
        # 确认
        self.action.click(self.select_time_confirm_locator)
        # 结束时间
        self.action.click(self.end_time_locator)
        # 确认
        self.action.click(self.select_time_confirm_locator)
        # 上限
        self.action.send_keys(self.quantity_ceiling_locator, value=18888)
        # 下限
        self.action.send_keys(self.lower_number_locator, value=100)
        pass

    def _invoice_amount_android(self):
        """
        服务契约义务项(发货单量)
        :return:
        """
        # 点击类型
        self.action.click(self.type_locator)
        # 发货单量
        self.action.click(self.invoice_amount_locator)
        # 确认
        self.action.click(self.confirm_locator)
        # 开始时间
        self.action.click(self.start_time_locator)
        # 确认
        self.action.click(self.select_time_confirm_locator)
        # 结束时间
        self.action.click(self.end_time_locator)
        # 确认
        self.action.click(self.select_time_confirm_locator)
        # 上限
        self.action.send_keys(self.quantity_ceiling_locator, value=99999)
        # 下限
        self.action.send_keys(self.lower_number_locator, value=100)
        # 容忍
        self.action.click(self.tolerate_locator)

    def _assert_continue_ios(self):
        res = self.action.is_element_present(self.all_compulsory_items_locator)
        assert_that(res, equal_to(True), u"已添加所有义务项")
        sleep(2)
        self.action.click(self.all_compulsory_items_locator)

    def _continue_add_android(self):
        """
        android:继续添加
        :return:
        """
        self.action.click(self.continue_add_locator)
        res = self.action.is_element_present(self.continue_add_locator)
        assert_that(res, equal_to(True), u"已添加所有义务项")

    def _all_compulsory_android(self):
        """
        ios:点击已添加所有义务项
        :return:
        """
        self.action.click(self.all_compulsory_items_locator)

    def _complete_android(self):
        """
        ios:点击完成
        :return:
        """
        self.action.click(self.complete_locator)

    def close(self):
        """
        ios:关闭键盘
        :return:
        """
        self.action.click(self.close_locator)



