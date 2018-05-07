from UIAutomation.Page.Mobile.CommodityQualityConversion.CommodityQualityConversionPage import \
    CommodityQualityConversionPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.SetPromotionTemplate.SetPromotionTemplate import SetPromotionTemplatePage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
"""
SIT环境下执行 商品品质转换
"""
__author__ = "Yuetianzhuang"
__package__ = 'IscsUIAutomation'


class FunCommodityQualityConversionSmoke_test(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        self.role = "login"
        # 初始化账号
        self.usr = '15268509694'
        self.pwd = '12345678'
        # 初始化page
        LoginPage(self.driver).login(self.usr, self.pwd)
        LongCardPage(self.driver).click_long_task_card()
        SetPromotionTemplatePage(self.driver).click_set_promotion_Template_card_ios()
        pass

    def test_set_promotion_template(self):
        """
        登录成功后，点击长期卡片，进入长期卡片后滑动至发布仓储需求界面，并进入，进行冒烟测试
        """
        CommodityQualityConversionPage(self.driver).commodity_quality_conversion()
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
