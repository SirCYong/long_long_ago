# coding=utf-8
"""
时间操作
"""
import sys
import datetime
import time as sys_time
import logging
__package__ = "IscsUIAutomation"
__author__ = 'zzh'

old_sys_path = sys.path
sys.path = sys.path[1:] + sys.path[:1]

# 获取当前时间戳
now = sys_time.time()
sys.path = old_sys_path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(__name__)

DAY_TS = 86400


def get_expire_time(expire_days, begin_time=0):
    """
    计算过期时间，精准到毫秒（13位时间戳）

    int ->

    :param begin_time: 开始时间（时间戳）

    :param expire_days: 有效天数，不可以为0

    .. code-block:: python
        :linenos:

        >>> ts = get_expire_time(1, 0)
        >>> print ts

    """
    if begin_time == 0:
        # 现在的时间戳
        begin_time = int(sys_time.time()) * 1000 + datetime.datetime.now().microsecond/1000

    expires_microsecond = 1000 * 60 * 60 * 24 * int(expire_days)

    expire_time = begin_time + expires_microsecond

    return expire_time


def gen_time_str(t_info):
    """
    从时间信息生成要访问的日志文件名

    20150101

    """
    year = str(t_info.tm_year)

    if t_info.tm_mon < 10:
        month = '0'+str(t_info.tm_mon)
    else:
        month = str(t_info.tm_mon)

    if t_info.tm_mday < 10:
        day = '0'+str(t_info.tm_mday)
    else:
        day = str(t_info.tm_mday)

    return year+month+day


def get_date_ymd():
    """

    :return:

    .. code-block:: python
        :linenos:

        >>> ymd = get_date_ymd()
        >>> print ymd

    """

    now = sys_time.time()

    ltime = sys_time.localtime(now)

    return gen_time_str(ltime)


def info():
    """

    info() -> time_struct

    :return:

    .. code-block:: python
        :linenos:

        >>> time_struct = info()
        >>> print time_struct

    """
    print("time")
    return sys_time.localtime()


def get_ts():
    """
    系统时间戳，整型
    """
    return int(sys_time.time())


def get_log_time():
    """
    返回下划线分割的格式

    .. code-block:: python

        >>> print get_log_time()

    """
    return datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')


def get_cur_date(fmt="%Y-%m-%d"):
    """

    :param fmt:
    :return:

    .. code-block:: python

        >>> get_cur_date()
        >>> get_cur_date("%Y%m%d")

    """
    return datetime.datetime.now().strftime(fmt)


class CoTime(object):
    def __init__(self, init_day=None):
        """

        :param init_day:
        :return:
        """
        self.ts = 0
        self.fmt = "%Y-%m-%dT%H:%M:%S"

        if init_day is None:
            init_day = sys_time.time()

        if isinstance(init_day, float) or isinstance(init_day, int):
            # print "浮点型"
            self.ts = int(init_day)
            self.t_info = sys_time.localtime(self.ts)

            # 浮点表示
            self.ts_f = sys_time.mktime(self.t_info)
        elif isinstance(init_day, str):
            # print "字符串"
            # 字符串 -> 时间结构
            self.t_info = sys_time.strptime(init_day, "%Y-%m-%d %H:%M:%S")
            self.ts_f = sys_time.mktime(self.t_info)
            self.ts = int(self.ts_f)

    def get_dt(self):
        """
        ts -> datetime

        """
        return datetime.datetime(self.get_year(), self.get_month(), self.get_day(), 0, 0, 0)

    def get_ts(self):
        return self.ts

    def get_year(self):
        return self.t_info.tm_year

    def get_month(self):
        return self.t_info.tm_mon

    def get_day(self):
        return self.t_info.tm_mday

    def get_weekday(self):
        """
        返回周几
        周一返回1
        """
        return self.t_info.tm_wday + 1

    def get_t_info(self):
        """

        """
        return self.t_info

    def next_day(self, factor=1):
        self.ts += DAY_TS * factor
        self.t_info = sys_time.localtime(self.ts)
        return self

    def get_format_str(self, f=None):
        """
        """
        if f is None:
            f = self.fmt

        return sys_time.strftime(f, self.t_info)

    def iso8601(self):
        fmt = "%Y-%m-%dT%H:%M:%S"
        return self.get_format_str(fmt)


def dt():
    """
    返回当前时区日期时间对象

    void -> datetime

    :return:

    .. code-block::python

        >>> print dt()
        >>> print type(dt())

    """
    return datetime.datetime.now()


def dt_to_struct(s):
    """
    datetime -> time_struct

    :param s:
    :return:

    .. code-block:: python

        >>> dt = datetime.datetime.now()
        >>> print dt_to_struct(dt)
    """
    return s.timetuple()


def dt_to_int(s):
    """

    s -> int

    :param s:
    :return:
    """
    timestamp = int(sys_time.mktime(s.timetuple()))
    return timestamp


def struct_to_int(s):
    timeStamp = int(sys_time.mktime(s))
    return timeStamp


def int_to_struct(ts):
    t_info = sys_time.localtime(ts)
    return t_info


def int_to_str(ts, fmt="%Y-%m-%d"):
    t_info = int_to_struct(ts)
    return sys_time.strftime(fmt, t_info)


def dt_to_str(dt, fmt="%Y-%m-%d"):
    return dt.strftime(fmt)


def str_to_o(s, fmt="%Y-%m-%d"):
    ts = sys_time.mktime(sys_time.strptime(s, fmt))
    return CoTime(ts)


def utc():
    """

    :return:
    """
    print(datetime.datetime.utcnow())


def main():
    # struct -> int
    dt = datetime.datetime.now()
    print("从datetime转为int")
    print(dt_to_int(dt))
    print("从struct转为int")
    ts = struct_to_int(dt.timetuple())
    print(ts)

    print(int_to_str(ts))

    print("datetime utc标准日期时间", utc())


if __name__ == '__main__':
    info()

    logger.info("获取今天时间戳")
    time_o = str_to_o("2015-12-01")
    logger.info(time_o.get_ts())
    logger.info(time_o.get_dt())

    print("获取当前时间戳，浮点数")
    print(sys_time.time())

    print("获取当前时间戳，整型")
    print(get_ts())

    print("获取当前时间struct")
    print(sys_time.localtime())

    print("datetime获取当前时间")
    print(datetime.datetime.now())

    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
    print("三天前的时间字符串Y-m-d H:i:s")
    print(threeDayAgo)

    # datetime -> struct
    print("三天前的时间struct")
    print(threeDayAgo.timetuple())

    main()

    print("从struct转为int")
    print("从str转为int")
    # struct -> int

    # mktime(str) -> struct
    # strftime
    timeStamp = int(sys_time.mktime(threeDayAgo.timetuple()))
    otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
    print(timeStamp)
    print(otherStyleTime)
    print(get_log_time())

    import time
    print("Y-m-d")
    print(time.strftime("%Y-%m-%d"))
    d = "2014-01-01 0:0:0"
    # time format
    tf = "%Y-%m-%d %H:%M:%S"
    # strptime(str, format) -> struct
    # struct -> int/float
    # int/float -> str
    # mktime
    # format, struct -> str
    # time.strftime()
    t = time.mktime(time.strptime(d, "%Y-%m-%d %H:%M:%S"))
    print(time.strptime(d, tf))
    print("时间戳", t)

    # 测试CoTime类
    cot1 = CoTime(time.time())
    print("获取cot1时间戳", cot1.get_ts())
    print(cot1.get_weekday())

    cot2 = CoTime(d)
    print("获取cot2时间戳", cot2.get_ts())
    print(cot2.get_weekday())

