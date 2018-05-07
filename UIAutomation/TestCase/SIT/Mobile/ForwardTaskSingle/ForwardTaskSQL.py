# -*- coding: utf-8 -*-
# language:zh-CN
'''
    author: sdy
    还原任务转发数据
'''
from UIAutomation.Utils import basic_cit, close_oracle
# from UIAutomation.Utils import basic_sit, close_oracle


def restore_forward_task(from_user_id=None, to_user_id=None):
    con, curs = basic_cit()

    # con, curs = basic_sit()
    # 还原任务
    try:
        # creator_ukid = get_creator_ukid(user_id)
        sql1 = ['''update xdw_app.cm_participant_relation set participant_ukid= 10001577 where relation_status=20 and participant_ukid=%s ''' % to_user_id,
                '''delete FROM xdw_app.ms_user_message where sender_id='%s' ''' % from_user_id]
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原任务成功')
    except Exception as e:
        print('还原任务失败')
        print(e)
        close_oracle(con, curs)


def get_forward_task_data(to_user_id=None):
    con, curs = basic_cit()
    try:
        result_data = {}
        sql1 = '''select count(*) FROM xdw_app.cm_participant_relation
                   WHERE relation_status=20 and participant_ukid=%s '''\
               % to_user_id
        print(sql1)
        curs.execute(sql1)
        result = curs.fetchall()
        result_data['forward_task_record_no'] = result[0][0]
        print('转发对象取得成功')
        return result_data
    except Exception as e:
        print('转发对象取得失败')
        print(e)
        close_oracle(con, curs)


def get_user_message_info(from_user_id=None):
    con, curs = basic_cit()
    try:
        get_data = {}
        sql2 = '''select count(*) FROM xdw_app.ms_user_message WHERE sender_id='%s' and receiver_id IN ('10001488','10001588')
               ''' % from_user_id
        print(sql2)
        curs.execute(sql2)
        info_data = curs.fetchall()
        get_data['user_message_info_no'] = info_data[0][0]
        print('取得消息通知成功')
        return get_data
    except Exception as e:
        print('取得消息通知失败')
        print(e)
        close_oracle(con, curs)


if __name__ == '__main__':
    #from_user_id = 10001577
    #restore_forward_task(from_user_id)
    restore_forward_task()
