from UIAutomation.Page.Mobile import CardCentralPage
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils.HttpWrapper import eject_logged_user, get_table_list
from .FunSmoke002SQL import reduction_non_service_certification_task, restore_card, \
    reduction_task
from UIAutomation.Page.Mobile.LoginPage.LoginPage import LoginPage
from UIAutomation.Page.Mobile.Android.NonServiceCertification.NonServiceCertificationPage import NonServiceCertification
__author__ = 'zhoujin'


class FuncSmoke002(BaseTestCase):
    """
        冒烟移交非服务认证任务
        有非服务认证任务的账号:10001503，手机号：18585858888,
        被非服务认证审核的账号：10001505，手机号：15920203131
        10001503将非服务认证任务移交给10001504 ，手机号： 17921213434
        10001504对10001505进行非服务认证审核
    """
    def setUp(self):
        reduction_non_service_certification_task()
        restore_card()
        reduction_task()
        self.user_id = 10001503
        mobile = 18585858888
        password = 123456
        BaseTestCase.setUp(self)
        token, userid = eject_logged_user(mobile, password)
        # 得到所有临时卡片的排序信息， 不在这地方获取有问题
        card_list_index = get_table_list(token, userid)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        # 计算出卡片的位置
        CardCentralPage(self.driver, str(mobile), password, card_list_index).click_expected_card('非服务认证')
        pass

    def test_DistributionManagerAndSupervisor(self):
        self.FUN_TaskHandover()

    def FUN_TaskHandover(self):
        NonServiceCertification(self.driver).image_click(self)
        print('非服务认证移交成功')
        ExitAppPage(self.driver).logout_app()
        self.invitee_id = 10001504
        mobile = 17921213434
        password = 123456
        BaseTestCase.setUp(self)
        token, userid = eject_logged_user(mobile, password)
        card_list_index = get_table_list(token, userid)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        CardCentralPage(self.driver, str(mobile), password, card_list_index).click_expected_card('非服务认证')
        NonServiceCertification(self.driver).only_one(self)
        NonServiceCertification(self.driver).submit()
        ExitAppPage(self.driver).logout_app()

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
