from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage
__author__ = 'zhoujin'


class TaskHandoverPage(BasePage):
    """
    非服务认证审核任务移交
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.icon_send_locator = None
        self.select_locator = None
        self.forward_locator = None
        self.phone_locator = None
        self.don_hand_over_locator = None
        self.hand_over_locator = None
        self.yes_locator = None
        self.audit_pass_locator = None
        try:
            self.is_loaded()
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
        name_list = ['icon_send',
                     'select',
                     'forward',
                     'phone',
                     "don_hand_over",
                     'hand_over',
                     'pass',
                     'audit_pass']
        ele_dic = page_element_factory(__file__, name_list)
        self.icon_send_locator = ele_dic['icon_send']
        self.select_locator = ele_dic['select']
        self.forward_locator = ele_dic['forward']
        self.phone_locator = ele_dic['phone']  # 确定
        self.don_hand_over_locator = ele_dic['don_hand_over']  # 取消
        self.hand_over_locator = ele_dic['hand_over']  #
        self.yes_locator = ele_dic['pass']  # 通过
        self.audit_pass_locator = ele_dic['audit_pass']  # 通过
        # self.no_locator = ele_dic['no']  # 驳回
        pass

    def is_loaded(self):
        pass

    def handover(self):
        self.initial_element()
        get_element(self.driver, self.icon_send_locator).click()
        get_element(self.driver, self.select_locator).send_keys(u'白云')  #移交人
        get_element(self.driver, self.select_locator).click()
        get_element(self.driver, self.forward_locator).click()  # 转发
        get_element(self.driver, self.hand_over_locator).click()  # 确认移交

