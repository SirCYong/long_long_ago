import os
import unittest

from nose.tools import assert_equal
from nose.tools import assert_not_equal

from UIAutomation.Utils import find_xml, page_locator_factory, page_element_factory


class TestElement(unittest.TestCase):
    def test_find_xml(self):
        assert_equal(os.path.basename(find_xml('test_element.xml')), 'test_element.xml')
        assert_not_equal(os.path.basename(find_xml('test_element.xml')), 'test_dak.xml')
        pass

    def test_page_element_factory(self):
        texts = ('LoginInput1', 'PwdInput1')
        expected_element_locators = {'PwdInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[2]/input'),
                                     'LoginInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[3]/input')}
        assert expected_element_locators == page_element_factory('test_element.xml', texts)
        texts = ('LoginInput1', 'PwdInput1', 'LoginInput2')
        expected_element_locators = {'PwdInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[2]/input'),
                                     'LoginInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[3]/input'),
                                     'LoginInput2': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[6]')}
        assert expected_element_locators == page_element_factory('test_element.xml', texts)
        texts = ('LoginInput2', 'LoginInput5', 'PwdInput1', 'LoginInput4', 'PwdInput3')
        expected_element_locators = {'PwdInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[2]/input'),
                                     'PwdInput3': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[6]'),
                                     'LoginInput2': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[6]'),
                                     'LoginInput5': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[6]'),
                                     'LoginInput4': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[3]/input')}
        assert expected_element_locators == page_element_factory('test_element.xml', texts)
        pass

    def test_page_locator_factory(self):
        text = ['LoginInput1', 'PwdInput1']
        expect_val =[{'LoginInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[3]/input')},
                     {'PwdInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[2]/input')}]
        assert page_locator_factory('test_element.xml', *text) == expect_val
        text = ['LoginInput1', 'PwdInput1', 'PwdInput6']
        expect_val =[{'LoginInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[3]/input')},
                     {'PwdInput1': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[2]/input')},
                     {'PwdInput6': ('XPATH', 'html/body/div[1]/login/div/div/div[2]/aside/div/ul[1]/div[6]')}]
        assert page_locator_factory('test_element.xml', *text) == expect_val
        pass
