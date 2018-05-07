# -*- coding: utf-8 -*-
import abc
import sys
import time
import importlib
import inspect
from selenium.common.exceptions import NoSuchElementException
from UIAutomation.Utils import CoEnv
from UIAutomation.Utils import ParseXmlErrorException
from UIAutomation.Utils import Action
from UIAutomation.Utils import GlobalVarClass


def platform(platform_name):
    """
    平台装饰器
    :param platform_name: ios/android/all
    :return:
    应用example：
        @platform("ios")
        def login_ios():
            print("ios")

        @platform("android")
        def login_android():
            print("android")

        @platform("all")
        def login_all():
            print("all")

        if __name__ == "__main__":
            # 只需要调用3个login其中的一个，就可以根据运行平台自动识别运行哪个函数
            login_ios()
    """
    def _platform(func):
        def __platform(*args, **kwargs):
            if func.__name__.find(GlobalVarClass.get_platform()) >= 0:
                func(*args, **kwargs)
            elif func.__name__.find("all") >= 0 and GlobalVarClass.get_circle_num() > 1:
                func(*args, **kwargs)
            else:
                GlobalVarClass.set_circle_num(GlobalVarClass.get_circle_num() + 1)
                cls = args[0]
                func_name = func.__name__.replace(platform_name, GlobalVarClass.get_platform())
                new_args = list(args)
                new_args.pop(0)
                try:
                    getattr(cls, func_name)(*new_args, **kwargs)
                except Exception as e:
                    func_name = func.__name__.replace(platform_name, "all")
                    getattr(cls, func_name)(*new_args, **kwargs)
                    GlobalVarClass.set_circle_num(1)
                pass
        return __platform
    return _platform


def compatible(device_name):
    """
    设备兼容性装饰器
    :param device_name:
    :return:
    应用example：
        @compatible("huawei6")
        def login_huawei6():
            print("huawei6")

        @compatible("hongmi")
        def login_hongmi():
            print("hongmi")

        @compatible("all")
        def login_all():
            print("all")

        if __name__ == "__main__":
            # 只需要调用3个login其中的一个，就可以根据运行设备自动识别运行哪个函数
            login_hongmi()
    """
    def _compatible(func):
        def __compatible(*args, **kwargs):
            if func.__name__.find(GlobalVarClass.get_device_name()) >= 0:
                func(*args, **kwargs)
            elif func.__name__.find("all") >= 0 and GlobalVarClass.get_circle_num() > 1:
                func(*args, **kwargs)
            else:
                GlobalVarClass.set_circle_num(GlobalVarClass.get_circle_num() + 1)
                cls = args[0]
                func_name = func.__name__.replace(device_name, GlobalVarClass.get_device_name())
                new_args = list(args)
                new_args.pop(0)
                try:
                    getattr(cls, func_name)(*new_args, **kwargs)
                except Exception as e:
                    func_name = func.__name__.replace(device_name, "all")
                    getattr(cls, func_name)(*new_args, **kwargs)
                    GlobalVarClass.set_circle_num(1)
                pass
        return __compatible
    return _compatible


class BasePage(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver, filename):
        self.screen_shot_name = __name__
        self.driver = driver
        self.action = Action(driver)

        if self.is_run_ios():
            self.xml_file = filename[:filename.rfind(".")] + "IOS.xml"
            self.standard_xml_file = filename[:filename.rfind(".")] + "_ios.xml"
        else:
            self.xml_file = filename[:filename.rfind(".")] + "Android.xml"
            self.standard_xml_file = filename[:filename.rfind(".")] + "_android.xml"

        try:
            self.is_loaded()
        except NoSuchElementException:
            pass
        finally:
            pass

    def is_run_ios(self):
        """
        判断当前运行的是否是IOS
        :return:
        """
        if sys.platform == "darwin":
            return True
        else:
            return False

    def screen_shot(self):
        self.driver.save_screenshot(self.screen_shot_name)

        pass

    @abc.abstractmethod
    def is_loaded(self):
        """
        assert
        判断是否是当前页面
        try:
            self.driver.find_element_by_name("q")
            :return Ture
        :except NoSuchElementException:
            :return False

        """
        pass

    @abc.abstractmethod
    def page_factory(self):
        pass
        # try:
        #     raise ParseXmlErrorException(u"解析XML出错！")
        # except ParseXmlErrorException:
        #     print(u"解析XML出错！")
        # pass

    @abc.abstractmethod
    def initial_element(self):

        pass

    def get_exclude_initialized_element(self, driver, name_list, __file__):
        self.is_loaded()
        return

    def is_long_card_present_by_swipe(self, locator, swipe_count):
        """
        找到对应的长期卡片
        :param locator:
        :param swipe_count: 预计最多需要左划的次数
        :return: True or False
        """
        if self.action.is_element_present(locator):
            return True
        else:
            for i in range(swipe_count):
                width = self.action.get_window_size()["width"]
                height = self.action.get_window_size()["height"]
                start_x = width * 9/10
                start_y = height - 20
                end_x = width * 1/10
                end_y = 10
                self.action.swipe(start_x, start_y, end_x, end_y, 2000)
                time.sleep(2)
                if self.action.is_element_present(locator):
                    return True
            return False

