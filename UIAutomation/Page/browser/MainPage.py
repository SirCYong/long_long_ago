# -*- coding: utf-8 -*-
from UIAutomation.Page import BasePage


class MainPage(BasePage):

    def initial_element(self):
        pass

    def page_factory(self):
        pass

    def is_loaded(self):
        assert self.driver.title in u'网仓3号'
        pass
