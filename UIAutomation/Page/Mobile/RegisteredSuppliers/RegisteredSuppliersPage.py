import time
from UIAutomation.Page import BasePage
from UIAutomation.Utils import GlobalVarClass, run_info_log, page_element_factory, is_element_present, get_elements
__author__ = "Yuetianzhuang"
__doc__ = "注册供应商"


class RegisterSuppliersPage(BasePage):
    def is_loaded(self):
        pass

    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.company_name_locator = None
        self.company_principal_locator = None
        self.mobile_locator = None
        self.single_personName_locator = None
        self.single_person_mobile_locator = None
        self.reconciliation_person_locator = None
        self.reconciliation_personName_locator = None
        self.reconciliation_personMobile_locator = None
        self.pay_locator = None
        self.pay_personName_locator = None
        self.pay_personMobile_locator = None
        self.registerBtn_locator = None
        self.register_supply_locator = None
        self.completed_btn_locator = None
        self.check_people_locator = None
        self.pay_people_locator = None

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
        name_list = ['company_name', 'company_principal', 'mobile',
                     'single_personName', 'single_person_mobile', 'reconciliation_personName',
                     'reconciliation_personMobile',
                     'pay', 'pay_personName', 'pay_personMobile',
                     'registerBtn', 'register_supply', 'completed_btn']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.company_name_locator = ele_dic['company_name']  # 企业简称
        self.company_principal_locator = ele_dic['company_principal']  # 企业负责人
        self.mobile_locator = ele_dic['mobile']  # 手机
        self.single_personName_locator = ele_dic['single_personName']  # 接单人姓名
        self.single_person_mobile_locator = ele_dic['single_person_mobile']  # 接单人联系方式
        self.reconciliation_personName_locator = ele_dic['reconciliation_personName']  # 对账人姓名
        self.reconciliation_personMobile_locator = ele_dic['reconciliation_personMobile']  # 对账人联系方式
        self.pay_personName_locator = ele_dic['pay_personName']  # 付款人姓名
        self.pay_personMobile_locator = ele_dic['pay_personMobile']  # 付款人联系方式
        self.registerBtn_locator = ele_dic['registerBtn']  # 注册按钮
        # IOS独立的控件
        if self.is_run_ios():
            name_list = ['reconciliation_person',
                         'pay', 'register_supply', 'completed_btn']
            ele_dic = page_element_factory(self.xml_file, name_list)
            self.reconciliation_person_locator = ele_dic['reconciliation_person']  # 对账人
            self.pay_locator = ele_dic['pay']  # 付款人
            self.register_supply_locator = ele_dic['register_supply']  # 注册供应商卡片
            self.completed_btn_locator = ele_dic['completed_btn']  # 小键盘完成按钮
        # Android 独立的控件
        if not self.is_run_ios():
            name_list = ['check_people', 'pay_people']
            ele_dic = page_element_factory(self.xml_file,name_list)
            self.check_people_locator = ele_dic['check_people']  # 对账人
            self.pay_people_locator = ele_dic['pay_people']  # 对账人

        pass

    # 注册供应商，必填项
    def input_required(self):
        # 输入企业简称
        self.action.set_value(self.company_name_locator, '思科系统')
        self.action.set_value(self.company_principal_locator, 'michael')
        self.action.set_value(self.mobile_locator, '15268509694')
        self.driver.hide_keyboard()  # 影藏数字键盘
        pass

    # 注册供应商，必填项
    def input_required_android(self):
        # 输入企业简称
        self.action.send_keys(self.company_name_locator, '思科系统')
        self.action.send_keys(self.company_principal_locator, 'michael')
        self.action.send_keys(self.mobile_locator, '15268509694')
        self.driver.hide_keyboard()  # 影藏数字键盘
        pass

    # 选填项-接单人
    def single_person(self):
        self.action.set_value(self.single_personName_locator, '路易斯')
        self.action.set_value(self.single_person_mobile_locator, '13387131396')
        pass

    # 选填项-接单人
    def single_person_android(self):
        self.action.send_keys(self.single_personName_locator, '路易斯')
        self.action.send_keys(self.single_person_mobile_locator, '13387131396')
        pass

    # 选填项-对账人_ios
    def reconciliation_ios(self):
        self.action.click(self.reconciliation_person_locator)
        self.action.set_value(self.reconciliation_personName_locator, '艾伦')
        self.action.set_value(self.reconciliation_personMobile_locator, '18772959096')
        pass

    # 选填项-对账人_android
    def reconciliation_android(self):
        self.action.click(self.check_people_locator)
        self.action.send_keys(self.reconciliation_personName_locator, '艾伦')
        self.action.send_keys(self.reconciliation_personMobile_locator, '18772959096')
        self.driver.hide_keyboard()  # 影藏小键盘
        pass

    # 选填项-付款人_ios
    def pay_person_ios(self):
        self.action.click(self.pay_locator)
        self.action.set_value(self.pay_personName_locator, '雷克斯')
        self.action.set_value(self.pay_personMobile_locator, '15268199910')
        self.action.click(self.completed_btn_locator)
        pass

    # 选填项-付款人_android
    def pay_person_android(self):
        self.action.click(self.pay_people_locator)
        self.action.send_keys(self.pay_personName_locator, '雷克斯')
        self.action.send_keys(self.pay_personMobile_locator, '15268199910')
        self.driver.hide_keyboard()  # 影藏数字键盘
        pass

    # 注册
    def register(self):
        if is_element_present(self.driver, self.registerBtn_locator):
            self.action.click(self.registerBtn_locator)
        pass

    # 寻找长期卡片
    def click_register_supply_card_ios(self):
        if self.is_long_card_present_by_swipe(self.register_supply_locator, 5):
            self.action.click(self.register_supply_locator)
        else:
            assert False
        pass
