from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'liyu'


class StoragePointPage(BasePage):
    """
    扫码点数详细信息界面
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.carton_locator = None
        self.commoditycode_locator = None
        self.productbatch_locator = None
        self.amount_locator = None
        self.units_locator = None
        self.box_locator = None
        self.piece_locator = None
        self.mention_locator = None
        self.bag_locator = None
        self.determine_locator = None
        self.defectivegoods_locator = None
        self.non_defectiveProduct_locator = None
        self.takingpictures_locator = None
        self.completeinspection_locator = None
        self.checknext_locator = None
        self.photograph_locator = None
        self.use_photo_locator = None
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
        name_list = ['Carton', 'CommodityCode', 'ProductBatch', 'Amount', 'Units', 'Box', 'Piece', 'Mention',
                     'Bag', 'Determine', 'DefectiveGoods', 'Non-DefectiveProduct', 'TakingPictures',
                     'CompleteInspection', 'CheckNext', 'Photograph', 'Use_photo']
        ele_dic = page_element_factory(__file__, name_list)
        self.carton_locator = ele_dic['Carton']
        self.commoditycode_locator = ele_dic['CommodityCode']
        self.productbatch_locator = ele_dic['ProductBatch']
        self.amount_locator = ele_dic['Amount']
        self.units_locator = ele_dic['Units']
        self.box_locator = ele_dic['Box']
        self.piece_locator = ele_dic['Piece']
        self.mention_locator = ele_dic['Mention']
        self.bag_locator = ele_dic['Bag']
        self.determine_locator = ele_dic['Determine']
        self.defectivegoods_locator = ele_dic['DefectiveGoods']
        self.non_defectiveProduct_locator = ele_dic['Non-DefectiveProduct']
        self.takingpictures_locator = ele_dic['TakingPictures']
        self.completeinspection_locator = ele_dic['CompleteInspection']
        self.checknext_locator = ele_dic['CheckNext']
        self.photograph_locator = ele_dic['Photograph']
        self.use_photo_locator = ele_dic['Use_photo']

        pass

    def click_storage_point_step(self, carton=None, commodity_code=None, amount=None):
        """
        点击扫码具体操作(不需要扫批次号和拍照)
        :param carton: 外箱码
        :param commodity_code: 商品条码
        :param amount: 数量
        :return:
        """
        self.initial_element()
        self.action.click(self.carton_locator).send_keys(carton)   # 扫外箱码
        # tz3228747110 不需要扫批次号和拍照
        self.action.click(self.commoditycode_locator).send_keys(commodity_code)  # 商品条码
        self.action.click(self.amount_locator).send_keys(amount)       # 数量1
        self.action.click(self.defectivegoods_locator)         # 次品
        self.action.click(self.checknext_locator)
        pass

    def click_storage_point_batch(self, commodity_code=None, product_batch=None, amount=None):
        """
        点击扫码具体操作(需要扫批次号和拍照)
        :param commodity_code: 商品条码
        :param product_batch: 批次号
        :param amount: 数量
        :return:
        """
        self.initial_element()
        # tx7719tx7719010100  需要输入批次号，拍照
        self.action.click(self.commoditycode_locator).send_keys(commodity_code)
        self.action.click(self.productbatch_locator).send_keys(product_batch)  # 批次号
        self.action.click(self.amount_locator).send_keys(amount)  # 数量1
        self.action.click(self.non_defectiveProduct_locator)  # 良品
        self.action.click(self.takingpictures_locator)   # 拍照
        sleep(5)
        # 点击拍照按钮
        self.action.click(self.photograph_locator)
        sleep(2)
        # 点击使用照片
        self.action.click(self.use_photo_locator)

    def click_check_next(self):
        """
        点击检查下一个按钮

        """
        self.initial_element()
        self.action.click(self.checknext_locator)
        pass

    def click_complete_inspection(self):
        """
        点击完成检查按钮

        """
        self.initial_element()
        self.action.click(self.completeinspection_locator)
        pass






