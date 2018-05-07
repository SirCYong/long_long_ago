from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import is_element_present
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
__author__ = 'zhoujin'


class OptimizeAddressBookAndInviteLink(BasePage):
    """
    通讯录状态
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.choice_locator = None
        self.search_locator = None
        self.name_locator = None
        self.invite_locator = None
        self.icon_back_locator = None
        self.create_locator = None
        self.register_locator = None
        self.task_locator = None
        self.permission_locator = None
        self.copy_locator = None
        self.allocate_locator = None
        self.com_locator = None
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
        name_list = ('choice', 'search', 'name', 'name_two', 'invite', 'icon_back', 'create', 'register', 'task',
                     'permission', 'copy', 'name_three', 'allocate', 'com')
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.choice_locator = ele_dic['choice']  # 选择好友
        self.search_locator = ele_dic['search']  # 搜索
        self.name_locator = ele_dic['name']  # 输入名字（不在网仓体系下）
        self.invite_locator = ele_dic['invite']  # 邀请状态
        self.icon_back_locator = ele_dic['icon_back']  # 返回键
        self.create_locator = ele_dic['create']  # 选择创造方
        self.register_locator = ele_dic['register']   # 已注册
        self.task_locator = ele_dic['task']       # 分配权限
        self.permission_locator = ele_dic['permission']  # 选择权限
        self.copy_locator = ele_dic['copy']   # 复制权限
        self.allocate_locator = ele_dic['allocate']  # 无需分配
        self.com_locator = ele_dic['com']   # 消除键盘

    def is_loaded(self):
        pass

    def optimize_address_book_and_invite_link(self):
        if self.is_run_ios():
            self._optimize_address_book_and_invite_link_ios()
        else:
            self._optimize_address_book_and_invite_link_android()

    def _optimize_address_book_and_invite_link_ios(self):
        """
        查看通讯录中邀请人的状态，提前添加一个人在通讯录中
        当前添加的这个人不在网仓体系下
        """
        # self.action.click(self.create_locator)
        self.action.click(self.choice_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).set_value('周锦')
        self.action.click(self.com_locator)

    def _optimize_address_book_and_invite_link_android(self):
        """
        查看通讯录中邀请人的状态，提前添加一个人在通讯录中
        当前添加的这个人不在网仓体系下
        周锦：18555093086
        """
        self.action.click(self.choice_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).send_keys('周锦')

    def judge_method(self):
        if self.is_run_ios():
            self._judge_method_ios()
        else:
            self._judge_method_android()

    def _judge_method_ios(self):
        if is_element_present(self.driver, ("ACCESSIBILITY_ID", "邀请")):
            print('邀请状态')
        else:
            assert False, '没有看到邀请状态'

    def _judge_method_android(self):
        if is_element_present(self.driver, ("xpath",
                                            "//*[@resource-id='com.iscs.mobilewcs:id/btn_type_content' and @text='邀请']")):
            print('邀请状态')
        else:
            assert False, '没有看到邀请状态'

    def optimize_address_book_and_invite_link_two(self):
        if self.is_run_ios():
            self._optimize_address_book_and_invite_link_two_ios()
        else:
            self._optimize_address_book_and_invite_link_two_android()

    def _optimize_address_book_and_invite_link_two_ios(self):
        """
        查看通讯录中邀请人的状态，提前添加一个人在通讯录中
        当前添加的这个人在网仓体系下
        百合：18555090013
        """
        self.action.click(self.choice_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).set_value('百合')
        self.action.click(self.com_locator)

    def _optimize_address_book_and_invite_link_two_android(self):
        """
        查看通讯录中邀请人的状态，提前添加一个人在通讯录中
        当前添加的这个人在网仓体系下
        """
        self.action.click(self.choice_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).send_keys('百合')

    def judge_method_two(self):
        if self.is_run_ios():
            self._judge_method_two_ios()
        else:
            self._judge_method_two_android()

    def _judge_method_two_ios(self):
        if is_element_present(self.driver, ("ACCESSIBILITY_ID", "已注册")):
            print('已注册状态')
        else:
            assert False, '没有看到已注册状态'

    def _judge_method_two_android(self):
        if is_element_present(self.driver, ("xpath",
                                            "//*[@resource-id='com.iscs.mobilewcs:id/btn_type_content' and @text='已注册']")):
            print('已注册状态')
        else:
            assert False, '没有看到已注册状态'

    def optimize_address_book_and_invite_link_three(self):
        if self.is_run_ios():
            self._optimize_address_book_and_invite_link_three_ios()
        else:
            self._optimize_address_book_and_invite_link_three_android()

    def _optimize_address_book_and_invite_link_three_ios(self):
        """
        分配权限查看通讯录中邀请人的状态
        提前添加一个人在通讯录中
        当前分配的这个人已经有该权限
        薄荷糖：18555090006
        """
        self.action.click(self.task_locator)
        self.action.click(self.permission_locator)
        self.action.click(self.copy_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).set_value('薄荷糖')
        self.action.click(self.com_locator)

    def _optimize_address_book_and_invite_link_three_android(self):
        """
        分配权限查看通讯录中邀请人的状态
        提前添加一个人在通讯录中
        当前分配的这个人已经有该权限
        """
        self.action.click(self.task_locator)
        self.action.click(self.permission_locator)
        self.action.click(self.copy_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).send_keys('薄荷糖')

    def judge_method_three(self):
        if self.is_run_ios():
            self._judge_method_three_ios()
        else:
            self._judge_method_three_android()

    def _judge_method_three_ios(self):
        if is_element_present(self.driver, ("ACCESSIBILITY_ID", "无需分配")):
            print('无需分配状态')
        else:
            assert False, '没有看到无需分配状态'

    def _judge_method_three_android(self):
        if is_element_present(self.driver, ("xpath",
                                            "//*[@resource-id='com.iscs.mobilewcs:id/btn_type_content' and @text ='无需分配']")):
            print('无需分配状态')
        else:
            assert False, '没有看到无需分配状态'

    def optimize_address_book_and_invite_link_four(self):
        if self.is_run_ios():
            self._optimize_address_book_and_invite_link_four_ios()
        else:
            self._optimize_address_book_and_invite_link_four_android()

    def _optimize_address_book_and_invite_link_four_ios(self):
        """
        分配权限查看通讯录中邀请人的状态
        提前添加一个人在通讯录中
        当前分配的这个人已经有该权限
        """
        self.action.click(self.task_locator)
        self.action.click(self.permission_locator)
        self.action.click(self.copy_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).set_value('千')
        self.action.click(self.com_locator)

    def _optimize_address_book_and_invite_link_four_android(self):
        """
        分配权限查看通讯录中邀请人的状态
        提前添加一个人在通讯录中
        当前分配的这个人已经有该权限
        千：18555090047
        """
        self.action.click(self.task_locator)
        self.action.click(self.permission_locator)
        self.action.click(self.copy_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).send_keys('千')

    def judge_method_four(self):
        if self.is_run_ios():
            self._judge_method_four_ios()
        else:
            self._judge_method_four_android()

    def _judge_method_four_ios(self):
        if is_element_present(self.driver, ("ACCESSIBILITY_ID", "认证中")):
            print('认证中状态')
        else:
            assert False, '没有看到认证中状态'

    def _judge_method_four_android(self):
        if is_element_present(self.driver, ("xpath",
                                            "//*[@resource-id='com.iscs.mobilewcs:id/btn_type_content' and @text ='认证中']")):
            print('认证中状态')
        else:
            assert False, '没有看到认证中状态'

    def optimize_address_book_and_invite_link_five(self):
        if self.is_run_ios():
            self._optimize_address_book_and_invite_link_five_ios()
        else:
            self._optimize_address_book_and_invite_link_five_android()

    def _optimize_address_book_and_invite_link_five_ios(self):
        """
        分配权限查看通讯录中邀请人的状态
        提前添加一个人在通讯录中
        当前分配的这个人已经有该权限
        的：18555090043
        """
        self.action.click(self.task_locator)
        self.action.click(self.permission_locator)
        self.action.click(self.copy_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).set_value('的')
        self.action.click(self.com_locator)

    def _optimize_address_book_and_invite_link_five_android(self):
        """
        分配权限查看通讯录中邀请人的状态
        提前添加一个人在通讯录中
        当前分配的这个人已经有该权限
        """
        self.action.click(self.task_locator)
        self.action.click(self.permission_locator)
        self.action.click(self.copy_locator)
        self.action.click(self.search_locator)
        get_element(self.driver, self.name_locator).send_keys('的')

    def judge_method_five(self):
        if self.is_run_ios():
            self._judge_method_five_ios()
        else:
            self._judge_method_five_android()

    def _judge_method_five_ios(self):
        if is_element_present(self.driver, ("ACCESSIBILITY_ID", "选择")):
            print('选择状态')
        else:
            assert False, '没有看到选择状态'

    def _judge_method_five_android(self):
        if is_element_present(self.driver, ("xpath",
                                            "//*[@resource-id='com.iscs.mobilewcs:id/btn_type_content' and @text ='选择']")):
            print('选择状态')
        else:
            assert False, '没有看到选择状态'

    def submit(self):
        if self.is_run_ios():
            self._submit_ios()
        else:
            self._submit_android()

    def _submit_ios(self):
        get_element(self.driver, ['ACCESSIBILITY_ID', 'icon back desktop']).click()
        pass

    def _submit_android(self):
        self.driver.keyevent(4)
        self.driver.keyevent(4)
        self.driver.keyevent(4)
        pass
