from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.MainPage.MainPage import MainPage
from UIAutomation.Page.Mobile.PublishLabour.PublishLabour import PublishLabour
from UIAutomation.Utils import ParseXmlErrorException, initial_element_error_wrapper
from UIAutomation.Utils import is_element_present
from UIAutomation.Utils import page_element_factory

__author__ = "LiYu"
__doc__ = "发布仓储供应"


class PublishWarehouseSupply(BasePage):
    def is_loaded(self):
        pass

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

    def page_factory(self):
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ['Electricity', 'Transshipment', 'Un_electricity', 'Cross_border', 'SelectStartDate',
                     'level', 'Throughput', 'Price', 'Area', 'PriceSquareMeters', 'next_step']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.electricity_localtor = ele_dic['Electricity']
        self.trans_ship_ment_localtor = ele_dic['Transshipment']
        self.un_electricity_localtor = ele_dic['Un_electricity']
        self.cross_border_localtor = ele_dic['Cross_border']
        self.select_date_localtor = ele_dic['SelectStartDate']
        self.levelr_localtor = ele_dic['level']
        self.through_put_localtor = ele_dic['Throughput']
        self.price_localtor = ele_dic['Price']
        self.area_border_localtor = ele_dic['Area']
        self.price_square_meters_localtor = ele_dic['PriceSquareMeters']
        self.next_step_localtor = ele_dic['next_step']

    def click_publish_warehouse_supply(self):
        """
        发布仓储供应
        :return:
        """
        if self.is_run_ios():
            if is_element_present(self.driver, ('ACCESSIBILITY_ID', '找劳务需求')):
                test_public_labour = PublishLabour(self.driver)
                # 滑动1次，滑到'发布仓储供应'卡片位置
                test_public_labour.click_swipe_left(x1=1.5, y1=0.5, x2=0.2, y2=0.5, time=2000)
            main_page = MainPage(self.driver)
            main_page.click_publish_supply_ios()
            self._click_publish_warehouse_supply_ios()
            pass
        if not self.is_run_ios():
            if is_element_present(self.driver, ("XPATH", "//*[@resource-id='com.iscs.mobilewcs:id/text' and @text='找劳务需求']")):
                sleep(3)
                test_public_labour = PublishLabour(self.driver)
                # 滑动3次，滑到'发布仓储供应'卡片位置
                test_public_labour.click_swipe_left(x1=1.5, y1=0.5, x2=0.2, y2=0.5, time=2000)
                sleep(3)
                test_public_labour.click_swipe_left(x1=1.5, y1=0.5, x2=0.2, y2=0.5, time=2000)
                sleep(3)
                test_public_labour.click_swipe_left(x1=1.5, y1=0.5, x2=0.2, y2=0.5, time=2000)
            main_page = MainPage(self.driver)
            main_page.click_publish_supply_android()
            self._click_publish_warehouse_supply_android()
            pass

    def _click_publish_warehouse_supply_ios(self):
        """
        IOS:发布仓储供应详细信息页面
        :return:
        """
        self.action.click(self.electricity_localtor)
        PublishLabour(self.driver).select_time_ios()
        self.action.click(self.levelr_localtor)
        self.action.set_value(self.through_put_localtor, 50000)
        labour = PublishLabour(self.driver)
        labour.close()
        self.action.set_value(self.price_localtor, 1.5)
        labour.close()
        self.action.set_value(self.area_border_localtor, 80000)
        labour.close()
        self.action.set_value(self.price_square_meters_localtor, 2.5)
        labour.close()
        self.action.click(self.next_step_localtor)

    def _click_publish_warehouse_supply_android(self):
        """
        android:发布仓储供应详细信息页面
        :return:
        """
        self.action.click(self.electricity_localtor)
        self.action.click(self.levelr_localtor)
        self.action.send_keys(self.through_put_localtor, 50000)
        self.action.send_keys(self.price_localtor, 12)
        self.action.send_keys(self.area_border_localtor, 80000)
        self.action.send_keys(self.price_square_meters_localtor, 2)
        self.action.click(self.next_step_localtor)
        pass

