from time import sleep
from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Page.BasePage import compatible, platform
from UIAutomation.Page.Mobile.LongCardPage import LongCardPage
from UIAutomation.Page.Mobile.MainPage.MainPage import MainPage
from UIAutomation.Utils import is_element_present
from UIAutomation.Utils import page_element_factory,ParseXmlErrorException, initial_element_error_wrapper


__author__ = "LiYu"
__doc__ = "发布劳务需求的任务"


class PublishLabour(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver

        try:
            self.initial_element()
        except ParseXmlErrorException:
            initial_element_error_wrapper(self.driver)
            raise

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            initial_element_error_wrapper(self.driver)
            raise
        pass

    def page_factory(self):
        """
        初始化页面控件
        """
        # 2端统一的控件
        name_list = ['Please_select', 'Picking', 'Packaging', 'Handover', 'move', 'unload', 'Shelves',
                     'Warehousing_transition', 'point', 'confirm', 'input', 'DayShift', 'SelectDate',
                     'SelectAddress', 'Province', 'Provinces_city', 'Provinces_cities_area', 'Location',
                     'Yuan_time', 'Yuan_piece', 'Immediately_release', 'close', 'Location', 'complete']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.please_select_locator = ele_dic['Please_select']
        self.picking_locator = ele_dic['Picking']
        self.packaging_locator = ele_dic['Packaging']
        self.handover_locator = ele_dic['Handover']
        self.shelves_locator = ele_dic['Shelves']  # 上架
        self.move_locator = ele_dic['move']
        self.unload_locator = ele_dic['unload']
        self.warehousing_transition_locator = ele_dic['Warehousing_transition']
        self.point_locator = ele_dic['point']
        self.confirm_locator = ele_dic['confirm']
        self.input_locator = ele_dic['input']
        self.dayshift_locator = ele_dic['DayShift']
        self.selectdate_locator = ele_dic['SelectDate']
        self.selectaddress_locator = ele_dic['SelectAddress']
        self.province_locator = ele_dic['Province']
        self.provinces_city_locator = ele_dic['Provinces_city']
        self.provinces_cities_area_locator = ele_dic['Provinces_cities_area']
        self.location_locator = ele_dic['Location']
        self.yuan_time_locator = ele_dic['Yuan_time']
        self.yuan_piece_locator = ele_dic['Yuan_piece']
        self.immediately_release_locator = ele_dic['Immediately_release']
        self.close_locator = ele_dic['close']
        self.location_locator = ele_dic['Location']
        self.complete_locator = ele_dic['complete']

    def click_public_labor(self):
        """
        发布劳务需求
        :return:
        """
        if self.is_run_ios():
            if is_element_present(self.driver, ('ACCESSIBILITY_ID', '发布劳务需求')):
                MainPage(self.driver).click_publish_labor_ios()
                self._publish_labour_ios()
        if not self.is_run_ios():
            #LongCardPage(self.driver).click_expected_card(user_id=10001396, card_name='发布劳务需求')
            if is_element_present(self.driver, ("XPATH", "//*[@resource-id='com.iscs.mobilewcs:id/text' and @text='找劳务需求']")):
                sleep(5)
                self.click_swipe_left(x1=1.5, y1=0.5, x2=0.2, y2=0.5, time=2000)
                self.click_swipe_left(x1=1.5, y1=0.5, x2=0.2, y2=0.5, time=2000)
            MainPage(self.driver).click_publish_labor_android()
            self._public_labour_android()
            pass

    def is_loaded(self):
        pass

    def _publish_labour_ios(self):
        self.select_work_type_ios()
        # 白班
        self.action.click(self.dayshift_locator)
        # 起始时间
        self.select_time_ios()
        # 人数
        self.action.set_value(self.input_locator, value=58)
        self.close()
        # 选择地址
        self.action.click(self.selectaddress_locator)
        self.select_address_ios()
        res = self.action.is_element_present(self.location_locator)
        assert_that(res, equal_to(True), u"浙江省 杭州市 西湖区")
        sleep(2)
        self.action.set_value(self.yuan_time_locator, value=26)
        self.close()
        self.action.set_value(self.yuan_piece_locator, value=2.5)
        self.close()
        # 立即发布
        self.action.click(self.immediately_release_locator)
        pass

    def select_work_type_ios(self):
        """
        ios:选择工种(全选)
        :return:
        """
        # 请选择
        self.action.click(self.please_select_locator)
        # 拣选
        self.action.click(self.picking_locator)
        # 包装
        self.action.click(self.packaging_locator)
        # 移动
        self.action.click(self.move_locator)
        # 交接
        self.action.click(self.handover_locator)
        # 入库交接
        self.action.click(self.warehousing_transition_locator)
        # 卸货
        self.action.click(self.unload_locator)
        # 点数
        self.action.click(self.point_locator)
        # 上架
        self.action.click(self.shelves_locator)
        # 确定
        self.action.click(self.confirm_locator)

    def select_time_ios(self):
        """
        公共控件：选择时间（方便其他模块使用）
        :return:
        """
        self.action.click(self.selectdate_locator)
        self.action.click(self.confirm_locator)

    def select_address_ios(self):
        """
        公共控件：选择地址省、市、区
        :return:
        """
        self.action.click(self.province_locator)
        self.action.click(self.provinces_city_locator)
        self.action.click(self.provinces_cities_area_locator)

    def close(self):
        """
        ios:关闭键盘
        :return:
        """
        self.action.click(self.close_locator)

    def _public_labour_android(self):
        self.select_work_type_android()
        # 班次：白班
        self.action.click(self.dayshift_locator)
        # 人数：50
        self.action.clear(self.input_locator)
        self.action.send_keys(self.input_locator, value=50)
        self.action.clear(self.yuan_time_locator)
        self.action.send_keys(self.yuan_time_locator, value=18)
        self.action.clear(self.yuan_piece_locator)
        self.action.send_keys(self.yuan_piece_locator, value=12)  # 输入浮点型会报错，暂时未查看具体原因
        self.select_time_android()
        self.select_address_android()
        self.action.click(self.immediately_release_locator)
        pass

    def select_work_type_android(self):
        """
        android:选择工种
        :return:
        """
        self.action.click(self.please_select_locator)
        self._select_work_type_all()
        pass

    @compatible("huawei6")
    def _select_work_type_huawei6(self):
        window_width = self.action.get_window_size()['width']
        window_height = self.action.get_window_size()['height']

        self.action.tap_driver([(window_width*0.5046, window_height*0.3755)])
        sleep(1)
        self.action.tap_driver([(window_width*0.4814, window_height*0.9284)])

    @compatible("all")
    def _select_work_type_all(self):
        window_width = self.action.get_window_size()['width']
        window_height = self.action.get_window_size()['height']

        self.action.tap_driver([(window_width * 0.5046, window_height * 0.3755)])
        sleep(1)
        self.action.tap_driver([(window_width * 0.4814, window_height * 0.9284)])

    def select_time_android(self):
        """
        android：选择时间
        :return:
        """
        self.action.click(self.selectdate_locator)
        self.action.click(self.complete_locator)
        #self.action.tap_driver([(self.x1, 1700)], 1000)
        pass

    def select_address_android(self):
        """
        android:选择省市区(浙江省/杭州市/西湖区)
        :return:
        """
        self.action.click(self.selectaddress_locator)
        self.click_swipe_up(x1=1, y1=1, x2=1, y2=1/2, time=2000)
        sleep(2)
        self.action.click(self.province_locator)
        self.action.click(self.provinces_city_locator)
        self.action.click(self.provinces_cities_area_locator)

    def get_windows_size(self):
        mobile_size = self.action.get_window_size()
        x = mobile_size['width']
        y = mobile_size['height']
        self.y1 = 479 / 1280.0 * y
        self.x1 = x / 2.0
        return self.x1, self.y1

    def click_swipe_left(self, x1, y1, x2, y2, time):
        """
        左划
        :return:
        """
        l = self.get_windows_size()
        print(l)
        self.action.swipe(x1*l[0], y1*l[1], x2*l[0], y2*l[1], time)
        pass

    def click_swipe_right(self, x1, y1, x2, y2, time):
        """
        右划
        :return:
        """
        l = self.get_windows_size()
        print(l)
        self.action.swipe(x1*l[0], y1*l[1], x2*l[0], y2*l[1], time)
        pass

    def click_swipe_up(self, x1, y1, x2, y2, time):
        """
        上划
        :return:
        """
        l = self.get_windows_size()
        print(l)
        self.action.swipe(x1 * l[0], y1 * l[1], x2 * l[0], y2 * l[1], time)
        pass

    def click_swipe_down(self, x1, y1, x2, y2, time):
        """
        下划
        :return:
        """
        l = self.get_windows_size()
        print(l)
        self.action.swipe(x1 * l[0], y1 * l[1], x2 * l[0], y2 * l[1], time)
        pass



