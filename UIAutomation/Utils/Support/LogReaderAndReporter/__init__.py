# coding: utf-8

# Author: Yong_li
from os import path
from . import License
from .info import __VERSION__
from .import timemachine
# <p>Copyright (c) 2016-2020 Yong li Zhuang, ISCS Zhe Jiang Ltd</p>
# <p>This module is part of the TestCase package, which is released under a
# BSD-style licence.</p>
import sys
from .LogHandler import log_handler_copy_others, log_handler_analysis, report_to_jira, create_jira_issue_content, log_handler_catalina_out
import os
error_code = 'java.lang.NullPointerException'


"""


"""


def do_log_analysis(env='cit', err_level='critical', logfile=sys.stdout):
    # 由于SCP的关系,目前不支持Windows
    if os.name == 'nt':
        raise OSError
    log = log_handler_copy_others(env)
    analysis_result = log_handler_analysis(log, error_code)
    create_jira_issue_content(analysis_result, error_code)
    pass


def do_catalina_log_analysis(env='DEV'):
    log_handler_catalina_out(env, error_code)



if __name__ == '__main__':
    do_catalina_log_analysis()
