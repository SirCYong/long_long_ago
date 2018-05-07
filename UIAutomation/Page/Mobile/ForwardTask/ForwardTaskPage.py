from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, get_elements

__author__ = 'sdy'


class ForwardTask(BasePage):
    """
    任务转发
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.forwardButton_locator = None
        self.forwardByAll_locator = None
        self.forwardBySingle_locator = None
        self.searchButton_locator = None
        self.searchText_locator = None
        self.choiceButton_locator = None
        self.cancelButton_locator = None
        self.saveButton_locator = None
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
        name_list = ['forwardButton', 'forwardByAll', 'forwardBySingle', 'searchButton', 'searchText',
                     'choiceButton', 'cancelButton', 'saveButton']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.forwardButton_locator = ele_dic['forwardButton']
        self.forwardByAll_locator = ele_dic['forwardByAll']
        self.forwardBySingle_locator = ele_dic['forwardBySingle']
        self.searchButton_locator = ele_dic['searchButton']
        self.searchText_locator = ele_dic['searchText']
        self.choiceButton_locator = ele_dic['choiceButton']
        self.cancelButton_locator = ele_dic['cancelButton']
        self.saveButton_locator = ele_dic['saveButton']

    def is_loaded(self):
        pass

    def forward_task(self):
        if self.is_run_ios():
            self._forward_task_ios()
        else:
            self._forward_task_android()

    def forward_task_all(self):
        if self.is_run_ios():
            self._forward_task_all_ios()
        else:
            self._forward_task_all_android()

    def _forward_task_ios(self):
        """
        IOS私有方法：任务转发
        """
        # self.action.click(self.forwardButton_locator)  # 选择转发按钮
        a = get_elements(self.driver, self.forwardButton_locator)
        a[1].click()
        self.action.click(self.forwardBySingle_locator)  # 选择【转发该任务】
        self.action.click(self.searchButton_locator)  # 点击通讯录【搜索】按钮
        self.action.send_keys(self.searchText_locator, '审')  # 搜索框输入【审】
        self.action.click(self.choiceButton_locator)  # 点击【选择】按钮
        self.action.click(self.saveButton_locator)  # 点击【确认转发】按钮

    def _forward_task_android(self):
        """
        android私有方法：任务转发
        """
        self.action.click(self.forwardButton_locator)  # 选择转发按钮
        self.action.click(self.forwardBySingle_locator)  # 选择【转发该任务】
        self.action.click(self.searchButton_locator)  # 点击通讯录【搜索】按钮
        self.action.send_keys(self.searchText_locator, '审')  # 搜索框输入【审】
        self.action.click(self.choiceButton_locator)  # 点击【选择】按钮
        self.action.click(self.saveButton_locator)  # 点击【确认转发】按钮

    def _forward_task_all_ios(self):
        """
        IOS私有方法：任务转发
        """
        self.action.click(self.forwardButton_locator)  # 选择转发按钮
        self.action.click(self.forwardByAll_locator)  # 选择【转发全部】
        self.action.click(self.searchButton_locator)  # 点击通讯录【搜索】按钮
        self.action.send_keys(self.searchText_locator, '审')  # 搜索框输入【审】
        self.action.click(self.choiceButton_locator)  # 点击【选择】按钮
        self.action.click(self.saveButton_locator)  # 点击【确认转发】按钮

    def _forward_task_all_android(self):
        """
        android私有方法：任务转发
        """
        self.action.click(self.forwardButton_locator)  # 选择转发按钮
        self.action.click(self.forwardByAll_locator)  # 选择【转发全部】
        self.action.click(self.searchButton_locator)  # 点击通讯录【搜索】按钮
        self.action.send_keys(self.searchText_locator, '审')  # 搜索框输入【审】
        self.action.click(self.choiceButton_locator)  # 点击【选择】按钮
        self.action.click(self.saveButton_locator)  # 点击【确认转发】按钮

    def submit(self):
        if self.is_run_ios():
            self._submit_ios()
        else:
            self._submit_android()

    def _submit_ios(self):
        # get_element(self.driver, ['ACCESSIBILITY_ID', 'icon back']).click()
        get_element(self.driver, ['ACCESSIBILITY_ID', 'icon back']).click()
        pass

    def _submit_android(self):
        self.driver.keyevent(4)
        pass
