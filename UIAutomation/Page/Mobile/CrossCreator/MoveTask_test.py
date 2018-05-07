# coding: utf-8

"""
 跨创造者移交任务
 Cy
 测试环境 CIT
 前提：
    手机通讯录第一个号码必须是18915121114、第二个号码必须是  13755553333
    以上两个号有数据，等迁移至SIT在更改号码
"""
from UIAutomation.Page.Mobile.CrossCreator.TransferTaskPage import TransferTask
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_user_id, sleep


class MoveTask(BaseTestCase):
    def setUp(self):
        self.password = 123456
        self.mobile1 = 18915121114
        self.mobile2 = 13755553333
        self.user_id1 = get_user_id(self.mobile1)
        self.user_id2 = get_user_id(self.mobile2)
        BaseTestCase.setUp(self)
        LoginPage(self.driver).login(self.mobile1, self.password)
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

    def test_personToHandOverTask(self):
        TransferTask(self.driver).operation_transfer_task()
        ExitAppPage(self.driver).logout_app()
        LoginPage(self.driver).login(self.mobile2, self.password)
        TransferTask(self.driver).operation_transfer_task1()
        pass