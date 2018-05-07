# -*- coding: utf-8 -*-
"""
 iOS系统Sprint1全流程自动化测试流程覆盖场景1.
 1. 已经创建了一个新的用户,通过操作数据库实现数据回滚循环测试,目前定义好的用户ID为199236, 手机号码为：13577889900
 2. 目前CIT环境中已经创建了这个用户，初始状态处于处理“选择服务类型的卡片”
 3. 要求：
    -- 手机通讯录上存在一致的通讯目录（昌为补充）
    -- 每张卡片生成的测试数据需要全部删除，必须要删除的必须要保证不影响下次测试.
    -- 任务中枢的数据需要删除掉只剩下状态为0的且值只存在RegService服务类型的一条数据

    select * from task_app.ts_operation where ppt_ukid = 199236 and operation_type =
    'RegService';  ---只保留一条状态为0的RegSserivice数据

    select * from task_app.MS_CARD where RECEIVER_ID = 199236 and card_type = 'RegService'
    ; ---只保留一条状态为0的RegSserivice数据

4. 测试账号注册信息：
    select * from basic_owner.cm_business_area_fee;
    select * from basic_owner.ba_user where mobile = 13888886666 ;
    select * from basic_owner.Cm_Human;
    select * from basic_owner.cm_identify;
    select * from basic_owner.cm_participant;
5. 各个业务创建的数据查询以及删除
     ---卡片和支付（李宇）
    delete from task_owner.TS_PAYMENT_RECORDS t where t.create_user_id=199236;

    delete from task_owner.ts_payment_bill_detail n where n.bill_ukid  in
    (select o.bill_ukid from task_owner.ts_payment_bill  o  where  o.create_user_id=199236);

    delete from task_owner.ts_payment_bill  o  where  o.create_user_id=199236;

    ---只保留一条状态为0的RegSserivice数据
    select * from task_app.ts_operation where ppt_ukid = 199236 and operation_type = 'RegService';
    delete from task_app.ts_operation where ppt_ukid = 199236 and operation_type != 'RegService';
    update task_app.ts_operation set status = '0'where  ppt_ukid = 199236;

    ---只保留一条状态为0的RegSserivice数据
    select * from task_app.MS_CARD where RECEIVER_ID = 199236 and card_type = 'RegService';
    delete from task_app.MS_CARD where  RECEIVER_ID = 199236 and CARD_type != 'RegService';
    update task_app.MS_CARD set STATUS = '0'where RECEIVER_ID = 199236;

     --- 选择服务类型（曹永）
            delete from CM_REGISTERED_SUPPLY_DEMAND where CREATE_USER_ID = self.admin
     --- 分配权限和发起服务认证邀请（昌为）

银联测试账号：6216261000000000018   证件号码：341126197709218366    短信验证码：123456（必须先点击获取验证码）


"""
from time import sleep
from unittest import TestCase
from appium import webdriver

from UIAutomation.Page.Mobile.Android.SelectServiceScope.ChoosePayPage import ChoosePayPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.CardListPage import CardPage
from UIAutomation.Page.Mobile.iOS.DistributionManagerAndSupervisor.DistributionManagerAndSupervisorPage import \
    DistributionManagerAndSupervisor
from UIAutomation.Page.Mobile.iOS.MailList.MailListPage import MailListPage
from UIAutomation.Page.Mobile.iOS.MonitorAuthorization.MonitorAuthorizationPage import MonitorAuthorization
from UIAutomation.Page.Mobile.iOS.SelectServiceScope.SelectServiceScope import SelectServiceScope
from UIAutomation.Page.Mobile.iOS.TaskHandover.TaskHandoverPage import TaskHandoverPage
from UIAutomation.TestCase.SIT.iOS.Sprint1.SitSprint1Full001SQL import reduction_monitor_and_manager_permissions, \
    reduction_service_type, reduction_payment_info, view_permissions, reduction_non_service_certification_task, \
    restore_card, reduction_task, get_distribution_manager_and_supervisor_task_status, \
    reduction_distribution_manager_and_supervisor_task
from UIAutomation.Utils import get_ios_udid, stop_ios_appium,start_ios_appium,get_element, get_elements, is_element_present




class SitSprintFull001(TestCase):
    def setUp(self):
        self.user_id = 199270
        self.invitee_id = 199276
        # 用户账号从199236变为428, 从迭代二数据结构变化导致的老账号失效
        self.admin = 199236
        reduction_monitor_and_manager_permissions()  # 还原监控者管理者权限
        reduction_distribution_manager_and_supervisor_task()  # 还原分配监控者和管理者任务
        reduction_service_type()
        reduction_payment_info()
        
        self.udid = get_ios_udid()
        sleep(3)
        stop_ios_appium()
        start_ios_appium(self.udid)
        # 连接ios设备
        self.desired_caps = {'platformName': 'iOS', 'deviceName': 'iPhone SE', 'device': 'iOS',
                             'bundleId': 'com.iscs.SmallAnimal', 'version': '9.3', 'udid': self.udid}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(3)
        self.get_ui_locator(self.driver)
        LoginPage(self.driver).login(username=self.admin)  # 登录

        pass

    def tearDown(self):
        self.driver.quit()
        stop_ios_appium()

        pass

    def test_DistributionManagerAndSupervisor(self):
        self.full()
        self.FUN_DistributionManagerAndSupervisor()  # 分配管理者和监控者
        self.FUN_MonitorAuthorization()  # 监控者授权
        self.FUN_ManagerAuthorization()  # 管理者授权
        self.FUN_TaskHandover()  # 移交任务
        self.FUN_NonServiceCertification()  # 非服务认证

    def full(self):
        # 临时增加了首页任务页面
        # 临时的卡片中心,没有名称,通过XPAH临时进入
        CardPage(self.driver).click_card_one()  # 卡片1
        CardPage(self.driver).click_select_service_scope()  # 点击选择服务范围卡片
        sleep(2)
        select_servcie_scope_instance = SelectServiceScope(self.driver)
        select_servcie_scope_instance.click_MakeProduction()  # 搞生产
        select_servcie_scope_instance.click_Freight()  # 运货
        select_servcie_scope_instance.click_ManageLabor()  # 管劳务
        # a = self.driver.find_element_by_xpath().is_enabled()  # 判断是否高亮显示
        # assert a == True
        select_servcie_scope_instance.click_Paydeposit()  # 交纳保证金
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '提交保证金')):

            get_element(self.driver, ('ACCESSIBILITY_ID', '提交保证金')).click()

        sleep(2)
        ChoosePayPage(self.driver).click_union_pay()   # 选择银联支付
        sleep(10)
        # g = self.driver.find_elements_by_class_name('UIATextField')
        # self.driver.find_element_by_class_name('UIATextField').send_keys("6216 2610 0000 0000 018 ")

        # self.driver.find_element_by_accessibility_id(u'下一步').click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '下一步']).click()
        sleep(5)
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '确定')):
            get_element(self.driver, ['ACCESSIBILITY_ID', '确定']).click()
            get_element(self.driver, ['ACCESSIBILITY_ID', '下一步']).click()
        # self.driver.find_element_by_accessibility_id(u'证件号').send_keys("3411 2619 7709 2183 66")
        # self.driver.find_element_by_accessibility_id(u'免费获取').click()
        print('进入支付页面,调用银联支付')
        get_element(self.driver, ['ACCESSIBILITY_ID', '免费获取']).click()
        edit_elements = self.driver.find_elements_by_class_name('UIATextField')
        edit_elements[-1].set_value("123456")
        # self.driver.find_element_by_accessibility_id(u'完成').click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '完成']).click()
        # self.driver.find_element_by_accessibility_id(u'确认付款').click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '确认付款']).click()
        sleep(5)
        # self.driver.find_element_by_accessibility_id(u'返回商户').click()

        get_element(self.driver, ['ACCESSIBILITY_ID', '返回商户']).click()
        sleep(5)
        print('付款完成,返回商铺')
        # print()
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '确定需要的服务类型']):
            get_element(self.driver, ['ACCESSIBILITY_ID', '确定需要的服务类型']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '可靠的保险']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '选择好了']).click()

        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '确定被服务的服务类型']):
            get_element(self.driver, ['ACCESSIBILITY_ID', '确定被服务的服务类型']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '向我借钱']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '完成']).click()

        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '填写拥有的资产类型']):
            get_element(self.driver, ['ACCESSIBILITY_ID', '填写拥有的资产类型']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '仓库']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', '选择好了']).click()

        pass

    def FUN_DistributionManagerAndSupervisor(self):  # 分配管理者和监控者，都分配给自己
        reduction_monitor_and_manager_permissions()  # 还原监控者管理者权限
        reduction_distribution_manager_and_supervisor_task()  # 还原分配监控者和管理者任务
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '分配管理者和监控者']):
            CardPage(self.driver).distribution_manager_and_supervisor_card()  # 分配管理者和监控者

        get_elements(self.driver, self.assigned_to_me_locator)[0].click()  # 监控者分配给我
        get_element(self.driver, self.assigned_to_me_locator).click()  # 管理者分配给我
        get_element(self.driver, self.distribution_success_button_locator).click()  # 点击分配成功\
        sleep(20)
        while is_element_present(self.driver, ('ACCESSIBILITY_ID', 'icon back')):
            get_element(self.driver, ('ACCESSIBILITY_ID', 'icon back')).click()  # 不稳定，有时候会跳转进具体卡片，而不是桌面

        assert get_distribution_manager_and_supervisor_task_status() == 10
               # and judge_manager_and_supervisor_result() is True  # sql判断权限
        assert is_element_present(self.driver, ('ACCESSIBILITY_ID', '分配管理者和监控者')) is False  # 分配管理者和监控者卡片消失
        assert get_element(self.driver, ('ACCESSIBILITY_ID', '管理者授权')).get_attribute('name'). \
                   encode('utf-8') == '管理者授权'  # 生成管理者授权
        assert get_element(self.driver, ('ACCESSIBILITY_ID', '监控者授权')).get_attribute('name'). \
                   encode('utf-8') == '监控者授权'  # 生成监控者授权

    def FUN_MonitorAuthorization(self):  # 监控者授权

        # 一级监控者移交权限
        while is_element_present(self.driver, ('ACCESSIBILITY_ID', 'icon back')):
            get_element(self.driver, ('ACCESSIBILITY_ID', 'icon back')).click()  # 不稳定，有时候会跳转进具体卡片，而不是桌面
        permissions_199236_before = view_permissions(participant=self.admin, role_type='31')  # 获取一级监控者的权限
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '监控者授权']):
            CardPage(self.driver).monitor_authorization_card()  # 进入监控者授权

        # 移交权限:拿取容器,质检,下采购单,选择一级监控者用户
        self.monitor_authorization_instant.assign_permission(self.transfer_jurisdiction_locator,
                                                             u'一级监控者', permission_type1=self.take_container_locator,
                                                             permission_type2=self.quality_testing_locator,
                                                             permission_type3=self.purchase_order_locator)

        permissions_199236_after = view_permissions(participant=self.admin, role_type='31')  # 移交权限后获取一级监控者的权限
        permissions_199276_after = view_permissions(participant='199276', role_type='32')  # 被移交人的监控者权限
        self.tmp = [u'拿取容器'.encode('utf-8'), u'质检'.encode('utf-8'), u'下采购单'.encode('utf-8')]
        # assert permissions_199236_before == permissions_199236_after and \
        #        set(self.tmp).issubset(set(permissions_199276_after)) is True  # 移交后，判断一级监控者的和被分配者的权限
        print('一级监控者移交权限给用户199276')

        # 一级监控者复制权限
        CardPage(self.driver).click_card_one()  # 卡片1
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '监控者授权']):
            CardPage(self.driver).monitor_authorization_card()  # 进入监控者授权
        # 复制权限:拣选商品,打印入库单,采购计划,选择一级监控者用户
        self.monitor_authorization_instant.assign_permission(self.copy_jurisdiction_locator,
                                                             u'一级监控者', permission_type1=self.picking_goods_locator,
                                                             permission_type2=self.print_receipt_locator,
                                                             permission_type3=self.procurement_planning_locator)
        permissions_199236_after2 = view_permissions(participant=self.admin, role_type='31')  # 复制权限后获取一级监控者的权限
        # permissions_199276_after2 = view_permissions(participant='199276', role_type='32')  # 被移交人的监控者权限
        # assert permissions_199236_before == permissions_199236_after2  # 经过复制分配后，一级监控者权限均不变
        print('一级监控者复制权限给用户199276')

        # 普通监控者199276移交权限
        self.driver.quit()  # 退出重新登录被分配的用户
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username='199276')  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        sleep(2)
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '监控者授权']):
            CardPage(self.driver).monitor_authorization_card()  # 进入监控者授权
        sleep(1)
        # 移交权限:拿取容器,质检,下采购单,选择阿瑟用户
        self.monitor_authorization_instant2 = MonitorAuthorization(self.driver)
        self.monitor_authorization_instant2.page_factory()
        self.monitor_authorization_instant2.assign_permission(self.transfer_jurisdiction_locator,
                                                              u'阿瑟', permission_type1=self.take_container_locator,
                                                              permission_type2=self.quality_testing_locator,
                                                              permission_type3=self.purchase_order_locator)
        permissions_199276_after3 = view_permissions(participant='199276', role_type='31')  # 移交权限后获取普通监控者的权限
        permissions_1111111002_after = view_permissions(participant='1111111002', role_type='32')  # 被移交人的监控者权限

        # assert u'拿取容器'.encode('utf-8') not in permissions_199276_after3 and u'质检'.encode('utf-8') \
        #         not in permissions_199276_after3 and u'下采购单'.encode('utf-8') not in permissions_199276_after3 \
        #        and set(self.tmp).issubset(set(permissions_1111111002_after)) is True  # sql判断权限是否移交出去
        print('普通监控者199276移交权限给1111111002')

        # 普通监控者199276复制权限
        CardPage(self.driver).click_card_one()  # 卡片1
        CardPage(self.driver).monitor_authorization_card()  # 进入监控者授权
        # 判断拿取容器、质检、下采购单是否还在
        assert is_element_present(self.driver, self.take_container_locator) is False and \
               is_element_present(self.driver, self.quality_testing_locator) is False and \
               is_element_present(self.driver, self.purchase_order_locator) is False

        # 复制权限:拣选商品,打印入库单,采购计划,选择阿瑟用户
        self.monitor_authorization_instant2.assign_permission(self.copy_jurisdiction_locator,
                                                              u'阿瑟', permission_type1=self.picking_goods_locator,
                                                              permission_type2=self.print_receipt_locator,
                                                              permission_type3=self.procurement_planning_locator)

        permissions_199276_after4 = view_permissions(participant='199276', role_type='31')  # 复制权限后获取普通监控者的权限+

        assert permissions_199276_after3 == permissions_199276_after4
        print('普通监控者199276复制权限给1111111002')

        # 普通监控者 1111111002登陆查看卡片和权限
        self.driver.quit()  # 退出重新登录被分配的用户
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username='1111111002')  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        sleep(3)
        while is_element_present(self.driver, ('ACCESSIBILITY_ID', 'icon back')):
            get_element(self.driver, ('ACCESSIBILITY_ID', 'icon back')).click()  # 不稳定，有时候会跳转进具体卡片，而不是桌面

        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '监控者授权']) is True:
            CardPage(self.driver).monitor_authorization_card()  # 进入监控者授权

        assert is_element_present(self.driver, self.take_container_locator) is True and \
               is_element_present(self.driver, self.quality_testing_locator) is True and \
               is_element_present(self.driver, self.purchase_order_locator) is True and \
               is_element_present(self.driver, self.picking_goods_locator) is True and \
               is_element_present(self.driver, self.print_receipt_locator) is True and \
               is_element_present(self.driver, self.copy_jurisdiction_locator) is True
        pass

    def FUN_ManagerAuthorization(self):  # 管理者授权
        # 普通监控者 1111111002登陆查看卡片和权限
        self.driver.quit()  # 退出重新登录被分配的用户
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=self.admin)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        # 一级管理者移交权限
        permissions_199236_before = view_permissions(participant=self.admin, role_type='21')  # 获取一级管理者的权限
        sleep(20)
        while is_element_present(self.driver, ('ACCESSIBILITY_ID', 'icon back')):
            get_element(self.driver, ('ACCESSIBILITY_ID', 'icon back')).click()  # 不稳定，有时候会跳转进具体卡片，而不是桌面

        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '管理者授权']):
            CardPage(self.driver).manager_authorization_card()  # 进入管理者授权

        # 移交权限:拿取容器,质检,下采购单,选择一级监控者用户
        self.monitor_authorization_instant3 = MonitorAuthorization(self.driver)
        self.monitor_authorization_instant3.page_factory()
        self.monitor_authorization_instant3.assign_permission(self.transfer_jurisdiction_locator,
                                                              u'一级监控者', permission_type1=self.take_container_locator,
                                                              permission_type2=self.quality_testing_locator,
                                                              permission_type3=self.purchase_order_locator)

        permissions_199236_after = view_permissions(participant=self.admin, role_type='21')  # 移交权限后获取一级管理者的权限
        permissions_199276_after = view_permissions(participant='199276', role_type='22')  # 被移交人的管理者权限
        self.tmp = [u'拿取容器'.encode('utf-8'), u'质检'.encode('utf-8'), u'下采购单'.encode('utf-8')]
        assert permissions_199236_before == permissions_199236_after and \
               set(self.tmp).issubset(set(permissions_199276_after)) is True  # 移交后，判断一级管理者和被分配者的权限
        print('一级管理者移交权限给用户199276')

        # 一级管理者复制权限
        CardPage(self.driver).click_card_one()  # 卡片1
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '管理者授权']):
            CardPage(self.driver).manager_authorization_card()  # 进入管理者授权

        # 复制权限:拣选商品,打印入库单,采购计划,选择一级监控者用户
        self.monitor_authorization_instant3.assign_permission(self.copy_jurisdiction_locator,
                                                              u'一级监控者', permission_type1=self.picking_goods_locator,
                                                              permission_type2=self.print_receipt_locator,
                                                              permission_type3=self.procurement_planning_locator)
        permissions_199236_after2 = view_permissions(participant=self.admin, role_type='21')  # 复制权限后获取一级管理者的权限
        # assert permissions_199236_before == permissions_199236_after2  # 经过复制分配后，一级管理者权限均不变，被分配者获取一级管理者所有权限
        print('一级管理者复制权限给用户199276')

        # 普通管理者199276移交权限
        self.driver.quit()  # 退出重新登录被分配的用户
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username='199276')  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        sleep(2)
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '管理者授权']):
            CardPage(self.driver).manager_authorization_card()  # 进入管理者授权

        sleep(1)
        # 移交权限:拿取容器,质检,下采购单,选择阿瑟用户
        self.monitor_authorization_instant4 = MonitorAuthorization(self.driver)
        self.monitor_authorization_instant4.page_factory()
        self.monitor_authorization_instant4.assign_permission(self.transfer_jurisdiction_locator,
                                                              u'阿瑟', permission_type1=self.take_container_locator,
                                                              permission_type2=self.quality_testing_locator,
                                                              permission_type3=self.purchase_order_locator)
        permissions_199276_after3 = view_permissions(participant='199276', role_type='21')  # 移交权限后获取普通管理者的权限
        permissions_1111111002_after = view_permissions(participant='1111111002', role_type='22')  # 被移交人的管理者权限

        # assert u'拿取容器'.encode('utf-8') not in permissions_199276_after3 and u'质检'.encode('utf-8') \
        #                                   not in permissions_199276_after3 and u'下采购单'.encode(
        #     'utf-8') not in permissions_199276_after3 \
        #        and set(self.tmp).issubset(set(permissions_1111111002_after)) is True  # sql判断权限是否移交出去
        print('普通管理者199276移交权限给1111111002')

        # 普通管理者199276复制权限权限
        CardPage(self.driver).click_card_one()  # 卡片1
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '管理者授权']):
            CardPage(self.driver).manager_authorization_card()  # 进入管理者授权
        # 判断拿取容器、质检、下采购单是否还在
        assert is_element_present(self.driver, self.take_container_locator) is False and \
               is_element_present(self.driver, self.quality_testing_locator) is False and \
               is_element_present(self.driver, self.purchase_order_locator) is False

        # 复制权限:拣选商品,打印入库单,采购计划,选择阿瑟用户
        self.monitor_authorization_instant4.assign_permission(self.copy_jurisdiction_locator,
                                                              u'阿瑟', permission_type1=self.picking_goods_locator,
                                                              permission_type2=self.print_receipt_locator,
                                                              permission_type3=self.procurement_planning_locator)

        permissions_199276_after4 = view_permissions(participant='199276', role_type='21')  # 复制权限后获取普通管理者的权限
        permissions_1111111002_after2 = view_permissions(participant='1111111002', role_type='22')  # 被移交人的管理者权限

        # assert permissions_199276_after3 == permissions_199276_after4  # 判断权限
        print('普通管理者199276复制权限给1111111002')

        # 普通管理者1111111002登陆查看卡片和权限
        self.driver.quit()  # 退出重新登录被分配的用户
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username='1111111002')  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        sleep(3)
        while is_element_present(self.driver, ('ACCESSIBILITY_ID', 'icon back')):
            get_element(self.driver, ('ACCESSIBILITY_ID', 'icon back')).click()  # 不稳定，有时候会跳转进具体卡片，而不是桌面
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '管理者授权']):
            CardPage(self.driver).manager_authorization_card()  # 进入管理者授权

        assert is_element_present(self.driver, self.take_container_locator) is True and \
               is_element_present(self.driver, self.quality_testing_locator) is True and \
               is_element_present(self.driver, self.purchase_order_locator) is True and \
               is_element_present(self.driver, self.picking_goods_locator) is True and \
               is_element_present(self.driver, self.print_receipt_locator) is True and \
               is_element_present(self.driver, self.procurement_planning_locator) is True
        pass

    def FUN_TaskHandover(self):
        reduction_non_service_certification_task()
        restore_card()
        reduction_task()
        self.driver.quit()  # 退出重新登录被分配的用户
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=self.user_id)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '非服务认证']):
            CardPage(self.driver).click_non_service_certification_card()  # 非服务认证
        self.swipe()
        sleep(2)
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', 'icon send']) is False:
            self.swipe()
        self.icon_send_ele = get_element(self.driver, self.icon_send_locator)
        self.icon_send_ele.click()
        get_element(self.driver, self.select_locator).send_keys(u'一级监控者')
        get_element(self.driver, self.select_locator).click()

        get_element(self.driver, self.forward_locator).click()  # 转发
        get_element(self.driver, self.hand_over_locator).click()  # 确认移交
        sleep(3)
        self.driver.quit()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username=self.invitee_id)  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '非服务认证']):
            CardPage(self.driver).click_non_service_certification_card()  # 非服务认证

        print('199270移交非服务认证任务给199276')
        pass

    def FUN_NonServiceCertification(self):
        get_element(self.driver, self.yes_locator).click()
        get_element(self.driver, self.audit_pass_locator).click()
        sleep(1)
        self.tmp2 = [u'拣选商品'.encode('utf-8'), u'打印入库单'.encode('utf-8'), u'下采购单'.encode('utf-8'), u'非服务认证'.encode('utf-8')]

        self.driver.quit()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        LoginPage(self.driver).login(username='199272')  # 登录
        CardPage(self.driver).click_card_one()  # 卡片1
        sleep(2)
        if is_element_present(self.driver, ['ACCESSIBILITY_ID', '管理者授权']):
            CardPage(self.driver).manager_authorization_card()

        assert is_element_present(self.driver, self.print_receipt_locator) is True and \
               is_element_present(self.driver, self.picking_goods_locator) is True and \
               is_element_present(self.driver, self.purchase_order_locator) is True
        print('199276认证通过，199272获取权限')

    def swipe(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width / 2, height * 3 / 7, width / 2, (height * 4 / 7), 1000)  # 下滑

    def get_ui_locator(self, driver):
        # 分配监控者和管理者页面
        self.dstribution_manager_and_supervisor_instant = DistributionManagerAndSupervisor(driver)
        self.dstribution_manager_and_supervisor_instant.page_factory()
        self.assigned_to_me_locator = self.dstribution_manager_and_supervisor_instant.assigned_to_me_locator  # 分配给我
        self.distribution_success_button_locator = self.dstribution_manager_and_supervisor_instant. \
            distribution_success_button_locator  # 分配成功

        # 监控者授权页面
        self.monitor_authorization_instant = MonitorAuthorization(driver)
        self.monitor_authorization_instant.page_factory()
        self.take_container_locator = self.monitor_authorization_instant.take_container_locator  # 拿取容器
        self.picking_goods_locator = self.monitor_authorization_instant.picking_goods_locator  # 拣选商品
        self.quality_testing_locator = self.monitor_authorization_instant.quality_testing_locator  # 质检
        self.print_receipt_locator = self.monitor_authorization_instant.print_receipt_locator  # 打印入库单
        self.purchase_order_locator = self.monitor_authorization_instant.purchase_order_locator  # 下采购单
        self.procurement_planning_locator = self.monitor_authorization_instant.procurement_planning_locator  # 采购计划
        self.copy_jurisdiction_locator = self.monitor_authorization_instant.copy_jurisdiction_locator  # 复制权限
        self.transfer_jurisdiction_locator = self.monitor_authorization_instant.transfer_jurisdiction_locator  # 移交权限
        self.do_not_want_to_assign_button_locator = self.monitor_authorization_instant. \
            do_not_want_to_assign_button_locator  # 不想分配
        self.sure_assign_button_locator = self.monitor_authorization_instant.sure_assign_button_locator  # 确认分配

        # 通讯录页面
        self.mail_list_instant = MailListPage(driver)
        self.mail_list_instant.page_factory()
        self.search_locator = self.mail_list_instant.search_locator  # 搜索
        self.assign_locator = self.mail_list_instant.assign_locator  # 分配
        self.invite_and_assign_locator = self.mail_list_instant.invite_and_assign_locator  # 邀请并分配

        #  移交任务，认证
        self.task_handover_instant = TaskHandoverPage(driver)
        self.task_handover_instant.page_factory()
        self.icon_send_locator = self.task_handover_instant.icon_send_locator  # icon_send
        self.select_locator = self.task_handover_instant.select_locator  #
        self.forward_locator = self.task_handover_instant.forward_locator  # 转发
        self.don_hand_over_locator = self.task_handover_instant.don_hand_over_locator  # 不想移交
        self.phone_locator = self.task_handover_instant.phone_locator  # 电话
        self.hand_over_locator = self.task_handover_instant.hand_over_locator  # 确认移交
        self.yes_locator = self.task_handover_instant.yes_locator  #
        self.audit_pass_locator = self.task_handover_instant.audit_pass_locator  # 确认移交