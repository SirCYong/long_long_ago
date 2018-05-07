import unittest
from nose.tools import assert_equal
import sys
from UIAutomation.Utils import CMD


class TestCMD(unittest.TestCase):
    def test_exec_cmd_function(self):
        if is_run_ios():
            assert_equal(CMD.exec_cmd('echo this is test'), ['this is test\n'])
        print(CMD.exec_cmd('echo this is test'))
        assert_equal(CMD.exec_cmd('echo this is test'), ['this is test\n'])
        assert_equal(CMD.exec_cmd('echo this is second time test'), ['this is second time test\n'])



def is_run_ios():
    """
    判断当前运行的是否是IOS
    :return:
    """
    if sys.platform == "darwin":
        return True
    else:
        return False

if __name__ == '__main__':
    unittest.main()