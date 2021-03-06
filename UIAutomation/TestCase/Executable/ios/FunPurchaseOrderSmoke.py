from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.PurchaseOrder.PurchaseOrderPage import PurchaseOrderPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
"""
SIT环境下执行iOS 选购下单
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
        PurchaseOrderPage(self.driver).click_purchase_order_card_ios()
        pass

    def test_purchase_order(self):
        """
        登录成功后，点击长期卡片，进入长期卡片后滑动至发布仓储需求界面，并进入，进行冒烟测试
        """
        try:
            PurchaseOrder = PurchaseOrderPage(self.driver)
            PurchaseOrder.click_purchase_order_ios()
        except Exception as e:
            print(e)
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
