from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.iOS.SignLaborContract.SignLaborContractPage import SignLaborContract
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.iOS.Sprint2.FUNSignLaborSupplyContractSQL import reduction_labor_contract, \
    get_labor_contract_info, get_new_labor_contract, delete_labor_contract, get_labor_contract_ukid
from UIAutomation.Utils.Element import get_element


class FUNSignLaborSupplyContract(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        self.user_id = 10001465
        mobile = 15356563538
        password = 123456
        self.la_participant_ukid = 10001465
        reduction_labor_contract()  # 还原劳务契约
        delete_labor_contract(self.user_id, self.la_participant_ukid)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        self.get_ui_locator(self.driver)
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

    def test_SignLaborSupplyContract(self):
        self.no_hour = '29'
        self.no_piece = '0.95'
        self.no = '2'
        self.type = '包装'
        self.shift = '白班'
        self.unit_hour1 = '元/小时'
        self.unit_hour = '计时 (元/小时)'
        self.unit_piece = '计件 (元/件)'
        self.position = '海南省三沙市中沙群岛的岛礁及其海域'
        self.start_time = '2018/12/23'
        self.end_time = '2018/12/23'
        LongCardPage(self.driver).click_expected_card(10001465, '找劳务需求')
        # 判断第一个卡片的信息
        signed_labor_demand_contract_instant = SignLaborContract(self.driver)
        signed_labor_demand_contract_instant.page_factory()
        labor_contract_info = get_labor_contract_info(self.la_participant_ukid)
        print(labor_contract_info)
        start_time2 = '开始: ' + self.start_time
        end_time2 = '结束: ' + self.end_time

        assert get_element(self.driver, self.la_type_locator).text == self.type  # 判断工种
        assert get_element(self.driver, self.la_no_locator).text == self.no_hour   # 判断价钱
        assert get_element(self.driver, self.la_unit_locator).text == self.unit_hour1  # 判断计算单位
        assert get_element(self.driver, self.la_start_time_locator).text == start_time2  # 判断开始时间
        assert get_element(self.driver, self.la_end_time_locator).text == end_time2  # 判断结束时间

        # 下面属于page的内容
        get_element(self.driver, self.la_unit_locator).click()
        sleep(1)

        self.assert_la()
        self.position1 = '位置'
        assert self.position1 == get_element(self.driver, self.position_locator).text

        # 点击报名
        signed_labor_demand_contract_instant.think_more()
        signed_labor_demand_contract_instant.choice_amount_and_submit()  # 报名参加
        labor_contract_info = get_labor_contract_info(self.la_participant_ukid)
        status = str(labor_contract_info['status'])
        assert status == '20'
        sleep(2)
        new_labor_contract = get_new_labor_contract(self.user_id)
        print(new_labor_contract)
        new_labor_contract_no = int(new_labor_contract['new_labor_contract_no'])
        operation_record_no = int(new_labor_contract['operation_record_no'])
        rs_repository_no = int(new_labor_contract['rs_repository_no'])

        print(new_labor_contract_no, rs_repository_no, operation_record_no)
        assert new_labor_contract_no * 2 == rs_repository_no == operation_record_no * 2

        get_element(self.driver, self.la_unit_locator).click()
        sleep(1)
        get_element(self.driver, self.enter_for_locator).click()
        get_element(self.driver, self.enter_me_locator).click()
        sleep(2)
        labor_contract_info = get_labor_contract_info(self.la_participant_ukid)
        status = str(labor_contract_info['status'])
        assert status == '30'  # 判断状态
        labor_contract1 = get_labor_contract_ukid(self.user_id, self.la_participant_ukid)
        print(labor_contract1)
        new_labor_contract = get_new_labor_contract(self.user_id)
        new_labor_contract_no = int(new_labor_contract['new_labor_contract_no'])
        operation_record_no = int(new_labor_contract['operation_record_no'])
        rs_repository_no = int(new_labor_contract['rs_repository_no'])
        assert new_labor_contract_no * 2 == rs_repository_no == operation_record_no * 2
        pass

    def assert_la(self):
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.no]).text == self.no  # 判断数量
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.no_hour]).text == self.no_hour
        # 判断时间价钱
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.no_piece]).text == self.no_piece
        # 判断件价钱
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.unit_hour]).text == self.unit_hour
        # 判断时间单位
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.unit_piece]).text == self.unit_piece
        # 判断件单位
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.type]).text == self.type  # 判断工种
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.shift]).text == self.shift  # 判断班次
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.position]).text == self.position
        # 判断地址
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.start_time]).text == self.start_time
        # 判断开始时间
        assert get_element(self.driver, ['ACCESSIBILITY_ID', self.end_time]).text == self.end_time
        # 判断结束时间

    def get_ui_locator(self, driver):
        # 生成劳务需求页面
        self.sign_labor_contract_instant = SignLaborContract(driver)
        self.sign_labor_contract_instant.page_factory()
        self.la_card_picking_locator = self.sign_labor_contract_instant.la_card_picking_locator  # 拣选员
        self.la_card_shelve_locator = self.sign_labor_contract_instant.la_card_shelve_locator  # 上架员
        self.la_card_packing_locator = self.sign_labor_contract_instant.la_card_packing_locator  # 包装员
        self.la_card_transfer_locator = self.sign_labor_contract_instant.la_card_transfer_locator  # 交接员
        self.position_locator = self.sign_labor_contract_instant.position_locator  # 位置
        self.enter_for_locator = self.sign_labor_contract_instant.enter_for_locator  # 报名参加
        self.enter_me_locator = self.sign_labor_contract_instant.enter_me_locator  # 我参加
        self.return_map_locator = self.sign_labor_contract_instant.return_map_locator  # 返回
        self.la_type_locator = self.sign_labor_contract_instant.la_type_locator  # 判断工种
        self.la_no_locator = self.sign_labor_contract_instant.la_no_locator  # 判断价钱
        self.la_unit_locator = self.sign_labor_contract_instant.la_unit_locator  # 判断计算单位
        self.la_start_time_locator = self.sign_labor_contract_instant.la_start_time_locator  # 判断开始时间
        self.la_end_time_locator = self.sign_labor_contract_instant.la_end_time_locator  # 判断结束时间
        self.think_locator = self.sign_labor_contract_instant.think_locator  # 再考虑


