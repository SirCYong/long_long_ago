import time
from UIAutomation.Page.main.pkg_common_page.page_login import PageLogin
from UIAutomation.Page.main.pkg_common_page.page_long_card import PageLongCard
from UIAutomation.Page.main.pkg_activate_warehouse.page_activate_warehouse import PageActivateWarehouse
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.main.pkg_activate_warehouse.data_activate_warehouse import DataActivateWarehouse


__author__ = 'zzh'
__desc__ = "激活仓库"


class TestActivateWarehouse(BaseTestCase):
    """
    激活仓库测试用例
    """
    def setUp(self):
        BaseTestCase.setUp(self)

        # 初始化page
        self.page_login = PageLogin(self.driver)
        self.page_long_card = PageLongCard(self.driver)
        self.page_activate_warehouse = PageActivateWarehouse(self.driver)

        # 登录
        self.page_login.login(DataActivateWarehouse.username, DataActivateWarehouse.password, logout=0)
        # 点击激活仓库长期卡片
        self.page_long_card.click_button_long_card_by_card_name(DataActivateWarehouse.activate_warehouse_long_card_name)

        pass

    def test_activate_warehouse_success(self):
        """
        激活仓库成功
        """
        # 激活仓库表单测试数据结构
        form_data = {
            "warehouse_name": DataActivateWarehouse.warehouse_name_success,
            "warehouse_area": DataActivateWarehouse.warehouse_area_success,
            "warehouse_rent": DataActivateWarehouse.warehouse_rent_success,
            "warehouse_contact": DataActivateWarehouse.warehouse_contact_success,
            "warehouse_phone": DataActivateWarehouse.warehouse_phone_success
        }
        # 填充激活仓库表单
        self.page_activate_warehouse.fill_warehouse_form(form_data)
        pass

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass




