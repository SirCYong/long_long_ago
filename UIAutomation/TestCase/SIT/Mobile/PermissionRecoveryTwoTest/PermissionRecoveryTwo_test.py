from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.PermissionRecovery.PermissionRecoveryPage import PermissionRecovery
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_user_id
from .PermissionRecoveryTwoSQL import reduction_permission_recovery, get_new_permission_recovery
__author__ = 'zhoujin'


class PermissionRecoveryTwoTest(BaseTestCase):
    """
        权限收回
        假设，参与者已经给其他人分配过权限
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        mobile1 = 18555090013
        password = 123456
        mobile2 = 18555090015
        mobile3 = 18555090016
        self.user_id = get_user_id(mobile1)
        self.user1_id = get_user_id(mobile2)
        self.user2_id = get_user_id(mobile3)
        reduction_permission_recovery(self.user1_id)  # 还原权限收回数据
        reduction_permission_recovery(self.user2_id)  # 还原权限收回数据
        LoginPage(self.driver).login(username=mobile1, password=password)  # 登录
        pass

    def test_management_business_unit(self):
        LongCardPage(self.driver).click_expected_card(self.user_id, '管理者权限收回')
        sleep(3)
        PermissionRecovery(self.driver).permission_recovery_two()
        PermissionRecovery(self.driver).submit()
        sleep(3)

        new_permission_recovery = get_new_permission_recovery(self.user1_id)
        recovery_record_no = int(new_permission_recovery['recovery_record_no'])
        permission_record_no = int(new_permission_recovery['permission_record_no'])
        log_no = int(new_permission_recovery['log_no'])
        print(recovery_record_no, permission_record_no, log_no)

        new_permission_recovery = get_new_permission_recovery(self.user2_id)
        recovery_record_no = int(new_permission_recovery['recovery_record_no'])
        permission_record_no = int(new_permission_recovery['permission_record_no'])
        log_no = int(new_permission_recovery['log_no'])
        print(recovery_record_no, permission_record_no, log_no)

        assert recovery_record_no == permission_record_no == log_no == 1
        print("权限收回成功！")

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

