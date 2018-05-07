from time import sleep
from UIAutomation.Utils import GetCardListFailureException, close_oracle, basic_sit, cit, sit
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import ParseXmlErrorException, get_env_script_runs_on
from UIAutomation.Page import BasePage

__author__ = 'Yong_li'
__package__ = 'IscsUIAutomation'
"""
点击长期卡片,通过sql知道卡片排序,获取想要点击的卡片的位置,滑动到当前页面,点击
"""


class LongCardPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        try:
            self.initial_element()
        except ParseXmlErrorException:
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            raise
        pass

    def is_loaded(self):
        pass

    def click_expected_card(self, user_id, card_name):
        """
        如果想要点击自己期望的那个卡片，传入卡片的中文名字就可以了．
        :param user_id:
        :param card_name:
        :type card_name:
        :return:
        :rtype:
        """
        position = self._get_long_card_position(user_id, card_name)
        swipe_time = self._swap_times(position)

        print("swipe_time------->", swipe_time)
        width = self.action.get_window_size()['width']
        height = self.action.get_window_size()['height']
        self.click_long_task_card()
        sleep(2)
        if self.is_run_ios():
            if swipe_time > 0:
                for i in range(swipe_time):
                    self._swipe_card(width, height)
            self.action.click(('ACCESSIBILITY_ID', card_name))
        else:
            if swipe_time > 0:
                for i in range(swipe_time):
                    self._swipe_card(width, height)
            sleep(2)
            self.driver.find_elements_by_xpath("//*[@text='" + card_name + "']")[-1].click()
        pass

    def click_long_task_card(self):
        """
        点击xx个长期任务
        """
        if self.is_run_ios():
            mobile_size = self.action.get_window_size()
            print(mobile_size)
            width = mobile_size['width']
            height = mobile_size['height']
            h = 479 / 1280.0 * height
            w = width * 0.32
            self.driver.tap([(w, h)], 100)
        else:
            self.action.click(('ID', "suishi_type_card"))
        pass

    def _swipe_card(self, width, height):
        if self.is_run_ios():
            self.action.swipe(width * 5 / 7, height / 2, -(width * 5 / 7), height / 2, 600)   # 6000 >during time > 500 by yongli
            sleep(1)
        else:
            sleep(2)
            self.action.swipe(0.9 * width, 0.5 * height, 0.1 * width, 0.5 * height, 250)
        pass

    @staticmethod
    def _swap_times(position):
        print(position)
        if position % 9 == 0:
            swap_times = int((position - 9) / 9)
        else:
            swap_times1 = (position - 9) / 9 + 1
            swap_times = int(str(swap_times1)[:str(swap_times1).find('.')])
        return swap_times
        pass

    @staticmethod
    def _get_long_card_position(user_id, card_name):
        card_list = []
        # con, curs = cit()
        # con, curs = basic_sit()
        if get_env_script_runs_on().lower() == 'cit':
            con, curs = cit()
        else:
            con, curs = sit()
        try:
            sql = ''' select card_name from xdw_app.v_feature_card v  where 1=1 and owner_bu_id =
            (select h.creator_ukid from xdw_app.hm_creator_relation h where h.participant_ukid = '%s')
            and receiver_id='%s' and client_show >=0 order by card_name''' % (user_id, user_id)
            curs.execute(sql)
            result = curs.fetchall()
            for r in result:
                card_list.append(r[0])
            try:
                position = card_list.index(card_name) + 1
            except Exception as e:
                print(e, 'Get Card List fail.')
                raise GetCardListFailureException
            return position

        except Exception as e:
            print('获取长期卡片出错')
            print(e)
            close_oracle(con, curs)
