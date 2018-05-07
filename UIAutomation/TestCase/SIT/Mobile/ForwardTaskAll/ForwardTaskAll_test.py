from time import sleep
import sys
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.CardCentralPage import CardCentralPage
from UIAutomation.Page.Mobile.ForwardTask.ForwardTaskPage import ForwardTask
from UIAutomation.Page.Mobile.iOS.PageTurnPage import SwipeDown
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_user_id
from UIAutomation.Utils.HttpWrapper import eject_logged_user, get_table_list
from .ForwardTaskAllSQL import restore_forward_task, get_forward_task_data, get_user_message_info
__author__ = 'sdy'


class ForwardTaskAllTest(BaseTestCase):
    """
        全部任务转发
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        self.mobile = 15519041025
        self.to_mobile = 18555090036
        self.password = 123456
        self.from_user_id = get_user_id(self.mobile)
        self.to_user_id = get_user_id(self.to_mobile)
        restore_forward_task(self.from_user_id, self.to_user_id)  # 恢复任务转发数据，移交者：10001577，被移交者：10001588
        # token, userid = eject_logged_user(self.mobile, self.password)
        # 得到所有临时卡片的排序信息， 不在这地方获取有问题
        # self.card_list_index = get_table_list(token, userid)
        LoginPage(self.driver).login(username=self.mobile, password=self.password)  # 登录
        pass

    def test_forward_task_unit(self):
        # CardCentralPage(self.driver, str(self.mobile),self.password,self.card_list_index).\
        #     click_expected_card(self.from_user_id, '非服务认证')
        if sys.platform == "darwin":
            self.driver.find_element_by_accessibility_id('非服务认证').click()
        else:
            self.driver.find_element_by_id('com.iscs.mobilewcs:id/card_layout').click()
        sleep(3)
        SwipeDown(self.driver)
        ForwardTask(self.driver).forward_task_all()
        ForwardTask(self.driver).submit()
        sleep(3)
        forward_task_data = get_forward_task_data(self.to_user_id)
        user_message_info = get_user_message_info(self.from_user_id)
        forward_task_record_no = int(forward_task_data['forward_task_record_no'])
        user_message_info_no = int(user_message_info['user_message_info_no'])
        print(forward_task_record_no)
        print(user_message_info_no)
        assert forward_task_record_no == 2 and user_message_info_no == 2
        print("该任务转发成功！")

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

