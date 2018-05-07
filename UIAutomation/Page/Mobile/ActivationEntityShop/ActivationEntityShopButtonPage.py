from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, is_element_present
from UIAutomation.Page import BasePage
__author__ = 'CaoYong'


class ActivationEntityShopButtonPage(BasePage):
    def __init__(self, driver):
        """
        激活实体店(点击按钮)
        """
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.click_button_locator = None
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
        name_list = ['goImport']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.click_button_locator = ele_dic['goImport']
        pass

    def is_loaded(self):

        pass

    def go_import(self):
        if self.is_run_ios():
            self._go_import_IOS()
        else:
            self._go_import_android()
        pass

    def _go_import_IOS(self):
        get_element(self.driver, self.click_button_locator).click()
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '步骤错误，请返回卡片桌面重试')):
            assert False, "数据库数据对不上"
        pass

    def _go_import_android(self):
        get_element(self.driver, self.click_button_locator).click()
        pass
