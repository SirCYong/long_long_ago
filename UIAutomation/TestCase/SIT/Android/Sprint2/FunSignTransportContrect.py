from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.SignContractCarriage.SignContractCarriagePage import SignContractCarriage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from .FunSignTransportContrectSQL import reduction_transport_contract, get_new_transport_contract, delete_transport_contract

__author__ = 'zhoujin'


class FunSignTransportContract(BaseTestCase):
    """
        签订运输供应契约
        先生成一个运输供应的契约,然后签订该契约
    """
    def setUp(self):
        delete_transport_contract()
        reduction_transport_contract()
        self.user_id = 10001476
        mobile = 15711041212
        password = 123456
        BaseTestCase.setUp(self)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_TransportContract(self):
        LongCardPage(self.driver).click_expected_card(10001476, '找运输供应')
        signed_carriage_supply_contract_instant = SignContractCarriage(self.driver)
        signed_carriage_supply_contract_instant.page_factory()
        # 签订运输契约
        signed_carriage_supply_contract_instant.click_the_first_carriage_card()  # 点击第一个卡片
        signed_carriage_supply_contract_instant.choice_amount_and_submit(is_choice=0)  # 全选并提交

        new_transport_contract = get_new_transport_contract(self.user_id, contract_ukid='51817000000009223')
        new_transport_contract_no = int(new_transport_contract['new_transport_contract_no'])
        operation_record_no = int(new_transport_contract['operation_record_no'])
        rs_repository_no = int(new_transport_contract['rs_repository_no'])
        print(new_transport_contract_no, rs_repository_no, operation_record_no)
        assert new_transport_contract_no * 2 == rs_repository_no == operation_record_no * 2
        print('签订运输供应契约成功')
        # 签订运输契约
        signed_carriage_supply_contract_instant.click_the_first_carriage_card()  # 点击第一个卡片
        signed_carriage_supply_contract_instant.choice_amount_and_submit()  # 全选并提交

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
