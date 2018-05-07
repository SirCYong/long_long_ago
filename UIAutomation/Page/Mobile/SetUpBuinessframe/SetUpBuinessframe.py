import time
from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, run_info_log, page_element_factory, get_elements

__author__ = "ytz"
__doc__ = "建立业务框架"


class WorkStationSetting(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

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
        name_list = ['', '', '',
                     '', '', '', '']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self._locator = ele_dic['']  #
        self._locator = ele_dic['']  #
        self._locator = ele_dic['']  #
        self._locator = ele_dic['']  #
        self._locator = ele_dic['']  #
        self._locator = ele_dic['']  #
        self._locator = ele_dic['']  #

        # IOS独立的控件
        if self.is_run_ios():
            name_list = []
            ele_dic = page_element_factory(self.xml_file, name_list)

        # Android独立的控件
        if not self.is_run_ios():
            name_list = ['more_button']
            ele_dic = page_element_factory(self.xml_file, name_list)
            # 左上角更多按钮
            self._locator = ele_dic['']

    def is_loaded(self):
        pass

    def Work_Station_Settion(self):
        if self.is_run_ios():
            self._work_station_setting_page_one_ios()
        else:
            self._work_station_setting_page_one_android()

    def _work_station_setting_page_one_ios(self):

        pass

        # 工作点设置第一页 ----------Android部分

    def _work_station_setting_page_one_android(self, Latitude):
        self.action.click()
        choose_depot = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
        choose_depot[0].click()
        #  确定
        self.action.click()
        # 选择需要变化的纬度：--物权
        pass

