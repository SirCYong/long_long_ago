from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.OptimizeAddressBookAndInviteLink.OptimizeAddressBookAndInviteLinkPage \
    import OptimizeAddressBookAndInviteLink
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.OptimizeAddressBookAndInviteLink.OptimizeAddressBookAndInviteLinkSQL import \
    delete_optimize_address_book_and_invite_link
from UIAutomation.Utils import get_user_id

__author__ = 'zhoujin'


class OptimizeAddressBookAndInviteLinkTest(BaseTestCase):
    """
        服务认证邀请，非服务认证邀请
        查看不在网仓体系下被邀请人的状态
        显示“邀请”状态
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        mobile = 18555090009
        password = 123456
        self.user_id = get_user_id(mobile)
        delete_optimize_address_book_and_invite_link()   # 删除数据
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_optimize_address_book_and_invite_link(self):
        LongCardPage(self.driver).click_expected_card(self.user_id, '服务认证邀请')
        sleep(3)
        OptimizeAddressBookAndInviteLink(self.driver).optimize_address_book_and_invite_link()
        OptimizeAddressBookAndInviteLink(self.driver).judge_method()
        sleep(3)
        OptimizeAddressBookAndInviteLink(self.driver).submit()

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

