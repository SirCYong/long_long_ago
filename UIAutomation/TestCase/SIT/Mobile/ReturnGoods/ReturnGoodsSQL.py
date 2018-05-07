# -*- coding: utf-8 -*-
# language:zh-CN
'''
    author: zhoujin
   申请退货数据管理
'''
from UIAutomation.Utils import basic_cit, close_oracle
# from UIAutomation.Utils import basic_sit, close_oracle


def delete_return_goods(user_id=None):
    con, curs = basic_cit()
    # con, curs = basic_sit()
    # 删除申请退货的相关数据
    try:
        # creator_ukid = get_creator_ukid(user_id)
        sql1 = ['''delete from xdw_app.TS_PURCHASE_RETURN_TASK where return_applicant_ukid = '%s' ''' % user_id,
                '''delete from xdw_app.TS_PURCHASE_RETURN_DETAIL where create_user_id = '%s' ''' % user_id,
                '''delete from xdw_app.dd_contract_return_tracking where operator_ukid = '%s' ''' % user_id,
                '''delete from xdw_app.ms_user_message a where a.receiver_id = '%s' ''' % user_id]
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('删除退货成功')
    except Exception as e:
        print('删除退货失败')
        print(e)
        close_oracle(con, curs)


def get_return_goods(user_id=None):
    # 申请退货成功后，通过消息通知来判断
    con, curs = basic_cit()
    # con, curs = basic_sit()
    try:
        dic = {}
        sql1 = '''select a.msg_content from xdw_app.ms_user_message a  where a.receiver_id = '%s'
                  order by a.create_time desc ''' % user_id
        print(sql1)
        curs.execute(sql1)
        result = curs.fetchall()
        dic['recovery_record_no'] = result[0][0]
        return dic
    except Exception as e:
        print('申请退货失败')
        print(e)
        close_oracle(con, curs)

if __name__ == '__main__':
    delete_return_goods()
