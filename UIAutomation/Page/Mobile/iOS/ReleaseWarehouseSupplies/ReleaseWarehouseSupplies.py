from time import sleep

from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'liyu'


class ReleaseWarehouse(BasePage):
    """
    功能：发布仓储供应页面
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.electricity_locator = None
        self.transshipment_locator = None
        self.un_electricity_locator = None
        self.cross_border_locator = None
        self.startdate_locator = None
        self.throughput_locator = None
        self.price_locator = None
        self.area_locator = None
        self.pricesquaremeters_locator = None
        self.immediatelyrelease_locator = None
        self.level_locator = None
        try:
            self.is_loaded()
        except ParseXmlErrorException:
            assert False

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
            pass

    def page_factory(self):
        name_list = ['Electricity', 'Transshipment', 'Un_electricity', 'Cross-border', 'SelectStartDate',
                     'Throughput', 'Price', 'Area', 'PriceSquareMeters', 'ImmediatelyRelease', 'level']
        ele_dic = page_element_factory(__file__, name_list)
        self.electricity_locator = ele_dic['Electricity']
        self.transshipment_locator = ele_dic['Transshipment']
        self.un_electricity_locator = ele_dic['Un_electricity']
        self.cross_border_locator = ele_dic['Cross-border']
        self.startdate_locator = ele_dic['SelectStartDate']
        self.throughput_locator = ele_dic['Throughput']
        self.price_locator = ele_dic['Price']
        self.area_locator = ele_dic['Area']
        self.pricesquaremeters_locator = ele_dic['PriceSquareMeters']
        self.immediatelyrelease_locator = ele_dic['ImmediatelyRelease']
        self.level_locator = ele_dic['level']
        pass

    def click_storage_supply(self):
        self.initial_element()
        get_element(self.driver, self.electricity_locator).click()  # 选择服装
        sleep(1)
        get_element(self.driver, self.throughput_locator).clear()  # 清空吞吐量
        sleep(1)
        get_element(self.driver, self.throughput_locator).send_keys('55')
        sleep(1)
        get_element(self.driver, self.price_locator).clear()
        sleep(1)
        get_element(self.driver, self.price_locator).send_keys("0.28")
        sleep(1)
        get_element(self.driver, self.area_locator).clear()
        sleep(1)
        get_element(self.driver, self.area_locator).send_keys("33")
        sleep(1)
        get_element(self.driver, self.pricesquaremeters_locator).clear()
        sleep(1)
        get_element(self.driver, self.pricesquaremeters_locator).send_keys("0.36")
        self.driver.find_element_by_accessibility_id(u'完成').click()
        get_element(self.driver, self.level_locator).click()
        get_element(self.driver, self.startdate_locator).click()
        pass

    def click_immediately_release(self):
        """
        点击'立即发布'
        :return:
        """
        get_element(self.driver, self.immediatelyrelease_locator).click()
        pass

    def assert_immediately_release(self):
        """
        选择时间后，验证是否跳转到'立即发布'页面
        :return:
        """
        self.initial_element()
        assert_that(self.action.is_element_present(self.immediatelyrelease_locator), equal_to(True))

    def is_loaded(self):
        pass
