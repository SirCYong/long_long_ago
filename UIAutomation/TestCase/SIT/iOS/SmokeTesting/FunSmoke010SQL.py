# -*- coding: utf-8 -*-
# Author:liyu

"""
发布运输数据恢复

"""

from UIAutomation.Utils import close_oracle, basic_cit_01


def release_transport_supply():
    con, curs = basic_cit_01()
    try:
        sql = [
               '''delete from XDW_APP.dd_unit_price n where n.contract_ukid=51756800000008078 ''',
               '''delete from XDW_APP.ru_transport_supply_log k where k.contract_ukid=51756800000008078 ''',
               '''update XDW_APP.dd_contract x set x.contract_status=10 where x.contract_ukid=51756800000008078 ''',
               '''update XDW_APP.ts_operation y set y.status=0 where y.operation_ukid=51756200000008117 ''',
               '''update XDW_APP.MS_CARD z set z.status=0 where z.operation_ukid=51756200000008117''',
               '''update xdw_app.cm_participant_relation kl  set kl.RELATION_STATUS=20 where kl.related_ukid=43156800000008456''']
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
    except Exception as e:
        print (e)
        print ("发布运输供应数据恢复失败！！！")
        close_oracle(con, curs)
    print ("发布运输供应数据恢复成功！！！")


def select_transport_supply():
    con, curs = basic_cit_01()
    try:
        w = []
        s = [20, 10, 10]
        sql = ['''select t.contract_status from xdw_app.dd_contract t  where  t.contract_ukid=51756800000008078''',
               '''select m.status from xdw_app.ts_operation  m  where  m.operation_ukid=51756200000008117''',
               ''' select n.status from xdw_app.ms_card  n where n.operation_ukid=51756200000008117''']

        for sql1 in sql:
            curs.execute(sql1)
            res1 = curs.fetchone()
            w.append(res1)
        assert w == s
        close_oracle(con, curs)
    except Exception as e:
        print (e)
        close_oracle(con, curs)
    print ("发布运输供应数据验证成功！！！")


