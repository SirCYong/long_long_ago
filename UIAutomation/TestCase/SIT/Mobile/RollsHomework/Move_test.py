from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.RollsHomework.Move import MovePage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.RollsHomework.PackingSQL import restore_container
from UIAutomation.Utils.HttpWrapper import eject_logged_user

__author__ = 'LiYu'
""" 功能：分拣"""


class Move(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        restore_container()
        eject_logged_user(account=17676769090, password=123456)
        login_page = LoginPage(self.driver)
        login_page.login(username=17676769090, password=123456)
        pass

    def tearDown(self):
        # 注销app
        exit_app = ExitAppPage(self.driver)
        exit_app.logout_app()
        BaseTestCase.tearDown(self)

    def test_move_full(self):
        test_move = MovePage(self.driver)
        test_move.move()
        pass
