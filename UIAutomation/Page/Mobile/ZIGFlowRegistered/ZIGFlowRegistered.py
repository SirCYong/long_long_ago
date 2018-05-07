from time import sleep
from UIAutomation.Page import BasePage
from UIAutomation.Page.Mobile.ZIGFlowFlowSQL.RegisteredSQL import update_invite_SQL, get_invite_sql
from UIAutomation.Utils import GlobalVarClass, time, run_info_log, page_element_factory

__author__ = "ytz"
__doc__ = "注册"


class ZIGFlowRegistered(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.choose_friends_locator = None
        self.name_locator = None
        self.card_id_locator = None
        self.photo_locator = None
        self.nest_step_locator = None
        self.photo_okay_locator = None
        self.photo_done_locator = None
        self.photo_id_front_locator = None
        self.photo_id_back_locator = None
        self.id_photo_next_locator = None
        self.verify_num_locator = None
        self.verify_identify_code_locator = None
        self.verify_get_identify_code_locator = None
        self.verify_set_pwd_locator = None
        self.verify_confirm_pwd_locator = None
        self.verify_next_step_locator = None
        self.wechat_login_locator = None
        self.refresh_locator = None
        self.task_central_locator = None

        if self.is_run_ios():
            self.xml_file = __file__[:__file__.rfind(".")] + "IOS.xml"
        else:
            self.xml_file = __file__[:__file__.rfind(".")] + "Android.xml"

        try:
            self.initial_element()
        except Exception:
            screenshot_file = GlobalVarClass.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVarClass.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVarClass.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'XML解析失败.', GlobalVarClass.get_log_file())
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except Exception():
            print(u'控件不在当前页面上.')
            screenshot_file = GlobalVarClass.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
            self.driver.save_screenshot(GlobalVarClass.get_screenshot_path() + screenshot_file)
            print("错误截图：")
            print('<img src="' + GlobalVarClass.get_screenshot_path() + screenshot_file + '" width="800px" />')
            run_info_log(u'控件不在当前页面上.', GlobalVarClass.get_log_file())
            raise
        pass

    def is_loaded(self):
        pass

    def page_factory(self):
        # iOS and Android端统一的控件
        name_list = ['choose_friends', 'name', 'card_id', 'photo', 'nest_step', 'photo_okay',
                     'photo_done', 'photo_id_front', 'photo_id_back', 'id_photo_next',
                     'verify_num', 'verify_identify_code', 'verify_get_identify_code',
                     'verify_set_pwd', 'verify_confirm_pwd', 'verify_next_step',
                     'wechat_login', 'refresh', 'task_central']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.choose_friends_locator = ele_dic['choose_friends']  #
        self.name_locator = ele_dic['name']  #
        self.card_id_locator = ele_dic['card_id']  #
        self.photo_locator = ele_dic['photo']  #
        self.nest_step_locator = ele_dic['nest_step']  #
        self.photo_okay_locator = ele_dic['photo_okay']  #
        self.photo_done_locator = ele_dic['photo_done']  #
        self.photo_id_front_locator = ele_dic['photo_id_front']  #
        self.photo_id_back_locator = ele_dic['photo_id_back']  #
        self.id_photo_next_locator = ele_dic['id_photo_next']  #
        self.verify_num_locator = ele_dic['verify_num']  #
        self.verify_identify_code_locator = ele_dic['verify_identify_code']  #
        self.verify_get_identify_code_locator = ele_dic['verify_get_identify_code']  #
        self.verify_set_pwd_locator = ele_dic['verify_set_pwd']  #
        self.verify_confirm_pwd_locator = ele_dic['verify_confirm_pwd']  #
        self.verify_next_step_locator = ele_dic['verify_next_step']
        self.wechat_login_locator = ele_dic['wechat_login']  # 微信登录
        self.refresh_locator = ele_dic['refresh']  # 刷新
        self.task_central_locator = ele_dic['task_central']  # 任务中心

    pass

    def wechat_login(self):
            if self.is_run_ios():
                self._we_chat_login_ios()
            else:
                self._we_chat_login()

    def _we_chat_login_ios(self):
        pass

        #  微信登录
    def _we_chat_login(self):
        self.action.click(self.wechat_login_locator)
        sleep(3)
        #  确认登录
        self.driver.tap([(510, 1040)], 500)
        sleep(3)
        # 前往微信
        self.driver.tap([(530, 1490)], 500)
        sleep(3)
        # 进入微信聊天界面--点击折耳喵
        self.driver.tap([(470, 270)], 500)
        sleep(3)
        # 点击邀请链接
        self.driver.tap([(540, 440)], 500)
        sleep(5)
        # 点击右上角
        self.driver.tap([(1020, 120)], 500)
        sleep(3)
        # 在浏览器中打开
        self.driver.tap([(680, 1380)], 500)
        """
        跳转至填写基本信息界面
        """
        pass
    pass

    def _registered_page_ios(self):

        pass

    #  注册发送邀请链接至微信----------Android部分
    def service_identify_invite_android(self):
        self.action.click(self.choose_friends_locator)
        self.driver.tap([(950, 700)], 500)
        sleep(1)
        # 跳转到微信，点击微信好友
        self.driver.tap([(520, 630)], 500)
        sleep(1)
        # 分享按钮
        self.driver.tap([(850, 1280)], 500)
        sleep(1)
        #  返回网仓三号
        self.driver.tap([(780, 1140)], 500)
        pass



    def android_flow_register(self):
        self._basic_information()
        self._id_card_android()
        self._identify_android_page()
        pass

    def _basic_information(self):
        '''
        基本信息填写
        :return:
        包括拍摄头像、身份证正反面、手机号获取验证码，之后跳转至主页
        '''
        # 输入姓名、身份证号，头像
        self.action.click(self.wechat_login_locator)
        sleep(2)
        self.driver.tap([(640, 1065)], 500) # 微信界面确认登录
        sleep(2)
        self.action.send_keys(self.name_locator, '岳麻麻')
        self.action.send_keys(self.card_id_locator, '420310198710011234')
        self.action.click(self.photo_locator)
        sleep(5)
        self.driver.tap([(550, 1780)], 500)  # 照相机快门按钮
        sleep(5)
        self.driver.tap([(810, 100)], 500)  # 确定
        sleep(5)
        self.driver.tap([(840, 145)], 500)  # 完成
        sleep(5)
        self.action.click(self.nest_step_locator)
        pass

    def _id_card_android(self):
        """
        身份证正反面拍照
        :return:
        """
        self.action.click(self.photo_id_front_locator)
        sleep(5)
        self.driver.tap([(550, 1780)], 500)  # 照相机快门按钮
        sleep(5)
        self.driver.tap([(810, 100)], 500)  # 确定
        self.action.click(self.photo_id_back_locator)
        sleep(5)
        self.driver.tap([(550, 1780)], 500)  # 照相机快门按钮
        sleep(5)
        self.driver.tap([(810, 100)], 500)  # 确定
        sleep(5)
        self.action.click(self.id_photo_next_locator)
        pass

    def _identify_android_page(self):
        """
        手机号验证以及密码设置
        :return:
        主界面--刷新
        """
        self.action.send_keys(self.verify_num_locator, '15577778888')
        self.action.click(self.verify_get_identify_code_locator)
        sleep(6)
        # 获取该手机验证码v
        identify_code = get_invite_sql()
        self.action.send_keys(self.verify_identify_code_locator, value=identify_code)
        # 根据手机号查询验证码SQL
        self.action.send_keys(self.verify_set_pwd_locator, '123456')
        self.action.send_keys(self.verify_confirm_pwd_locator, '123456')
        self.action.click(self.verify_next_step_locator)  # 验证手机下一步
        # 下拉滑动
        self.driver.swipeUp(1000)
        #  刷新
        self.action.click(self.refresh_locator)
        update_invite_SQL()
        pass
