from time import sleep

from UIAutomation.Page.Mobile import CardCentralPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.DistributionManagerAndSupervisor.DistributionManagerAndSupervisorPage import \
    DistributionManagerAndSupervisor
from UIAutomation.Utils import is_element_present
from UIAutomation.Utils.HttpWrapper import eject_logged_user, get_table_list
from .FunSmoke003SQL import reduction_monitor_and_manager_permissions, \
    reduction_distribution_manager_and_supervisor_task, reduction_d, get_operation
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

__author__ = 'chenyanxiu'


class FuncSmoke003(BaseTestCase):
    """
        冒烟分配权限，分配代理人是临时卡片暂时无法定位
        起始点为分配权限的账号:10001496，手机号：17699990000
        Step1：分配管理者和监控者都直接分配给自己
    """
    def setUp(self):
        self.user_id = 10001496
        mobile = 17699990000
        password = 123456
        reduction_monitor_and_manager_permissions(user_id1=self.user_id, user_id2=self.user_id)  # 还原监控者管理者权限
        reduction_distribution_manager_and_supervisor_task(user_id=self.user_id)  # 还原分配监控者和管理者任务
        operation_ukid = get_operation(self.user_id)
        reduction_d(operation_ukid)
        # sleep(3)

        BaseTestCase.setUp(self)
        token, userid = eject_logged_user(mobile, password)
        # 得到所有临时卡片的排序信息， 不在这地方获取有问题
        card_list_index = get_table_list(token, userid)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        # 计算出卡片的位置
        CardCentralPage(self.driver, str(mobile), password, card_list_index).click_expected_card('分配代理人')
        CardCentralPage(self.driver, str(mobile), password, card_list_index).click_expected_card('分配代理人')

        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass

    def test_DistributionManagerAndSupervisor(self):
        # print(is_element_present(self.driver, ['ACCESSIBILITY_ID', '分配代理人']))
        # if is_element_present(self.driver, ['ACCESSIBILITY_ID', '分配代理人']):
        #     CardPage(self.driver).distribution_manager_and_supervisor_card()  # 分配代理人
        #     print(111)
        #     sleep(3)
        DistributionManagerAndSupervisor(self.driver).distribution_manager_supervisor_to_self()
        sleep(25)
        while is_element_present(self.driver, ('ACCESSIBILITY_ID', 'icon back')):
            get_element(self.driver, ('ACCESSIBILITY_ID', 'icon back')).click()  # 不稳定，有时候会跳转进具体卡片，而不是桌面
        # assert get_distribution_manager_and_supervisor_task_status() == 10
        # assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '分配管理者和监控者')) is False  # 分配管理者和监控者卡片消失
        # assert get_element(self.driver, ('ACCESSIBILITY_ID', '管理者授权')).\
        #            get_attribute('name').encode('utf-8') == '管理者授权'  # 生成管理者授权
        # assert get_element(self.driver, ('ACCESSIBILITY_ID', '监控者授权')).get_attribute('name'). \
        #            encode('utf-8') == '监控者授权'  # 生成监控者授

