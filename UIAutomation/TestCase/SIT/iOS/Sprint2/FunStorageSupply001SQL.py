"""
发布仓储供应数据恢复

"""

from UIAutomation.Utils import  close_oracle, basic_cit_01
__author__ = 'liyu'


def release_storage_supply(userid=199122):
    try:
        con, curs = basic_cit_01()
        sql = [''' delete from XDW_APP.dd_contract_item o where o.contract_ukid  in
        (select t.contract_ukid from XDW_APP.dd_contract  t where t.create_user_id='%s' )''' % userid,
               '''update XDW_APP.dd_contract x set x.contract_status=10 where x.create_user_id='%s' ''' % userid,
               '''update XDW_APP.ts_operation y set y.status=0 where y.create_user_id='%s' ''' % userid,
               '''update XDW_APP.MS_CARD z set z.status=0 where z.receiver_id='%s' ''' % userid]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
            close_oracle(con, curs)
    except Exception as e:
        print(e)
    print("数据恢复成功！！！")
