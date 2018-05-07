from time import sleep

from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_user_id
from UIAutomation.Utils.HttpWrapper import eject_logged_user
from .FunSmoke014SQL import reduction_transport_contract, get_new_transport_contract, delete_transport_contract
from UIAutomation.Page.Mobile.iOS.ContractCarriage.ContractCarriagePage import ContractCarriage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
__author__ = 'zhoujin'


class FunSmoke014(BaseTestCase):
    """
        签订运输供应契约
        先生成一个运输供应的契约,然后签订该契约
    """
    def setUp(self):
        delete_transport_contract()
        reduction_transport_contract()  # 还原运输供应契约
        mobile = 15711041212
        password = 123456
        self.user_id = get_user_id(mobile)
        BaseTestCase.setUp(self)
        # eject_logged_user(mobile, password)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_TransportContract(self):
        LongCardPage(self.driver).click_expected_card(self.user_id, '找运输供应')
        signed_carriage_supply_contract_instant = ContractCarriage(self.driver)
        signed_carriage_supply_contract_instant.page_factory()
        # 签订运输契约
        signed_carriage_supply_contract_instant.click_the_first_carriage_card()  # 点击第一个卡片
        signed_carriage_supply_contract_instant.choice_amount_and_submit()  # 全选并提交
        sleep(2)
        new_transport_contract = get_new_transport_contract(self.user_id, contract_ukid='51817000000009223')
        new_transport_contract_no = int(new_transport_contract['new_transport_contract_no'])
        operation_record_no = int(new_transport_contract['operation_record_no'])
        rs_repository_no = int(new_transport_contract['rs_repository_no'])
        print(new_transport_contract_no, rs_repository_no, operation_record_no)
        assert new_transport_contract_no * 2 == rs_repository_no == operation_record_no * 2
        print('签订运输供应契约成功')

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass
