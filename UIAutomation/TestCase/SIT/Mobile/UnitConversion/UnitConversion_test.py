from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.UnitConversion.UnitConversionPage import UnitConversionPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.UnitConversion.UnitConversion_sql import delete_unit_convert

__author__ = 'chenyanxiu'


class FunUnitConversion(BaseTestCase):
    """
        单位转换
        先生添加一个单位,然后添加该单位的转换
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        self.user_id = 10001566
        mobile = 15777778890
        password = 123456
        unit = '箱'
        delete_unit_convert(self.user_id, unit)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_UnitConversion(self):
        unit = '箱'
        goods = '大苹果124'
        LongCardPage(self.driver).click_expected_card(10001566, '管理单位')
        unit_conversion_instant = UnitConversionPage(self.driver)
        unit_conversion_instant.page_factory()
        unit_conversion_instant.add_unit(unit)  # 添加单位
        self.driver.keyevent(4)
        LongCardPage(self.driver).click_expected_card(10001566, '单位转换')
        unit_conversion_instant.unit_convert(unit, goods)
