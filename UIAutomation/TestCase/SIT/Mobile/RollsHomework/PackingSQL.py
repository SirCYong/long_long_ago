# -*- coding: utf-8 -*-
# Author:liyu

"""
恢复拣选容器

"""
from UIAutomation.Utils import basic_sit
from UIAutomation.Utils import close_oracle


def restore_container():
    try:
        con, curs = basic_sit()
        sql = ['''update xdw_app.dm_realistic_information  o  set  o.running_status=0  where o.item_ukid=999808
and o.sub_item_ukid=66600101''']
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
            close_oracle(con, curs)
    except Exception as e:
        print(e)
    print("数据恢复成功！！！")