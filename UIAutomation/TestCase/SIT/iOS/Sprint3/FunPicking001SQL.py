# -*- coding= utf-8 -*-

"""
恢复拣选数据
"""
from UIAutomation.Utils import basic_cit_01, close_oracle


def restore_picking():
    try:
        con, curs = basic_cit_01()
        sql = ['''UPDATE TS_OPERATION SET STATUS = 0 WHERE OPERATION_UKID = 51763800000008024''',
               '''UPDATE TS_STOCK_TASK_DETAIL SET TASK_DETAIL_STATUS = 0 ACTUAL_OPERATION_QTY = NULL
ACTUAL_START_INFO = NULL ACTUAL_END_INFO = NULL WHERE TASK_UKID = 892374982''',
               '''UPDATE MS_CARD SET STATUS = 0 WHERE CARD_UKID = 11730000000087300''',
               '''UPDATE CM_PARTICIPANT_RELATION SET RELATION_STATUS = 20 WHERE RELATION_SN = 51759100080219001''']
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
            close_oracle(con, curs)
    except Exception as e:
        print (e)
    print ("拣选数据恢复成功！！！")