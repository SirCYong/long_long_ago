# -*- coding: utf-8 -*-
# language:zh-CN
'''
    author: zhoujin
   权限回收数据管理
'''
# from UIAutomation.TestCase.SIT.Mobile.ManagementBusinessUnitSQL.ManagementBusinessUnit import get_creator_ukid
from UIAutomation.Utils import basic_cit, close_oracle
# from UIAutomation.Utils import basic_sit, close_oracle


def reduction_permission_recovery(participant_ukid =None):
    con, curs = basic_cit()
    # con, curs = basic_sit()
    # 还原权限
    try:
        # creator_ukid = get_creator_ukid(user_id)
        sql1 = ['''update xdw_app.au_role_item set status = 1 where participant_ukid = '%s' ''' % participant_ukid,
                '''update xdw_app.au_relation set status = 1 where grantee = '%s' ''' % participant_ukid,
                '''update xdw_app.au_auth_log set operation_type = 11 where label_ukid in
                  (select label_ukid from xdw_app.au_role_item where participant_ukid = '%s' )''' % participant_ukid]
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原权限成功')
    except Exception as e:
        print('还原权限失败')
        print(e)
        close_oracle(con, curs)


def get_new_permission_recovery(participant_ukid =None):
    # 权限回收成功后，通过数量来判断
    con, curs = basic_cit()
    # con, curs = basic_sit()
    try:
        dic = {}
        # creator_ukid = get_creator_ukid(user_id)
        sql1 = '''select count(*) from xdw_app.au_role_item t where t.status = 0 and participant_ukid = '%s' ''' \
               % participant_ukid
        print(sql1)
        curs.execute(sql1)
        result = curs.fetchall()
        dic['recovery_record_no'] = result[0][0]

        sql2 = ''' select count(*) from xdw_app.au_relation t where t.status = 0 and grantee ='%s'  ''' \
               % participant_ukid
        print(sql2)
        curs.execute(sql2)
        result2 = curs.fetchall()
        dic['permission_record_no'] = result2[0][0]

        sql3 = '''select count(*) from xdw_app.au_auth_log t where t.operation_type = 52 and grantee ='%s'  '''\
               % participant_ukid
        print(sql3)
        curs.execute(sql3)
        result3 = curs.fetchall()
        dic['log_no'] = result3[0][0]
        return dic

    except Exception as e:
        print('权限收回失败')
        print(e)
        close_oracle(con, curs)


if __name__ == '__main__':
    reduction_permission_recovery()