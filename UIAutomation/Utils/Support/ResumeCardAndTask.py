# -*- coding: utf-8 -*-
from common.common_method.database.ConnetToOracleDatabase import basic_cit, close_oracle
# Author:zhongchangwei


def resume_cards_and_tasks(participant_ukid, card_name):

    """
    还原当前卡片、任务、关系并且删除所有下游卡片、任务、关系
    :param participant_ukid: 参与者id
    :param card_name: 卡片或者任务名称
    """
    con, curs = basic_cit()
    try:
        # 获取卡片的创建时间和receiver_id
        sql1 = '''select receiver_id, create_time from xdw_app.ms_card where receiver_id in (select relation_sn from
                   xdw_app.cm_participant_relation where participant_ukid = %s) and card_name  = '%s' ''' \
               % (participant_ukid, card_name)
        curs.execute(sql1)
        result = curs.fetchall()
        receiver_id = result[0][0]
        card_create_time = result[0][1]
        card_create_time = card_create_time.strftime('%d-%m-%Y %H:%M:%S')

        # 获取任务的创建时间和pptr_ukid
        sql2 = '''select pptr_ukid, create_time from xdw_app.ts_operation where pptr_ukid in (select relation_sn from
                   xdw_app.cm_participant_relation where participant_ukid = %s) and operation_name  = '%s' ''' \
               % (participant_ukid, card_name)
        curs.execute(sql2)
        result = curs.fetchall()
        task_create_time = result[0][1]
        pptr_ukid = result[0][0]
        task_create_time = task_create_time.strftime('%d-%m-%Y %H:%M:%S')

        # 并且删除ts_tc_relation中删除下游信息
        sql3 = '''select card_ukid from (select * from xdw_app.ms_card where receiver_id in (select relation_sn from
                       xdw_app.cm_participant_relation where participant_ukid = '%s')) a where a.create_time >
                       to_date('%s', 'dd-mm-yyyy hh24:mi:ss') ''' % (participant_ukid, card_create_time)
        curs.execute(sql3)
        result = curs.fetchall()
        for r in result:
            sql4 = '''delete from xdw_app.ts_tc_relation where card_ukid in '%s' ''' % str(r[0])
            curs.execute(sql4)
            con.commit()

        # 删除下游的任务、卡片和关系
        sql_list = ['''delete from (select * from xdw_app.ms_card where receiver_id in (select relation_sn from
                       xdw_app.cm_participant_relation where participant_ukid = '%s')) a where a.create_time >
                       to_date('%s', 'dd-mm-yyyy hh24:mi:ss') ''' % (participant_ukid, card_create_time),
                    '''delete from (select * from xdw_app.ts_operation where pptr_ukid in (select relation_sn from
                       xdw_app.cm_participant_relation where participant_ukid = '%s')) a where a.create_time >
                       to_date('%s', 'dd-mm-yyyy hh24:mi:ss')''' % (participant_ukid, task_create_time),
                    '''delete from xdw_app.cm_participant_relation cmpr where cmpr.participant_ukid = '%s' and
                       cmpr.create_time>( select create_time from xdw_app.cm_participant_relation cmpr where
                       cmpr.relation_sn in '%s') and cmpr.relation_type = 'CARD' ''' % (participant_ukid, receiver_id),
                    '''delete from xdw_app.cm_participant_relation cmpr where cmpr.participant_ukid = '%s' and
                       cmpr.create_time>( select create_time from xdw_app.cm_participant_relation cmpr where
                       cmpr.relation_sn in '%s') and cmpr.relation_type = 'TASK' ''' % (participant_ukid, pptr_ukid)
                    ]
        for sql in sql_list:
            curs.execute(sql)
            con.commit()

        # 还原当前的卡片、任务、关系
        sql_list2 = ['''update xdw_app.ms_card set status = 0 where receiver_id in (select relation_sn from
                        xdw_app.cm_participant_relation where participant_ukid = %s) and card_name  = '%s'
                         ''' % (participant_ukid, card_name),
                     '''update xdw_app.ts_operation set status = 0 where pptr_ukid in (select relation_sn from
                        xdw_app.cm_participant_relation where participant_ukid = %s) and operation_name  = '%s'
                         ''' % (participant_ukid, card_name),
                     '''update xdw_app.cm_participant_relation set relation_status = 20 where relation_sn in %s'''
                     % receiver_id
                     ]
        for sql in sql_list2:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原成功')
    except Exception as e:
        print('还原失败')
        print(e)
        close_oracle(con, curs)
