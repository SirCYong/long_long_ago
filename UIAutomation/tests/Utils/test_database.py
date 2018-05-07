import unittest

from UIAutomation.Utils import basic_cit, basic_sit


class TestDatabase(unittest.TestCase):
    def test_basic_cit(self):
        con, curs = basic_cit()
        assert con is not None and curs is not None
        pass

    def test_basic_sit(self):
        con, curs = basic_sit()
        assert con is not None and curs is not None
        pass


