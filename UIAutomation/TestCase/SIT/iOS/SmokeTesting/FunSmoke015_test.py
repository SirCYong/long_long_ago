from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.SignedWarehousingSupplyContract.SignedWarehousingContractPage import \
    SignedWarehousingSupplyContract
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils.HttpWrapper import eject_logged_user
from .FunSmoke015_016SQL import reduction_warehouse_supply_contract, get_warehouse_sign_result

__author__ = "zhongchangwei"
__package__ = 'IscsUIAutomation'


class SitSprintFull001(BaseTestCase):
    """
        预先创建了两个仓储供应契约:分别为地产契约和仓储契约,
        并修改创建时间时间,让他们排在最前面,然后签订完成两个契约
    """
    def setUp(self):
        reduction_warehouse_supply_contract()  # 还原仓储供应卡片
        mobile = 13788883333
        password = 123456
        BaseTestCase.setUp(self)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

    def test_DistributionManagerAndSupervisor(self):
        LongCardPage(self.driver).click_expected_card(10001394, '找仓储供应')
        sleep(3)
        signed_warehousing_supply_contract_instant = SignedWarehousingSupplyContract(self.driver)
        signed_warehousing_supply_contract_instant.page_factory()
        # 签订地产类型的契约
        signed_warehousing_supply_contract_instant.click_the_first_warehouse_card(rs_type='WA')  # 点击第一个卡片
        sleep(3)
        signed_warehousing_supply_contract_instant.choice_amount_and_submit()  # 全选并提交
        sleep(5)
        result_dic = get_warehouse_sign_result(51817100000010009, user_id=10001394, type='WA')
        # sql判断结果
        assert result_dic['get_new_contract_no'] == 2 and result_dic['rs_repository_no'] == 4 \
            and result_dic['log_no'] == 1 and result_dic['contract_status'] == '20' and \
            result_dic['contract_no'] == 0

        sleep(7)
        # 签订仓储类型的契约
        signed_warehousing_supply_contract_instant.click_the_first_warehouse_card()  # 点击第一个卡片
        signed_warehousing_supply_contract_instant.choice_amount_and_submit()  # 全选并提交
        sleep(5)
        result_dic2 = get_warehouse_sign_result(51817100000010009, user_id=10001394)
        assert result_dic2['get_new_contract_no'] == 1 and result_dic2['rs_repository_no'] == 2 \
            and result_dic2['log_no'] == 2 and result_dic2['contract_status'] == '30' and \
            result_dic['contract_no'] == 0
        print('签订仓储供应契约成功')
