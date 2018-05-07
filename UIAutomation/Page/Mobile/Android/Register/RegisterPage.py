# -*- coding: utf-8 -*-
# language:zh-CN
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element
from UIAutomation.Page import BasePage


class RegisterPage(BasePage):
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
        name_list = ['NextStepBtn1', 'NameTextInput', 'IDCardNumText',
                     'PhotographBtn', 'CameraBtn', 'HookBtn', 'ConfirmBtn',
                     'MobilePhoneInputText', 'VerifyBtn',
                     'VerifyCodeText', 'Submitted_SuccessfullyBtn',
                     'NestStepBtn2', 'DoneBtn', 'WSXXBtn', 'ChooseCountryCodeBtn', 'WebChatLoginBtn']
        element_metadata_dict = page_element_factory(__file__, name_list)
        self.NextStepBtn1_element = element_metadata_dict['NextStepBtn1']
        self.NameTextInput_element = element_metadata_dict['NameTextInput']
        self.IDCardNumText_element = element_metadata_dict['IDCardNumText']
        self.PhotographBtn_element = element_metadata_dict['PhotographBtn']
        self.CameraBtn_element = element_metadata_dict['CameraBtn']
        self.HookBtn_element = element_metadata_dict['HookBtn']
        self.ConfirmBtn_element = element_metadata_dict['ConfirmBtn']
        self.MobilePhoneInputText_element = element_metadata_dict['MobilePhoneInputText']
        self.VerifyBtn_element = element_metadata_dict['VerifyBtn']
        self.VerifyCodeText_element = element_metadata_dict['VerifyCodeText']
        self.Submitted_SuccessfullyBtn_element = element_metadata_dict['Submitted_SuccessfullyBtn']
        self.NestStepBtn2_element = element_metadata_dict['NestStepBtn2']
        self.DoneBtn_element = element_metadata_dict['DoneBtn']
        self.WSXXBtn_element = element_metadata_dict['WSXXBtn']
        self.ChooseCountryCodeBtn_element = element_metadata_dict['ChooseCountryCodeBtn']
        self.WebChatLoginBtn_element = element_metadata_dict['WebChatLoginBtn']
        # self.TipAuditInformationText_element = element_metadata_dict['TipAuditInformationText']
        # self.WSXXNext_element = element_metadata_dict['WSXXNext']
        # self.SendVerificationBtn_element = element_metadata_dict['SendVerificationBtn']
        # self.AlterOkBtn_element = element_metadata_dict['AlterOkBtn']

        pass

    def is_loaded(self):
        pass

    def Click_NextStepBtn1_element(self):
        self.initial_element()
        get_element(self.driver, self.NextStepBtn1_element).click()

    #  姓名栏输入姓名
    def Click_NameTextInput_element(self):
        self.initial_element()
        get_element(self.driver, self.NameTextInput_element).send_keys('michael')

    #  身份证栏输入身份证号
    def Click_IDCardNumText_element(self):
        self.initial_element()
        get_element(self.driver, self.IDCardNumText_element).send_keys('622102196902150230')

    #  拍照认证button
    def Click_PhotographBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.PhotographBtn_element).click()

    def Click_HookBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.HookBtn_element).click()

    #  点击拍照
    def Click_CameraBtn_element(self):
        self.initial_element()

    # 应用按钮
    def Click_ConfirmBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.ConfirmBtn_element).click()

    def Click_MobilePhoneInputText_element(self):
        self.initial_element()
        get_element(self.driver, self.MobilePhoneInputText_element).send_keys('15268509694')

    #  获取验证码:
    def Click_VerifyBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.VerifyBtn_element).click()

    # 输入错误验证码:
    def Click_VerifyCodeText_element_Error(self):
        self.initial_element()
        get_element(self.driver, self.VerifyCodeText_element).send_keys('123412')

    #  输入正确验证码:
    def Click_VerifyCodeText_element_Correct(self):
        self.initial_element()
        get_element(self.driver, self.VerifyCodeText_element).send_keys('888888')

    # 提交审核确定按钮:
    def Click_Submitted_SuccessfullyBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.VerifyCodeText_element).click()

    #  提交审核确定按钮:
    def Click_NestStepBtn2_element(self):
        self.initial_element()
        get_element(self.driver, self.NestStepBtn2_element).click()

    def Click_DoneBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.DoneBtn_element).click()

    def Click_WSXXBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.WSXXBtn_element).click()

    def Click_ChooseCountryCodeBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.ChooseCountryCodeBtn_element).click()

    #  微信登录
    def Click_WebChatLoginBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.WebChatLoginBtn_element).click()

