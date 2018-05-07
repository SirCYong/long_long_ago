# -*- coding: utf-8 -*-
from time import sleep
from hamcrest import *
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.SignedWarehousingSupplyContract.SignedWarehousingContractPage import \
    SignedWarehousingSupplyContract
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.Keywords import EatToast
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke015_016SQL import reduction_warehouse_demand_contract, \
    get_warehouse_sign_result
from UIAutomation.Utils.HttpWrapper import eject_logged_user

__author__ = 'zhongchangwei'
__package__ = 'IscsUIAutomation'


class FunFindWarehouseDemandSmokeTest(BaseTestCase):
    """
        预先创建了两个仓储需求契约:分别为地产契约和仓储契约,
        并修改创建时间时间,让他们排在最前面,然后签订完成两个契约
    """
    def setUp(self):
        reduction_warehouse_demand_contract()

        mobile = 13788883333
        password = 123456
        BaseTestCase.setUp(self)
        # 顶出已经登录的用户

        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

    def test_sign_warehouse_demand_success(self):
        LongCardPage(self.driver).click_expected_card(10001394, '找仓储需求')
        signed_warehousing_supply_contract_instant = SignedWarehousingSupplyContract(self.driver)
        signed_warehousing_supply_contract_instant.page_factory()
        # 签订地产类型的契约
        signed_warehousing_supply_contract_instant.click_the_first_warehouse_card(contract_type='DEMAND')
        signed_warehousing_supply_contract_instant.choice_amount_and_submit(contract_type='DEMAND')  # 全选并提交
        sleep(5)
        result_dic2 = get_warehouse_sign_result(51817200000010012, contract_ascription='DEMAND', user_id=10001394)
        assert_that(result_dic2, has_key('get_new_contract_no'))
        assert_that(result_dic2, has_key('rs_repository_no'))
        assert_that(result_dic2, has_key('log_no'))
        assert_that(result_dic2, has_key('contract_status'))
        assert_that(result_dic2, has_key('contract_no'))
        sleep(1)
        # 签订仓储类型的契约
        signed_warehousing_supply_contract_instant.click_the_first_warehouse_card(contract_type='DEMAND', rs_type='WA')
        signed_warehousing_supply_contract_instant.choice_amount_and_submit(contract_type='DEMAND')  # 全选并提交
        sleep(5)
        result_dic = get_warehouse_sign_result(51817200000010012,
                                               contract_ascription='DEMAND', user_id=10001394, type='WA')
        # sql判断结果
        assert result_dic['get_new_contract_no'] == 2 and result_dic['rs_repository_no'] == 4 and result_dic['log_no'] \
            == 2 and result_dic['contract_status'] == '30' and result_dic['contract_no'] == 0

        print('签订仓储需求契约成功')
