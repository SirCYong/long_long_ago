# -*- coding: utf-8 -*-
# language:zh-CN
'''
    author: zhoujin
   认证中状态数据恢复
'''
# from UIAutomation.TestCase.SIT.Mobile.ManagementBusinessUnitSQL.ManagementBusinessUnit import get_creator_ukid
from UIAutomation.Utils import basic_cit, close_oracle
# from UIAutomation.Utils import basic_sit, close_oracle


def delete_optimize_address_book_and_invite_link_five(user1_id=None):
    con, curs = basic_cit()
    # con, curs = basic_sit()
    # 查询已注册状态的数据
    try:
        sql1 = '''delete from xdw_app.au_role_item where participant_ukid = '%s' and operation_unit_ukid = '%s' ''' % user1_id
        curs.execute(sql1)
        con.commit()
        close_oracle(con, curs)
        print('选择状态更新成功')
    except Exception as e:
        print('选择状态更新失败')
        print(e)

