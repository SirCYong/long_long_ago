from time import sleep

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, ParseXmlErrorException, \
    initial_element_error_wrapper
__author__ = 'zhongchangwei'


class ManualLocationMap(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

        try:
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

    def _page_factory_ios(self):
        name_list = ['area', 'detail_address', 'search_button', 'search', 'confirm_search', 'search_address',
                     'search_detail_address', 'map_default_address', 'map_default_detail_address', 'back',
                     'current_address']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.area_locator = ele_dic['area']  # 所在区域
        self.detail_address_locator = ele_dic['detail_address']  # 详细地址
        self.search_button_locator = ele_dic['search_button']  # 搜索按钮
        self.search_locator = ele_dic['search']  # 搜索
        self.confirm_search_locator = ele_dic['confirm_search']  # 搜索
        self.search_address_locator = ele_dic['search_address']  # 搜索的地址
        self.search_detail_address_locator = ele_dic['search_detail_address']  # 搜索的详细地址
        self.map_default_address_locator = ele_dic['map_default_address']  # 地图的默认地址
        self.map_default_detail_address_locator = ele_dic['map_default_detail_address']  # 地图的默认详细地址
        self.back_locator = ele_dic['back']  # 返回
        self.current_address_locator = ele_dic['current_address']  # 当前地址
        pass

    def _page_factory_android(self):
        name_list = ['area', 'detail_address', 'search_button', 'search', 'select_address',
                     'select_detail_address', 'map_default_address', 'map_default_detail_address']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.area_locator = ele_dic['area']  # 所在地址
        self.detail_address_locator = ele_dic['detail_address']  # 详细地址
        self.search_button_locator = ele_dic['search_button']  # 搜索按钮
        self.search_locator = ele_dic['search']  # 搜索

        self.select_address_locator = ele_dic['select_address']  # 选择的地址
        self.select_detail_address_locator = ele_dic['select_detail_address']  # 选择的详细地址
        self.map_default_address_locator = ele_dic['map_default_address']  # 地图的默认地址
        self.map_default_detail_address_locator = ele_dic['map_default_detail_address']  # 地图的详细地址
        pass

    def is_loaded(self):
        pass

    def page_factory(self):
        if self.is_run_ios():
            self._page_factory_ios()
        else:
            self._page_factory_android()

    def choice_address(self):
        if self.is_run_ios():
            self._choice_address_ios()
        else:
            self._choice_address_android()

    def check_default_map_address(self):
        if self.is_run_ios():
            self._check_default_map_address_ios()
        else:
            self._check_default_map_address_android()

    def _choice_address_ios(self):
        """
        选择地址
        """
        self.action.click(self.area_locator)
        self.action.click(self.search_button_locator)
        self.action.send_keys(self.search_locator, '计量科学研究院')
        sleep(5)
        self.action.click(self.confirm_search_locator)
        select_address = self.action.text(self.search_address_locator)
        select_detail_address = self.action.text(self.search_detail_address_locator)
        self.action.click(self.search_address_locator)
        self.address = self.action.text(self.area_locator)
        self.detail_address = self.action.text(self.detail_address_locator)
        assert select_address == self.address and select_detail_address == self.detail_address
        pass

    def _choice_address_android(self):
        """
        进入地图选择地址，选择成功后，判断选择的地址是否正确
        """
        self.action.click(self.area_locator)
        self.action.click(self.search_button_locator)
        self.action.send_keys(self.search_locator, '计量科学研究院')
        select_address = self.action.text(self.select_address_locator, locator_order=0)
        select_detail_address = self.action.text(self.select_detail_address_locator, locator_order=0)
        self.action.click(self.select_address_locator, locator_order=0)
        self.address = self.action.text(self.area_locator)
        self.detail_address = self.action.text(self.detail_address_locator, locator_order=1)
        assert select_address == self.address and select_detail_address == self.detail_address
        pass

    def _check_default_map_address_android(self):
        self.action.click(self.area_locator)
        map_default_address = self.action.text(self.map_default_address_locator, locator_order=0)
        map_default_detail_address = self.action.text(self.map_default_detail_address_locator, locator_order=0)
        assert map_default_address == self.address and map_default_detail_address == self.detail_address
        self.driver.back()

    def _check_default_map_address_ios(self):
        self.action.click(self.area_locator)
        map_default_address = self.action.text(self.map_default_address_locator)
        map_default_detail_address = self.action.text(self.map_default_detail_address_locator)
        current_address = self.action.text(self.current_address_locator)
        current_address = current_address[current_address.find(']') + 1:]
        assert map_default_address == self.address and map_default_detail_address == self.detail_address \
            and current_address == self.address
        self.action.click(self.back_locator)
