from __future__ import print_function
import sys
__package__ = "IscsUIAutomation"


def __open_xml(path):
    """

    :param path:
    :type path:
    :return:
    :rtype:
    """
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    try:
        tree = ET.parse(path)                              # 打开xml文档
        root = tree.getroot()
        return root
    except Exception as e:
        print ("Error: Cannot parse file:%s" % path)
        print(e)
        sys.exit(1)


def __open_xml_tree(path):
    """

    :param path:
    :type path:
    :return:
    :rtype:
    """
    try:
            import xml.etree.cElementTree as ET
    except ImportError:
            import xml.etree.ElementTree as ET
    try:
            tree = ET.parse(path)  # 打开xml文档
            return tree
    except Exception as e:
            print("Error: Cannot parse file:%s" % path)
            print(e)
            sys.exit(1)


# 解析根节点的元素值,并返回一个字典型
def parse_xml_getroot_dic(path):
    # 用全局的变量把所有的字典类型的数据抓取出来,最后统一格式转成为字典类型
    """
    :param path:
    :type path:
    :return:
    :rtype:
    """
    temp_string = ""
    # 从RF传进来的字符串为unicode（u''str'）类型的,需要做一次强制类型转换
    temp_path = str(path)
    root = __open_xml(temp_path)
    for child in root:
        temp_dict = str(child.attrib)
        temp_string += temp_dict
    return eval(temp_string)                          # 返回一个字典型,这样可以在RF里通过key和value去访问


def parse_xml_get_son_list(path):
    """

    :param path:
    :type path:
    :return:
    :rtype:
    """
    temp_path = str(path)
    tree = __open_xml_tree(temp_path)
    list_all = tree.findall(path='./page/')
    list_tup = []
    for locator in range(len(list_all)):
        tup_temp = (list_all[locator].text, list_all[locator].get('type'), list_all[locator].get('value'))
        list_tup.append(tup_temp)
    print(list_tup)
    return list_tup


def del_first_and_last_char(st):
    """

    :param st:
    :type st:
    :return:
    :rtype:
    """
    str_list = list(st)
    str_list.pop(0)
    print("".join(str_list))
    str_list.pop()
    print("".join(str_list))
    return "".join(str_list)


def get_locator_value_by_text(text, path):
    """

    :param text:
    :type text:
    :param path:
    :type path:
    :return:
    :rtype:
    """
    tree = __open_xml_tree(path)
    for element in tree.getiterator('locator'):
        if element.text == str(text):                 # RF 进来的是Unicode数据
            return element.get('type'), element.get('value')



def xml_text_conflict_check(path):
    """

    :param path:
    :type path:
    """
    tree = __open_xml_tree(path)
    text_list = []
    duplicate_text_list = []
    for element in tree.getiterator('locator'):
        # if element.text == (str)(text):                 # RF 进来的是Unicode数据
        #     return element.get('value')
        text_list.append(element.text)

    print(len(text_list))
    print(text_list)

    for element in text_list:
        if text_list.count(element) > 1 and element not in duplicate_text_list:
            duplicate_text_list.append(element)
    print("下面是重复的")
    print(duplicate_text_list)


if __name__ == '__main__':
    xml_text_conflict_check("D:\\test\\ATDD\\features\\uiLoator.xml")