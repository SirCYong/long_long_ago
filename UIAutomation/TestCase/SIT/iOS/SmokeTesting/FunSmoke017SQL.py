# -*- coding: utf-8 -*-
from UIAutomation.Utils import close_oracle, basic_cit

# Author:chenyanxiu


def reduction_non_service_certification_task(user_id):  # 还原非服务认证任务
    try:
        con, curs = basic_cit()
        sql1 = ['''delete from xdw_app.au_role_item where au_role_ukid in(select au_role_ukid from
                    xdw_app.au_role where participant_ukid  ='%s' )''' % user_id,
                '''delete from xdw_app.au_role where participant_ukid ='%s' ''' % user_id]
        for sql in sql1:
            curs.execute(sql)
            con.commit()

        sql2 = ['''delete from xdw_app.ms_card where card_type = 'ManagerAuthorizeService' and RECEIVER_ID
in (select relation_sn from xdw_app.CM_PARTICIPANT_RELATION where PARTICIPANT_UKID='%s'and relation_status=20)'''
                % user_id,
                '''delete from xdw_app.TS_OPERATION where pptr_ukid in (select relation_sn from xdw_app.CM_PARTICIPANT_RELATION
              where PARTICIPANT_UKID='%s'and relation_status=20) and card_type='ManagerAuthorizeService' ''' % user_id,
                '''delete from xdw_app.CM_PARTICIPANT_RELATION where relation_sn in'%s' ''' % user_id,
                '''delete from xdw_app.HM_CREATOR_RELATION where participant_ukid ='%s' ''' % user_id,
                '''delete from xdw_app.ts_operation tso where tso.pptr_ukid in (select relation_sn from
XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in(%s)) ''' % user_id,
                '''delete from xdw_app.ms_card msc where msc.receiver_id in (select relation_sn from
XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in(%s)) ''' % user_id]
        for sql in sql2:
            curs.execute(sql)
            con.commit()
        sql3 = '''update XDW_APP.CM_PARTICIPANT cmp set status ='2' where cmp.participant_ukid ='%s' ''' % user_id
        curs.execute(sql3)
        con.commit()
        close_oracle(con, curs)
        print('还原非服务认证任务')
    except Exception as e:
        print(e)


def restore_card(invitee_id):
    try:
        con, curs = basic_cit()
        sql1 = ['''update  xdw_app.MS_CARD m  set m.status=0, m.is_view=0 where 1=1 and receiver_id in
                   (select c.relation_sn from xdw_app.cm_participant_relation c where c.participant_ukid = '%s') and
                   m.card_type='RegNoService' ''' % invitee_id,
                '''update XDW_APP.TS_OPERATION set status = '0' where OPERATION_ukid in(select OPERATION_ukid
from xdw_app.ms_card where  card_type='RegNoService' and receiver_id in(select relation_sn from
xdw_app.CM_PARTICIPANT_RELATION where PARTICIPANT_UKID='%s') )and card_type='RegNoService' ''' % invitee_id,
                '''update xdw_app.CM_PARTICIPANT_RELATION set relation_status=20 where relation_status=30 and
relation_sn in( select receiver_id from xdw_app.ms_card where  card_type='RegNoService' and receiver_id in
(select relation_sn from xdw_app.CM_PARTICIPANT_RELATION where PARTICIPANT_UKID='%s'and relation_status=30) )
                ''' % invitee_id]
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原非服务认证任务kp')
    except Exception as e:
        print(e)


def reduction_task(user_id, invitee_id):  # 还原任务移交
    try:
        con, curs = basic_cit()  # 删除邀请表信息
        creator_id = get_creator_ukid(user_id)
        sql = '''UPDATE xdw_app.CM_PARTICIPANT_RELATION set relation_status=20 where relation_sn =(select receiver_id
from xdw_app.ms_card where card_type='RegNoService' and receiver_id in(select relation_sn from
xdw_app.CM_PARTICIPANT_RELATION where PARTICIPANT_UKID='%s'and relation_status=90))
and participant_ukid ='%s' ''' % (user_id, user_id)

        print(user_id, invitee_id)
        curs.execute(sql)
        con.commit()
        sql1 = ['''delete from xdw_app.CM_PARTICIPANT_RELATION where relation_sn =(select receiver_id
from xdw_app.ms_card where card_type='RegNoService' and receiver_id in(select relation_sn from
xdw_app.CM_PARTICIPANT_RELATION where PARTICIPANT_UKID='%s'and relation_status=20))
and participant_ukid ='%s' ''' % (invitee_id, invitee_id),
                '''UPDATE xdw_app.ms_card set OWNER_BU_ID='%s' where card_type='RegNoService' and receiver_id in(select relation_sn from
xdw_app.CM_PARTICIPANT_RELATION where PARTICIPANT_UKID='%s')''' % (creator_id, user_id)]
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原任务移交\n')
    except Exception as e:
        print(e)


def reduction_select(invitee_id):  # 还原图片选中
    try:
        con, curs = basic_cit()# 删除邀请表信息
        sql = '''update  xdw_app.ba_user set locked='' where user_id='%s' ''' % invitee_id
        curs.execute(sql)
        con.commit()
        close_oracle(con, curs)
        print('还原图片选中\n')
    except Exception as e:
        print(e)


# 获取创造者id
def get_creator_ukid(user_id):
    con, curs = basic_cit()
    try:
        sql1 = '''select count(*) from xdw_app.au_role where role_type = 1 and participant_ukid='%s' ''' \
               % user_id
        curs.execute(sql1)
        result = curs.fetchall()
        if result[0][0] >= 1:
            return user_id
        else:
            sql2 = '''select creator_ukid from xdw_app.hm_creator_relation where participant_ukid='%s' ''' \
                   % user_id
            curs.execute(sql2)
            result2 = curs.fetchall()
            return result2[0][0]
    except Exception as e:
        print('获取创造者信息失败')
        print(e)
        close_oracle(con, curs)

