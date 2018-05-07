# -*- coding:utf-8 -*-
# language:zh-CN
from UIAutomation.Utils import Independent_cit


def PublishWarehouseDemandSQl_one(OPERATION_UKID=51765800000034170):
    try:
        con, curs = Independent_cit()
        # 更新任务状态根据
        sql1='''UPDATE XDW_APP.TS_OPERATION SET STATUS=0 WHERE OPERATION_UKID= %s ''' % OPERATION_UKID,
        sql2 = '''UPDATE XDW_APP.cm_participant_relation SET relation_status = 20 WHERE RELATED_UKID= %s ''' % OPERATION_UKID,
        curs.execute(sql1)
        curs.execute(sql2)
        con.commit()
        result = curs.fetchall()
        con.close()
    except Exception as e:
        print(e)
        print("CIT_TASK 数据库数据恢复")
    pass





