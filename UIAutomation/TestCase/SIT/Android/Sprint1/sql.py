# -*- coding: utf-8 -*-
# language:zh-CN
from time import sleep

# 还原注册邀请表数据
from UIAutomation.Utils import task_cit, basic_cit


def setFirstOne():
    try:  # 连接数据库配置还原注册信息，删除table中已插入的数据
        con, curs = task_cit()
        # 通过get到手机号查询CREATE_USER_ID
        sql = '''DELETE FROM task_owner.ru_invite where INVITEE_MOBILE=15268509694'''
        # 将结果赋值给state
        curs.execute(sql)
        con.commit()
        result = curs.fetchall()
        con.close()
    except Exception as e:
        print(e)
    print("CIT_TASK 数据库数据恢复")
    pass

def setSQlDelete_common():
    try:    # 连接数据库配置还原注册信息，删除table中已插入的数据
        con, curs = basic_cit()
        # 通过get到手机号查询CREATE_USER_ID
        sql = ''' SELECT CREATE_USER_ID FROM basic_owner.ba_user WHERE MOBILE=15268509694'''
        # 将结果赋值给state
        curs.execute(sql)
        stated = curs.execute(sql)
        result = []
        for item in stated:
            result = item
            break

        print(result[0])
        # 删除4个表中关于该用户的记录
        delete_sql1 = '''delete from  XDW_APP.cm_participant where CREATE_USER_ID= '%s' ''' % result
        delete_sql2 = '''delete from  XDW_APP.cm_identify where CREATE_USER_ID= %s ''' % result
        delete_sql3 = '''delete from  XDW_APP.Cm_Human where CREATE_USER_ID= %s ''' % result
        delete_sql4 = '''delete from  XDW_APP.ba_user where CREATE_USER_ID= %s ''' % result
        # update1 = ''' UPDATE  XDW_APP.RU_INVITE SET CREATE_TIME = SYSDATE, STATUS = 1, OPENID = NULL, SERVICE_TYPE = 1, AUTH_TASK_OPERATION_UKID = NULL,INVALID_TIME = SYSDATE + 1/48WHERE INVITE_CODE = 4e03116091b911e6a437fc952ffd4494'''
        #  执行5条sql语句
        curs.execute(delete_sql1)
        curs.execute(delete_sql2)
        curs.execute(delete_sql3)
        curs.execute(delete_sql4)
        # curs.execute(update1)
        con.commit()
        con.close()
    except Exception as e:
        print(e)
    print("CIT_BASIC 数据库数据恢复")
    pass
