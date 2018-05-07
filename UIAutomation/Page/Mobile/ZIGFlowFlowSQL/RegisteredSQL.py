from UIAutomation.Utils import basic, re, close_oracle, dev


def update_invite_SQL():
    # 更新邀请链接
    try:
        con, curs = dev()
        sql = ['''UPDATE XDW_APP.RU_INVITE SET CREATE_TIME = SYSDATE, STATUS = 1, OPENID = NULL, SERVICE_TYPE = 1, AUTH_TASK_OPERATION_UKID = NULL, INVALID_TIME = SYSDATE + 1/48 WHERE INVITE_CODE = '5356f030fcdc11e682838e3caea07349' ''',
            '''UPDATE XDW_APP.TS_OPERATION SET OPERATION_UNIT_UKID = 100001, CARD_TYPE = 'WriteRegInfo', STATUS = 0, OPERATION_ROUTE_UKID = NULL WHERE OPERATION_UKID = 51884200000045012''']
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
    except Exception as e:
        print(e)
    pass


def get_invite_sql():
    # 获取手机验证码
        try:
            con, curs = dev()
            get_invite_sql = '''select SEND_CONTENT from xdw_app.sa_sms a where mobile_no =     xdw_app.des_encrypt(15577778888, 'b0NmiFbH') and a.create_time < trunc(sysdate + 1) order by  a.create_time desc '''
            curs.execute(get_invite_sql)
            #你可以把字符串拉出来，然后传化为列表，通过循环判断is_digital(是不是数字)的方法，来得到
            value = curs.fetchone()
            # 获取到验证码进行截取，截取后传值
            invite_code = value[0][10:16]
            #invite_code = re.findall("\d+", values)
            close_oracle(con, curs)
            return invite_code
        except Exception as e:
            print(e)


def del_registered_info():
    # 删除邀请手机号以及注册相关信息
    try:
        con, curs = dev()
        # 得到USER_ID
        mobile_info = '''select user_id from ba_user  where mobile = xdw_app.des_encrypt(15577778888,'b0NmiFbH')'''
        curs.execute(mobile_info)
        if mobile_info != None:
            id1 = curs.fetchone()
            # 第一条SQL:删除邀请手机号  /剩余其他删除注册相关信息
            del_info = ['''delete from  XDW_APP.cm_participant where CREATE_USER_ID= %s''' % id1,
                        '''delete FROM XDW_APP.ru_invite where invitee_mobile = xdw_app.des_encrypt(15577778888,'b0NmiFbH')''',
                        '''delete from  XDW_APP.cm_participant where CREATE_USER_ID=%s''' % id1,
                        '''delete from  XDW_APP.cm_identify where CREATE_USER_ID= %s''' % id1,
                        '''delete from  XDW_APP.Cm_Human where CREATE_USER_ID=%s''' % id1,
                        '''delete from  XDW_APP.ba_user where CREATE_USER_ID=%s''' % id1,
                        '''delete from xdw_app.ba_account where account_id=%s''' % id1,
                        '''delete from xdw_app.sa_sms a where mobile_no = xdw_app.des_encrypt(15577778888, 'b0NmiFbH') and a.create_time < trunc(sysdate + 1)''']
            for sq in del_info:
                curs.execute(sq)
                con.commit()
        else:
            pass
        con.close()
    except Exception as e:
        print(e)
    pass


def get_user_id():
    # 获取user id
    con, curs = dev()
    try:
        user_idSQL = '''select user_id from ba_user  where mobile = xdw_app.des_encrypt(15577778888,'b0NmiFbH')'''
        get_id = curs.execute(user_idSQL)
        con.close()
        return get_id
    except Exception as e:
        print(e)
    pass



