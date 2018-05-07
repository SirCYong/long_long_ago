from time import sleep

from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from .FUNSignLaborSupplyContractSQL import reduction_labor_contract, get_new_labor_contract, get_labor_contract_info, \
    delete_labor_contract

from UIAutomation.Page.Mobile.Android.SignLaborContract.SignLaborContractPage import SignLaborContract
__author__ = 'chenyanxiu'


class FUNSignLaborSupplyContract(BaseTestCase):
    """
        签订劳务需求契约
        先生成一个劳务需求的契约,然后签订该契约
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        self.la_participant_ukid = 10001465
        self.user_id = 10001465
        mobile = 15356563538
        password = 123456
        delete_labor_contract(self.user_id, self.la_participant_ukid)
        reduction_labor_contract()  # 还原劳务契约
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_SignLaborSupplyContract(self):
        LongCardPage(self.driver).click_expected_card(10001465, '找劳务需求')
        sleep(3)
        signed_labor_demand_contract_instant = SignLaborContract(self.driver)
        signed_labor_demand_contract_instant.page_factory()
        # 签订劳务契约
        signed_labor_demand_contract_instant.click_the_first_labor_card()  # 点击第一个卡片
        signed_labor_demand_contract_instant.choice_amount_and_submit()  # 报名参加

        labor_contract_info = get_labor_contract_info(self.la_participant_ukid)
        status = str(labor_contract_info['status'])
        assert status == '20'
        sleep(5)
        new_labor_contract = get_new_labor_contract(self.user_id)
        print(new_labor_contract)
        new_labor_contract_no = int(new_labor_contract['new_labor_contract_no'])
        operation_record_no = int(new_labor_contract['operation_record_no'])
        rs_repository_no = int(new_labor_contract['rs_repository_no'])

        print(new_labor_contract_no, rs_repository_no, operation_record_no)
        assert new_labor_contract_no * 2 == rs_repository_no == operation_record_no * 2
        print('签订劳务需求契约成功')
        # 签订完成劳务契约
        signed_labor_demand_contract_instant.click_the_first_labor_card_twice()  # 点击第一个卡片
        signed_labor_demand_contract_instant.choice_amount_and_submit()  # 报名参加
        sleep(2)
        new_labor_contract = get_new_labor_contract(self.user_id, contract_ukid='51817000000010130')
        new_labor_contract_no = int(new_labor_contract['new_labor_contract_no'])
        operation_record_no = int(new_labor_contract['operation_record_no'])
        rs_repository_no = int(new_labor_contract['rs_repository_no'])
        print(new_labor_contract_no, rs_repository_no, operation_record_no)
        assert new_labor_contract_no * 2 == rs_repository_no == operation_record_no * 2

        labor_contract_info = get_labor_contract_info(self.la_participant_ukid)
        status = str(labor_contract_info['status'])
        assert status == '30'  # 判断状态
        print('签订劳务需求契约成功')

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass

