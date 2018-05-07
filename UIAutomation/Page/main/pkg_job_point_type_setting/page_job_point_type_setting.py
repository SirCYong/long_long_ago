from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Page.BasePage import BasePage

from UIAutomation.Utils import ParseXmlErrorException, page_element_factory, initial_element_error_wrapper

from hamcrest import *

__author__ = "zzh"
__desc__ = "作业点设置page"


class PageJobPointTypeSetting(BasePage):
    """
    作业点设置Page
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.is_loaded()
            self.initial_element()
        except ParseXmlErrorException:
            initial_element_error_wrapper(self.driver)
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        name_list = ["button_select_warehouse",
                     "button_warehouse_first",
                     "button_warehouse_confirm",
                     "button_dimension_change",
                     "button_next",
                     "input_job_point_name",
                     "button_select_job_point_type",
                     "button_job_point_first",
                     "button_job_point_confirm",
                     "button_complete",
                     "button_add_next",
                     "verify_job_point_detail"]

        ele_dic = page_element_factory(self.standard_xml_file, name_list)
        # 选择需要操作的仓库
        self.button_select_warehouse = ele_dic["button_select_warehouse"]
        # 选择仓库页面:选择第一个仓库
        self.button_warehouse_first = ele_dic["button_warehouse_first"]
        # 选择仓库页面：确定按钮
        self.button_warehouse_confirm = ele_dic["button_warehouse_confirm"]
        # 选择需要变化的维度：id一样，用index区分
        self.button_dimension_change = ele_dic["button_dimension_change"]
        # 下一步按钮
        self.button_next = ele_dic["button_next"]
        # 输入作业点名称
        self.input_job_point_name = ele_dic["input_job_point_name"]
        # 请选择作业点类型
        self.button_select_job_point_type = ele_dic["button_select_job_point_type"]
        # 选择作业点类型页面：选择第一个作业点类型
        self.button_job_point_first = ele_dic["button_job_point_first"]
        # 选择作业点类型页面：确定按钮
        self.button_job_point_confirm = ele_dic["button_job_point_confirm"]
        # 完成并查看按钮
        self.button_complete = ele_dic["button_complete"]
        # 新增下一个按钮
        self.button_add_next = ele_dic["button_add_next"]
        # 新增成功后的页面全部作业点类型页面的作业点详情
        self.verify_job_point_detail = ele_dic["verify_job_point_detail"]

    def is_loaded(self):
        pass

    def select_warehouse(self):
        """
        选择一个仓库
        :return:
        """
        # 点击选择需要操作的仓库的按钮
        self.action.click(self.button_select_warehouse)
        # 点击选择仓库页面的确定按钮
        self.action.click(self.button_warehouse_confirm)

    def select_all_demension(self):
        """
        选择所有维度
        :return:
        """
        self.action.click(self.button_dimension_change, [0, 1, 2, 3, 4, 5])

    def click_button_next(self):
        """
        点击下一步按钮
        :return:
        """
        self.action.click(self.button_next)

    def send_keys_job_point_name(self, job_point_name):
        """
        输入作业点类型名称
        :param job_point_name: 作业点类型名称
        :return:
        """
        self.action.clear(self.input_job_point_name)
        self.action.send_keys(self.input_job_point_name, job_point_name)

    def select_job_point_type(self):
        """
        选择作业点类型
        :return:
        """
        # 点击请选择类型
        self.action.click(self.button_select_job_point_type)
        # 在作业点类型选择页面中点击确定按钮
        self.action.click(self.button_job_point_confirm)

    def click_button_complete(self):
        """
        点击完成并查看按钮，并验证新增成功后是否跳到全部作业点类型界面
        :return:
        """
        self.action.click(self.button_complete)
        assert_that(self.action.is_element_present(self.verify_job_point_detail), equal_to(True))












