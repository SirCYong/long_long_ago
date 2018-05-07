# coding=utf-8

from UIAutomation.Utils import CoEnv as cofFile
import configparser
import os
import logging

from .CoTime import get_log_time

__package__ = "IscsUIAutomation"
__author__ = 'zzh'

# 全局变量
gblCfp = configparser.ConfigParser()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CFGTYPE = None
CASELEVEL = None


class MyCfg(object):
    """
    配置信息对象

    ..code-block:: python

        >>> conf_o = MyCfg('cfg.ini')
        >>> conf_o.set_section('section')
        >>> conf_o.get('key')

    """

    # 版本
    VERSION = ""

    # 测试标识
    TEST = "test-" + str(get_log_time())

    # 报告列表
    REPORTS = None

    # 日志级别
    LOGLEVEL = logging.ERROR

    CASE_INFO = dict()

    CASE_TYPE = 'ui'

    def __init__(self, path):
        app_loc = cofFile.get_app_loc()
        cfg_type = get_cfg_type()

        if cfg_type == "debug":
            cfg_type = "test"

        path = app_loc + 'config' + os.sep + cfg_type + os.sep + path
        ex_path = cofFile.expand_links(path)
        if not os.path.exists(ex_path):
            print("config file is not exist (" + ex_path + ")")
            raise Exception("配置文件不存在" + ex_path)
        self.path = ex_path
        self.sec = ""
        self.cfg_obj = configparser.ConfigParser()
        self.cfg_obj.read(self.path)

    def set_section(self, section):
        self.sec = section

    def get(self, key):
        logger.info(self.sec)
        logger.info(key)
        return self.cfg_obj.get(self.sec, key)

    # 为section的字段赋值
    def set(self, section, option, value):
        self.set(section, option, value)

    def get_section(self, sec_name):
        return self.cfg_obj.items(sec_name)


# 获取配置类型
def get_cfg_type_path():
    filepath = cofFile.get_app_loc() + 'config/cfgtype.ini'
    logger.info(filepath)
    return filepath


# 获取配置目录
def get_cfg_type():

    if CFGTYPE is None:
        filepath = get_cfg_type_path()
        cfgtype = None

        try:
            gblCfp.read(filepath)
            cfgtype = gblCfp.get('cfg', "type")
        except Exception as e:
            logger.error(e)

        if cfgtype is None or cfgtype == "None":
            cfgtype = "development"

        return cfgtype
    else:
        return CFGTYPE


def set_cfg_type(env='test'):
    filepath = get_cfg_type_path()
    gblCfp.read(filepath)
    cfgtype = gblCfp.set('cfg', "type", env)
    gblCfp.write(open(filepath, "w"))
    return cfgtype


def read_db_cfg(cfgfile, db):
    """读取数据配置数据"""
    cf = configparser.ConfigParser()
    cf.read(cfgfile)
    dbcfg = dict()
    dbcfg['host'] = cf.get(db, "hostname")
    dbcfg['user'] = cf.get(db, "username")
    dbcfg['pass'] = cf.get(db, "password")
    dbcfg['db'] = cf.get(db, "database")
    return dbcfg

if __name__ == "__main__":
    o = MyCfg('cfg.ini')
    o.set_section('report')
    print(o.get('path'))
