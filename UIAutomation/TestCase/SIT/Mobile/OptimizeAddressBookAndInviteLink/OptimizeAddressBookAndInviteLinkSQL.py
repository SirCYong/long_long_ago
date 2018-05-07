# -*- coding: utf-8 -*-
# language:zh-CN
'''
    author: zhoujin
   邀请状态数据恢复
'''
# from UIAutomation.TestCase.SIT.Mobile.ManagementBusinessUnitSQL.ManagementBusinessUnit import get_creator_ukid
from UIAutomation.Utils import basic_cit, close_oracle
# from UIAutomation.Utils import basic_sit, close_oracle


def delete_optimize_address_book_and_invite_link():
    con, curs = basic_cit()
    # con, curs = basic_sit()
    # 删除邀请状态
    try:
        sql1 = ['''delete from xdw_app.cm_participant t where t.ppt_name = '周锦'  ''',
                '''delete from xdw_app.ru_invite t where t.invitee_name = '周锦' ''',
                '''delete from xdw_app.ba_user t where t.user_name = '周锦' ''']
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('邀请状态数据恢复成功')
    except Exception as e:
        print('邀请状态数据恢复失败')
        print(e)

if __name__ == '__main__':
    delete_optimize_address_book_and_invite_link()

