from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage
__Author__ = 'liyu'


class StorageInventoryPage(BasePage):
    """
    功能：上架详细信息页面
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.carton_locator = None
        self.next_step_locator = None
        self.outer_box_code_locator = None
        self.commoditycode_locator = None
        self.amount_locator = None
        self.units_locator = None
        self.box_locator = None
        self.piece_locator = None
        self.mention_locator = None
        self.bag_locator = None
        self.determine_locator = None
        self.storage_code_locator = None
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
        name_list = ['Carton', 'Next_step', 'Outer_box_code', 'Commodity_code', 'Amount', 'Units', 'Box',\
                     'Piece', 'Mention', 'Bag', 'Determine', 'Storage_code']
        ele_dic = page_element_factory(__file__, name_list)
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
        pass

    def click_carton(self, carton=None):

        """
        扫入上架外箱码

        """
        self.initial_element()
        self.action.click(self.carton_locator).send_keys(carton)
        sleep(2)
        self.action.click(self.next_step_locator)
        pass

    def click_inventory(self, outer_box_code=None, commodity_code=None, amount=None, storage_code=None):
        """
        入库上架具体步骤

        """
        self.initial_element()
        # 扫入外箱码
        self.action.click(self.outer_box_code_locator).send_keys(outer_box_code)
        sleep(2)
        # 商品条码
        self.action.click(self.commoditycode_locator).send_keys(commodity_code)
        sleep(2)
        # 输入上架数量
        self.action.click(self.amount_locator).send_keys(amount)
        sleep(2)
        # 点击库位码
        self.action.click(self.storage_code_locator).send_keys(storage_code)
        pass

    # def click_next_inventory(self):
    #
    #     """
    #     上架第2个商品
    #
    #     """
    #     self.initial_element()
    #     # 扫入外箱码
    #     self.action.click(self.outer_box_code_locator).send_keys('PL00006')
    #     sleep(2)
    #     # 商品条码
    #     self.action.click(self.commoditycode_locator).send_keys('tz3228747110')
    #     sleep(2)
    #     # 输入上架数量
    #     self.action.click(self.amount_locator).send_keys(80)
    #     sleep(2)
    #     # 点击库位码
    #     self.action.click(self.storage_code_locator).send_keys('GS01006')
    #     pass

