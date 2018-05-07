from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, sleep

__author__ = 'zhoujin'


class ReturnGoods(BasePage):
    """
    申请退货
    假定已经手机下单过
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver_locator = driver
        self.order_number_locator = None
        self.number_locator = None
        self.first_locator = None
        self.mode_locator = None
        self.reject_locator = None
        self.sure_locator = None
        self.add_number_locator = None
        self.select_all_locator = None
        self.return_goods_locator = None
        self.confirm_locator = None
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
        name_list = ['order_number', 'number', 'first', 'mode', 'reject', 'sure', 'add_number',
                     'select_all', 'return_goods', 'confirm']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.order_number_locator = ele_dic['order_number']
        self.number_locator = ele_dic['number']
        self.first_locator = ele_dic['first']
        self.mode_locator = ele_dic['mode']
        self.reject_locator = ele_dic['reject']
        self.sure_locator = ele_dic['sure']
        self.add_number_locator = ele_dic['add_number']
        self.select_all_locator = ele_dic['select_all']
        self.return_goods_locator = ele_dic['return_goods']
        self.confirm_locator = ele_dic['confirm']

    def is_loaded(self):
        pass

    def return_goods(self):
        if self.is_run_ios():
            self._return_goods_ios()
        else:
            self._return_goods_android()

    def _return_goods_ios(self):
        """
        申请退货
        IOS端
        """
        self.action.click(self.order_number_locator)
        get_element(self.driver, self.number_locator).set_values('51860400000008034')
        self.action.click(self.select_all_locator)
        self.action.click(self.select_all_locator)
        self.action.click(self.first_locator)
        self.action.click(self.mode_locator)
        self.action.click(self.reject_locator)
        self.action.click(self.sure_locator)
        self.action.click(self.return_goods_locator)
        self.action.click(self.confirm_locator)

    def _return_goods_android(self):
        """
        申请退货
        安卓端
        """
        self.action.click(self.order_number_locator)
        get_element(self.driver, self.number_locator).send_keys('51860400000008034')
        self.driver.keyevent(66)
        self.action.click(self.select_all_locator)
        self.action.click(self.select_all_locator)
        self.action.click(self.first_locator)
        self.action.click(self.mode_locator)
        self.action.click(self.reject_locator)
        self.action.click(self.sure_locator)
        self.action.click(self.return_goods_locator)
        self.action.click(self.confirm_locator)

    def return_goods_two(self):
        if self.is_run_ios():
            self._return_goods_two_ios()
        else:
            self._return_goods_two_android()

    def _return_goods_two_ios(self):
        """
        申请退货
        IOS端
        """
        self.action.click(self.order_number_locator)
        get_element(self.driver, self.number_locator).set_values('51860400000008034')
        self.action.click(self.select_all_locator)
        self.action.click(self.select_all_locator)
        self.action.click(self.first_locator)
        self.action.click(self.mode_locator)
        self.action.click(self.reject_locator)
        self.action.click(self.sure_locator)
        self.action.click(self.return_goods_locator)
        self.action.click(self.confirm_locator)

    def _return_goods_two_android(self):
        """
        申请退货
        安卓端
        """
        self.action.click(self.order_number_locator)
        get_element(self.driver, self.number_locator).send_keys('12045690031')
        self.driver.keyevent(66)
        self.action.click(self.select_all_locator)
        self.action.click(self.select_all_locator)
        self.action.click(self.first_locator)
        self.action.click(self.mode_locator)
        self.action.click(self.reject_locator)
        self.action.click(self.sure_locator)
        self.action.click(self.return_goods_locator)
        self.action.click(self.confirm_locator)

    def submit(self):
        if self.is_run_ios():
            self._submit_ios()
        else:
            self._submit_android()

    def _submit_ios(self):
        get_element(self.driver, ['ACCESSIBILITY_ID', 'icon back']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', 'icon back']).click()
        pass

    def _submit_android(self):
        self.driver.keyevent(4)
        pass
