from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.UpDeliveryOrder.UpDeliveryOrderPage import UpDeliveryOrderPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
"""
SIT环境下执行iOS 上传送货单
"""
__author__ = "Yuetianzhuang"
__package__ = 'IscsUIAutomation'


class FunUpDeliveryOrderSmoke_test(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        self.role = "login"
        # 初始化账号
        self.usr = '15268509694'
        self.pwd = '12345678'
        # 初始化page
        LoginPage(self.driver).login(self.usr, self.pwd)
        LongCardPage(self.driver).click_long_task_card()
        LongCardPage(self.driver).click_expected_card(10001473, '上传送货单')
        pass

    def test_up_delivery_order(self):
        """
        登录成功后，点击长期卡片，进入长期卡片后滑动至发布仓储需求界面，并进入，进行冒烟测试
        """
        UpDeliveryOrderPage(self.driver).click_up_delivery_order_ios()
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
