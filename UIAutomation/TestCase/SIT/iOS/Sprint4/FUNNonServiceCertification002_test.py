from time import sleep
from unittest import TestCase
from appium import webdriver

from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium, is_element_present
from UIAutomation.page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.page.Mobile.iOS.NonServiceCertification.NonServiceCertificationPage import NonServiceCertification
from UIAutomation.TestCase.SIT.iOS.Sprint4.FUNNonServiceCertificationSQL import \
    reduction_non_service_certification_task, restore_card

__author__ = 'chenyanxiu'


class FUNNonServiceCertification002(BaseTestCase):
    """
        非服务认证二期
        199566 邀请199585
    """
    def setUp(self):
        self.user_id = 199566
        self.passwdus = 11122223333
        self.me = 199585
        self.passwdme = 11133332222
        reduction_non_service_certification_task(self.me)
        restore_card(self.user_id)
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
        LoginPage(self.driver).login(username=self.passwdus, password=123456)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()
        pass

    def test_NonServiceCertification002(self):
        self.NonServiceCertification002()
        pass

    def NonServiceCertification002(self):
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '非服务认证']):
            CardPage(self.driver).click_non_service_certification_card()  # 非服务认证
        self.non_service_certification_instant = NonServiceCertification(self.driver)
        self.non_service_certification_instant.page_factory()
        self.non_service_certification_instant.only_one(self.me)
        self.non_service_certification_instant.submit()
        sleep(1)
        print(u'认证通过')
        self.driver.quit()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=self.passwdme, password=123456)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        sleep(2)
        print('认证通过，获取权限')
        # self.tmp2 = [u'拣选商品'.encode('utf-8'), u'打印入库单'.encode('utf-8'),
        # u'下采购单'.encode('utf-8'), u'非服务认证'.encode('utf-8')]
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '管理者授权']):
            CardPage(self.driver).manager_authorization_card()  # 管理者授权
        pass


