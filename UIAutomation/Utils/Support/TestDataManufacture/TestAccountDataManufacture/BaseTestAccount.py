# coding: utf-8
# Author: Yong_li
import abc


class BaseTestAccount(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.role_definition()
        print("""
        测试账号
        """)
        pass


    @abc.abstractmethod
    def is_defined_in_database(self):
        pass

    @abc.abstractmethod
    def recover_to_original(self):
        pass

    def role_definition(self):
        pass
