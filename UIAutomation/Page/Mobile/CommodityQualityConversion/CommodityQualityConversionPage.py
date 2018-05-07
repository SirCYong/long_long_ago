from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVar, time, run_info_log, page_element_factory, get_elements, is_element_present

__author__ = "Yuetianzhuang"
__doc__ = "商品品质转换"


class CommodityQualityConversionPage(BasePage):

    def __init__(self, driver):
        self.chooseBtn_locator = None
        self.confirm_locator = None
        self.back_locator = None

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
        name_list = ['chooseBtn', 'confirm', 'back']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.chooseBtn_locator = ele_dic['chooseBtn']  # 选择滑动开关部
        self.confirm_locator = ele_dic['confirm']  # 确认
        self.back_locator = ele_dic['back']  # 返回
    pass

    def commodity_quality_conversion(self):
        self.action.click(self.chooseBtn_locator)
        self.action.click(self.confirm_locator)
        pass





