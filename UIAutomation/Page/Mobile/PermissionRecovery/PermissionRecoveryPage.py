from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
__author__ = 'zhoujin'


class PermissionRecovery(BasePage):
    """
    权限回收
    假定已经分配过权限
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.permission_locator = None
        self.storage_locator = None
        self.invite_locator = None
        self.recovery_locator = None
        self.sure_locator = None
        self.person_locator = None
        self.jurisdiction_locator = None
        self.transfer_locator = None
        self.first_locator = None
        self.second_locator = None
        self.submit_locator = None
        self.search_locator = None
        self.services_locator = None
        self.sweep_points_locator = None
        self.change_locator = None
        self.name_locator =None
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
        name_list = ['permission', 'storage', 'invite', 'recovery', 'sure', 'person', 'jurisdiction', 'transfer',
                     'first', 'second', 'submit', 'search', 'services', 'sweep_points', 'change', 'name']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.permission_locator = ele_dic['permission']
        self.storage_locator = ele_dic['storage']
        self.invite_locator = ele_dic['invite']
        self.recovery_locator = ele_dic['recovery']
        self.sure_locator = ele_dic['sure']
        self.person_locator = ele_dic['person']
        self.jurisdiction_locator = ele_dic['jurisdiction']
        self.transfer_locator = ele_dic['transfer']
        self.first_locator = ele_dic['first']
        self.second_locator = ele_dic['second']
        self.submit_locator = ele_dic['submit']
        self.search_locator = ele_dic['search']
        self.services_locator = ele_dic['services']
        self.sweep_points_locator = ele_dic['sweep_points']
        self.change_locator = ele_dic['change']
        self.name_locator = ele_dic['name']

    def is_loaded(self):
        pass

    def permission_recovery(self):
        if self.is_run_ios():
            self._permission_recovery_ios()
        else:
            self._permission_recovery_android()

    def _permission_recovery_ios(self):
        """
        权限收回
        前提：当前用户已经分配过权限
        """
        self.action.click(self.permission_locator)   # 管理者权限收回
        self.action.click(self.storage_locator)        # 入库上架
        self.action.click(self.invite_locator)          # 邀请
        self.action.click(self.recovery_locator)     # 收回权限
        self.action.click(self.sure_locator)        # 确定

    def _permission_recovery_android(self):
        """
        权限收回
        前提：当前用户已经分配过权限
        """
        self.action.click(self.permission_locator)
        self.action.click(self.storage_locator)
        self.action.click(self.invite_locator)
        self.action.click(self.recovery_locator)
        self.action.click(self.sure_locator)

    def permission_recovery_two(self):
        if self.is_run_ios():
            self._permission_recovery_two_ios()
        else:
            self._permission_recovery_two_android()

    def _permission_recovery_two_ios(self):
        self.action.click(self.jurisdiction_locator)
        self.action.click(self.transfer_locator)
        self.action.click(self.first_locator)
        self.action.click(self.second_locator)
        self.action.click(self.submit_locator)
        self.action.click(self.sure_locator)

    def _permission_recovery_two_android(self):
        self.action.click(self.jurisdiction_locator)
        self.action.click(self.transfer_locator)
        self.action.click(self.first_locator)
        self.action.click(self.second_locator)
        self.action.click(self.submit_locator)
        self.action.click(self.sure_locator)

    def permission_recovery_three(self):
        if self.is_run_ios():
            self._permission_recovery_three_ios()
        else:
            self._permission_recovery_three_android()

    def _permission_recovery_three_ios(self):
        self.action.click(self.person_locator)
        self.action.click(self.search_locator)
        self.action.send_keys(self.name_locator, u'百合九')
        self.driver.keyevent(4)
        self.action.click(self.services_locator)
        self.action.click(self.sweep_points_locator)
        self.action.click(self.change_locator)
        self.action.click(self.recovery_locator)
        self.action.click(self.sure_locator)

    def _permission_recovery_three_android(self):
        self.action.click(self.person_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator)
        self.driver.keyevent(4)
        self.action.click(self.services_locator)
        self.action.click(self.sweep_points_locator)
        self.action.click(self.change_locator)
        self.action.click(self.recovery_locator)
        self.action.click(self.sure_locator)

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
