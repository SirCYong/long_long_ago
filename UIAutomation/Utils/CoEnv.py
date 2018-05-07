# coding=utf-8
import os
__package__ = "IscsUIAutomation"
__author__ = 'zzh'


# 获取当前ui_test的文件夹所在位置，如 E:\project\ui_test
def get_app_loc():
    local_dir = os.path.dirname(__file__)

    if not local_dir:
        local_dir = "."

    return local_dir + '/../'


def expand_links(path):
    """
    将路径扩展为绝对路径

    主程序在不同目录下进行测试
    """
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)

    return path
