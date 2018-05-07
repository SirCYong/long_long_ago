import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from .Logger import run_info_log
from .GlobalVar import GlobalVarClass
from .ParseXmlByText import get_locator_value_by_text
import traceback
__package__ = "IscsUIAutomation"


def get_element(driver, element_meta_data):
    """

    :param element_meta_data:
    :type element_meta_data:
    :param driver:
    :type driver:
    :return:
    :rtype:
    :rtype: element
    """
    by = element_meta_data[0]
    by = by.upper()
    value = element_meta_data[1]
    try:
        if by == 'IOS_UIAUTOMATION':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_ios_uiautomation(value))
        if by == 'ANDROID_UIAUTOMATOR':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_android_uiautomator(value))
        if by == 'ACCESSIBILITY_ID':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_accessibility_id(value))
        if by == 'ID':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(value))
        if by == 'XPATH':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(value))
        if by == 'LINK_TEXT':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_link_text(value))
        if by == 'PARTIAL_LINK_TEXT':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_partial_link_text(value))
        if by == 'NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_name(value))
        if by == 'TAG_NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_tag_name(value))
        if by == 'CLASS_NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name(value))
        if by == 'CSS_SELECTOR':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector(value))
        else:
            # print(u'元素的定位type不正确，请检查xml的type是否符合要求.')
            # run_info_log(u'元素的定位type不正确，请检查xml的type是否符合要求.', GlobalVarClass.get_log_file())
            raise
    except Exception as e:
        # print(u'没有找到(' + by + u":" + value + u')元素')
        # run_info_log(str(traceback.format_exc()), GlobalVarClass.get_log_file())
        # run_info_log(e, GlobalVarClass.get_log_file())
        raise


def get_elements(driver, element_meta_data):
    """
    :param testcase_name:
    :param element_meta_data:
    :type element_meta_data:
    :param driver:
    :type driver:
    :return:
    :rtype:
    :rtype: element
    """
    by = element_meta_data[0]
    by = by.upper()
    value = element_meta_data[1]
    try:
        if by == 'IOS_UIAUTOMATION':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_ios_uiautomation(value))
        if by == 'ANDROID_UIAUTOMATOR':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_android_uiautomator(value))
        if by == 'ACCESSIBILITY_ID':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_accessibility_id(value))
        if by == 'RESOURCE_ID':
            return  WebDriverWait(driver, 10).until(lambda x: x.find_element_by_resource_id(value))
        if by == 'ID':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_id(value))
        if by == 'XPATH':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_xpath(value))
        if by == 'LINK_TEXT':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_link_text(value))
        if by == 'PARTIAL_LINK_TEXT':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_partial_link_text(value))
        if by == 'NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_name(value))
        if by == 'TAG_NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_tag_name(value))
        if by == 'CLASS_NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_class_name(value))
        if by == 'CSS_SELECTOR':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_css_selector(value))
        else:
            # print(u'元素的定位type不正确，请检查xml的type是否符合要求.')
            # run_info_log(u'元素的定位type不正确，请检查xml的type是否符合要求.', GlobalVarClass.get_log_file())
            raise
    except Exception as e:
        # print(u'没有找到(' + by + u":" + value + u')元素')
        # run_info_log(str(traceback.format_exc()), GlobalVarClass.get_log_file())
        # run_info_log(e, GlobalVarClass.get_log_file())
        raise


def is_element_present(driver, locator):
    try:
        get_element(driver, locator)
        return True
    except:
        return False


def page_locator_factory(page_name, *text):
    """

    :return:
    :rtype:
    :param page_name:
    :type page_name:
    :param text:
    :type text:
    :return:
    :rtype:
    """
    try:
        element_list = []
        for element in text:
            ele = get_locator_value_by_text(element, find_xml(page_name))
            element_dic = {element: ele}
            element_list.append(element_dic)
        return element_list
    except Exception as e:
        print(e)
        return []


def page_element_factory(page_name, text):
    """
    返回当前页面内需要被实例化的element的text值.
    :param page_name:
    :type page_name:
    :param text:
    :type text:
    :return: element meta data in xml file.
    :rtype:dict
    """
    try:
        element_locator = page_locator_factory(page_name, *text)
        element_meta_data_original = {}
        element_meta_data_middle = {}
        for i in range(len(element_locator)):
            element_meta_data_original.update({text[i]: element_locator[i]})
        for element in text:
            element_meta_data_middle.update(element_meta_data_original[element])
        return element_meta_data_middle
    except Exception as e:
        print(e)
        run_info_log(e, GlobalVarClass.get_log_file())


# 寻找当前目录下的XML文件
def find_xml(page_name):
    """

    :param page_name:
    :type page_name:
    :return:
    :rtype:
    """
    root = os.path.dirname(os.path.realpath(page_name))  # 当前目录
    try:
        page_name = os.path.basename(page_name)[:os.path.basename(page_name).rfind(".")]
        s = os.listdir(root)
        flag = 0
        for i in s:
            if _end_with(i, page_name + '.xml'):
                return root + '/' + page_name + '.xml'
        if flag == 0:
            run_info_log('XML 文件未找到！', GlobalVarClass.get_log_file())
    except Exception as e:
        print(e)


# 判断是否存在XML文件
def _end_with(s, *end_string):
    """

    :param s:
    :type s:
    :param end_string:
    :type end_string:
    :return:
    :rtype:
    """
    try:
        array = map(s.endswith, end_string)
        if True in array:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
