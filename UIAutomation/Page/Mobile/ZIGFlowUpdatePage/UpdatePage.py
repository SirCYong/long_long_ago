from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, time, run_info_log, page_element_factory
from UIAutomation.Utils import is_element_present

__author__ = "ytz"
__doc__ = "请求更新界面"


class UpDatePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.late_update_locator = None

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
        name_list = ['late_update']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.late_update_locator = ele_dic['late_update']  # 稍后更新
    pass

    # 更新界面

    def update_page(self):
        if is_element_present(self.driver,self.late_update_locator):
            self.action.click(self.late_update_locator)
        else:
            pass
    pass
