# -*- coding: utf-8 -*-

from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import ParseXmlErrorException, page_element_factory


__author__ = 'LiYu'


class MainPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.release_labor_demand_locator = None
        self.release_warehouse_locator = None
        self.system_service_agreement_locator = None
        self.submit_deposit_locator = None
        self.empty_card_locator = None
        self.sorting_clerk_locator = None
        self.location_locator = None
        self.long_task_card_locator = None

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

    def is_loaded(self):
        pass

    def page_factory(self):
        name_list = ['Release_labor_demand', 'Release_warehouse', 'System_service_agreement', 'Submit_deposit',
                     'Empty_card', 'Sorting_clerk', 'Location', 'LongTaskCard', 'Release_Long_labor_demand']
        ele_dic = page_element_factory(__file__, name_list)
        self.release_labor_demand_locator = ele_dic['Release_labor_demand']
        self.release_warehouse_locator = ele_dic['Release_warehouse']
        self.system_service_agreement_locator = ele_dic['System_service_agreement']
        self.submit_deposit_locator = ele_dic['Submit_deposit']
        self.empty_card_locator = ele_dic['Empty_card']
        self.sorting_clerk_locator = ele_dic['Sorting_clerk']
        self.location_locator = ele_dic['Location']
        self.long_task_card_locator = ele_dic['LongTaskCard']
        self.Long_labor_demand_locator = ele_dic['Release_Long_labor_demand']
        pass

    def click_long_card(self):
        """
        点击长期任务卡片
        :return:
        """
        self.action.click(self.long_task_card_locator)

    def click_empty_card(self):
        """
        点击空白卡片
        :return:
        """
        self.action.click(self.empty_card_locator)

    def click_release_labor_demand(self):
        """
        临时卡片：发布劳务需求
        :return:
        """
        self.action.click(self.release_labor_demand_locator)
        pass

    def click_long_release_labor_demand(self):
        """
        长期卡片：发布劳务需求的任务
        :return:
        """
        self.action.click(self.Long_labor_demand_locator)

    def assert_labor_demand_present(self):
        """
        判断劳务需求发布劳务需求的卡片是否存在
        :return:
        """
        assert_that(self.action.is_element_present(self.release_labor_demand_locator), equal_to(True))

    def click_release_warehouse(self):
        """
        点击发布仓储供应
        :return:
        """
        self.action.click(self.release_warehouse_locator)
        pass

    def assert_release_warehouse(self):
        """
        判断发布仓储供应的卡片是否存在
        :return:
        """
        assert_that(self.action.is_element_present(self.release_warehouse_locator), equal_to(True))

    def click_system_service(self):
        """
        点击系统服务契约
        :return:
        """
        self.action.click(self.system_service_agreement_locator)

    def click_deposit(self):
        """
        提交保证金
        :param self:
        :return:
        """
        self.action.click(self.submit_deposit_locator)





