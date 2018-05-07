# -*- coding: utf-8 -*-
from time import sleep

from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.MainPage import MainPage
from UIAutomation.Page.Mobile.RollsHomework.Picking import Picking
from UIAutomation.TestCase import BaseTestCase

__author__ = 'LiYu'
""" 功能：拣选 """


class Fun001Picking(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
        LoginPage(self.driver).login(username=17676769090, password=123456)
        pass

    def test_full(self):
        sleep(10)
        MainPage(self.driver).select_page()
        sleep(5)
        Picking(self.driver).select_packing()
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
