from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.PublishWarehouseDemand.PublishWarehouseDemandPage import PublishWarehouseDemandPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

"""
SIT环境下执行Android 发布仓储需求
"""
__author__ = "Yuetianzhuang"
__package__ = 'IscsUIAutomation'


class Fun_Publish_Warehouse_Demand_Smoke_test_Android(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        self.role = "login"
        # 初始化账号
        self.usr = '15268509694'
        self.pwd = '12345678'
        # 初始化page
        LoginPage(self.driver).login(self.usr, self.pwd)
        LongCard = LongCardPage(self.driver)
        LongCard.click_expected_card(10001473, '发布仓储需求')
        pass

    def test_warehouse_demand_android(self):
        """
        登录成功后，点击长期卡片，进入长期卡片后滑动至发布仓储需求界面，并进入，进行冒烟测试
        """
        # 点击进入长期卡片
        PublishWarehouseDemandPage(self.driver).click_business(TradeType='电商')

        PublishWarehouseDemandPage(self.driver).click_level(LevelType='大众')
        # 选择日期和地点
        PublishWarehouseDemandPage(self.driver).click_cross_border_button_android()
        # 填写吞吐量和面积
        PublishWarehouseDemandPage(self.driver).click_processing_capacity_button_android()
        # 发布
        PublishWarehouseDemandPage(self.driver).click_complete()
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass
