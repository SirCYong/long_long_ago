from UIAutomation.Page import BasePage
from UIAutomation.Page.SwipeModel import SwipeModel
from UIAutomation.Utils import GlobalVarClass, time, run_info_log, page_element_factory, is_element_present

__author__ = "ytz"
__doc__ = "上传送货单"


class UpDeliveryOrderPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.supplier_locator = None
        self.needs_locator = None
        self.needs_unit_locator = None
        self.invoice_number_locator = None
        self.destination_locator = None
        self.ship_date_locator = None
        self.upload_file_locator = None
        self.confirm_locator = None
        self.upDelivery_order_locator = None
        self.completeBtn_locator = None
        self.confirm_time_locator = None

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

    def is_loaded(self):
        pass

    def page_factory(self):
        # iOS and Android端统一的控件
        name_list = ['supplier',
                     'needs',
                     'invoice_number',
                     'destination',
                     'ship_date',
                     'confirm',
                     'upload_file']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.supplier_locator = ele_dic['supplier']  # 供方
        self.needs_locator = ele_dic['needs']  # 需方
        self.invoice_number_locator = ele_dic['invoice_number']  # 发货单号
        self.destination_locator = ele_dic['destination']  # 到货仓库
        self.ship_date_locator = ele_dic['ship_date']  # 到货日期确认
        self.confirm_locator = ele_dic['confirm']  # 确定
        self.upload_file_locator = ele_dic['upload_file']  # PC端导入

        # IOS独立的控件
        if self.is_run_ios():
            name_list = ['needs_unit',
                         'upDelivery_order',
                         'completeBtn']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.needs_unit_locator = ele_dic['needs_unit']  # 需方单位
            self.upDelivery_order_locator = ele_dic['upDelivery_order']  # 上传送货单卡片
            self.completeBtn_locator = ele_dic['completeBtn']  # 小键盘完成按钮

        # Android独立的控件
        if not self.is_run_ios():
            name_list = ['confirm_time']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.confirm_time_locator = ele_dic['confirm_time']
    pass

    def click_up_delivery_order_ios(self):
        # 点击供方
        self.action.click(self.supplier_locator)
        # 滑动需方单位
        SwipeModel(self.driver).swipe_down(t=1000)
        # 选择确定
        self.action.click(self.confirm_locator)
        # 点击需方
        self.action.click(self.needs_locator)
        # 滑动需方单位
        # 选择确定
        self.action.click(self.confirm_locator)
        # 输入发货单号
        self.action.set_value(self.invoice_number_locator, 'TX100008911')
        # 小键盘完成按钮
        self.action.click(self.completeBtn_locator)
        # 到货地址
        self.action.set_value(self.destination_locator, '江干区新加坡科技园2号楼23楼')
        # 小键盘完成按钮
        self.action.click(self.completeBtn_locator)
        # 点击发货日期
        self.action.click(self.ship_date_locator)
        # 发货日期确认
        self.action.click(self.confirm_locator)
        # 点击去PC端导入
        if is_element_present(self.driver, self.upload_file_locator):
            self.action.click(self.upload_file_locator)
        else:
            print("录入信息不完整")

    def click_up_delivery_order_card_ios(self):
        if self.is_long_card_present_by_swipe(self.upDelivery_order_locator, 5):
                self.action.click(self.upDelivery_order_locator)
        else:
            print("未找到长期卡片!")
        pass

    def click_up_delivery_order_android(self):
        # 点击供方
        self.action.click(self.supplier_locator)
        # 选择确定
        self.action.click(self.confirm_locator)
        # 点击需方
        self.action.click(self.needs_locator)
        # 滑动需方单位
        SwipeModel(self.driver).swipe_down(t=1000)

        self.action.click(self.confirm_locator)
        # 输入发货单号
        self.action.send_keys(self.invoice_number_locator, 'TX100008911')
        # 到货地址
        self.action.send_keys(self.destination_locator, '江干区新加坡科技园2号楼23楼')
        # 点击发货日期
        self.action.click(self.ship_date_locator)
        # 发货日期确认
        self.action.click(self.confirm_time_locator)
        # 点击去PC端导入
        if is_element_present(self.driver, self.upload_file_locator):
            self.action.click(self.upload_file_locator)
        else:
            print("录入信息不完整")



