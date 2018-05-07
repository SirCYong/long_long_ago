# coding: utf-8

"""
这个元类定义了强制使用约束,约束类的方法名不能为大小混合命名.
"""
__author__ = 'Yongli'
__package__ = "IscsUIAutomation"

# Python >2.7
class NoMixedCaseMethodNameMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name' + name)
        return super(NoMixedCaseMethodNameMeta, cls).__new__(cls, clsname, bases, clsdict)
    pass


# Python3.5
class MetaClassTorestrictMethodNaming(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name {}'.format(name))
        return super.__new__(cls, clsname, bases, clsdict)
    pass

