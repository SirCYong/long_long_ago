from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.PublishGoodsSupply.PublishGoodsSupplyPage import PublishGoodsSupplyPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
"""
SIT环境下执行Android 发布供货供应
"""
__author__ = "Yuetianzhuang"
__package__ = 'IscsUIAutomation'


class Fun_Publish_Goods_Supply_Smoke_test(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        self.role = "login"
        # 初始化账号
        self.usr = '15268509694'
        self.pwd = '12345678'
        # 初始化page
        LoginPage(self.driver).login(self.usr, self.pwd)
        LongCard = LongCardPage(self.driver)
        LongCard.click_expected_card(10001473, '发布供货供应')
        pass

    def test_registered_supply(self):
        """
        登录成功后，点击长期卡片，进入长期卡片后滑动至发布仓储需求界面，并进入，进行冒烟测试
        """
        PublishGoodsSupplyPage(self.driver).publish_goods_supply_android()
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()  # 退出当前账号
        BaseTestCase.tearDown(self)
        pass
