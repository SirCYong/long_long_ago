from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'liyu'


class WarehouseTask(BasePage):
    """
    库内作业卡片
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.picking_locator = None
        self.sorting_locator = None
        self.packing_locator = None
        self.deposit_locator = None
        self.release_locator = None
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

    def is_loaded(self):
        pass

    def page_factory(self):
        name_list = ['picking', 'sorting', 'packing', 'deposit', 'release']
        ele_dic = page_element_factory(__file__, name_list)
        self.picking_locator = ele_dic['picking']
        self.sorting_locator = ele_dic['sorting']
        self.packing_locator = ele_dic['packing']
        self.deposit_locator = ele_dic['deposit']
        self.release_locator = ele_dic['release']
        pass

    def click_picking(self):
        """
        拣选
        :return:
        """
        self.action.click(self.picking_locator)

    def click_sorting(self):
        """
        分拣
        :return:
        """
        self.action.click(self.sorting_locator)

    def click_packing(self):
        """
        包装
        :return:
        """
        self.action.click(self.packing_locator)
