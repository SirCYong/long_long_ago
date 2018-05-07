# coding: utf-8
from selenium.common.exceptions import NoSuchWindowException

from UIAutomation.Utils import page_element_factory, get_element
from UIAutomation.page import BasePage


class RegisterBtnPage(BasePage):
    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
        pass

    def page_factory(self):
        name_list = ['RegisterBtn','VerifyCodeText','NameTest','IDCardNumText','Upload','ProfilePhotos']
        element_metadata_dict = page_element_factory(__file__, name_list)
        self.RegisterBtn_element = element_metadata_dict['RegisterBtn']
        self.VerifyCodeText_element = element_metadata_dict['VerifyCodeText']
        self.NameTest_element = element_metadata_dict['NameTest']
        self.IDCardNumText_element = element_metadata_dict['IDCardNumText']
        self.Upload_element = element_metadata_dict['Upload']
        self.ProfilePhotos_element = element_metadata_dict['ProfilePhotos']
        pass

    def is_loaded(self):
        pass

    def click_register_button(self):
        self.initial_element()
        get_element(self.driver, self.RegisterBtn_element).click()

    def click_verify_code_text(self):
        self.initial_element()
        get_element(self.driver, self.VerifyCodeText_element).click()

    def click_name_test(self):
        self.initial_element()
        get_element(self.driver, self.NameTest_element).click()

    def click_id_card_num_text(self):
        self.initial_element()
        get_element(self.driver, self.IDCardNumText_element).click()

    def click_upload(self):
        self.initial_element()
        get_element(self.driver, self.Upload_element).click()

    def click_profile_photos(self):
        self.initial_element()
        get_element(self.driver, self.ProfilePhotos_element).click()