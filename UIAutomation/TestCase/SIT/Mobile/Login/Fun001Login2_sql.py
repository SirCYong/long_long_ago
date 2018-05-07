# coding=utf-8
from UIAutomation.Utils import close_oracle, basic_cit


def login_state(phone):  # 还原非服务认证任务
    try:
        con, curs = basic_cit()
        sql1 = '''select platform,login_mode,status from  xdw_app.ru_login_log where MOBILE='%s'
order by login_time desc''' % phone
        curs.execute(sql1)
        result = curs.fetchall()
        close_oracle(con, curs)
        print('登陆')
        print(result)
        if (result[0][0] == 1 and result[0][1] == 1 and result[0][2] == 1):
            return True
        elif(result[0][0] == 1 and result[0][1] == 1 and result[0][2] == 0):
            return False
    except Exception as e:
        print(e)


