from time import sleep

from UIAutomation.Page.Mobile.ExitAppPage import ExitAppPage
from UIAutomation.Page.Mobile.LoginPage import LoginPage
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.ReturnGoods.ReturnGoodsPage import ReturnGoods
from UIAutomation.TestCase.BaseTestCase import BaseTestCase
from UIAutomation.Utils import get_user_id
from .ReturnGoodsSQL import delete_return_goods, get_return_goods
__author__ = 'zhoujin'


class ReturnGoodsTest(BaseTestCase):
    """
      申请退货，按订单号退货
        已经手机下单
    """
    def setUp(self):
        BaseTestCase.setUp(self)
        mobile = 18555090070
        password = 123456
        self.user_id = get_user_id(mobile)
        delete_return_goods(self.user_id)  # 还原申请退货数据
        LoginPage(self.driver).login(username=mobile, password=password)  # 登录
        pass

    def test_return_goods(self):
        LongCardPage(self.driver).click_expected_card(self.user_id, '申请退货')
        sleep(3)
        ReturnGoods(self.driver).return_goods()
        ReturnGoods(self.driver).submit()
        sleep(3)
        new_return_goods = get_return_goods(self.user_id)
        recovery_record_no = (new_return_goods['recovery_record_no'])
        print(recovery_record_no)
        assert recovery_record_no == '公明提交了退货申请. 订单号:51860400000008034'
        print("申请退货成功！")

    def tearDown(self):
        ExitAppPage(self.driver).logout_app()
        BaseTestCase.tearDown(self)
        pass

