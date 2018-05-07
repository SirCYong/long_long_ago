from time import sleep

from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import initial_element_error_wrapper
from UIAutomation.Utils import page_element_factory

__author__ = "LiYu"
__doc__ = "入库扫码点数"


class StoragePoint(BasePage):
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

        name_list = ['Carton', 'CommodityCode', 'ProductBatch', 'Amount', 'Units', 'Box', 'Piece', 'Mention',
                     'Bag', 'Determine', 'DefectiveGoods', 'Non-DefectiveProduct', 'TakingPictures',
                     'CompleteInspection', 'CheckNext', 'Photograph', 'Use_photo']
        ele_dic = page_element_factory(self.xml_file, name_list)
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

    def click_storage_point(self):
        """
        扫码点数
        :return:
        """
        q = ['PL00006', 'tz3228747110', 'tx7719tx7719010100', 10, 20160803]
        if self.is_run_ios():
            self._click_storage_point_step_ios(carton=q[0], commodity_code=q[1], amount=q[3])
            self._click_check_next_ios()
            self._click_storage_point_step_ios(carton=q[2], commodity_code=q[4], amount=q[3])
            self._click_check_next_ios()
            self.click_complete_inspection_ios()
            pass
        if not self.is_run_ios():
            pass

    def _click_storage_point_step_ios(self, carton=None, commodity_code=None, amount=None):
        """
        点击扫码具体操作(不需要扫批次号和拍照)
        :param carton: 外箱码
        :param commodity_code: 商品条码
        :param amount: 数量
        :return:
        """
        self.action.set_value(self.carton_locator, value=carton)   # 扫外箱码
        # tz3228747110 不需要扫批次号和拍照
        self.action.set_value(self.commoditycode_locator, value=commodity_code)  # 商品条码
        self.action.set_value(self.amount_locator, value=amount)       # 数量1
        self.action.click(self.defectivegoods_locator)         # 次品
        self.action.click(self.checknext_locator)
        pass

    def _click_storage_point_batch_ios(self, commodity_code=None, product_batch=None, amount=None):
        """
        点击扫码具体操作(需要扫批次号和拍照)
        :param commodity_code: 商品条码
        :param product_batch: 批次号
        :param amount: 数量
        :return:
        """
        # tx7719tx7719010100  需要输入批次号，拍照
        self.action.set_value(self.commoditycode_locator, value=commodity_code)
        self.action.set_value(self.productbatch_locator, value=product_batch)  # 批次号
        self.action.set_value(self.amount_locator, value=amount)  # 数量1
        self.action.click(self.non_defectiveProduct_locator)  # 良品
        self.action.click(self.takingpictures_locator)   # 拍照
        sleep(5)
        # 点击拍照按钮
        self.action.click(self.photograph_locator)
        sleep(2)
        # 点击使用照片
        self.action.click(self.use_photo_locator)

    def _click_check_next_ios(self):
        """
        点击检查下一个按钮

        """
        self.action.click(self.checknext_locator)
        pass

    def click_complete_inspection_ios(self):
        """
        点击完成检查按钮

        """
        self.action.click(self.completeinspection_locator)
        pass




