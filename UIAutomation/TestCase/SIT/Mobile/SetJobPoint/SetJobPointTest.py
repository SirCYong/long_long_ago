# coding=utf-8
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
import pytest
from UIAutomation.Page.Mobile.CommonPage.LoginPage import LoginPage
from UIAutomation.Page.Mobile.CommonPage.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.SetJobPoint.SetJobPointPage import SetJobPointPage
from UIAutomation.TestCase.SIT.Mobile.SetJobPoint.SetJobPointData import SetJobPointData

__doc__ = "维护工作点"
__author__ = "zzh"


@pytest.mark.tryfirst
class TestFunSetJobPoint(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)

        # 恢复测试数据

        # 初始化page
        self.login_page = LoginPage(self.driver)
        self.long_card_page = LongCardPage(self.driver)
        self.set_job_point_page = SetJobPointPage(self.driver)

        # 登录
        self.login_page.login(SetJobPointData.username, SetJobPointData.password, logout=0)
        # 点击维护工作点
        self.long_card_page.click_expected_card(SetJobPointData.user_id, SetJobPointData.job_point_long_card_name)

        pass

    def test_add_job_point_success(self):
        """
        新增工作点成功
        """
        # 输入工作点条码
        self.set_job_point_page.input_job_point_code(SetJobPointData.job_point_code_add_success)
        # 点击工作点类型
        self.set_job_point_page.click_job_point_name()
        # 选择一个工作点类型
        self.set_job_point_page.swipe_wheel_vendor()
        # 点击工作点类型选择中的确定按钮
        self.set_job_point_page.click_btn_confirm()
        # 点击完成按钮
        self.set_job_point_page.click_btn_finish()
        pass

    def test_add_job_point_fail(self):
        """
        新增工作点失败
        :return:
        """
        # 输入工作点条码
        self.set_job_point_page.input_job_point_code(SetJobPointData.job_point_code_add_fail)
        # 检查页面不会跳到下一页
        self.set_job_point_page.check_job_point_name_exist()

    def test_modify_job_point_success(self):
        """
        维护工作点成功
        :return:
        """
        # 输入工作点条码
        self.set_job_point_page.input_job_point_code(SetJobPointData.job_point_code_modify_success)
        # 点击工作点类型
        self.set_job_point_page.click_job_point_name()
        # 选择一个工作点类型
        self.set_job_point_page.swipe_wheel_vendor()
        # 点击工作点类型选择中的确定按钮
        self.set_job_point_page.click_btn_confirm()
        # 点击完成按钮
        self.set_job_point_page.click_btn_finish()
        pass

    def test_modify_job_point_fail(self):
        """
        维护工作点失败
        :return:
        """
        # 输入工作点条码
        self.set_job_point_page.input_job_point_code(SetJobPointData.job_point_code_modify_fail)
        # 检查页面不会跳到下一页
        self.set_job_point_page.check_job_point_name_exist()

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass