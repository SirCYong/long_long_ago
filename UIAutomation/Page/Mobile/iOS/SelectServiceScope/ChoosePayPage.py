from selenium.common.exceptions import NoSuchWindowException

from time import sleep

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage
__auhtor__ = 'liyu'


class ChoosePayPage(BasePage):
    """
    选择支付页面
    银联测试账号：6216261000000000018   证件号码：341126197709218366    短信验证码：123456（必须先点击获取验证码）
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.ALIPAY_element = None
        self.UnionPay_element = None
        self.ToPay_element = None
        try:
            self.is_loaded()
            self.initial_element()
        except ParseXmlErrorException:
            assert False

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
        pass

    def page_factory(self):
        name_list = ['ALIPAY','UnionPay','ToPay']
        ele_dic = page_element_factory(__file__, name_list)
        self.ALIPAY_element = get_element(self.driver, ele_dic['ALIPAY'])     #支付宝
        self.UnionPay_element = get_element(self.driver, ele_dic['UnionPay'])       #银联
        self.ToPay_element = get_element(self.driver, ele_dic['ToPay'])       #去支付
        pass

    def click_alipay(self):
        self.ALIPAY_element.click()
        self.ToPay_element.click()
        print('支付宝支付成功')
        pass

    def click_union_pay(self):
        self.UnionPay_element.click()
        self.ToPay_element.click()
        # 支付有时候会返回支付失败
        sleep(5)
        try:
            self.ToPay_element.click()
        except:
            pass
        print('银联支付成功')
        pass



    def is_loaded(self):
        pass
