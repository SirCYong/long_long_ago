from time import sleep

from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Page.Mobile.iOS.LoginPage import LoginPage
from UIAutomation.Page.Mobile.iOS.SignLaborContract.SignLaborContractPage import SignLaborContract
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.TestCase.Keywords import EatToast
from UIAutomation.TestCase.SIT.iOS.SmokeTesting.FunSmoke013SQL import delete_labor_contract, reduction_labor_contract, \
    get_new_labor_contract
from UIAutomation.Utils import get_user_id
from UIAutomation.Utils.HttpWrapper import eject_logged_user

__author__ = 'zhoujin'


class FunSmoke013(BaseTestCase):
    """
        签订劳务需求契约
        先生成一个劳务需求的契约,然后签订该契约
    """
    def setUp(self):
        delete_labor_contract()
        reduction_labor_contract()     # 还原劳务契约
        mobile = 17630301114
        password = 123456
        self.user_id = get_user_id(mobile)
        BaseTestCase.setUp(self)
        # eject_logged_user(mobile, password)
        sleep(12)
        # self.driver.find_element_by_accessibility_id('我知道了').click()
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        # EatToast(self.driver, '您的账号在别的地方登录', '我知道了').eat_toast()
        # sleep(10)
        # self.driver.find_element_by_accessibility_id('我知道了').click()
        LoginPage(self.driver).login(username=mobile, password=password)
        LongCardPage(self.driver).click_expected_card(self.user_id, '找劳务需求')
        pass

    def test_LaborContract(self):
        # LongCardPage(self.driver).click_expected_card(self.user_id, '找劳务需求')
        signed_labor_demand_contract_instant = SignLaborContract(self.driver)
        signed_labor_demand_contract_instant.page_factory()
        # 签订劳务契约
        signed_labor_demand_contract_instant.click_the_first_labor_card()  # 点击第一个卡片
        signed_labor_demand_contract_instant.choice_amount_and_submit()  # 全选并提交
        sleep(2)
        new_labor_contract = get_new_labor_contract(self.user_id, contract_ukid='51817000000010130')
        new_labor_contract_no = int(new_labor_contract['new_labor_contract_no'])
        operation_record_no = int(new_labor_contract['operation_record_no'])
        rs_repository_no = int(new_labor_contract['rs_repository_no'])
        print(new_labor_contract_no, rs_repository_no, operation_record_no)
        assert new_labor_contract_no * 2 == rs_repository_no == operation_record_no * 2
        print('签订劳务需求契约成功')

    def tearDown(self):
        BaseTestCase.tearDown(self)
        pass


