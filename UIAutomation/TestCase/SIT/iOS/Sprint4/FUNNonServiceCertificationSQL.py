# -*- coding: utf-8 -*-
from UIAutomation.Utils import close_oracle, basic_cit

# Author:chenyanxiu


def reduction_non_service_certification_task(user_id):  # 还原非服务认证任务
    try:
        con, curs = basic_cit()
        sql1 = ['''delete from xdw_app.au_role_item where participant_ukid  ='%s' )''' % user_id,
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
XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s')) ''' % user_id,
                '''delete from xdw_app.ms_card msc where msc.receiver_id in (select relation_sn from
XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s')) ''' % user_id]
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


def view_permissions(participant, role_type):   # 查看权限
    try:
        con, curs = basic_cit()
        sql = '''select ari.au_role_item_ukid,ari.status,ari.racix,ari.perform_switch,ari.operation_unit_ukid,
                  ari.creator_ukid,ari.role_type,cou.process_name from xdw_app.au_role_item ari,
                  xdw_app.cf_operation_unit cou where ari.operation_unit_ukid = cou.operation_unit_ukid
                  and ari.participant_ukid = '%s'order by ari.creator_ukid,ari.role_type = '%s' '''\
                % (participant, role_type)
        curs.execute(sql)
        result = curs.fetchall()
        close_oracle(con, curs)
        l1 = []
        for r in result:
            l1.append(r[0])
        return l1

    except Exception as e:
        print(e)


def reduction_select(invitee_id):  # 还原图片选中
    try:
        con, curs = basic_cit()  # 删除邀请表信息
        sql = '''update xdw_app.ba_user set locked='' where user_id='%s' ''' % invitee_id
        curs.execute(sql)
        con.commit()
        close_oracle(con, curs)
        print('还原图片选中\n')
    except Exception as e:
        print(e)


def insert_data(invitee_id):
    try:
        con, curs = basic_cit()
        sql1 = ['''insert into xdw_app.ba_user (USER_ID, USER_NAME, PASSWORD, CREATE_TIME, UPDATE_USER_ID, UPDATE_TIME,
         PASSWORD_CHANGE_NEXT, EXPIRED_DATE, LOCKED, LOCKED_DATE, MOBILE, CREATE_USER_ID, FACE_URI, OPENID, COUNTRY_CALLING_CODE)
        values ('%s', '薄荷', '8CE1904AB59D2529D7109DE13268E846', to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'),
         '', to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'), '', null, '', null, '17934560908', '%s',
          '/temp/9b07a5f9-a912-4f73-8aea-1e63dbd70d5d.jpeg', 'o8niLvyLIeX7tZUjwd5JTcy0k7x0', '+86')
          ''' % (invitee_id, invitee_id),
                '''insert into xdw_app.cm_human (HUMAN_ID, HUMAN_NAME, HUMAN_SEX, HUMAN_HEIGHT, HUMAN_WEIGHT,
HUMAN_BIRTHDAY, IDENTIFY_ID, BIRTH_PLACE, CREATE_TIME, UPDATE_TIME, UPDATE_USER_ID, CREATE_USER_ID)
values ('%s', '薄荷', '', '', '', null, '%s', '', to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'),
 to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'), '', '%s')''' % (invitee_id, invitee_id, invitee_id,),
                '''insert into xdw_app.cm_participant (PARTICIPANT_UKID, PPT_TYPE, PPT_NAME, IDENTIFY_ID, CREATE_TIME,
                    UPDATE_TIME, UPDATE_USER_ID, CREATE_USER_ID, STATUS)
values ('%s', 'P', '薄荷', '', to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'),
 to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'), '', '%s', '2')''' % (invitee_id, invitee_id),
                '''insert into xdw_app.cm_identify (IDENTIFY_UKID, IDENTIFY_TYPE, RELATED_TYPE, IDENTIFY_CODE,
IDENTIFY_NAME, MEDIAS_UKID, ISSUE_PARTY, PARTICIPANT_UKID, CREATE_TIME, UPDATE_TIME, UPDATE_USER_ID, CREATE_USER_ID)
values ('%s', '身份证', 'PPT', '341022195673241517', '薄荷', '51792700000062140', '10', '260001',
to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'), to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'), '',
 '%s')''' % (invitee_id, invitee_id),
                '''insert into xdw_app.ru_invite (UKID, INVITEE_NAME, INVITEE_MOBILE, INVITEE_PARTICIPANT_UKID,
 AUTH_TASK_OPERATION_UKID, INVITE_TASK_OPERATION_UKID, MESSAGE_TOPIC, SERVICE_TYPE, ROLE_TYPE, INVITE_PURPOSE,
 INVITE_CODE, CREATE_TIME, CREATE_USER_ID, INVALID_TIME, INVITER_PARTICIPANT_UKID, STATUS, UPDATE_TIME, UPDATE_USER_ID,
  REGISTER_TASK_OPERATION_UKID, OPENID, CREATOR_UKID)
values ('51792100000062151', '别拿', '18915121114', '%s', '51792700000062143', '1', 'notServiceInvite', '2', '2',
 '{"roleType":"2","mobile":"18915121114","inviteeType":"2","authority":[{"id":"100022","racix":"1","name":"发布运输供应的任务"},
 {"id":"100053","racix":"1","name":"下载在售商品"},{"id":"100057","racix":"1","name":"导入历史采购单"}],"operationUkid":"0",
 "grantor":"199566","inviteeName":"别拿","operationType":"1","cardUkid":"1","inviteeContent":"品牌片邀请您下载网仓3号并注册账号，同时授予您一些权限",
 "operationer":"0","creatorUkid":199566}', '921dae00b51811e6b93fa24bc6fae6a5', to_date('28-11-2016 11:13:01', 'dd-mm-yyyy hh24:mi:ss'),
 '199566', to_date('28-11-2016 11:43:01', 'dd-mm-yyyy hh24:mi:ss'), '199566', '2', to_date('28-11-2016 11:16:08', 'dd-mm-yyyy hh24:mi:ss'),
  '199566', '51792900000062137', 'o8niLvyLIeX7tZUjwd5JTcy0k7x0', '199566') ''' % invitee_id,
                '''insert into xdw_app.cm_Wechat_msg (OPENID, NICKNAME, SEX, PROVINCE, CITY, COUNTRY, HEADIMGURL,
PRIVILIGE, UNIONID, PARTICIPANT_UKID)
values ('o8niLvyLIeX7tZUjwd5JTcy0k7x0', '周锦', '2', 'Anhui', 'Hefei', 'CN',
'http://wx.qlogo.cn/mmopen/qnJx7zxm04lWXAJoKyBj8tOFH4h3Q1EVqthvkbanCo2mG8wpe9Ngqk4u8un2AmY709ibialicbiaRfO5Tmg1j30bjc1Bjdz2UHpe/0',
'', 'o08F4wy9B_YjDW5xoH00ATb0ntDE', '%s')''' % invitee_id]
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原数据\n')
    except Exception as e:
        print (e)




