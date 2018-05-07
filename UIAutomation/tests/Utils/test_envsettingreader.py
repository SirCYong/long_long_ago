import unittest

from nose.tools import assert_equal
from UIAutomation.Utils import get_setting_configuration, get_env_script_runs_on


class TestEnvSettingReader(unittest.TestCase):
    def test_get_setting_configuration(self):
        assert_equal('Android', get_setting_configuration('android', 'platformName'))
        assert_equal('.activity.base.LauncherActivity', get_setting_configuration('android', 'appActivity'))
        assert_equal('com.iscs.SmallAnimal', get_setting_configuration('ios', 'bundleId'))

    def test_get_env_script_runs_on(self):
        assert get_env_script_runs_on().lower() == 'cit' or get_env_script_runs_on().lower() == 'sit'


