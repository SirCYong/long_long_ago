from time import sleep
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.ManualLocationMap.ManualLocationMapPage import ManualLocationMap
from UIAutomation.TestCase.BaseTestCase import BaseTestCase

__author__ = "zhongchangwei"
__package__ = 'IscsUIAutomation'


class ManualLocationMapSmoke(BaseTestCase):
    """
        预先创建了两个仓储供应契约:分别为地产契约和仓储契约,
        并修改创建时间时间,让他们排在最前面,然后签订完成两个契约
    """
    def setUp(self):
        mobile = 13766663333
        password = 123456
        BaseTestCase.setUp(self)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

    def test_DistributionManagerAndSupervisor(self):
        LongCardPage(self.driver).click_expected_card(10001646, '注册业务关系人')
        sleep(3)
        manual_location_map_instant = ManualLocationMap(self.driver)
        manual_location_map_instant.page_factory()
        manual_location_map_instant.choice_address()   # 选择地图地址
        manual_location_map_instant.check_default_map_address()   # 选择完成后再次进入地图判断地址

