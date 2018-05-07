"""
发布劳务需求数据恢复

"""
from UIAutomation.Utils import basic_cit_01, close_oracle
__author__ = 'liyu'


def release_labor_demand(userid=199122):
    con, curs = basic_cit_01()
    try:

        sql = [''' delete from XDW_APP.dd_contract_item o where o.contract_ukid  in
        (select t.contract_ukid from XDW_APP.dd_contract  t where t.create_user_id='%s' )''' % userid,
               '''delete from XDW_APP.RU_LABOUR_LOG m where m.create_user_id='%s' ''' % userid,
               '''delete from XDW_APP.dd_unit_price n where n.create_user_id='%s' ''' % userid,
               '''delete from XDW_APP.rs_labour_publish k where k.create_user_id='%s' ''' % userid,
               '''update XDW_APP.dd_contract x set x.contract_status=10 where x.create_user_id='%s' ''' % userid,
               '''update XDW_APP.ts_operation y set y.status=0 where y.create_user_id='%s' ''' % userid,
               '''update XDW_APP.MS_CARD z set z.status=0 where z.receiver_id='%s' ''' % userid]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
            close_oracle(con, curs)
    except Exception as e:
        print (e)
        close_oracle(con, curs)
    print ("数据恢复成功！！！")
