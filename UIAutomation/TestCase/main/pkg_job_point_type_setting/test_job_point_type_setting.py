import time
from UIAutomation.Page.main.pkg_common_page.page_login import PageLogin
from UIAutomation.Page.main.pkg_common_page.page_long_card import PageLongCard
from UIAutomation.Page.main.pkg_job_point_type_setting.page_job_point_type_setting import PageJobPointTypeSetting
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.main.pkg_job_point_type_setting.data_job_point_type_setting import *


__author__ = 'zzh'
__desc__ = "作业点设置"


class TestJobPointTypeSetting(BaseTestCase):
    """
    作业点设置测试用例
    """
    def setUp(self):
        BaseTestCase.setUp(self)

        # 初始化page
        self.page_login = PageLogin(self.driver)
        self.page_long_card = PageLongCard(self.driver)
        self.page_job_point_type_setting = PageJobPointTypeSetting(self.driver)

        # 登录
        self.page_login.login(DataJobPointTypeSetting.username, DataJobPointTypeSetting.password, logout=0)
        # 点击激活仓库长期卡片
        self.page_long_card.click_button_long_card_by_card_name(DataJobPointTypeSetting.job_point_type_setting_long_card_name)

        pass

    def test_job_point_type_setting_success(self):
        """
        作业点设置成功
        """
        # 选择一个仓库
        self.page_job_point_type_setting.select_warehouse()
        # 选择所有维度（只要前一次选中所有，后面都会选中所有）
        # self.page_job_point_type_setting.select_all_demension()
        # 点击下一步按钮
        self.page_job_point_type_setting.click_button_next()
        # 输入作业点类型名称
        self.page_job_point_type_setting.send_keys_job_point_name(DataJobPointTypeSetting.job_point_type_name)
        # 选择作业点类型
        self.page_job_point_type_setting.select_job_point_type()
        # 点击完成并查看按钮
        self.page_job_point_type_setting.click_button_complete()
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass




