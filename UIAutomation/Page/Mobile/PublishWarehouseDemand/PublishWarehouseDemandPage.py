import time
from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, run_info_log, page_element_factory, is_element_present, \
    get_elements, ParseXmlErrorException

__author__ = "Yuetianzhuang"
__doc__ = "发布仓储需求"


class PublishWarehouseDemandPage(BasePage):
    # 变量初始化
    def __init__(self, driver):
        self.ds_locator = None
        self.zy_locator = None
        self.fds_locator = None
        self.kj_locator = None
        self.dz_locator = None
        self.sc_locator = None
        self.qs_locator = None
        self.pl_locator = None
        self.chooseTime_locator = None
        self.confirmTimeBtn_locator = None
        self.chooseAddress_locator = None
        self.beijing_locator = None
        self.beijing_city_locator = None
        self.east_city_zone_locator = None
        self.processing_capacity_locator = None
        self.warehouse_locator = None
        self.immediate_release_locator = None
        self.completed_btn_locator = None
        self.continue_locator = None
        self.wc_btn_locator = None
        self.bd_btn_locator = None
        self.pub_warehouseDemand_locator = None

        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        if self.is_run_ios():
            self.xml_file = __file__[:__file__.rfind(".")] + "IOS.xml"
        else:
            self.xml_file = __file__[:__file__.rfind(".")] + "Android.xml"

        try:
            self.initial_element()
        except ParseXmlErrorException:
            print(u'XML解析失败.')
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
        name_list = ['ds_btn', 'transport_btn', 'fds_btn',
                     'kj_btn', 'dz_btn', 'sc_btn',
                     'qs_btn', 'pl_btn',
                     'choose_start_time_btn', 'confirm_time_btn', 'choose_address',
                     'processing_capacity_btn', 'warehouse_area_btn', 'immediate_release']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.ds_locator = ele_dic['ds_btn']  # 电商
        self.zy_locator = ele_dic['transport_btn']
        self.fds_locator = ele_dic['fds_btn']  # 非电商
        self.kj_locator = ele_dic['kj_btn']  # 跨境
        self.dz_locator = ele_dic['dz_btn']  # 大众
        self.sc_locator = ele_dic['sc_btn']  # 奢侈
        self.qs_locator = ele_dic['qs_btn']  # 轻奢
        self.pl_locator = ele_dic['pl_btn']  # 跑量
        self.chooseTime_locator = ele_dic['choose_start_time_btn']  # 选择 起始日期
        self.confirmTimeBtn_locator = ele_dic['confirm_time_btn']  # 确认时间
        self.chooseAddress_locator = ele_dic['choose_address']  # 选择地点
        self.processing_capacity_locator = ele_dic['processing_capacity_btn']  # 处理量
        self.warehouse_locator = ele_dic['warehouse_area_btn']  # 仓储面积
        self.immediate_release_locator = ele_dic['immediate_release']  # 立即发布
        # IOS独立的控件
        if self.is_run_ios():
            name_list = ['beijing','beijing_city', 'east_city_zone',
                         'completed_btn', 'immediate_release',
                         'continue_btn', 'wc_btn', 'bd_btn', 'pub_warehouseDemand']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.beijing_locator = ele_dic['beijing']  # 北京
            self.beijing_city_locator = ele_dic['beijing_city']  # 北京市
            self.east_city_zone_locator = ele_dic['east_city_zone']  # 东城区
            self.completed_btn_locator = ele_dic['completed_btn']  # 完成
            self.continue_locator = ele_dic['continue_btn']  # 继续发布
            self.wc_btn_locator = ele_dic['wc_btn']
            self.bd_btn_locator = ele_dic['bd_btn']  # 绑定
            self.pub_warehouseDemand_locator = ele_dic['pub_warehouseDemand']  # 发布仓储需求
        # Android独立的控件
        # if not self.is_run_ios():
        #     name_list = []
        #     ele_dic = page_element_factory(self.xml_file, name_list)
        #     # 左上角更多按钮
        pass

    def click_business(self, TradeType):
        # 通用模块
        if TradeType == '电商':
            self.action.click(self.ds_locator)
        elif TradeType == '转运':
            self.action.click(self.zy_locator)
        elif TradeType == '非电商':
            self.action.click(self.fds_locator)
        elif TradeType == '跨境':
            self.action.click(self.kj_locator)
        else:
            self.action.click(self.ds_locator)
        pass

    def click_level(self, LevelType):
        # 通用模块
        if LevelType == '大众':
            self.action.click(self.dz_locator)
        elif LevelType == '奢侈':
            self.action.click(self.sc_locator)
        elif LevelType == '轻奢':
            self.action.click(self.qs_locator)
        elif LevelType == '跑量':
            self.action.click(self.pl_locator)
        else:
            self.action.click(self.dz_locator)
    pass

    def click_cross_border_button_android(self):
        # 选择日期
        '''
        安卓端
        :return:
        '''
        self.action.click(self.chooseTime_locator)  # 点击日期
        self.action.click(self.confirmTimeBtn_locator)  # 确定日期
        self.action.click(self.chooseAddress_locator)  # 选择地点
        LinearLayout = get_elements(self.driver, ("CLASS_NAME", "android.widget.FrameLayout"))
        # 北京 北京市、宣武区
        LinearLayout[1].click()
        LinearLayoutCity = get_elements(self.driver, ("CLASS_NAME", "android.widget.FrameLayout"))
        LinearLayoutCity[0].click()
        LinearLayoutLocation = get_elements(self.driver, ("CLASS_NAME", "android.widget.RelativeLayout"))
        LinearLayoutLocation[3].click()


        pass

    def click_processing_capacity_button_android(self):
        # 填写处理量和仓储面积
        self.action.click(self.processing_capacity_locator)
        self.action.click(self.warehouse_locator)
        self.driver.hide_keyboard()  # 影藏键盘
        pass

    def click_pub_warehouse_demand_card_ios(self):
        # IOS端获取
        if self.is_long_card_present_by_swipe(self.pub_warehouseDemand_locator, 5):
            self.action.click(self.pub_warehouseDemand_locator)
        pass

    def click_cross_border_button_ios(self):
        # 选择日期
        self.action.click(self.chooseTime_locator)
        # 选择日期中的确认按钮
        self.action.click(self.confirmTimeBtn_locator)
        # 选择地点
        self.action.click(self.chooseAddress_locator)
        # 选择详细地址
        self.action.click(self.beijing_locator)
        # 北京市
        self.action.click(self.beijing_city_locator)
        # 东城区
        self.action.click(self.east_city_zone_locator)
        pass

    def click_processing_capacity_button_ios(self):
        self.action.set_value(self.processing_capacity_locator, '18000')
        # 填写仓储面积
        self.action.set_value(self.warehouse_locator, '300')
        #  小键盘的完成按钮
        self.action.click(self.wc_btn_locator)
        pass

    def click_complete(self):
        if is_element_present(self.driver, self.immediate_release_locator):
            self.action.click(self.immediate_release_locator)
        pass

