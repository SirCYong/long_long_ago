import os
import unittest

from UIAutomation.Utils import get_locator_value_by_text


class TestParseXmlByText(unittest.TestCase):
    file_path = os.path.realpath('test_element.xml')

    def test_get_locator_value_by_text(self):
        tp, val = get_locator_value_by_text('LoginInput', self.file_path)
        assert tp == 'XPATH' and val == 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[2]/input'
        tp, val = get_locator_value_by_text('PwdInput', self.file_path)
        assert tp == 'XPATH' and val == 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[3]/input'
        pass
