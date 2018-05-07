# -*- coding: utf-8 -*-
# Author:liyu
"""
发布仓储供应数据恢复
"""
from UIAutomation.Utils import  close_oracle, basic_cit_01

def release_storage_supply():
    con, curs = basic_cit_01()
    try:
        sql = [
            '''delete from XDW_APP.dd_contract_item o where o.contract_ukid=51767000000160018''',
            '''update XDW_APP.dd_contract x set x.contract_status=10 where x.contract_ukid=51767000000160018''',
            '''update XDW_APP.ts_operation y set y.status=0 where y.operation_ukid=11342455101230011 ''',
            '''update XDW_APP.MS_CARD z set z.status=0 where z.operation_ukid=11342455101230011''',
            '''update xdw_app.cm_participant_relation kl set kl.RELATION_STATUS=20 where kl.related_ukid=11712400012112101'''
        ]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
    except Exception as e:
        print (e)
        print ("发布仓储供应数据恢复失败！！！")
        close_oracle(con, curs)
    print ("发布仓储供应数据恢复成功！！！")


def select_storage_supply():
    con, curs = basic_cit_01()
    try:
        w = []
        s = [20, 10, 10]
        sql = ['''select t.contract_status from xdw_app.dd_contract t  where  t.contract_ukid=51767000000160018''',
               '''select m.status from xdw_app.ts_operation  m  where  m.operation_ukid=11342455101230011''',
               ''' select n.status from xdw_app.ms_card  n where n.operation_ukid=11342455101230011''']

        for sql1 in sql:
            curs.execute(sql1)
            res1 = curs.fetchone()
            w.append(res1)
        assert w == s
        close_oracle(con, curs)
    except Exception as e:
        print (e)
        close_oracle(con, curs)
    print ("发布仓储供应数据验证成功！！！")
