# coding:utf-8

from time import sleep

from UIAutomation.Utils import get_elements
from UIAutomation.Page.Mobile.Android.Register.follow import FollowPage


class HWMobilePhone():

    def MobilePhoneForHw(self):

        PageFollow = FollowPage(self.driver)
        PageFollow.click_team_three_btn_element()  # 点击伟大的三组button
        sleep(1)
        PageFollow.click_login_input_element()  # 进入界面后，输入10000243
        sleep(1)
        PageFollow.click_login_btn_element()  # 点击登录
        # 服务认证邀请
        LinearLayout = get_elements(self.driver, ("CLASS_NAME", "android.widget.LinearLayout"))
        LinearLayout[3].click()
        PageFollow.click_select_friend_btn_element()  # 选择好友
        sleep(1)
        # 选择测试账号
        Invite_Button = get_elements(self.driver, ("CLASS_NAME", "android.widget.Button"))
        Invite_Button[1].click()
        sleep(2)
        # 跳转至微信界并点击人物
        self.driver.tap([(240, 590)], 500)
        sleep(2)
        # 分享按钮
        self.driver.tap([(870, 1190)], 500)
        sleep(4)
        # 留在微信
        # self.driver.tap([(757, 1055)], 500)
        self.driver.tap([(820, 1155)], 500)
        sleep(2)
        # 点击微信界面：测试账号
        self.driver.tap([(240, 590)], 500)
        sleep(2)
        # 点击邀请链接
        self.driver.tap([(620, 835), 500])
        sleep(2)
        # 点击下载客户端右边按钮
        self.driver.tap([(1015, 130), 500])
        sleep(2)
        # 点击在浏览器中打开 -->跳入网仓三号
        self.driver.tap([(900, 700), 500])
        pass