from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory,  ParseXmlErrorException
from UIAutomation.Page import BasePage

# Author:zhongchangwei


class DistributionManagerAndSupervisor(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
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
        name_list = ['choice', 'assigned_to_me', 'distribution_success_button', 'name', 'phone',
                     'monitor', 'manager']
        ele_dic = page_element_factory(__file__, name_list)
        self.choice_locator = ele_dic['choice']  # 请选择
        self.assigned_to_me_locator = ele_dic['assigned_to_me']  # 分配给我
        self.distribution_success_button_locator = ele_dic['distribution_success_button']  # 分配成功
        self.name_locator = ele_dic['name']  # 用户名
        self.phone_locator = ele_dic['phone']  # 电话
        self.monitor_locator = ele_dic['monitor']  # 监控者
        self.manager_locator = ele_dic['manager']  # 管理者
        pass

    def is_loaded(self):
        pass

    def distribution_manager_supervisor_to_self(self):
        self.action.click(self.assigned_to_me_locator, [0])
        self.action.click(self.assigned_to_me_locator)  # 管理者分配给我
        self.action.click(self.distribution_success_button_locator)     # 点击分配成功


