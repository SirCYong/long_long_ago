# 还原注册邀请表数据
from UIAutomation.Utils import Independent_cit


def UpdateURL1():
    try:
        con, curs = Independent_cit()
        # 跟新邀请链接信息
        sql = ''' UPDATE XDW_APP.RU_INVITE SET CREATE_TIME = SYSDATE, STATUS = 1, OPENID = NULL, SERVICE_TYPE = 1, AUTH_TASK_OPERATION_UKID = NULL,
INVALID_TIME = SYSDATE + 1/48 WHERE INVITE_CODE = '95b5c0a0a01611e698b0e4e4b715094a' '''
        # 跟新任务状态
        # 将结果赋值给state
        curs.execute(sql)
        con.commit()
        result = curs.fetchall()
        print(result)
        con.close()
    except Exception as e:
        print(e)
    print(" 数据库数据恢复")
    pass


def UpdateURL2():
    try:
        con, curs = Independent_cit()
        # 跟新邀请链接信息
        sql = ''' UPDATE XDW_APP.TS_OPERATION
        SET OPERATION_UNIT_UKID = 100001, CARD_TYPE = 'WriteRegInfo', STATUS = 0, OPERATION_ROUTE_UKID = NULL
        WHERE OPERATION_UKID = 51766800000007426 '''
        # 跟新任务状态
        # 将结果赋值给state
        curs.execute(sql)
        con.commit()
        result = curs.fetchall()
        print(result)
        con.close()
    except Exception as e:
        print(e)
    print(" 数据库数据恢复")
    pass
