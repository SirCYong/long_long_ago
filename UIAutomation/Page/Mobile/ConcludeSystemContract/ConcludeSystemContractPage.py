import time
from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, run_info_log, page_element_factory, get_elements, is_element_present

__author__ = "ytz"
__doc__ = "签订系统契约"


class ConcludeSystemContract(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.conclude_contract_locator = None

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
        name_list = ['conclude_contract']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.conclude_contract_locator = ele_dic['conclude_contract']  # 签订契约服务页面 同意

        # # IOS独立的控件
        # if self.is_run_ios():
        #     name_list = []
        #     ele_dic = page_element_factory(self.xml_file, name_list)
        # Android独立的控件
        # if not self.is_run_ios():
        #     name_list = ['more_button']
        #     ele_dic = page_element_factory(self.xml_file, name_list)
        #     # 左上角更多按钮
        #     self._locator = ele_dic['']

    def is_loaded(self):
        pass

    def conclude_system_contract(self):
        if self.is_run_ios():
            self._conclude_system_contract_ios()
        else:
            self._conclude_system_contract_android()

        # 签订契约服务页面 同意IOS
    def _conclude_system_contract_ios(self):
        if is_element_present(self.driver,self.conclude_contract_locator):
            self.action.click(self.conclude_contract_locator)
        else:
            print("未找到Button")
        pass

        # 签订契约服务页面 同意ANDROID
    def _conclude_system_contract_android(self):
        if is_element_present(self.driver,self.conclude_contract_locator):
            self.action.click(self.conclude_contract_locator)
        else:
            print("未找到Button")
        pass
