from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.SetPromotionTemplate.SetPromotionTemplate import SetPromotionTemplatePage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
"""
SIT环境下执行iOS 注册供应商
"""
__author__ = "Yuetianzhuang"
__package__ = 'IscsUIAutomation'


class FunSetPromotionTemplateSmoke_test(BaseTestCase):
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
        SetPromotionTemplate = SetPromotionTemplatePage(self.driver)

        SetPromotionTemplate.Set_PromotionTemplate_SupplierAndNeeds_ios()
        SetPromotionTemplate.ChooseServiceType(Type='促销劳务服务')
        SetPromotionTemplate.SetPromotionTemplate_Promotion_type_ios(PromotionType='满总金额减总金额')
        SetPromotionTemplate.SetPromotionTemplate_PromotionTime_ios()
        SetPromotionTemplate.SetPromotionTemplate_TotalAmount_ios()
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass
