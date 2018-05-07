import unittest

import sys
from nose.tools import assert_equal
from nose.tools import assert_is_not_none

from UIAutomation.Page import BasePage
from UIAutomation.Utils import get_user_id, get_android_udid, get_ios_udid
from UIAutomation.Utils.EnvSettingReader import get_env_script_runs_on


class TestAppium(unittest.TestCase):
    def test_get_user_id(self):
        cit_username = 15514511010
        sit_username = 15624301115
        if get_env_script_runs_on().lower() == 'cit':
            assert_equal(get_user_id(cit_username), 10001469)
        else:
            assert_equal(get_user_id(sit_username), 10001474)
            pass

    def test_get_ud_id(self):
        if sys.platform == "darwin":
            assert_is_not_none(get_ios_udid())
        else:
            assert_is_not_none(get_android_udid())