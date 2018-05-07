# -*- coding: utf-8 -*-


# Author:zhongchangwei
from UIAutomation.Utils import basic_cit, sit
from UIAutomation.Utils import close_oracle


def reduction_payment_info(userid=10000428):
    try:
        con, curs = basic_cit()
        sql1 = ['''delete from xdw_app.TS_PAYMENT_RECORDS t where t.create_user_id='%s' ''' % userid,
                '''delete from xdw_app.ts_payment_bill_detail n where n.bill_ukid  in
                  (select o.bill_ukid from xdw_app.ts_payment_bill  o  where  o.create_user_id='%s')''' % userid,
                '''delete from xdw_app.ts_payment_bill  o  where  o.create_user_id='%s' ''' % userid,
                '''delete from xdw_app.ts_operation where pptr_ukid in (select ppt_relation_ukid from
                   XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s')) and operation_type !='RegService'
                   ''' % userid,
                '''update xdw_app.ts_operation set status = '0'where  pptr_ukid in (select ppt_relation_ukid from
                   XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s')) ''' % userid,
                '''delete from xdw_app.MS_CARD where  RECEIVER_ID = '%s' and CARD_type != 'RegService' ''' % userid,
                '''update xdw_app.MS_CARD set STATUS = '0' where RECEIVER_ID = '%s' ''' % userid]
        for sql in sql1:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
    except Exception as e:
        print(e)


def reduction_service_type(userid=10000428):
    con, curs = basic_cit()
    sql1 = '''delete from xdw_app.CM_REGISTERED_SUPPLY_DEMAND where CREATE_USER_ID = '%s' ''' % userid
    curs.execute(sql1)
    con.commit()
    close_oracle(con, curs)


def view_permissions(participant='1111111002', role_type='32'):   # 查看权限
    try:
        con, curs = basic_cit()
        sql = '''select aui.item_type from  xdw_app.au_item aui,xdw_app.au_role_item auri  left join
                xdw_app.au_role aur  on auri.au_role_ukid  =  aur.au_role_ukid where auri.au_role_ukid in (select
                au_role_ukid from xdw_app.au_role where PARTICIPANT_UKID ='%s') and auri.au_item_ukid =
                aui.au_item_ukid and auri.status = 0 and aur.role_type = '%s' order by aui.item_type'''\
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


# 还原监控者和管理者权限,并删除任务和卡片
def reduction_monitor_and_manager_permissions(user_id1=1111111002, user_id2=1111111003):
    try:
        con, curs = basic_cit()
        sql = ''' delete from xdw_app.au_role_item auri where au_role_item_ukid in(
                select auri.au_role_item_ukid from xdw_app.au_role aur,xdw_app.au_role_item auri where
                aur.au_role_ukid =auri.au_role_ukid  and aur.PARTICIPANT_UKID in ('%s','%s')
                and role_type in ('22','32'))''' % (user_id1, user_id2)
        curs.execute(sql)
        con.commit()

        sql2 = '''delete from xdw_app.au_role where PARTICIPANT_UKID in ('%s','%s')
                  and role_type in ('22','32') ''' % (user_id1, user_id2)
        curs.execute(sql2)
        con.commit()

        sql3 = ['''select * from xdw_app.ts_operation tso where tso.pptr_ukid in (select ppt_relation_ukid from
                  XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s','%s')) and
                tso.card_type in ('MonitorAuthorizeService', 'ManagerAuthorizeService') ''' % (user_id1, user_id2),
                '''delete from xdw_app.ms_card where RECEIVER_ID in ('%s','%s') and card_type in
                ( 'MonitorAuthorizeService','ManagerAuthorizeService')''' % (user_id1, user_id2)]
        for sql in sql3:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原监控者和管理者权限')
    except Exception as e:
        print(e)


def reduction_distribution_manager_and_supervisor_task(user_id=10000428):  # 还原分配管理者和监控者任务
    try:
        con, curs = basic_cit()
        sql1 = ['''delete from xdw_app.au_role_item auri where au_role_item_ukid in(
                    select auri.au_role_item_ukid from xdw_app.au_role aur,
                    xdw_app.au_role_item auri where aur.au_role_ukid =
                    auri.au_role_ukid  and aur.create_user_id = '%s' and role_type in ('21','31'))''' % user_id,
                '''delete from xdw_app.au_role where create_user_id ='%s' and role_type in ('21','31')''' % user_id,
                '''delete from xdw_app.au_role where participant_ukid ='%s' and role_type in ('1') ''' % user_id]
        for sql in sql1:
            curs.execute(sql)
            con.commit()

        sql2 = ['''update xdw_app.ts_operation set status = 0 where pptr_ukid in (select ppt_relation_ukid from
                  XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s'))
                    and card_type in ('AllotManagerAndMonitorService') ''' % user_id,
                '''delete from xdw_app.ts_operation tso where tso.pptr_ukid in (select ppt_relation_ukid from
                    XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s')) and
                    tso.card_type in ('ManagerAuthorizeService','MonitorAuthorizeService','QueryNewEmployeesService')
                    ''' % user_id,
                '''update xdw_app.ms_card set status = 0 where RECEIVER_ID = '%s' and card_type =
                    'AllotManagerAndMonitorService' ''' % user_id,
                '''delete from xdw_app.ms_card where RECEIVER_ID = '%s' and card_type
                    in( 'ManagerAuthorizeService','MonitorAuthorizeService','QueryNewEmployeesService')''' % user_id]
        for sql in sql2:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原分配管理者和监控者任务')
    except Exception as e:
        print(e)


def get_distribution_manager_and_supervisor_task_status(user_id=10000428):    # 获取任务状态
    try:
        con, curs = basic_cit()
        sql1 = '''select tso.status from xdw_app.ts_operation tso where tso.pptr_ukid in
                  (select ppt_relation_ukid from  XDW_APP.CM_PARTICIPANT_relation  where
                  PARTICIPANT_UKID in('%s')) and card_type = 'AllotManagerAndMonitorService' ''' % user_id
        curs.execute(sql1)
        result = curs.fetchall()
        close_oracle(con, curs)
        return result[0][0]
    except Exception as e:
        print(e)


def judge_manager_and_supervisor_result(user_id=10000428):   # 分配成功后，查看角色和权限
    try:
        con, curs = basic_cit()
        sql1 = "select role_type from xdw_app.au_role where create_user_id ='%s' and status = 1" % user_id  # 获取角色
        curs.execute(sql1)
        result = curs.fetchall()
        if len(result) == 2 and result[0][0] in (21, 31) and result[1][0] in (21, 31) and result[1][0] != result[0][0]:
            pass
        else:
            return False

        sql2 = '''select aui.item_type from  xdw_app.au_item aui,xdw_app.au_role_item auri  left join
             xdw_app.au_role aur  on auri.au_role_ukid  =  aur.au_role_ukid where auri.au_role_ukid in (select
             au_role_ukid from xdw_app.au_role where PARTICIPANT_UKID ='%s') and auri.au_item_ukid = aui.au_item_ukid
             and auri.status = 0 and aur.role_type = 21 order by aui.item_type''' % user_id
        curs.execute(sql2)
        result2 = curs.fetchall()

        sql3 = '''select item_type from xdw_app.au_item order by item_type '''
        curs.execute(sql3)
        result3 = curs.fetchall()
        if result2 == result3:     # 判断管理者权限集
            pass
        else:
            return False

        sql4 = ''' select aui.item_type from  xdw_app.au_item aui,xdw_app.au_role_item auri  left join
                xdw_app.au_role aur  on auri.au_role_ukid  =  aur.au_role_ukid where auri.au_role_ukid in (select
                au_role_ukid from xdw_app.au_role where PARTICIPANT_UKID ='%s') and auri.au_item_ukid =
                aui.au_item_ukid and auri.status = 0 and aur.role_type = 31 order by aui.item_type''' % user_id
        curs.execute(sql4)
        result4 = curs.fetchall()
        close_oracle(con, curs)

        if result4 == result3:     # 判断监控者权限集
            flag = 1
        else:
            return False
        if flag == 1:
            return True
        else:
            return False
    except Exception as e:
        print(e)


def reduction_non_service_certification_task(user_id=10000387):  # 还原非服务认证任务
    try:
        con, curs = basic_cit()
        sql1 = ['''delete from xdw_app.au_role_item where au_role_ukid in(select au_role_ukid from
                    xdw_app.au_role where participant_ukid  ='%s' )''' % user_id,
                '''delete from xdw_app.au_role where participant_ukid ='%s' ''' % user_id]
        for sql in sql1:
            curs.execute(sql)
            con.commit()

        sql2 = ['''delete from xdw_app.ms_card where RECEIVER_ID = '%s' and card_type = 'ManagerAuthorizeService' '''
                % user_id,
                '''delete from xdw_app.TS_OPERATION where pptr_ukid in (select ppt_relation_ukid from
                  XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s')) and
                  card_type='ManagerAuthorizeService' ''' % user_id]
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


def restore_card(inviter_id=10000237):
    try:
        con, curs = basic_cit()
        sql1 = ['''update xdw_app.ms_card set status = 0  where RECEIVER_ID = '%s' and card_type =
                  'RegNoService' ''' % inviter_id,
                '''update xdw_app.TS_OPERATION set status = '0' where
                  pptr_ukid in (select ppt_relation_ukid from  XDW_APP.CM_PARTICIPANT_relation
                  where PARTICIPANT_UKID in('%s')) and card_type='RegNoService' ''' % inviter_id]
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
        sql = '''UPDATE xdw_app.ms_card set receiver_id='%s',update_user_id='%s'where card_type='RegNoService' and
                receiver_id='%s' ''' % (user_id, user_id, invitee_id)
        curs.execute(sql)
        con.commit()

        sql1 = '''UPDATE XDW_APP.CM_PARTICIPANT_RELATION SET PARTICIPANT_UKID='%s'WHERE PARTICIPANT_UKID='%s' ''' \
               % (user_id, invitee_id)
        curs.execute(sql1)
        con.commit()
        close_oracle(con, curs)
        print('还原任务移交\n')
    except Exception as e:
        print(e)

# CY


def delete_customer_card(user_id=199251):
    try:
        con, curs = cit()
        sql = ['''delete from xdw_app.ms_card t
                  where t.owner_bu_id = '%s' and t.card_name = '确定被服务的服务类型' ''' % user_id,
               '''update xdw_app.ts_operation t set t.status = '0' where t.operation_name = '确定需要的服务类型'
                  and t.owner_bu_id = '%s' ''' % user_id,
               '''update xdw_app.ms_card t set t.status = '0' where t.card_name = '确定需要的服务类型'
                  and t.owner_bu_id = '%s' ''' % user_id,
               '''update xdw_app.cm_participant_relation t set t.relation_status = '20'where t.ppt_relation_ukid =
                (select t.receiver_id from xdw_app.ms_card t where t.owner_bu_id = '%s' and t.card_name =
                '确定需要的服务类型' )''' % user_id]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print ('删除我要客户卡片\n')
    except Exception as e:
        print (e)


def delete_warehouse_card(user_id=199251):   # 删除仓储需求、仓储供给、运输供应卡片
    try:
        con, curs = cit()
        sql = ['''delete from xdw_app.ms_card t where t.owner_bu_id = '%s' and t.card_name =
               '发布仓储供应' ''' % user_id,
               '''delete from xdw_app.ms_card t where t.owner_bu_id = '%s' and t.card_name =
               '发布供货供应' ''' % user_id,
               '''delete from xdw_app.ms_card t where t.owner_bu_id = '%s' and t.card_name =
               '发布运输供应' ''' % user_id]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print ('供应卡片\n')
    except Exception as e:
        print (e)


def delete_commodity(user_id=None):
    try:
        con, curs = sit()
        sql = ['''delete from xdw_app.cm_identify_relation t where t.issue_party='%s'
                  and t.identify_type='ITEM_CODE' ''' % user_id,
               '''update xdw_app.ts_operation t set t.status = '0' where t.operation_name = '激活商品'
                  and t.owner_bu_id =  '%s' ''' % user_id,
               '''update xdw_app.ts_operation t set t.status = '0' where t.operation_name = '激活商品'
                  and t.owner_bu_id = '%s' ''' % user_id,
               '''update xdw_app.ms_card t set t.status = '0' where t.card_name = '激活商品'
                  and t.owner_bu_id = '%s' ''' % user_id,
               '''update xdw_app.cm_participant_relation t set t.relation_status = '20'
                  where t.ppt_relation_ukid = (select t.receiver_id from xdw_app.ms_card t
                  where t.owner_bu_id = '%s' and t.card_name = '激活商品' )''' % user_id
               ]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print('恢复激活商品\n')
    except Exception as e:
        print(e)


def delete_entity_shop(admin=None):
    try:
        con, curs = sit()
        sql = [  # 恢复激活实体店的输入项
            '''update xdw_app.ts_operation t set t.status = '0' where t.operation_name = '导入历史采购单'
and t.owner_bu_id = '%s' ''' % admin,
            '''update xdw_app.ms_card t set t.status = '0' where t.card_name = '导入历史采购单'
and t.owner_bu_id = '%s' ''' % admin,
            '''update xdw_app.cm_participant_relation t set t.relation_status = '20'where t.ppt_relation_ukid =
(select t.receiver_id from xdw_app.ms_card t where t.owner_bu_id = '%s' and t.card_name = '导入历史采购单' )''' % admin,
            '''update xdw_app.ts_operation t set t.status = '0' where t.operation_name = '激活实体店'
and t.owner_bu_id = '%s' ''' % admin,
            '''update xdw_app.ms_card t set t.status = '0' where t.card_name = '激活实体店' and t.owner_bu_id = '%s' '''
            % admin,
            '''update xdw_app.cm_participant_relation t set t.relation_status = '20' where t.ppt_relation_ukid =
(select t.receiver_id from xdw_app.ms_card t where t.owner_bu_id = '%s' and t.card_name = '激活实体店' )''' % admin,
            '''update xdw_app.ms_card t set t.card_step = '' where t.card_ukid =(select t.card_ukid
from xdw_app.ms_card t where t.owner_bu_id = '%s' and t.card_name = '激活实体店')''' % admin,
            '''delete from xdw_app.im_item_area t where t.building_ukid = (select t.sales_building_ukid
from basic_owner.ba_sales_building t where t.item_ukid =(select t.item_ukid from basic_owner.IM_ITEM t where
t.create_user_id = '%s'  and t.item_type = '实体店'))''' % admin,
            '''delete from xdw_app.IM_ITEM_ADDRESS t where t.building_ukid = (select t.sales_building_ukid
            from basic_owner.ba_sales_building t where t.item_ukid =(select t.item_ukid from basic_owner.IM_ITEM t where
            t.create_user_id = '%s'  and t.item_type = '实体店'))''' % admin,
            '''delete from basic_owner.IM_ITEM t where t.create_user_id = '%s'  and t.item_type = '实体店' ''' % admin,
            '''delete from xdw_app.ba_shop t where t.shop_name = '店大欺人' '''
#             '''delete from xdw_app.ts_tc_relation t where t.sn =
# (select t.operation_ukid||'-UploadPurchaseExcel' from
# (select  to_char(t.operation_ukid) operation_ukid  from xdw_app.ts_operation t
# where t.owner_bu_id = '%s' and t.operation_type = 'PhysicalStoreService' )t) ''' % admin
               ]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print('恢复实体店原始状态成功，不含杂质\n')
    except Exception as e:
        print(e)


def delete_depot_card(admin=None):
    try:
        con, curs = sit()
        sql = [  # 恢复激活仓库的输入项
            '''delete from xdw_app.im_item_area t where t.building_ukid =
(select t.warehouse_building_ukid from xdw_app.ba_warehouse_building t where t.item_ukid =
(select t.item_ukid from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  'STOCK'))''' % admin,
            '''delete from xdw_app.IM_ITEM_ADDRESS t where t.building_ukid =
(select t.warehouse_building_ukid from xdw_app.ba_warehouse_building t where t.item_ukid =
(select t.item_ukid from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  'STOCK'))''' % admin,
            '''delete from xdw_app.im_warehouse_item t where t.item_ukid =
(select t.item_ukid from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  'STOCK')''' % admin,
            '''delete from xdw_app.dd_resources_cost t where t.item_ukid =
(select t.item_ukid from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  'STOCK')''' % admin,
            '''delete from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  'STOCK' ''' % admin
        ]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print('恢复仓库原始状态成功，不含杂质\n')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    delete_depot_card(10001472)

# print(reduction_non_service_certification_task())
# print(restore_card())
# print (reduction_task())
