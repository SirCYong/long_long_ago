# coding: utf-8
import getpass

import sys
import jenkins
import logging


__author__ = 'yong_li'


"""
Basic Jenkins Job handler.
PBD has problem, so debug pls in cli.
"""

logger = logging.getLogger(__name__)

class Jober(object):
    def __init__(self, url='http://jenkins.iscs.com.cn/'):
        """
        ISCS default Jenkins address.
        :param url:
        :type url:
        """
        if sys.version_info < (3, 6, 0):
            username = raw_input('Enter your jenkins username:')
        else:
            username = input('Enter your jenkins username')
        if sys.platform == 'win32':
            password = getpass.win_getpass()
        else:
            password = getpass.unix_getpass()
        self.server = jenkins.Jenkins(url, username, password)
        logger.debug('Connect to Jenkins successfully.')
        pass

    def create_new_job(self, job_name, job_config_xml):
        """
        Create new job when the Job name not exist.
        :param job_name:
        :type job_name:
        :param job_config_xml:
        :type job_config_xml:
        :return:
        :rtype:
        """
        try:
            self.server.create_job(job_name, job_config_xml)
        except jenkins.JenkinsException as e:
            # logger.error(e.message)
            print(e.message)
        pass

    def create_job(self, job_name, job_config_xml):
        """
        Create new job anyway.
        :param job_name:
        :type job_name:
        :param job_config_xml:
        :type job_config_xml:
        :return:
        :rtype:
        """
        try:
            self.delete_job(job_name)
        except jenkins.JenkinsException:
            self.create_new_job(job_name, job_config_xml)
            return
        self.create_new_job(job_name, job_config_xml)
        pass

    def delete_job(self, job_name):
        self.server.delete_job(job_name)
        pass

    def update_job(self):
        pass

    def enable_job(self,job_name):
        self.server.enable_job(job_name)
        pass



