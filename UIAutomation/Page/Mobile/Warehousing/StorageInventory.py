from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Utils import page_element_factory

__author__ = "LiYu"
__doc__ = "入库上架"


class StorageInventory(BasePage):
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

        name_list = ['Carton', 'Next_step', 'Outer_box_code', 'Commodity_code', 'Amount', 'Units', 'Box',
                     'Piece', 'Mention', 'Bag', 'Determine', 'Storage_code']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.carton_locator = ele_dic['Carton']
        self.next_step_locator = ele_dic['Next_step']
        self.outer_box_code_locator = ele_dic['Outer_box_code']
        self.commoditycode_locator = ele_dic['CommodityCode']
        self.amount_locator = ele_dic['Amount']
        self.units_locator = ele_dic['Units']
        self.box_locator = ele_dic['Box']
        self.piece_locator = ele_dic['Piece']
        self.mention_locator = ele_dic['Mention']
        self.bag_locator = ele_dic['Bag']
        self.determine_locator = ele_dic['Determine']
        self.storage_code_locator = ele_dic['Storage_code']

    def click_storage_inventory(self):
        """
        入库上架
        :return:
        """
        w = ['PL00006', 'tz3228747110', '150', 'GS01005', 'tx7719tx7719010100', '100', 'GS01006']
        if self.is_run_ios():
            self._click_carton_ios(carton=w[0])
            self._click_inventory_ios(outer_box_code=w[0], commodity_code=w[1], amount=w[2], storage_code=w[3])
            self._click_inventory_ios(outer_box_code=w[0], commodity_code=w[4], amount=w[5], storage_code=w[6])
        if not self.is_run_ios():
            pass

    def _click_carton_ios(self, carton=None):

        """
        扫入上架外箱码

        """
        self.action.set_value(self.carton_locator, value=carton)
        sleep(2)
        self.action.click(self.next_step_locator)
        pass

    def _click_inventory_ios(self, outer_box_code=None, commodity_code=None, amount=None, storage_code=None):
        """
        入库上架具体步骤

        """
        # 扫入外箱码
        self.action.set_value(self.outer_box_code_locator, value=outer_box_code)
        sleep(2)
        # 商品条码
        self.action.set_value(self.commoditycode_locator, value=commodity_code)
        sleep(2)
        # 输入上架数量
        self.action.set_value(self.amount_locator, value=amount)
        sleep(2)
        # 点击库位码
        self.action.set_value(self.storage_code_locator, value=storage_code)
        pass



