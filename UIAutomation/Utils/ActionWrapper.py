# coding=utf-8
from .Element import get_element
from .Element import get_elements
from .Element import is_element_present
from appium.webdriver.common.touch_action import TouchAction
from .Logger import run_info_log
from .GlobalVar import GlobalVarClass
import traceback
import time

__author__ = "zzh"
__package__ = "IscsUIAutomation"

"""
Action Wrapper, when action placed corresponding log will be recorded in log file.
"""


def action_decorate(func):
    """
    action装饰器
    :param func:
    :return:
    应用example：
        @action_decorate
        def is_element_present(self, locator):
            pass
    """
    def _action_decorate(*args, **kwargs):
        track_str = traceback.extract_stack()
        page_name_all = track_str[-2][0]
        page_name = page_name_all.split("Page\\")[1]
        page_name = page_name.replace("\\\\", "\\")
        msg = "当前执行的Page：" + page_name
        print(msg)
        run_info_log(msg, GlobalVarClass.get_log_file())
        msg = "    Page中执行的函数：" + str(track_str[-2][2])
        print(msg)
        run_info_log(msg, GlobalVarClass.get_log_file())
        msg = "    Page中执行的函数所在行：" + str(track_str[-2][1])
        print(msg)
        run_info_log(msg, GlobalVarClass.get_log_file())
        args_str = ""
        for k, v in enumerate(args):
            if k != 0:
                args_str += str(v) + "  "
        args_str.replace("\\", "")
        msg = "    Action中执行的函数名：" + func.__name__ + "；参数：" + args_str
        print(msg)
        run_info_log(msg, GlobalVarClass.get_log_file())
        try:
            result = func(*args, **kwargs)
            msg = "        操作运行结果：" + str(result)
            print(msg)
            print("")
            run_info_log(msg, GlobalVarClass.get_log_file())
            return result
        except Exception as e:
            msg = "        操作运行结果：失败！"
            print(msg)
            print("")
            run_info_log(msg, GlobalVarClass.get_log_file())
            raise
    return _action_decorate


class Action(object):
    def __init__(self, driver):
        self.driver = driver

    @action_decorate
    def is_element_present(self, locator):
        """
        适用： Android、IOS、Web
        判断当前元素是否存在
        :param locator: 操作的控件
        :return: True or False
        """
        try:
            return is_element_present(self.driver, locator)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def click(self, locator, locator_order=None):
        """
        适用： Android、IOS、Web
        点击操作
        :param locator: 操作的控件
        :param locator_order: list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        # track_str = traceback.extract_stack()
        # msg = "run page：" + str(track_str[-2][2])
        # print(msg)
        # run_info_log(msg, GlobalVarClass.get_log_file())
        # msg = "run action：" + str(locator) + ".click()"
        # print(msg)
        # run_info_log(msg, GlobalVarClass.get_log_file())

        try:
            if locator_order:
                elements = get_elements(self.driver, locator)
                for i in locator_order:
                    elements[i].click()
            else:
                get_element(self.driver, locator).click()
        except Exception as e:
            # print traceback.format_exc()
            # print e.message
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def tap_element(self, locator=None, x=None, y=None, count=1, locator_order=None):
        """
        适用： Android、IOS
        短暂点击控件的指定位置
        :param locator:操作控件
        :param x:在控件上的x坐标位置
        :param y:在控件上的y坐标位置
        :param count:点击次数
        :param locator_order: list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        try:
            if locator_order:
                elements = get_elements(self.driver, locator)
                for i in locator_order:
                    TouchAction(self.driver).tap(elements[i], x, y, count).release().perform()
            else:
                TouchAction(self.driver).tap(get_element(self.driver, locator), x, y, count).release().perform()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def tap_driver(self, positions, duration=None):
        """
        适用： Android、IOS
        短暂点击屏幕上指定的位置，最多可以5根手指同时点击5个位置
        :param positions:点击的位置列表，可以是1-5个位置，eq：[(100,100), (50, 50), [150,30]]
        :param duration:点击的时间，单位为ms
        :return:
        """
        try:
            self.driver.tap(positions, duration)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def long_press(self, locator=None, x=None, y=None, duration=1000, locator_order=None):
        """
        适用： Android、IOS
        长按控件
        :param locator:操作控件
        :param x:在控件上的x坐标位置
        :param y:在控件上的y坐标位置
        :param duration:操作时间，单位为ms
        :param locator_order: list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        try:
            if locator_order:
                elements = get_elements(self.driver, locator)
                for i in locator_order:
                    TouchAction(self.driver).long_press(elements[i], x, y, duration).release().perform()
            else:
                TouchAction(self.driver).long_press(get_element(self.driver, locator), x, y, duration).release().perform()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    def log_screenshot(self, e):
        screenshot_file = GlobalVarClass.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
        self.driver.save_screenshot(GlobalVarClass.get_screenshot_path() + screenshot_file)
        print("        错误截图：")
        print('        <img src="http://192.168.200.171:8020/screenshot/' + screenshot_file + '" width="800px" />')
        run_info_log(str(traceback.format_exc()), GlobalVarClass.get_log_file())
        run_info_log(e, GlobalVarClass.get_log_file())

    @action_decorate
    def clear(self, locator, locator_order=None):
        """
        适用：Android、IOS、Web
        清空text控件中的文本
        :param locator:操作的控件
        :param locator_order:list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        try:
            if locator_order:
                elements = get_elements(self.driver, locator)
                for i in locator_order:
                    elements[i].clear()
            else:
                get_element(self.driver, locator).clear()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def send_keys(self, locator, value, locator_order=None):
        """
        适用： Android、IOS、Web
        在控件上模拟键盘输入,会实现清空原来的值重新输入
        :param locator: 操作的控件
        :param value: 要输入的值
        :param locator_order: list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        try:
            if locator_order:
                elements = get_elements(self.driver, locator)
                for i in locator_order:
                    elements[i].send_keys(str(value))
            else:
                get_element(self.driver, locator).send_keys(str(value))
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def set_value(self, locator, value, locator_order=None):
        """
        适用： IOS
        为控件输入值
        :param locator: 操作的控件
        :param value: 要输入的值
        :param locator_order: list，eq.,[0],[0, 1, 2],默认None。如果控件定位到的是多个控件，要对第几个控件进行操作，
                            可以对多个控件进行操作
        :return:
        """
        try:
            if locator_order:
                elements = get_elements(self.driver, locator)
                for i in locator_order:
                    elements[i].set_value(str(value))
            else:
                get_element(self.driver, locator).set_value(str(value))
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def keyevent(self, code):
        """
        适用Android
        执行键盘操作，如返回、确认等
        :param code:对应的键盘值，int类型。
            home键    66
            菜单键     82
            返回键     4
            电源键     26
            回车键     66
            具体查找    http://blog.csdn.net/doubeizhucele/article/details/44780591
        :return:
        """
        try:
            self.driver.keyevent(int(code))
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def text(self, locator, locator_order=None):
        """
        适用： Android、IOS、Web
        获取控件的text属性值
        :param locator: 操作的控件
        :param locator_order: int,eq.,0,1,默认None。如果控件定位到的是多个控件，要对第几个控件进行操作
        :return: 控件的文本值
        """
        try:
            if locator_order:
                elements = get_elements(self.driver, locator)
                return elements[locator_order].text
            else:
                return get_element(self.driver, locator).text
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def flick(self, start_x, start_y, end_x, end_y):
        """
        适用： Android、IOS
        手指在屏幕上的轻划操作，主要用于实现页面的快速滚动和翻页功能
        :param start_x:移动起点x坐标
        :param start_y:移动起点y坐标
        :param end_x:移动终点x坐标
        :param end_y:移动终点y坐标
        :return:
        """
        try:
            self.driver.flick(start_x, start_y, end_x, end_y)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        """
        适用： Android、IOS
        模拟手指在屏幕上的划动操作，从屏幕起点坐标移动到终点坐标，主要用于激活列表项的快捷操作菜单
        :param start_x:移动起点x坐标
        :param start_y:移动起点y坐标
        :param end_x:移动终点x坐标
        :param end_y:移动终点y坐标
        :param duration:移动花的时间，单位为ms
        :return:
        """
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def scroll(self, origin_locator, destination_locator):
        """
        适用： Android、IOS
        从一个控件位置滚动到另一个控件
        :param origin_locator:源操作控件
        :param destination_locator:滚动到的操作控件
        :return:
        """
        try:
            self.driver.scroll(get_element(self.driver, origin_locator), get_element(self.driver, destination_locator))
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def drag_and_drop(self, origin_locator, destination_locator):
        """
        适用： Android、IOS
        把源控件拖曳到目标控件上
        :param origin_locator:源操作控件
        :param destination_locator:目标操作控件
        :return:
        """
        try:
            self.driver.drag_and_drop(get_element(self.driver, origin_locator),
                                      get_element(self.driver, destination_locator))
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def pinch(self, locator, percent=200, steps=50):
        """
        适用： Android、IOS
        放大操作，可以打开订阅源、打开文章的详情，放大图片
        :param locator:操作控件
        :param percent:放大的%倍数，200即放大200%
        :param steps:放大时操作的步数
        :return:
        """
        try:
            self.driver.pinch(get_element(self.driver, locator), percent, steps)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    def zoom(self, locator, percent=200, steps=50):
        """
        适用： Android、IOS
        缩小操作，可以实现缩小图片等
        :param locator:操作控件
        :param percent:缩小的%倍数，200即放大200%
        :param steps:缩小时操作的步数
        :return:
        """
        try:
            self.driver.zoom(get_element(self.driver, locator), percent, steps)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def get_window_size(self):
        """
        适用： Android、IOS、Web
        获取窗口的尺寸大小
        :return:{"height": xx, "width":xx}
        """
        try:
            return self.driver.get_window_size()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def lock(self, seconds):
        """
        适用： IOS
        锁住设备一段时间
        :param seconds:锁住多少s
        :return:
        """
        try:
            self.driver.lock(seconds)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def pull_file(self, path):
        """
        适用： Android、IOS
        读取设备上的文件内容，以Base64的编码方式返回
        :param path:文件在设备上的绝对路径
        :return:文件内容
        """
        try:
            return self.driver.pull_file(path)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def pull_folder(self, path):
        """
        适用： Android、IOS
        获取设备上的文件夹，以压缩和Base64编码形式返回
        :param path:文件夹在设备上的绝对路径
        :return:文件夹
        """
        try:
            return self.driver.pull_folder(path)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def push_file(self, path, base64data):
        """
        适用： Android、IOS
        将文件上传到设备中
        :param path:文件在设备上的绝对路径
        :param base64data:base64编码的文件内容
        :return:
        """
        try:
            self.driver.push_file(path, base64data)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def reset(self):
        """
        适用： Android、IOS
        重启当前应用
        :return:
        """
        try:
            self.driver.reset()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def contexts(self):
        """
        返回当前session所有的contexts
        :return: context list
        """
        try:
            return self.driver.contexts
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def current_context(self):
        """
        返回当前context
        :return: context
        """
        try:
            return self.driver.current_context
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def background_app(self, seconds):
        """
        适用： Android、IOS
        将允许的应用置为后台运行程序，过一段时间后会自动恢复
        :param seconds:多少s后恢复,int类型
        :return:
        """
        try:
            self.driver.background_app(seconds)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def is_app_installed(self, bundle_id):
        """
        适用： Android、IOS
        确定应用是否安装
        :param bundle_id:应用标识符
        :return:True or False
        """
        try:
            self.driver.is_app_installed(bundle_id)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def install_app(self, app_path):
        """
        适用： Android、IOS
        安装应用
        :param app_path:安装包在设备上的绝对路径
        :return:
        """
        try:
            self.driver.install_app(app_path)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def remove_app(self, app_id):
        """
        适用： Android、IOS
        卸载应用
        :param app_id:应用id
        :return:
        """
        try:
            self.driver.remove_app(app_id)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def launch_app(self):
        """
        适用： Android、IOS
        启动配置在desired_caps中的应用
        :return:
        """
        try:
            self.driver.launch_app()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def close_app(self):
        """
        适用： Android、IOS
        关闭配置在desired_caps中的应用
        :return:
        """
        try:
            self.driver.close_app()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def start_activity(self, app_package, app_activity):
        """
        适用： Android
        打开另外一个activity，activity可以属于另外的应用，此时会启动该应用
        :param app_package:应用包名
        :param app_activity:activity名称
        :return:
        """
        try:
            self.driver.start_activity(app_package, app_activity)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def current_activity(self):
        """
        适用： Android、IOS
        获取当前活动的activity
        :return:activity的字符串
        """
        try:
            self.driver.current_activity
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def wait_activity(self, activity, timeout, interval=1):
        """
        适用： Android、IOS
        等待输入的activity加载
        :param activity:activity字符串
        :param timeout:最长加载等待时间，单位为s
        :param interval:每次重新操作的等待时间，单位为s
        :return:True or False,是否等待加载成功
        """
        try:
            return self.driver.wait_activity(activity, timeout, interval)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def network_connection(self):
        """
        适用： Android
        获取当前网络配置项
        Possible values:
            Value (Alias)      | Data | Wifi | Airplane Mode
            -------------------------------------------------
            0 (None)           | 0    | 0    | 0
            1 (Airplane Mode)  | 0    | 0    | 1
            2 (Wifi only)      | 0    | 1    | 0
            4 (Data only)      | 1    | 0    | 0
            6 (All network on) | 1    | 1    | 0
        :return:
        """
        try:
            return self.driver.network_connection
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def set_network_connection(self, connection_type):
        """
        适用： Android
        设置当前网络配置项
        :param connection_type:配置项，int类型
            Possible values:
                Value (Alias)      | Data | Wifi | Airplane Mode
                -------------------------------------------------
                0 (None)           | 0    | 0    | 0
                1 (Airplane Mode)  | 0    | 0    | 1
                2 (Wifi only)      | 0    | 1    | 0
                4 (Data only)      | 1    | 0    | 0
                6 (All network on) | 1    | 1    | 0
        :return:
        """
        try:
            self.driver.set_network_connection(connection_type)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def available_ime_engines(self):
        """
        适用： Android
        获取当前设备可用的输入法
        :return:e.g., ['com.android.inputmethod.latin/.LatinIME']
        """
        try:
            return self.driver.available_ime_engines
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def is_ime_active(self):
        """
        适用： Android
        是否有输入法被激活
        :return:True or False
        """
        try:
            return self.driver.is_ime_active()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def active_ime_engine(self):
        """
        适用： Android
        获取当前激活的输入法
        :return: 当前激活的输入法，e.g.,'com.android.inputmethod.latin/.LatinIME'
        """
        try:
            return self.driver.active_ime_engine
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def activate_ime_engine(self, engine):
        """
        适用： Android
        激活一个输入法
        :param engine:输入法，e.g.,'com.android.inputmethod.latin/.LatinIME'
        :return:
        """
        try:
            return self.driver.activate_ime_engine(engine)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def deactivate_ime_engine(self):
        """
        适用： Android
        将当前的输入法设置为不激活
        :return:
        """
        try:
            return self.driver.deactivate_ime_engine()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def get_settings(self):
        """
        适用： Android、IOS
        获取当前appium的相关设置项，https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md
        属性：
        ignoreUnimportantViews：True or False，由于 Accessibility 命令在忽略部分元素的情况下执行速度会加快，这个关键字能加快测试执行的速度。被忽略的元素将不能够被找到
        actionAcknowledgmentTimeout：ms，默认3000ms，设置事件动作之间的默认延时。超时和默认延时是不一样的概念，每个动作都会有默认延时，但是不一定都超时，超时主要出现在查找组件上，查找默认是10秒的查找时间，十秒无法找到就会抛出异常
                                    另外改变了动作默认延时，是可以模拟出快速多次点击的效果的，当然这个效果是需要你调节对应的默认时间，调节出来的，这里的调节就如同用swipe来时间拖动一样，需要自己把握，而没有一个固定的值
        keyInjectionDelay：ms，默认200ms，key之间键入的延时
        scrollAcknowledgmentTimeout：ms，默认200ms，滚动动作的延时
        waitForIdleTimeout：ms，默认10000ms，等待当前应用程序空闲的等待时间
        waitForSelectorTimeout：ms，默认10000ms，等待控件被找到的等待时间
        :return:{u'ignoreUnimportantViews': False}
        """
        try:
            return self.driver.get_settings()
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass

    @action_decorate
    def update_settings(self, settings):
        """
        适用： Android、IOS
        设置当前appium的相关设置项，https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md
        属性：
        ignoreUnimportantViews：True or False，由于 Accessibility 命令在忽略部分元素的情况下执行速度会加快，这个关键字能加快测试执行的速度。被忽略的元素将不能够被找到
        actionAcknowledgmentTimeout：ms，默认3000ms，设置事件动作之间的默认延时。超时和默认延时是不一样的概念，每个动作都会有默认延时，但是不一定都超时，超时主要出现在查找组件上，查找默认是10秒的查找时间，十秒无法找到就会抛出异常
                                    另外改变了动作默认延时，是可以模拟出快速多次点击的效果的，当然这个效果是需要你调节对应的默认时间，调节出来的，这里的调节就如同用swipe来时间拖动一样，需要自己把握，而没有一个固定的值
        keyInjectionDelay：ms，默认200ms，key之间键入的延时
        scrollAcknowledgmentTimeout：ms，默认200ms，滚动动作的延时
        waitForIdleTimeout：ms，默认10000ms，等待当前应用程序空闲的等待时间
        waitForSelectorTimeout：ms，默认10000ms，等待控件被找到的等待时间
        :param settings:设置项，e.g.,{u'ignoreUnimportantViews': False}
        :return:
        """
        try:
            return self.driver.update_settings(settings)
        except Exception as e:
            self.log_screenshot(e)
            raise
        pass
