# -*- coding: utf-8 -*-
# language:zh-CN
'''
    author: zhoujin
   已注册状态数据恢复
'''
# from UIAutomation.TestCase.SIT.Mobile.ManagementBusinessUnitSQL.ManagementBusinessUnit import get_creator_ukid
from UIAutomation.Utils import basic_cit, close_oracle
# from UIAutomation.Utils import basic_sit, close_oracle


def get_optimize_address_book_and_invite_link_two():
    con, curs = basic_cit()
    # con, curs = basic_sit()
    # 查询已注册状态的数据
    try:
        sql1 = ['''select * from xdw_app.cm_participant t where t.ppt_name = '百合'  ''',
                '''select * from xdw_app.ru_invite t where t.invitee_name = '百合' ''',
                '''select * from xdw_app.ba_user t where t.user_name = '百合' ''']
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('已注册状态查询成功')
    except Exception as e:
        print('已注册状态查询失败')
        print(e)
if __name__ == '__main__':
    get_optimize_address_book_and_invite_link_two()


def update_optimize_address_book_and_invite_link_two():
    con, curs = basic_cit()
    # con, curs = basic_sit()
    # 更新已注册状态的数据
    try:
        sql1 = ['''insert into xdw_app.cm_participant (PARTICIPANT_UKID, PPT_TYPE, PPT_NAME, IDENTIFY_ID, CREATE_TIME,
                                            UPDATE_TIME, UPDATE_USER_ID, CREATE_USER_ID, STATUS)
                    values ('10001501', 'P', '百合', '', to_date('30-12-2016 13:37:24', 'dd-mm-yyyy hh24:mi:ss'),
                    to_date('30-12-2016 13:37:24', 'dd-mm-yyyy hh24:mi:ss'), '10001501', '10001501', '0') '''
                '''insert into xdw_app.ru_invite (UKID, INVITEE_NAME, INVITEE_MOBILE, INVITEE_PARTICIPANT_UKID,
                    AUTH_TASK_OPERATION_UKID, INVITE_TASK_OPERATION_UKID, MESSAGE_TOPIC, SERVICE_TYPE, ROLE_TYPE,
                    INVITE_PURPOSE, INVITE_CODE, CREATE_TIME, CREATE_USER_ID, INVALID_TIME, INVITER_PARTICIPANT_UKID,
                    STATUS, UPDATE_TIME, UPDATE_USER_ID, REGISTER_TASK_OPERATION_UKID, OPENID, CREATOR_UKID)
                  values ('51825900000010020', '百合', 'enc_F5C377AA0C5EE309E87C165947741A6C', '10001501',
                  '51825600000010027', '51825300000010013', 'serviceInvite', '1', '1',
                   '{"cardType":"ServiceInviteService","cardUkid":"1","inviteeContent":"测试一邀请您下载网仓三号",
                   "inviteeName":"百合","inviteeType":"1","mobile":"18555090013","participantUkid":10001469,"creatorUkid":10001469}',
                    'bc649500ce5111e6b6988438856d3571', to_date('30-12-2016 13:35:13', 'dd-mm-yyyy hh24:mi:ss'), '10001469',
                     to_date('30-12-2016 14:05:12', 'dd-mm-yyyy hh24:mi:ss'), '10001469', '2', to_date('30-12-2016 13:37:24', 'dd-mm-yyyy hh24:mi:ss'),
                      '', '51825200000010018', 'o8niLvyLIeX7tZUjwd5JTcy0k7x0', '10001469') '''
                '''insert into xdw_app.ba_user (USER_ID, USER_NAME, PASSWORD, CREATE_TIME, UPDATE_USER_ID, UPDATE_TIME,
                       PASSWORD_CHANGE_NEXT, EXPIRED_DATE, LOCKED, LOCKED_DATE, MOBILE, CREATE_USER_ID, FACE_URI, OPENID,
                       COUNTRY_CALLING_CODE, LOGIN_TIMES)
                  values ('10001501', '百合', 'B5B70B0E64E080AA9F5C8D0571E0DA7A', to_date('30-12-2016 13:37:24', 'dd-mm-yyyy hh24:mi:ss'),
                  '', to_date('30-12-2016 13:37:24', 'dd-mm-yyyy hh24:mi:ss'), '', null, '', null,
                   'enc_F5C377AA0C5EE309E87C165947741A6C', '10001501', '/temp/93300f81-4b9a-4ec3-adca-0d98ed4bfd26.png',
                   '', '86', '0')''']
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('更新已注册状态成功')
    except Exception as e:
        print('更新已注册状态失败')
        print(e)
