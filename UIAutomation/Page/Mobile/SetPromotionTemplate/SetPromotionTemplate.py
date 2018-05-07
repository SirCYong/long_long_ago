
import time
from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, run_info_log, page_element_factory, is_element_present

__author__ = "ytz"
__doc__ = "设置促销模板"


class SetPromotionTemplatePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.template_name_locator = None
        self.supplier_unit_locator = None
        self.supplier_unit_one_locator = None
        self.needs_unit_locator = None
        self.needs_unit_one_locator = None
        self.service_type_locator = None
        self.promotions_service_locator = None
        self.promotions_warehousing_locator = None
        self.promotions_trans_locator = None
        self.promotions_availability_locator = None
        self.promotion_type_locator = None
        self.total_amount_locator = None
        self.total_amount_Discount_locator = None
        self.total_amount_minus_locator = None
        self.total_quantity_discount_locator = None
        self.single_product_delivery_locator = None
        self.packing_total_amount_locator = None
        self.trans_total_amount_locator = None
        self.throughput_total_amount_locator = None
        self.promotion_date_locator = None
        self.superposition_template_locator = None
        self.template_desc_locator = None
        self.promotion_type_locator = None
        self.full_money_locator = None
        self.minus_money_locator = None
        self.picking_hs_day_locator = None
        self.picking_hs_week_locator = None
        self.picking_hs_month_locator = None
        self.picking_hs_year_locator = None
        self.picking_satisfy_amount_locator = None
        self.picking_reward_locator = None
        self.trans_total_amount_locator = None
        self.confirm_locator = None
        self.completeBtn_locator = None
        self.next_stepBtn_locator = None
        self.set_promotion_template_locator = None
        self.s_completeBtn_locator = None
        self.turn_complete_locator = None
        if self.is_run_ios():
            self.xml_file = __file__[:__file__.rfind(".")] + "IOS.xml"
        else:
            self.xml_file = __file__[:__file__.rfind(".")] + "Android.xml"
        try:
            self.initial_element()
        except Exception:

            screenshot_file = GlobalVarClass.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVarClass.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVarClass.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'XML解析失败.', GlobalVarClass.get_log_file())
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except Exception():
            print(u'控件不在当前页面上.')
            screenshot_file = GlobalVarClass.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVarClass.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVarClass.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'控件不在当前页面上.', GlobalVarClass.get_log_file())
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
            name_list = ['template_name', 'supplier_unit', 'supplier_unit_one', 'needs_unit',
                         'needs_unit_one', 'service_type', 'promotions_service',
                         'promotions_warehousing', 'promotions_trans',
                         'promotions_availability',
                         'promotion_type', 'total_amount', 'total_amount_Discount',
                         'total_amount_minus',
                         'total_quantity_discount', 'single_product_delivery',
                         'packing_total_amount',
                         'throughput_total_amount', 'promotion_date',
                         'superposition_template',
                         'template_desc',
                         'promotion_type', 'full_money', 'minus_money',
                         'picking_hs_day', 'picking_hs_week', 'picking_hs_month',
                         'picking_hs_year',
                         'picking_satisfy_amount', 'picking_reward', 'trans_total_amount',
                         'confirm',
                         'completeBtn', 'next_stepBtn', 'completeBtn',
                         'set_promotion_template', 's_completeBtn', 'turn_complete']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.template_name_locator = ele_dic['template_name']
            self.supplier_unit_locator = ele_dic['supplier_unit']
            self.supplier_unit_one_locator = ele_dic['supplier_unit_one']
            self.needs_unit_locator = ele_dic['needs_unit']
            self.needs_unit_one_locator = ele_dic['needs_unit_one']
            self.service_type_locator = ele_dic['service_type']
            self.promotions_service_locator = ele_dic['promotions_service']
            self.promotions_warehousing_locator = ele_dic['promotions_warehousing']
            self.promotions_trans_locator = ele_dic['promotions_trans']
            self.promotions_availability_locator = ele_dic['promotions_availability']
            self.promotion_type_locator = ele_dic['promotion_type']
            self.total_amount_locator = ele_dic['total_amount']
            self.total_amount_Discount_locator = ele_dic['total_amount_Discount']
            self.total_amount_minus_locator = ele_dic['total_amount_minus']
            self.total_quantity_discount_locator = ele_dic['total_quantity_discount']
            self.single_product_delivery_locator = ele_dic['single_product_delivery']
            self.packing_total_amount_locator = ele_dic['packing_total_amount']
            self.trans_total_amount_locator = ele_dic['trans_total_amount']
            self.throughput_total_amount_locator = ele_dic['throughput_total_amount']
            self.promotion_date_locator = ele_dic['promotion_date']
            self.superposition_template_locator = ele_dic['superposition_template']
            self.template_desc_locator = ele_dic['template_desc']
            self.promotion_type_locator = ele_dic['promotion_type']
            self.full_money_locator = ele_dic['full_money']
            self.minus_money_locator = ele_dic['minus_money']
            self.picking_hs_day_locator = ele_dic['picking_hs_day']
            self.picking_hs_week_locator = ele_dic['picking_hs_week']
            self.picking_hs_month_locator = ele_dic['picking_hs_month']
            self.picking_hs_year_locator = ele_dic['picking_hs_year']
            self.picking_satisfy_amount_locator = ele_dic['picking_satisfy_amount']
            self.picking_reward_locator = ele_dic['picking_reward']
            self.trans_total_amount_locator = ele_dic['trans_total_amount']
            self.confirm_locator = ele_dic['confirm']
            self.completeBtn_locator = ele_dic['completeBtn']
            self.next_stepBtn_locator = ele_dic['next_stepBtn']
            self.set_promotion_template_locator = ele_dic['set_promotion_template']
            self.s_completeBtn_locator = ele_dic['s_completeBtn']
            self.turn_complete_locator = ele_dic['turn_complete']
        # Android独立的控件
        if not self.is_run_ios():
            name_list = ['more_button']
            ele_dic = page_element_factory(self.xml_file, name_list)
            # 左上角更多按钮
            self._locator = ele_dic['']

    def is_loaded(self):
        pass

    def Set_PromotionTemplate_SupplierAndNeeds_ios(self):
        self.action.set_value(self.template_name_locator, '测试模板一')
        # 点击供方
        self.action.click(self.supplier_unit_locator)
        # 选择供方其中一个
        self.action.click(self.supplier_unit_one_locator)
        # 点击确认
        self.action.click(self.confirm_locator)
        # 点击需方
        self.action.click(self.needs_unit_locator)
        # 选择需方中的一个
        self.action.click(self.needs_unit_one_locator)
        # 点击确认
        self.action.click(self.confirm_locator)

        # 选择服务类型
    def ChooseServiceType(self, Type):
        self.action.click(self.service_type_locator)
        if Type == '促销劳务服务':
            self.action.click(self.promotions_service_locator)
            self.action.click(self.confirm_locator)
        elif Type == '促销仓储服务':
            self.action.click(self.promotions_warehousing_locator)
            self.action.click(self.confirm_locator)
        elif Type == '促销运输服务':
            self.action.click(self.promotions_trans_locator)
            self.action.click(self.confirm_locator)
        elif Type == '促销供货服务':
            self.action.click(self.promotions_availability_locator)
            self.action.click(self.confirm_locator)
        pass

    # 选择促销类型
    def SetPromotionTemplate_Promotion_type_ios(self, PromotionType):
        self.action.click(self.promotion_type_locator)
        if PromotionType == '满总金额减总金额':
            self.action.click(self.total_amount_locator)
            self.action.click(self.confirm_locator)
        elif PromotionType == '满总金额总价折扣':
            self.action.click(self.total_amount_Discount_locator)
            self.action.click(self.confirm_locator)
        elif PromotionType == '满总数量减总金额':
            self.action.click(self.total_amount_minus_locator)
            self.action.click(self.confirm_locator)
        elif PromotionType == '满总数量总价折扣':
            self.action.click(self.total_quantity_discount_locator)
            self.action.click(self.confirm_locator)
        elif PromotionType == '单品满送单排数量':
            self.action.click(self.single_product_delivery_locator)
            self.action.click(self.confirm_locator)
        elif PromotionType == '拣选满数量总价折扣':
            self.action.click(self.packing_total_amount_locator)
            self.action.click(self.confirm_locator)
        elif PromotionType == '运输满数量总价折扣':
            self.action.click(self.trans_total_amount_locator)
            self.action.click(self.confirm_locator)
        elif PromotionType == '吞吐量满数量总价折扣':
            self.action.click(self.throughput_total_amount_locator)
            self.action.click(self.confirm_locator)
        pass

    def SetPromotionTemplate_PromotionTime_ios(self):
        # 设置促销时间
        self.action.click(self.promotion_date_locator)
        # 确定按钮
        self.action.click(self.confirm_locator)
        # 点击叠加模板
        self.action.click(self.superposition_template_locator)
        # 输入模板说明
        self.action.set_value(self.template_desc_locator, '这是一个临时的测试模板')
        # 点击小键盘的完成
        self.action.click(self.s_completeBtn_locator)
        # 下一步
        if is_element_present(self.driver,self.next_stepBtn_locator):
            self.action.click(self.next_stepBtn_locator)
        else:
            print("Fuck shit!!")

    def SetPromotionTemplate_TotalAmount_ios(self):
        # 通用满减金额类型模板 包括满足金额和减免金额
        self.action.set_value(self.full_money_locator, '150000')
        self.action.set_value(self.minus_money_locator, '300')
        self.action.click(self.turn_complete_locator)  # 小键盘的完成按钮
        if is_element_present(self.driver, self.completeBtn_locator):
            self.action.click(self.completeBtn_locator)  # 最后完成按钮
        pass

    def SetPromotionTemplate_CompleteBtn_ios(self):
        self.action.click(self.completeBtn_locator)
        pass

    def SetPromotionTemplate_WareHouseType_ios(self):
        # 核算周期：天
        self.action.click(self.picking_hs_day_locator)
        # 满足数量
        self.action.click(self.picking_satisfy_amount_locator)
        # 奖励幅度
        self.action.click(self.picking_reward_locator)
        # 完成

        pass

    # 获取设置促销模板长期卡片
    def click_set_promotion_Template_card_ios(self):
        if self.is_long_card_present_by_swipe(self.set_promotion_template_locator, 5):
                self.action.click(self.set_promotion_template_locator)
        else:
            print("未找到长期卡片!")
        pass




