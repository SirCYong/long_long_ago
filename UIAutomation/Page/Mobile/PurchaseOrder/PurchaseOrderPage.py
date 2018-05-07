import time
from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, run_info_log, page_element_factory, is_element_present

__author__ = "Yuetianzhuang"
__doc__ = "选购下单"


class PurchaseOrderPage(BasePage):
    def is_loaded(self):
        pass

    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.purchase_order_locator = None
        self.supplier_locator = None
        self.needs_locator = None
        self.purchase_goods_locator = None
        self.choose_goods_locator = None
        self.add_goodsBtn_locator = None
        self.confirm_goods_locator = None
        self.address_locator = None
        self.detail_address_locator = None
        self.confirm_address_locator = None
        self.order_locator = None
        self.purchase_order_confirm_locator = None
        self.purchase_order_complete_locator = None

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
        name_list = ['purchase_order', '', '', '']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self._locator = ele_dic['']
        self._locator = ele_dic['']
        self._locator = ele_dic['']
        self._locator = ele_dic['']
        # IOS独立的控件
        if self.is_run_ios():
            name_list = ['purchase_order',
                         'supplier',
                         'needs',
                         'purchase_goods',
                         'choose_goods',
                         'add_goodsBtn',
                         'confirm_goods',
                         'address',
                         'detail_address',
                         'confirm_address',
                         'order',
                         'purchase_order_confirm',
                         'purchase_order_complete']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.purchase_order_locator = ele_dic['purchase_order']  # 选购下单
            self.supplier_locator = ele_dic['supplier']  # 选择供方
            self.needs_locator = ele_dic['needs']  # 选择需方
            self.purchase_goods_locator = ele_dic['purchase_goods']  # 选购商品
            self.choose_goods_locator = ele_dic['choose_goods']  # 选择商品
            self.add_goodsBtn_locator = ele_dic['add_goodsBtn']  # 添加按钮
            self.confirm_goods_locator = ele_dic['confirm_goods']  # 确认商品
            self.address_locator = ele_dic['address']  # 添加收货地址
            self.detail_address_locator = ele_dic['detail_address']  # 详细地址
            self.confirm_address_locator = ele_dic['confirm_address']  # 确认选择该地址
            self.order_locator = ele_dic['order']  # 立即下单
            self.purchase_order_confirm_locator = ele_dic['purchase_order_confirm']  # 确定
            self.purchase_order_complete_locator = ele_dic['purchase_order_complete']  # 完成

        # Android独立的控件
        if not self.is_run_ios():
            name_list = ['confirm_supply_needs']
            ele_dic = page_element_factory(self.xml_file, name_list)
            # 左上角更多按钮
            self.confirm_supply_needs_locator = ele_dic['confirm_supply_needs']
            self._locator = ele_dic['']
            self._locator = ele_dic['']
        pass

    def click_purchase_order_ios(self):
        self.action.click(self.supplier_locator)  # 选择供方
        self.action.click(self.purchase_order_confirm_locator)  # 确定
        self.action.click(self.needs_locator)  # 选择需方
        self.action.click(self.purchase_order_confirm_locator)  # 确定
        self.action.click(self.purchase_goods_locator)  # 选购商品
        self.action.click(self.choose_goods_locator)  # 选择商品
        self.action.click(self.add_goodsBtn_locator)  # 添加按钮
        self.action.click(self.confirm_goods_locator)  # 确认商品
        self.action.click(self.address_locator)  # 添加收货地址
        self.action.send_keys(self.detail_address_locator, '天安南路东路华公社区8栋108号')  # 详细地址
        self.action.click(self.purchase_order_complete_locator)  # 完成
        self.action.click(self.confirm_address_locator)   # 确认选择该地址
        self.action.click(self.order_locator)  # 立即下单
        pass

    # 寻找长期卡片 选购下单
    def click_purchase_order_card_ios(self):
        if self.is_long_card_present_by_swipe(self.purchase_order_locator, 5):
            self.action.click(self.purchase_order_locator)
        else:
            print("未找到该元素")
        pass

    def click_other(self):
        pass



# android.widget.ImageView

# 请输入详细地址
# android.widget.RelativeLayout


