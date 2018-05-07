from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.OptimizeAddressBookAndInviteLink.OptimizeAddressBookAndInviteLinkPage \
    import OptimizeAddressBookAndInviteLink
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.OptimizeAddressBookAndInviteLinkTwo.OptimizeAddressBookAndInviteLinkTwoSQL import \
    get_optimize_address_book_and_invite_link_two, update_optimize_address_book_and_invite_link_two
from UIAutomation.Utils import get_user_id

__author__ = 'zhoujin'


class OptimizeAddressBookAndInviteLinkTwoTest(BaseTestCase):
    """
        服务认证邀请，
        查看在网仓体系下被邀请人的状态
        显示已注册状态
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        mobile = 18555090007
        password = 123456
        self.user_id = get_user_id(mobile)
        if get_optimize_address_book_and_invite_link_two():
            pass
        else:
            update_optimize_address_book_and_invite_link_two()
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_optimize_address_book_and_invite_link(self):
        LongCardPage(self.driver).click_expected_card(self.user_id, '服务认证邀请')
        sleep(3)
        OptimizeAddressBookAndInviteLink(self.driver).optimize_address_book_and_invite_link_two()
        OptimizeAddressBookAndInviteLink(self.driver).judge_method_two()
        sleep(3)
        OptimizeAddressBookAndInviteLink(self.driver).submit()

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

