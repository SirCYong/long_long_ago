from UIAutomation.Page.Mobile.ChangePassword.ChangePasswordPage import ChangePasswordPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

__author__ = 'LiYu'
""" 功能：忘记密码 """


class ChangePassword(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)

    def tearDown(self):
        BaseTestCase.tearDown(self)

    def test_change_password(self):
        change_password = ChangePasswordPage(self.driver)
        change_password.change_password()


