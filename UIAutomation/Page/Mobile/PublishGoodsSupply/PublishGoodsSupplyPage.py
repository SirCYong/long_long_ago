from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVar, time, run_info_log, page_element_factory, get_elements, is_element_present

__author__ = "Yuetianzhuang"
__doc__ = "发布供货供应"


class PublishGoodsSupplyPage(BasePage):

    def __init__(self, driver):
        self.inner_locator = None
        self.outside_locator = None
        self.back_locator = None
        self.complete_btn_locator = None

        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        if self.is_run_ios():
            self.xml_file = __file__[:__file__.rfind(".")] + "IOS.xml"
        else:
            self.xml_file = __file__[:__file__.rfind(".")] + "Android.xml"

        try:
            self.initial_element()
        except Exception:
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
        except Exception:
            print(u'控件不在当前页面上.')
            screenshot_file = GlobalVar.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVar.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVar.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'控件不在当前页面上.', GlobalVar.get_log_file())
            raise
        pass

    def is_loaded(self):
        pass

    def page_factory(self):
        # iOS and Android端统一的控件
        name_list = ['back', 'complete_btn', 'inner', 'outside']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.inner_locator = ele_dic['inner']  # 内部
        self.outside_locator = ele_dic['outside']  # 外部
        self.back_locator = ele_dic['back']  # 返回
        self.complete_btn_locator = ele_dic['complete_btn']  # 发布
    pass

    def publish_goods_supply_android(self):
        self.action.click(self.inner_locator)  # 点击内部
        InnerUnit = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))  # 内部业务单位
        InnerUnit[1].click()
        self.action.click(self.back_locator)  # 返回
        self.action.click(self.outside_locator)  # 点击外部
        OutSideUnit = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))  # 外部业务单位
        OutSideUnit[3].click()
        self.action.click(self.back_locator)  # 返回
        if is_element_present(self.driver, self.complete_btn_locator):
            self.action.click(self.complete_btn_locator)  # 发布
        else:
            print("未找到该元素！")

        pass






