# -*- coding= utf-8 -*-

"""
恢复拣选数据
"""
from UIAutomation.Utils import cit, close_oracle


def delete_business_framework(admin=None):
    try:
        con, curs = cit()
        sql = ['''update xdw_app.ms_card f set f.status=0 where
f.create_user_id='%s' and f.card_name='业务框架任务' ''' % admin,
               '''update xdw_app.ms_card f set f.status=0 where
f.create_user_id='%s' and f.card_name='业务框架任务' ''' % admin,
               '''delete from xdw_app.cm_participant_relation t where t.ppt_relation_ukid in
(select f.receiver_id from xdw_app.ms_card f where f.create_user_id='%s' and f.card_name='签订系统服务契约')''' % admin,
               '''update xdw_app.cm_participant_relation t set t.relation_status = '20' where t.ppt_relation_ukid =
(select t.receiver_id from xdw_app.ms_card t where t.owner_bu_id ='%s' and t.card_name = '业务框架任务' )''' % admin,
               '''delete from xdw_app.cm_participant_relation t where t.ppt_relation_ukid in
(select f.receiver_id from xdw_app.ms_card f where f.create_user_id='%s' and f.card_name='签订系统服务契约')''' % admin,
               '''delete from xdw_app.ts_operation t where
t.create_user_id='%s' and t.operation_name='签订系统服务契约' ''' % admin,
               '''delete from xdw_app.ms_card t where t.create_user_id='%s' and t.card_name='签订系统服务契约' ''' % admin,
               '''delete from xdw_app.dd_contract t where t.create_user_id='%s' ''' % admin,
               '''delete from xdw_app.ST_META_INVENTORY t where t.owner_id='%s' ''' % admin,
               '''delete from xdw_app.CM_PARTICIPANT t where t.create_user_id='%s' and t.status=2 ''' % admin,
               '''delete from xdw_app.RU_business_framework t where t.owner_id='%s' ''' % admin,
               '''delete from xdw_app.ru_operation_log t where t.log_user_id='%s' ''' % admin]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
            close_oracle(con, curs)
        print ("业务架构任务恢复成功！！！")
    except Exception as e:
        print (e)
