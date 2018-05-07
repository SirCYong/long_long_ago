from UIAutomation.Utils import GlobalVarClass, is_element_present, Action
"""
吃掉任何需要点击的Toast（提示）信息，只需要把提示信息以及需要点掉按钮输入就可以了.按钮信息可以是yes，也可以是No.
"""


class EatToast:
    def __init__(self, driver, message, confirm):
        self.driver = driver
        self.toast_message = message
        self.confirm = confirm
        self.action = Action(driver)

    def eat_toast(self):
        """
        吃掉用户被顶以后系统的提示框：‘您的账号在别的地方登陆’
        :return:
        :rtype:
        """

        if GlobalVarClass.get_case_platform() == "darwin" and is_element_present(self.driver, ('ACCESSIBILITY_ID', self.toast_message)):
            self.action.click(self.driver, ('ACCESSIBILITY_ID', self.confirm))
        elif is_element_present(self.driver, ("XPATH", "//*[@resource-id='android:id/message' and @text=%s]" % self.toast_message)):
            self.action.click(("XPATH", "//*[@resource-id='android:id/message' and @text=%s]" % self.confirm))
        pass
