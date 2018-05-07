from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.RegisteredSuppliers.FunRegisteredSuppliersSQL import register_suppliers_sql
from UIAutomation.Page.Mobile.RegisteredSuppliers.RegisteredSuppliersPage import RegisterSuppliersPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

"""
SIT环境下执行Android 注册供应商
"""
__author__ = "Yuetianzhuang"
__package__ = 'IscsUIAutomation'


class Fun_RegisterSupply_Smoke_test(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        self.role = "login"
        # 初始化账号
        self.usr = '15268509694'
        self.pwd = '12345678'
        # 初始化page
        LoginPage(self.driver).login(self.usr, self.pwd)
        LongCard = LongCardPage(self.driver)
        LongCard.click_expected_card(10001473, '注册供应商')
        register_suppliers_sql(user_id=10001473)  # 恢复数据
        pass

    def test_registered_supply(self):
        """
        登录成功后，点击长期卡片，进入长期卡片后滑动至发布仓储需求界面，并进入，进行冒烟测试
        """
        RegisterSuppliers = RegisterSuppliersPage(self.driver)
        RegisterSuppliers.input_required_android()  # 注册供应商，必填项
        RegisterSuppliers.single_person_android()  # 选填项-接单人
        RegisterSuppliers.reconciliation_android()  # 选填项-对账人
        RegisterSuppliers.pay_person_android()  # 选填项-付款人
        RegisterSuppliers.register()  # 注册
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass
