"""
Author:liyu
"""
# 功能：发布劳务需求


from appium import webdriver

from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.LaborDemand.LaborDemandPage import LaborDemandPage
from UIAutomation.Page.browser.MainPage import MainPage
from UIAutomation.TestCase import BaseTestCase
from UIAutomation.Utils import get_ios_udid, stop_ios_appium, start_ios_appium
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke008SQL import release_labor_demand, select_labor_demand


class FunSmoke008(BaseTestCase):

    def setUp(self):
        username = 13588880000
        password = 123456
        # 恢复测试数据
        release_labor_demand()
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        # 初始化page
        self.main_page = MainPage(self.driver, __file__)
        self.login_page = LoginPage(self.driver)
        self.labor_demand_page = LaborDemandPage(self.driver)
        # 登录
        self.login_page.login(username=username, password=password)
        # 登录后手机桌面空白卡片
        self.main_page.click_empty_card()
        self.main_page.assert_labor_demand_present()
        pass

    def test_full2242(self):
        # 点击'发布劳务需求的任务'卡片
        self.main_page.click_release_labor_demand()
        self.labor_demand_page.assert_picking_locator_present()
        self.labor_demand_page.click_packing()
        self.labor_demand_page.click_select_time()
        self.labor_demand_page.click_select_address()
        self.labor_demand_page.assert_location_present()
        self.labor_demand_page.click_complete()
        select_labor_demand()
        pass

    def tearDown(self):
        stop_ios_appium()
        pass
