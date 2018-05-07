from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.OptimizeAddressBookAndInviteLink.OptimizeAddressBookAndInviteLinkPage \
    import OptimizeAddressBookAndInviteLink
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.OptimizeAddressBookAndInviteLinkFive.OptimizeAddressBookAndInviteLinkFiveSQL import \
    delete_optimize_address_book_and_invite_link_five
from UIAutomation.Utils import get_user_id

__author__ = 'zhoujin'


class OptimizeAddressBookAndInviteLinkFiveTest(BaseTestCase):
    """
        服务认证邀请，
        查看在网仓体系下被邀请人的状态
        显示已注册状态
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        mobile = 18555090012
        password = 123456
        mobile1 = 18555090043
        self.user_id = get_user_id(mobile)
        self.user1_id = get_user_id(mobile1)
        delete_optimize_address_book_and_invite_link_five()
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_optimize_address_book_and_invite_link(self):
        LongCardPage(self.driver).click_expected_card(self.user_id, '监控者授权')
        sleep(3)
        OptimizeAddressBookAndInviteLink(self.driver).optimize_address_book_and_invite_link_five()
        OptimizeAddressBookAndInviteLink(self.driver).judge_method_five()
        sleep(3)
        OptimizeAddressBookAndInviteLink(self.driver).submit()

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

