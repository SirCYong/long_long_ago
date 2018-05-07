from time import sleep
from unittest import TestCase
from appium import webdriver
from .FunSmoke017SQL import reduction_non_service_certification_task, restore_card, \
    reduction_task

from UIAutomation.Utils import get_ios_udid, start_ios_appium, stop_ios_appium, is_element_present
from UIAutomation.page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.page.Mobile.iOS.NonServiceCertification.NonServiceCertificationPage import NonServiceCertification
from UIAutomation.page.Mobile.iOS.TaskHandover.TaskHandoverPage import TaskHandoverPage

__author__ = 'chenyanxiu'


class FuncSmoke017(TestCase):
    """
        冒烟移交非服务认证任务
        起始点为有非服务认证任务的账号:199306，手机号：13131313131
        Step1：199306任务移交给199309 手机号 15623232323 被邀请人 199330 手机号 18466886688
    """
    def setUp(self):
        self.user_id = 199306
        self.passwdus = 13131313131
        self.move_id = 199309
        self.passwdine = 15623232323
        self.me = 199330
        self.passwdme = 18466886688
        reduction_non_service_certification_task(self.me)
        restore_card(self.move_id)
        reduction_task(self.user_id, self.move_id)
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

    def test_DistributionManagerAndSupervisor(self):
        self.FUN_TaskHandover()

    def FUN_TaskHandover(self):
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '非服务认证']):
            CardPage(self.driver).click_non_service_certification_card()  # 非服务认证
        self.swipe()
        sleep(5)
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', 'icon send']) is False:
            self.swipe()
        #  移交任务，认证
        self.task_handover_instant = TaskHandoverPage(self.driver)
        self.task_handover_instant.page_factory()
        self.task_handover_instant.handover()
        print('移交非服务认证任务')
        sleep(7)
        self.driver.quit()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=self.passwdine, password=123456)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '刷新']):
            sleep(7)
            CardPage(self.driver).click_f5()  # 刷新
            sleep(7)
            CardPage(self.driver).click_f5()  # 刷新
            sleep(7)
            CardPage(self.driver).click_f5()  # 刷新
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '非服务认证']):
            CardPage(self.driver).click_non_service_certification_card()  # 非服务认证
        print('移交非服务认证任务给')
        self.non_service_certification_instant = NonServiceCertification(self.driver)
        self.non_service_certification_instant.page_factory()
        self.non_service_certification_instant.only_one(self.me)
        self.non_service_certification_instant.submit()
        sleep(1)
        # self.tmp2 = [u'拣选商品'.encode('utf-8'), u'打印入库单'.encode('utf-8'),
        # u'下采购单'.encode('utf-8'), u'非服务认证'.encode('utf-8')]
        self.driver.quit()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=self.passwdme, password=123456)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        sleep(2)
        print('认证通过，获取权限')

    def swipe(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width / 2, height * 3 / 7, width / 2, (height * 4 / 7), 1000)  # 下滑
