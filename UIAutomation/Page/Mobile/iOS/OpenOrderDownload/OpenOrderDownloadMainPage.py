from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory,ParseXmlErrorException
from UIAutomation.Page import BasePage


class OpenOrderDownloadMainPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.store_name_locator = None
        self.year_locator = None
        self.month_locator = None
        self.day_locator = None
        self.open_download_locator = None
        self.download_order_by_date_locator = None
        self.determine_locator = None
        self.return_locator = None
        try:
            self.is_loaded()
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
        name_list = ['store_name',
                     'year',
                     'month',
                     'day',
                     'open_download',
                     'download_order_by_date',
                     'determine',
                     'return']
        ele_dic = page_element_factory(__file__, name_list)
        self.store_name_locator = ele_dic['store_name']  # 旗舰店
        self.year_locator = ele_dic['year']  # 年
        self.month_locator = ele_dic['month']  # 月
        self.day_locator = ele_dic['day']  # 日
        self.open_download_locator = ele_dic['open_download']  # 开启下载
        self.download_order_by_date_locator = ele_dic['download_order_by_date']  # 返回
        self.determine_locator = ele_dic['determine']
        self.return_locator = ele_dic['return']
        pass

    def is_loaded(self):

        pass
