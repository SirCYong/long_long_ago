from time import sleep
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.PublishWarehouseDemand.PublishWarehouseDemandPage import PublishWarehouseDemandPage
from UIAutomation.Page.Mobile.ZIGFlowFlowSQL.RegisteredSQL import update_invite_SQL, del_registered_info
from UIAutomation.Page.Mobile.ZIGFlowRegistered.ZIGFlowRegistered import ZIGFlowRegistered
from UIAutomation.Page.Mobile.ZIGFlowUpdatePage.UpdatePage import UpDatePage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

"""
DEV环境
"""
__author__ = "Yuetianzhuang"
__package__ = 'IscsUIAutomation'


class Fun_ZIG_Flow_test_Android(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        sleep(7)
        del_registered_info()
        UpDatePage(self.driver).update_page()
        update_invite_SQL()
        registeredFlow = ZIGFlowRegistered(self.driver)
        ZIGFlowRegistered(self.driver).wechat_login()
        registeredFlow.android_flow_register()

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
