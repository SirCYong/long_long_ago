from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.PublishWarehouseDemand.PublishWarehouseDemandPage import PublishWarehouseDemandPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase


"""
SIT环境下执行iOS 发布仓储需求
"""
__author__ = "Yuetianzhuang"
__package__ = 'IscsUIAutomation'


class Fun_Publish_Warehouse_Demand_Smoke_test(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        self.role = "login"
        # 初始化账号
        self.usr = '15268509694'
        self.pwd = '12345678'
        # 初始化page
        LoginPage(self.driver).login(self.usr, self.pwd)
        LongCardPage(self.driver).click_long_task_card()
        PublishWarehouseDemandPage(self.driver).click_pub_warehouse_demand_card_ios()  # 自动到发布仓储需求卡片
        pass

    def test_warehouse_demand(self):
        """
        登录成功后，点击长期卡片，进入长期卡片后滑动至发布仓储需求界面，并进入，进行冒烟测试
        """
        # 进行一系列操作
        PublishWarehouseDemand = PublishWarehouseDemandPage(self.driver)
        # 点击进入长期卡片
        PublishWarehouseDemand.click_business(TradeType='电商')
        PublishWarehouseDemand.click_level(LevelType='大众')
        # 选择日期和地点
        PublishWarehouseDemand.click_cross_border_button_ios()
        # 填写吞吐量和面积
        PublishWarehouseDemand.click_processing_capacity_button_ios()
        # 发布
        PublishWarehouseDemand.click_complete()
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass
