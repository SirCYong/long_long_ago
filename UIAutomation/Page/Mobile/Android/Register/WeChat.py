# -*- coding: utf-8 -*-
# language:zh-CN

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element
from UIAutomation.Page import BasePage

class Webchat(BasePage):
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
        name_list = ['Touch_HumanBtn','URL_TouchBtn']
        element_metadata_dict = page_element_factory(__file__, name_list)
        self.Touch_HumanBtn_element = element_metadata_dict['Touch_HumanBtn']
        self.URL_TouchBtn_element = element_metadata_dict['URL_TouchBtn']
        self.SelectHumanBtn_element = element_metadata_dict['SelectHumanBtn']
        # self.PhotographBtn_element = element_metadata_dict['PhotographBtn']
        # self.CameraBtn_element = element_metadata_dict['CameraBtn']
        # self.HookBtn_element = element_metadata_dict['HookBtn']
        # self.ConfirmBtn_element = element_metadata_dict['ConfirmBtn']
        # self.MobilePhoneInputText_element = element_metadata_dict['MobilePhoneInputText']
        # self.VerifyBtn_element = element_metadata_dict['VerifyBtn']
        # self.VerifyCodeText_element = element_metadata_dict['VerifyCodeText']
        # self.Submitted_SuccessfullyBtn_element = element_metadata_dict['Submitted_SuccessfullyBtn']
        # self.NestStepBtn2_element = element_metadata_dict['NestStepBtn2']
        # self.DoneBtn_element = element_metadata_dict['DoneBtn']
        # self.WSXXBtn_element = element_metadata_dict['WSXXBtn']
        # self.ChooseCountryCodeBtn_element = element_metadata_dict['ChooseCountryCodeBtn']
        # self.ChooseCNCodeBtn_element = element_metadata_dict['ChooseCNCodeBtn']
        # self.ChooseUSACodeBtn_element = element_metadata_dict['ChooseUSACodeBtn']
        # self.LoginBtn_element = element_metadata_dict['LoginBtn']
        # self.SendVerificationBtn_element = element_metadata_dict['SendVerificationBtn']
        # self.AlterOkBtn_element = element_metadata_dict['AlterOkBtn']
        pass

    def is_loaded(self):
        pass
    #点击人物
    def Click_Touch_HumanBtn(self):
        self.initial_element()
        get_element(self.driver, self.Touch_HumanBtn).click()
    # 点击链接
    def Click_URL_TouchBtn(self):
        self.initial_element()
        get_element(self.driver, self.URL_TouchBtn).send_keys('michael')
    # w微信里边选择人物
    def Click_SelectHumanBtn_element(self):
        self.initial_element()
        get_element(self.driver, self.SelectHumanBtn_element).click()
    # # 拍照认证button
    # def Click_PhotographBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.PhotographBtn_element).click()
    #
    # def Click_HookBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.HookBtn_element).click()
    # # 点击拍照
    # def Click_CameraBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.CameraBtn_element).click()
    # # 应用按钮
    # def Click_ConfirmBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.ConfirmBtn_element).click()
    # # 手机号码输入:
    # def Click_MobilePhoneInputText_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.MobilePhoneInputText_element).send_keys('15268509694')
    # # 获取验证码:
    # def Click_VerifyBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.VerifyBtn_element).click()
    # # 错误验证码:
    # def Click_VerifyCodeText_element_Error(self):
    #     self.initial_element()
    #     get_element(self.driver, self.VerifyCodeText_element).send_keys('123412')
    #  # 正确验证码:
    # def Click_VerifyCodeText_element_Correct(self):
    #     self.initial_element()
    #     get_element(self.driver, self.VerifyCodeText_element).send_keys('888888')
    # # 提交审核确定按钮:
    # def Click_Submitted_SuccessfullyBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.VerifyCodeText_element).click()
    # # 提交审核确定按钮:
    # def Click_NestStepBtn2_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.NestStepBtn2_element).click()
    #
    # def Click_DoneBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.DoneBtn_element).click()
    #
    # def Click_WSXXBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.WSXXBtn_element).click()
    #     # 点击选择国家标码
    # def Click_ChooseCountryCodeBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.ChooseCountryCodeBtn_element).click()
    #     # 选择美国 +1
    # def Click_ChooseCNCodeBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.ChooseCNCodeBtn_element).click()
    #     # 选择中国+86
    # def Click_ChooseUSACodeBtn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.ChooseUSACodeBtn_element).click()
    #
    # # 登录按钮
    # def click_login_btn_element(self):
    #     self.initial_element()
    #     get_element(self.driver, self.LoginBtn_element).click()

