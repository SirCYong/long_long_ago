
from time import sleep
from unittest import TestCase
from appium import webdriver
from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium, is_element_present
from UIAutomation.page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.page.Mobile.iOS.NonServiceCertification.NonServiceCertificationPage import NonServiceCertification
from UIAutomation.TestCase.SIT.iOS.Sprint4.FUNNonServiceCertificationSQL import reduction_non_service_certification_task, \
      restore_card, insert_data, reduction_select

__author__ = 'chenyanxiu'


class FUNNonServiceCertification004(TestCase):
    """
        非服务认证二期
        199566 邀请10000954
    """
    def setUp(self):
        self.user_id = 199566
        self.passwdus = 11122223333
        self.me = 10000969
        self.passwdme = 17934560908
        self.udid = get_ios_udid()
        print(self.udid)
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        reduction_non_service_certification_task(self.me)
        restore_card(self.user_id)
        insert_data(self.me)
        LoginPage(self.driver).login(username=self.passwdus, password=123456)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        reduction_select(self.me)
        CardPage(self.driver).click_card_two()   # 卡片2
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass

    def test_NonServiceCertification004(self):
        self.NonServiceCertification004()
        pass

    def NonServiceCertification004(self):
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '非服务认证']):
            CardPage(self.driver).click_non_service_certification_card()  # 非服务认证
        self.non_service_certification_instant = NonServiceCertification(self.driver)
        self.non_service_certification_instant.page_factory()
        self.non_service_certification_instant.wrong_two()
        sleep(1)
        pass




