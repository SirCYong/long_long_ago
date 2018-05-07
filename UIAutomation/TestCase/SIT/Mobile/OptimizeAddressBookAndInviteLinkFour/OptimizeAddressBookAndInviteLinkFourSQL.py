# -*- coding: utf-8 -*-
# language:zh-CN
'''
    author: zhoujin
   认证中状态数据恢复
'''
# from UIAutomation.TestCase.SIT.Mobile.ManagementBusinessUnitSQL.ManagementBusinessUnit import get_creator_ukid
from UIAutomation.Utils import basic_cit, close_oracle
# from UIAutomation.Utils import basic_sit, close_oracle


def update_optimize_address_book_and_invite_link_four():
    con, curs = basic_cit()
    # con, curs = basic_sit()
    # 查询已注册状态的数据
    try:
        sql1 = '''update xdw_app.cm_participant set status =2 where ppt_name = '千' '''
        curs.execute(sql1)
        con.commit()
        close_oracle(con, curs)
        print('认证中状态更新成功')
    except Exception as e:
        print('认证中状态更新失败')
        print(e)

