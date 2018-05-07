from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page.BasePage import BasePage

from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, initial_element_error_wrapper

__author__ = "zzh"
__desc__ = "激活仓库page"


class PageActivateWarehouse(BasePage):
    """
    激活仓库Page
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.is_loaded()
            self.initial_element()
        except ParseXmlErrorException:
            initial_element_error_wrapper(self.driver)
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        name_list = ["input_warehouse_name",
                     "button_warehouse_address",
                     "button_warehouse_map_first",
                     "input_warehouse_detail_address",
                     "input_warehouse_area",
                     "input_warehouse_rent",
                     "input_warehouse_contact",
                     "input_warehouse_phone",
                     "button_activate",
                     "button_ok"]

        ele_dic = page_element_factory(self.standard_xml_file, name_list)
        # 仓库名称
        self.input_warehouse_name = ele_dic["input_warehouse_name"]
        # 所在地址：请选择地区
        self.button_warehouse_address = ele_dic["button_warehouse_address"]
        # 请选择地区打开的页面：第一个地址定位控件
        self.button_warehouse_map_first = ele_dic["button_warehouse_map_first"]
        # 详细地址
        self.input_warehouse_detail_address = ele_dic["input_warehouse_detail_address"]
        # 仓库面积
        self.input_warehouse_area = ele_dic["input_warehouse_area"]
        # 仓库租金
        self.input_warehouse_rent = ele_dic["input_warehouse_rent"]
        # 仓库联系人
        self.input_warehouse_contact = ele_dic["input_warehouse_contact"]
        # 仓库联系人手机号码
        self.input_warehouse_phone = ele_dic["input_warehouse_phone"]
        # 激活按钮
        self.button_activate = ele_dic["button_activate"]
        # 激活成功页面：好的按钮
        self.button_ok = ele_dic["button_ok"]

    def is_loaded(self):
        pass

    def fill_warehouse_form(self, form_data):
        if self.is_run_ios():
            self._fill_warehouse_form_ios(form_data)
        else:
            self._fill_warehouse_form_android(form_data)
        pass

    def _fill_warehouse_form_ios(self, form_data):
        # 输入仓库名称
        self.action.send_keys(self.input_warehouse_name, form_data["warehouse_name"])
        # 点击所在地址
        self.action.click(self.button_warehouse_address)
        # 选择一个地址
        self.action.click(self.button_warehouse_map_first)
        # # 输入详细地址
        # self.action.send_keys(self.input_warehouse_detail_address, form_data["warehouse_detail_address"])
        # 点击仓库面积控件，在输入仓库面积
        self.action.send_keys(self.input_warehouse_area, form_data["warehouse_area"], [2])
        # 点击并输入仓库租金
        self.action.send_keys(self.input_warehouse_rent, form_data["warehouse_rent"])
        # 输入仓库联系人
        self.action.send_keys(self.input_warehouse_contact, form_data["warehouse_contact"], [3])
        # 输入仓库联系人电话号码
        self.action.send_keys(self.input_warehouse_phone, form_data["warehouse_phone"], [4])
        # 点击激活按钮
        self.action.click(self.button_activate)
        # 点击激活成功页面的好的按钮
        self.action.click(self.button_ok)

    def _fill_warehouse_form_android(self, form_data):
        # 输入仓库名称
        self.action.clear(self.input_warehouse_name)
        self.action.send_keys(self.input_warehouse_name, form_data["warehouse_name"])
        # 点击所在地址
        self.action.click(self.button_warehouse_address)
        # 选择一个地址
        self.action.click(self.button_warehouse_map_first)
        # # 输入详细地址
        # self.action.send_keys(self.input_warehouse_detail_address, form_data["warehouse_detail_address"])
        # 点击仓库面积控件，在输入仓库面积
        self.action.clear(self.input_warehouse_area, [2])
        self.action.send_keys(self.input_warehouse_area, form_data["warehouse_area"], [2])
        # 点击并输入仓库租金
        self.action.clear(self.input_warehouse_rent)
        self.action.send_keys(self.input_warehouse_rent, form_data["warehouse_rent"])
        # 输入仓库联系人
        self.action.clear(self.input_warehouse_contact, [3])
        self.action.send_keys(self.input_warehouse_contact, form_data["warehouse_contact"], [3])
        # 输入仓库联系人电话号码
        self.action.clear(self.input_warehouse_phone, [4])
        self.action.send_keys(self.input_warehouse_phone, form_data["warehouse_phone"], [4])
        # 点击激活按钮
        self.action.click(self.button_activate)
        # 点击激活成功页面的好的按钮
        self.action.click(self.button_ok)


