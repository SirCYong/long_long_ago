from UIAutomation.TestCase.BaseTestCase import BaseTestCase
# from .FunSmoke013SQL import reduction_labor_contract, get_new_labor_contract
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.SignLaborContract.SignLaborContractPage import SignLaborContract
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
__author__ = 'zhoujin'


class FunSmoke013(BaseTestCase):
    """
        签订劳务需求契约
        先生成一个劳务需求的契约,然后签订该契约
    """
    def setUp(self):
        # reduction_labor_contract()     # 还原劳务契约
        self.user_id = 10001474
        mobile = 15624301115
        password = 123456
        BaseTestCase.setUp(self)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_LaborContract(self):
        LongCardPage(self.driver).click_expected_card(10001474, '管理业务单位')
        # signed_labor_demand_contract_instant = SignLaborContract(self.driver)
        # signed_labor_demand_contract_instant.page_factory()
        # # 签订劳务契约
        # signed_labor_demand_contract_instant.click_the_first_labor_card()  # 点击第一个卡片
        # signed_labor_demand_contract_instant.choice_amount_and_submit()  # 全选并提交
        # new_labor_contract = get_new_labor_contract(self.user_id, contract_ukid='51817400000009165')
        # new_labor_contract_no = int(new_labor_contract['new_labor_contract_no'])
        # operation_record_no = int(new_labor_contract['operation_record_no'])
        # rs_repository_no = int(new_labor_contract['rs_repository_no'])
        # print(new_labor_contract_no, rs_repository_no, operation_record_no)
        # assert new_labor_contract_no * 2 == rs_repository_no == operation_record_no * 2
        # print('签订劳务需求契约成功')

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass


