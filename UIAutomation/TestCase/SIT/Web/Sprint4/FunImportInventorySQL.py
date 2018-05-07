# -*- coding: utf-8 -*-
# Author:liyu
#  导入库位库存
from UIAutomation.Utils import close_oracle, basic_cit_01


def release_import_inventory():
    con, curs = basic_cit_01()
    try:
        sql = [
            ''' UPDATE XDW_APP.TS_OPERATION SET STATUS = 0, ACT_START_TIME = NULL, ACT_END_TIME = NULL WHERE OPERATION_UKID = 51766200780012166''',
            ''' UPDATE XDW_APP.MS_CARD SET STATUS = 0 WHERE CARD_UKID = 51761200980144011''',
            ''' DELETE FROM XDW_APP.RU_INVENTORY_LOG WHERE OPERATION_UKID = 51766200780012166 ''',
            ''' UPDATE XDW_APP.CM_PARTICIPANT_RELATION SET RELATION_STATUS = 20 WHERE RELATION_SN IN (51761700980144023, 51766200989012167)'''
        ]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)

    except Exception as e:
        print(e)
        print("导入库位库存数据失败")
        close_oracle(con, curs)
    print("导入库位库存数据成功")


def select_import_inventory():
        con, curs = basic_cit_01()
        try:
            w = []
            s = [10, 10]
            sql = ['''select m.status from xdw_app.ts_operation  m  where  m.operation_ukid=51766200780012166''',
                   ''' select n.status from xdw_app.ms_card  n where n. CARD_UKID = 51761200980144011''']

            for sql1 in sql:
                curs.execute(sql1)
                res1 = curs.fetchone()
                w.append(res1)
            assert w == s
            close_oracle(con, curs)
        except Exception as e:
            print(e)
            close_oracle(con, curs)
        print("导入库位库存数据验证成功！！！")


