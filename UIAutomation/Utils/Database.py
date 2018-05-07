import os
import cx_Oracle

__author__ = "zhongchangwei"
__package__ = "IscsUIAutomation"


def connect_oracle(username, password, data_base):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    con = cx_Oracle.connect(username, password, data_base)
    curs = con.cursor()
    return con, curs


def close_oracle(con, curs):
    curs.close()
    con.close()


def basic():
    con, curs = connect_oracle('basicdata_user01', 'oracle123', '192.168.6.132/BASICDATA')
    return con, curs


def dev():
    con, curs = connect_oracle('xdw_app', 'xdw_app#', '192.168.6.132/BASICDATA')
    return con, curs


def reality():
    con, curs = connect_oracle('realitydata_user01', 'oracle123', '192.168.6.132/REALITYDATA')
    return con, curs


def resource():
    con, curs = connect_oracle('resourcedata_user01', 'oracle123', '192.168.6.132/RESOURCEDATA')
    return con, curs


def external():
    con, curs = connect_oracle('externaldata_user01', 'oracle123', '192.168.6.132/EXTERNALDATA')
    return con, curs


def contract():
    con, curs = connect_oracle('contractdata_user01', 'oracle123', '192.168.6.132/CONTRACTDATA')
    return con, curs


def task():
    con, curs = connect_oracle('taskdata_user01', 'oracle123', '192.168.6.132/TASKDATA')
    return con, curs


def basic_cit():
    con, curs = connect_oracle('chenyx', 'RKSBM520', '192.168.6.29/BASICDATA')
    return con, curs


def reality_cit():
    con, curs = connect_oracle('CIT_TESTER', 'abc123', '192.168.6.29/REALITYDATA')
    return con, curs


def resource_cit():
    con, curs = connect_oracle('CIT_TESTER', 'abc123', '192.168.6.29/RESOURCEDATA')
    return con, curs


def external_cit():
    con, curs = connect_oracle('CIT_TESTER', 'abc123', '192.168.6.29/EXTERNALDATA')
    return con, curs


def contract_cit():
    con, curs = connect_oracle('CIT_TESTER', 'abc123', '192.168.6.29/CONTRACTDATA')
    return con, curs


def task_cit():
    con, curs = connect_oracle('CIT_TESTER', 'abc123', '192.168.6.29/TASKDATA')
    return con, curs


def Independent_cit():
    con, curs = connect_oracle('yuetz', 'abc123', '192.168.6.29/BASICDATA')
    return con, curs


def basic_cit_01():
    con, curs = connect_oracle('liy', 'abc123', '192.168.6.29/BASICDATA')
    return con, curs


def cit():
    con, curs = connect_oracle('caoy', 'wckj1234', '192.168.6.29/BASICDATA')
    return con, curs


def basic_sit():
    con, curs = connect_oracle('zhouj', 'OYZ18KM9', '192.168.6.61/BASICDATA')
    return con, curs


def sit():
    con, curs = connect_oracle('caoy', 'wckj1234', '192.168.6.61/BASICDATA')
    return con, curs

if __name__ == '__main__':
    kk,cc = basic_sit()
