# coding: utf-8

"""
Read TestStrategy from *.ini configuration file.
"""
import os
from configparser import ConfigParser
__author__ = 'Yong_li'

class TestStrategyHandler(object):
    def __init__(self):
        self.para_value = {}
        pass

    @staticmethod
    def find_strategy_file(start, name):
        for relpath, dirs, files in os.walk(start):
            if name in files:
                full_path = os.path.join(start, relpath, name)
                return full_path
        pass

    def strategy_reader(self, name):
        ini_abs_path = self.find_strategy_file(os.path.dirname(os.path.abspath(__name__)), name)
        """
        Get definition of strategy and return it to job creator.
        :return:
        :rtype:
        """
        configure_reader = ConfigParser()
        configure_reader.read_file(open(ini_abs_path))
        self.para_value.update({'strategy_name': configure_reader.get('TestStrategy', 'StrategyName')})
        self.para_value.update({'strategy_file': configure_reader.get('TestStrategy', 'FileRootPath')})
        self.para_value.update({'smoke_test': configure_reader.getboolean('TestStrategy', 'SmokeTest')})
        self.para_value.update({'run_first_set': configure_reader.get('TestStrategy', 'RunFirstSet')})
        self.para_value.update({'run_set': configure_reader.get('TestStrategy', 'RunSet')})
        self.para_value.update({'iOS_Run_Host': configure_reader.get('JenkinsiOSHost', 'iOSRunHost')})
        self.para_value.update({'android_run_host': configure_reader.get('JenkinsAndroidHost', 'AndroidRunHost')})
        self.para_value.update({'time_trigger_cycle': configure_reader.get('JenkinsJobParameters', 'TimeTriggerCycle')})
        self.para_value.update({'build_shell_1': configure_reader.get('JenkinsJobParameters', 'BuildShelll')})
        self.para_value.update({'build_shell_2': configure_reader.get('JenkinsJobParameters', 'BuildShell2')})
        self.para_value.update({'junit_test_reporter': configure_reader.get('JenkinsJobParameters', 'JunitTestReport')})
        self.para_value.update({'pass_threshold': configure_reader.get('JenkinsJobParameters', 'PassThreshold')})
        self.para_value.update({'recipient': configure_reader.get('JenkinsJobParameters', 'recipient')})
        return self.para_value
        pass
if __name__ == '__main__':
    print os.path.abspath(__name__)