from time import sleep

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.ActivationDepot.DepotMapPage import DepotMapPage
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException, is_element_present
__author__ = 'CaoYong'


class ActivationEntityShopPage(BasePage):
    """
    激活实体店(操作步骤)
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.input_entity_name_locator = None
        self.input_entity_address_locator = None
        self.input_entity_area_locator = None
        self.click_map_locator = None
        self.click_next_button_locator = None
        self.click_finish_button_locator = None
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
        name_list = ('entityShopName', 'entityShopMapChoice', 'entityShopAddress', 'entityShopArea',
                     'nextButton', 'finishButton')
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.input_entity_name_locator = ele_dic['entityShopName']
        self.input_entity_address_locator = ele_dic['entityShopAddress']
        self.input_entity_area_locator = ele_dic['entityShopArea']
        self.click_map_locator = ele_dic['entityShopMapChoice']
        self.click_next_button_locator = ele_dic['nextButton']
        self.click_finish_button_locator = ele_dic['finishButton']

    def is_loaded(self):

        pass

    def entity_shop_input_information(self):
        if self.is_run_ios():
            self._entity_shop_input_information_ios()
        else:
            self._entity_shop_input_information_android()

        pass

    def _entity_shop_input_information_ios(self):
        self.driver.hide_keyboard()  # 关闭软键盘
        self.action.set_value(self.input_entity_name_locator, '店大欺人啊')
        # get_element(self.driver, self.input_entity_name_locator).send_keys(u'店大欺人')
        self.action.set_value(self.input_entity_address_locator, '哈哈哈')
        self.action.set_value(self.input_entity_area_locator, '250')
        # get_element(self.driver, self.input_entity_area_locator).send_keys(250)
        self.action.click(self.click_map_locator)
        # get_element(self.driver, self.click_map_locator).click()
        sleep(2)
        DepotMapPage(self.driver).map_first()
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '完成')):
            sleep(1)
            self.action.click(self.click_finish_button_locator)
        self.action.click(self.click_next_button_locator)
        # get_element(self.driver, self.click_next_button_locator).click()
        sleep(10)
        pass

    def _entity_shop_input_information_android(self):
        # self.driver.hide_keyboard()  # 关闭软键盘
        self.action.send_keys(self.input_entity_name_locator, '林华亨小婊砸')
        # get_element(self.driver, self.input_entity_name_locator).send_keys(u'店大欺人')
        self.action.send_keys(self.input_entity_address_locator, '哈哈哈')
        # get_element(self.driver, self.input_entity_address_locator).send_keys(u'黄泉路')
        # self.action.send_keys(self.input_entity_area_locator, '250')
        # get_element(self.driver, self.input_entity_area_locator).send_keys(250)
        self.driver.find_element_by_id("com.iscs.mobilewcs:id/active_entry_shop_s_edt_before").send_keys('110')
        self.action.click(self.click_map_locator)
        # get_element(self.driver, self.click_map_locator).click()
        sleep(2)
        DepotMapPage(self.driver).map_first()
        self.action.click(self.click_next_button_locator)
        # get_element(self.driver, self.click_next_button_locator).click()
        pass
