from time import sleep

from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.SignContractCarriage.SignContractCarriagePage import SignContractCarriage
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.iOS.Sprint2.FunSignTransportContrectSQL import reduction_transport_contract, \
    get_new_transport_contract, delete_transport_contract

__author__ = 'chenyanxiu'


class FunSignTransportContrect(BaseTestCase):
    """
        签订运输需求契约
        先生成一个运输需求的契约,然后签订该契约
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        self.user_id = 10001476
        mobile = 15711041212
        password = 123456
        self.supply_id = 10001476
        self.tr_participant_ukid = 10001476
        delete_transport_contract(self.user_id, self.tr_participant_ukid)
        reduction_transport_contract()  # 还原运输供应契约
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_TransportContract(self):
        LongCardPage(self.driver).click_expected_card(10001476, '找运输供应')
        signed_carriage_supply_contract_instant = SignContractCarriage(self.driver)
        signed_carriage_supply_contract_instant.page_factory()
        signed_carriage_supply_contract_instant.assert_tr()  # 判断第一张卡片
        # 签订运输契约
        signed_carriage_supply_contract_instant.click_the_first_carriage_card()  # 点击第一个卡片
        signed_carriage_supply_contract_instant.tr_judgment()  # 判断详细内容
        signed_carriage_supply_contract_instant.choice_amount_and_submit(is_choice=0)  # 提交一个
        sleep(4)
        new_transport_contract = get_new_transport_contract(self.user_id, contract_ukid='51817000000009223')
        new_transport_contract_no = int(new_transport_contract['new_transport_contract_no'])
        operation_record_no = int(new_transport_contract['operation_record_no'])
        rs_repository_no = int(new_transport_contract['rs_repository_no'])
        print(new_transport_contract_no, rs_repository_no, operation_record_no)
        assert new_transport_contract_no * 2 == rs_repository_no == operation_record_no * 2
        signed_carriage_supply_contract_instant.click_the_first_carriage_card()  # 点击第一个卡片
        signed_carriage_supply_contract_instant.choice_amount_and_submit()  # 全选并提交
        sleep(3)
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

