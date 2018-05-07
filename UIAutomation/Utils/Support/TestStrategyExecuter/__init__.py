#  Copyright 2016-     iscs.com.cn
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
Jenkins Job automation creator:
It will create two Jobs iOS and Android job in Jenkins according to Test Strategy in configuration.ini

"""
import sys
import os

from Jober import Jober
from ConfigXML.ConfigXML import two_platform_jobs_xml
from TestStrategyHandler import TestStrategyHandler

__author__ = "yong_li"
__version__ = "0.0.1"
__all__ = ['Jober', 'two_platform_jobs_xml', 'TestStrategyHandler']

if __name__ == '__main__':
    """
    Main entrance to Create JOb according to Defined 'TestStrategy.ini'.
    """
    # .ini configuration file
    strategy_cfg_file = sys.argv[1]
    dir_name = os.path.dirname(os.path.abspath(__name__)) + '/TestStrategyConfiguration/'
    if strategy_cfg_file in os.listdir(dir_name):
        strategy_value = TestStrategyHandler().strategy_reader(strategy_cfg_file)
    else:
        raise ValueError("Input configuration '%s' is not exist." % strategy_cfg_file)
    job1_xml_configuration, job2_xml_configuration = two_platform_jobs_xml(strategy_value)
    jober = Jober()
    try:
        jober.create_job('Test_job1', job1_xml_configuration)
        jober.create_job('Test_job2', job2_xml_configuration)
        enable_job = raw_input('Enable Job(Y/N): ')
        if enable_job == 'Y' or enable_job == 'y':
            jober.enable_job('Test_job1')
            jober.enable_job('Test_job2')
    except Exception as e:
        print(e.message)







