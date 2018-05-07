import unittest

from time import sleep
from appium import webdriver

from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium, is_element_present
from UIAutomation.page.Mobile.iOS.LaborDemand.LaborDemandPage import LaborDemandPage
from UIAutomation.page.Mobile.iOS.LaborDemand.MagePage import MainPage
from UIAutomation.page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.TestCase.SIT.iOS.Sprint2.FunLaborDemand001SQL import release_labor_demand

__author__ = 'liyu'


class FunLaborDemand001(unittest.TestCase):
    """
        发布劳务需求功能
    """
    def setUp(self):
        # 恢复测试数据
        release_labor_demand()
        self.udid = get_ios_udid()
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        # 登录
        LoginPage(self.driver).login(username=13588880000, password=123456)
        # 登录后手机桌面空白卡片
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAScrollView[1]"
                                          "/UIACollectionView[1]/UIACollectionCell[2]").click()
        sleep(2)
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '发布劳务需求'))
        pass

    def test_full2242(self):
        # 点击'发布劳务需求的任务'卡片
        MainPage(self.driver).click_release_labor_demand()
        sleep(2)
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '工种'))
        sleep(2)
        choose_labor_demand = LaborDemandPage(self.driver)
        choose_labor_demand.click_packing()
        choose_labor_demand.click_select_time()
        choose_labor_demand.click_select_address()
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '浙江省 杭州市 西湖区'))
        choose_labor_demand.click_complete()
        pass

    def tearDown(self):
        self.driver.close()
        stop_ios_appium()
        pass
