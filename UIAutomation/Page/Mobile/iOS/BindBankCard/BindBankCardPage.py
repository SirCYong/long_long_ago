from time import sleep
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, is_element_present, ParseXmlErrorException, cit, close_oracle
from UIAutomation.Page import BasePage
__author__ = 'caoyong'


class BindBankCardPage(BasePage):
    """
    绑定银行卡
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.input_user_name_locator = None
        self.click_add_payment_account_locator = None
        self.click_bank_locator = None
        self.click_payment_locator = None
        self.click_we_chat_locator = None
        self.input_payment_name_locator = None
        self.input_number_locator = None
        self.click_confirm_locator = None
        self.click_get_verification_code_locatot = None
        self.input_verification_code_locator = None
        self.click_next_button_locator = None
        self.find_prompt_locator = None
        self.click_ok_locator = None
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
        name_list = ('inputUserName', 'addPaymentAccount', 'bankButton', 'payment', 'weChatButton', 'inputPaymentName',
                     'inputNumber', 'confirmButton', 'getVerificationCode', 'inputVerificationCode', 'nextButton',
                     'prompt', 'ok')
        ele_dic = page_element_factory(__file__, name_list)
        self.input_user_name_locator = ele_dic['inputUserName']
        self.click_add_payment_account_locator = ele_dic['addPaymentAccount']
        self.click_bank_locator = ele_dic['bankButton']
        self.click_payment_locator = ele_dic['payment']
        self.click_we_chat_locator = ele_dic['weChatButton']
        self.input_payment_name_locator = ele_dic['inputPaymentName']
        self.input_number_locator = ele_dic['inputNumber']
        self.click_confirm_locator = ele_dic['confirmButton']
        self.click_get_verification_code_locatot = ele_dic['getVerificationCode']
        self.input_verification_code_locator = ele_dic['inputVerificationCode']
        self.click_next_button_locator = ele_dic['nextButton']
        self.find_prompt_locator = ele_dic['prompt']
        self.click_ok_locator = ele_dic['ok']
        pass

    def is_loaded(self):

        pass

    def operation_bind_bank_card(self):
        self.action.set_value(self.input_user_name_locator, '测试账号')
        self.action.click(self.click_confirm_locator)
        sleep(2)
        if is_element_present(self.driver, ('ACCESSIBILITY_ID', '提示')):
            sleep(4)
            self.action.click(self.click_ok_locator)
        self.action.click(self.click_add_payment_account_locator)

        pass

    def operation_bank_payment(self):
        self.action.click(self.click_payment_locator)
        self.action.set_value(self.input_payment_name_locator, '支付宝')
        self.action.set_value(self.input_number_locator, '18888000031')
        self.action.click(self.click_confirm_locator)
        pass

    def operation_bank_bank(self):
        self.action.click(self.click_bank_locator)
        self.action.set_value(self.input_payment_name_locator, '各种银行')
        self.action.set_value(self.input_number_locator, '6228480402564890018')
        self.action.click(self.click_confirm_locator)
        pass

    def operation_bank_we_chat(self):
        self.action.click(self.click_we_chat_locator)
        self.action.set_value(self.input_payment_name_locator, '微信支付')
        self.action.set_value(self.input_number_locator, 'CaoY900')
        self.action.click(self.click_confirm_locator)
        pass

    def operation_bank_verification(self, admin=None):
        con, curs = cit()
        sql = '''select t.verification_code from xdw_app.cm_verification t where t.business_type = 'BANK'
and t.user_id = '%s' and t.status = 1''' % admin
        curs.execute(sql)
        number = curs.fetchone()
        close_oracle(con, curs)
        print (number)
        self.action.click(self.click_get_verification_code_locatot)
        self.action.set_value(number)
        self.action.click(self.click_next_button_locator)
        pass

