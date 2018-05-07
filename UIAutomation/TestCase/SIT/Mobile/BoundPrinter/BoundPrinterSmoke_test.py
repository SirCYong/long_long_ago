from time import sleep
from UIAutomation.Page.Mobile.BoundPrinter.BoundPrinterPage import BoundPrinter
from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.TestCase.SIT.Mobile.BoundPrinter.BoundPrinterSQL import delete_bound_printer, get_bound_printer_info

__author__ = "zhongchangwei"
__package__ = 'IscsUIAutomation'


class BoundPrinterSmokeSmoke(BaseTestCase):
    """
        预先创建了两个仓储供应契约:分别为地产契约和仓储契约,
        并修改创建时间时间,让他们排在最前面,然后签订完成两个契约
    """
    def setUp(self):
        mobile = 13766663333
        password = 123456
        delete_bound_printer()    # 删除绑定记录
        BaseTestCase.setUp(self)
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

    def test_DistributionManagerAndSupervisor(self):
        code = '1000144400001'
        LongCardPage(self.driver).click_expected_card(10001646, '补打快递单')
        sleep(1)
        bound_printer_instant = BoundPrinter(self.driver)
        bound_printer_instant.page_factory()
        bound_printer_instant.bound_printer(code)
        sleep(2)
        assert str(get_bound_printer_info()) == '1000144400001'

