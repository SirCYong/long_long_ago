import time
from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, run_info_log, page_element_factory, get_elements

__author__ = "ytz"
__doc__ = "工作点设置"


class WorkStationSetting(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.choose_warehouse_locator = None
        self.choose_warehouse_confirmBtn_locator = None
        self.enter_station_name_locator = None
        self.choose_type_locator = None
        self.next_locator = None
        self.completed_look_locator = None
        self.nextAdd_locator = None

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
        name_list = ['choose_warehouse', 'choose_warehouse_confirmBtn', 'enter_station_name',
                     'choose_type', 'next', 'completed_look', 'nextAdd']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.choose_warehouse_locator = ele_dic['choose_warehouse']  # 选择需要操作的仓库
        self.choose_warehouse_confirmBtn_locator = ele_dic['choose_warehouse_confirmBtn']  # 选择仓库确认
        self.enter_station_name_locator = ele_dic['enter_station_name']  # 输入作业点名称
        self.choose_type_locator = ele_dic['choose_type']  # 请选择类型
        self.next_locator = ele_dic['next']  # 下一步
        self.completed_look_locator = ele_dic['completed_look']  # 完成并查看
        self.nextAdd_locator = ele_dic['nextAdd']  # 新增下一个

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
        self.action.click(self.choose_warehouse_locator)
        choose_depot = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
        choose_depot[0].click()
        #  确定
        self.action.click(self.choose_warehouse_confirmBtn_locator)
        # 选择需要变化的纬度：--物权
        wq = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
        if Latitude == '所有':
            for i in wq:
                for xh in i:
                    xh[0].click()
                    xh[1].click()
                    xh[2].click()
                    xh[3].click()
                    xh[4].click()
                    xh[5].click()
                i[0] = '物权'
                i[1] = '委托'
                i[2] = '位置'
                i[3] = '品质'
                i[4] = '数量'
                i[5] = '组合'
        elif Latitude == '物权':
            wq1 = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
            wq1[0].click(0)
        elif Latitude == '委托':
            wt = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
            wt[1].click()
        elif Latitude == '位置':
            wz = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
            wz[2].click()
        elif Latitude == '品质':
            pz = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
            pz[3].click()
        elif Latitude == '数量':
            sl = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
            sl[4].click()

        elif Latitude == '组合':
            zh = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
            zh[5].click()
        pass

    #  设置作业点类型第二页
    def _work_station_setting_page_two_android(self, ):
        self.action.set_value(self.enter_station_name_locator, '拣选')
        self.action.click(self.choose_type_locator)
        jx = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
        jx[0].click()
        self.action.click(self.choose_warehouse_confirmBtn_locator)
        self.action.click(self.completed_look_locator)
        pass




