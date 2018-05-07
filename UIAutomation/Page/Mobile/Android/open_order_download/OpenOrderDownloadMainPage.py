# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchWindowException


from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage

#author:chenyanxiu
class OpenOrderDownloadMainPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

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
        name_list = ['ppt_name',
                     'date',
                     'open_download',
                     'tip_message',
                     'determine',
                     'open_tip_msg',
                     'cancel']
        ele_dic = page_element_factory(__file__, name_list)
        self.ppt_name_locator = ele_dic['ppt_name']  # 旗舰店
        self.date_locator = ele_dic['date']  # 年月日
        self.open_download_locator = ele_dic['open_download']  # 开启下载
        self.tip_message_locator = ele_dic['tip_message']  # 提示信息
        self.determine_locator = ele_dic['determine'] # 确定
        self.open_tip_msg_locator = ele_dic['open_tip_msg'] # 开启后提示信息
        self.cancel_locator = ele_dic['cancel'] # 取消
        pass

    def is_loaded(self):

        pass
