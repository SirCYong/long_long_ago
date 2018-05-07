# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, get_elements
from UIAutomation.Page import BasePage

# Author:ytz
# PC端发布供货供应界面

class GoodsSupplyPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
        pass

    def page_factory(self):
        name_list = ['card', 'upload_files_link', 'example_template',
                     'detail','close_detail_btn', 'reImport', 'import_detail','view_detail']
        element_metadata_dict = page_element_factory(__file__, name_list)
        self.card_locator = element_metadata_dict['card']
        self.upload_files_link_locator = element_metadata_dict['upload_files_link']
        self.example_template_locator = element_metadata_dict['example_template']
        self.detail_locator = element_metadata_dict['detail']
        self.close_detail_btn_locator = element_metadata_dict['close_detail_btn']
        self.reImport_locator = element_metadata_dict['reImport']
        self.import_detail_locator = element_metadata_dict['import_detail']
        self.view_detail_locator = element_metadata_dict['view_detail']
        pass

    def is_loaded(self):
        pass

    def card(self):
        self.initial_element()
        get_element(self.driver, self.card_locator).click()
        sleep(2)
        get_element(self.driver, self.example_template_locator).click()
        sleep(2)
        get_element(self.driver, self.upload_files_link_locator).click()

    # 重新上传
    '''
        Step:选择文件，执行.exe
    '''
    def click_re_upload_file(self):
        self.initial_element()
        get_element(self.driver, self.upload_files_link_locator).click()


    def click_detail(self):
        self.initial_element()
        get_element(self.driver, self.detail_locator).click()

    def click_close_detail_btn(self):
        self.initial_element()
        get_element(self.driver, self.close_detail_btn_locator)


    def click_reImport(self):
        self.initial_element()
        get_element(self.driver, self.reImport_locator).click()

    #  查看停用明细

    def click_view_detail(self):
        self.initial_element()
        get_element(self.driver, self.view_detail_locator).click()

