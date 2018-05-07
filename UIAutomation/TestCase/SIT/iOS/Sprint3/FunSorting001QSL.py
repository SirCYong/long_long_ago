# -*- coding: utf-8 -*-

"""
恢复分拣数据
"""
from UIAutomation.Utils import basic_cit_01, close_oracle


def restore_sorting():
    try:

        con, curs = basic_cit_01()
        sql = [
            '''update xdw_app.ts_operation t set t.status = 0 where t.operation_ukid = 51763400000008016 and
 t.status in(5,10)''',
            '''update  xdw_app.ts_stock_task_detail b set b.actual_start_info=NULL b.actual_end_info = NULL
 b.task_detail_status=0  where b.task_ukid=51763400000008016''',
            '''update  xdw_app.ms_card tk set tk.status=0  where tk.card_ukid = 51763300000008018''']
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
            close_oracle(curs, con)
    except Exception as e:
        print(e)
    print("分拣数据恢复成功！！！")
