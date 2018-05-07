import time
from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, run_info_log, page_element_factory, get_elements, is_element_present

__author__ = "ytz"
__doc__ = "分配代理人"


class DistributionAgent(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.select_supervisor_locator = None
        self.select_me_locator = None
        self.add_admin_locator = None
        self.add_admin_me_locator = None
        self.success_locator = None

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
        name_list = ['select_supervisor', 'select_me', 'add_admin',
                     'success']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.select_supervisor_locator = ele_dic['select_supervisor']  # 分配代理人页面 监控者请选择
        self.select_me_locator = ele_dic['select_me']  # 分配代理人页面 监控者分配给我
        self.add_admin_locator = ele_dic['add_admin']  # 分配代理人页面 管理者
        self.add_admin_me_locator = ele_dic['add_admin_me']  # 分配代理人页面 管理者分配给我
        self.success_locator = ele_dic['success']  # 分配代理人页面 分配完成

        # IOS独立的控件
        # if self.is_run_ios():
        #     name_list = []
        #     ele_dic = page_element_factory(self.xml_file, name_list)
        #
        # # Android独立的控件
        # if not self.is_run_ios():
        #     name_list = ['more_button']
        #     ele_dic = page_element_factory(self.xml_file, name_list)
        #     # 左上角更多按钮
        #     self._locator = ele_dic['']

    def is_loaded(self):
        pass

    def distribution_agent(self):
        if self.is_run_ios():
            self._distribution_agent_ios()
        else:
            self._distribution_agent_android()

    def _distribution_agent_ios(self):
        self.action.click(self.select_me_locator)
        self.action.click(self.add_admin_me_locator)
        if is_element_present(self.driver,self.success_locator):
            self.action.click(self.success_locator)
        else:
            print("无此按钮!")
        pass

        # ----------Android部分
    def _distribution_agent_android(self):
        self.action.click(self.select_me_locator)
        self.action.click(self.add_admin_me_locator)
        if is_element_present(self.driver, self.success_locator):
            self.action.click(self.success_locator)
        else:
            print("无此按钮!")
        pass
