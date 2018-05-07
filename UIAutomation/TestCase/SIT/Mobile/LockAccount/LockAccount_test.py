# -*- coding:utf-8 -*-
from time import sleep
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LockAccount.LockAccountPage import LockAccountPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.LockAccount.LockAccountSQL import assert_lock_account, assert_unlock_account

__author__ = 'LiYu'
""" 功能：锁定+解锁功能 """


class LockAccount(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        #eject_logged_user(account=18800001124, password=123456)
        login_page = LoginPage(self.driver)
        login_page.login(username=18072829287, password='wc123456')
        sleep(2)
        longcard = LongCardPage(self.driver)
        longcard.click_long_task_card()
        longcard.click_expected_card(10001574, u'锁定账号')
        sleep(5)
        pass

    def tearDown(self):
        # 注销app
        exit_app = ExitAppPage(self.driver)
        exit_app.logout_app()
        BaseTestCase.tearDown(self)

    def test_lock_full(self):
        lock_account = LockAccountPage(self.driver)
        lock_account.click_lock()
        assert_lock_account()
        # 返回到主界面后，查找'解锁账号'卡片
        self.driver.keyevent(4)
        longcard = LongCardPage(self.driver)
        longcard.click_expected_card(10001574, u'解锁账号')
        lock_account.click_unlock()
        assert_unlock_account()




