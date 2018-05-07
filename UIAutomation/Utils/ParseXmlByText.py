import sys


def __open_xml(path):
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        return root
    except Exception as e:
        print("Error: Cannot parse file:%s" % path)
        sys.exit(1)


def open_xml_tree(path):
        try:
            import xml.etree.cElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET
        try:
            tree = ET.parse(path)
            return tree
        except Exception as e:
            print("Error: Cannot parse file:%s" % path)
            sys.exit(1)


def parse_xml_getroot_dic(path):
    temp_string = ""
    temp_path = str(path)
    root = __open_xml(temp_path)
    for child in root:
        temp_dict = str(child.attrib)
        temp_string += temp_dict
    return eval(temp_string)


def parse_xml_get_son_list(path):
    temp_path = (str)(path)
    root = __open_xml(temp_path)
    tree = open_xml_tree(temp_path)
    list_all = tree.findall(path='./page/')
    list_tup = []
    for locator in range(len(list_all)):
        tup_temp = (list_all[locator].text, list_all[locator].get('type'), list_all[locator].get('value'))
        list_tup.append(tup_temp)
    print(list_tup)
    return list_tup


def del_first_and_last_char(st):
    str_list = list(st)
    str_list.pop(0)
    print("".join(str_list))
    str_list.pop()
    print("".join(str_list))
    return "".join(str_list)


def get_locator_value_by_text(text, path):
    tree = open_xml_tree(path)
    for element in tree.getiterator('locator'):
        if element.text == str(text):
            return element.get('type'), element.get('value')









