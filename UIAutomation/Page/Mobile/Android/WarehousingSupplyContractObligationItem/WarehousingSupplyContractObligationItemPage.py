from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ ='chenyanxiu'


class WarehousingSupplyContractObligationItemPage(BasePage):
    """
    仓储供应契约义务项
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.supplier_locator = None
        self.contract_number_locator = None
        self.add_obligations_locator = None
        self.type_locator = None
        self.type_consignment_locator = None
        self.type_service_star_locator = None
        self.confirm_locator = None
        self.startdate_locator = None
        self.rl_enddate_locator = None
        self.lower_limit_locator = None
        self.most_limit_locator = None
        self.btn_tolerate_locator = None
        self.btn_cancel_locator = None
        self.add_next_locator = None
        self.btn_finish_locator = None
        self.btn_complete_locator = None
        self.btn_next_locator = None
        try:
            self.is_loaded()
        except ParseXmlErrorException:
            assert False
        pass

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
        pass

    def page_factory(self):
        name_list = ['supplier', 'contract_number', 'add_obligations', 'type', 'type_consignment', 'type_service_star'
                     , 'confirm', 'startdate', 'rl_enddate', 'lower_limit', 'most_limit', 'btn_tolerate', 'btn_cancel',
                     'add_next',
                     'btn_finish', 'la_line_num', 'all_ele']
        ele_dic = page_element_factory(__file__, name_list)
        self.supplier_locator = ele_dic['supplier']  # 供方id
        self.contract_number_locator = ele_dic['contract_number']  # 契约ukid
        self.add_obligations_locator = ele_dic['add_obligations']  # 添加义务项
        self.type_locator = ele_dic['type']  # 类型
        self.type_consignment_locator = ele_dic['type_consignment']  # 发货单量义务项
        self.type_service_star_locator = ele_dic['type_service_star']  # 服务星级义务项
        self.confirm_locator = ele_dic['confirm']  # 确定
        self.startdate_locator = ele_dic['startdate']  # 开始时间
        self.rl_enddate_locator = ele_dic['rl_enddate']  # 结束时间
        self.lower_limit_locator = ele_dic['lower_limit']  # 下限
        self.most_limit_locator = ele_dic['most_limit']  # 上限
        self.btn_tolerate_locator = ele_dic['btn_tolerate']  # 容忍
        self.btn_cancel_locator = ele_dic['btn_cancel']  # 取消
        self.add_next_locator = ele_dic['add_next']  # 继续添加
        self.btn_finish_locator = ele_dic['btn_finish']  # 完成
        self.btn_complete_locator = ele_dic['btn_complete']  # 时间确定
        self.btn_next_locator = ele_dic['btn_next']  # 无需添加义务项
        pass

    def is_loaded(self):
        pass
