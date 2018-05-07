__author__ = 'chenyanxiu'
# 还原监控者和管理者权限,并删除任务和卡片
from UIAutomation.Utils import basic_cit, close_oracle, basic_sit


def reduction_monitor_and_manager_permissions(user_id1, user_id2):
    try:
        # con, curs = basic_cit()
        con, curs = basic_sit()
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

        sql3 = ['''delete from xdw_app.ts_operation tso where tso.pptr_ukid in (select relation_sn from
                  XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s','%s')) and
                tso.card_type in ('MonitorAuthorizeService', 'ManagerAuthorizeService') ''' % (user_id1, user_id2),
                '''delete from xdw_app.ms_card where RECEIVER_ID in (select cmpr.relation_sn from
                xdw_app.CM_PARTICIPANT_relation  cmpr where PARTICIPANT_UKID in ('%s', '%s')) and card_type in
                ( 'MonitorAuthorizeService','ManagerAuthorizeService')''' % (user_id1, user_id2)]
        for sql in sql3:
            curs.execute(sql)
            con.commit()

        sql4 = ['''delete from xdw_app.ts_operation tso where tso.pptr_ukid in (select relation_sn from
            XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s','%s')) and
          tso.card_type in ('QueryNewEmployeesService', 'PublishWarehouseSupply','PublishWarehouseDemand',
          'PublishLaborDemand','PublishWarehouseSupply','PublishGoodsSupply') ''' % (user_id1, user_id2),
                '''delete from xdw_app.ms_card where RECEIVER_ID in (select cmpr.relation_sn from
                xdw_app.CM_PARTICIPANT_relation  cmpr where PARTICIPANT_UKID in ('%s', '%s')) and card_type in
                ('QueryNewEmployeesService', 'PublishWarehouseSupply','PublishWarehouseDemand',
          'PublishLaborDemand','PublishWarehouseSupply','PublishGoodsSupply','PublishTransportSupply','ActiveStockService','PhysicalStoreService','ActiveShopService','ActiveGoodsService')''' % (user_id1, user_id2)]
        for sql in sql4:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原监控者和管理者权限')
    except Exception as e:
        print(e)


def reduction_distribution_manager_and_supervisor_task(user_id):  # 还原分配管理者和监控者任务
    try:
        # con, curs = basic_cit()
        con, curs = basic_sit()
        sql1 = ['''delete from xdw_app.au_role_item auri where au_role_item_ukid in(
                    select auri.au_role_item_ukid from xdw_app.au_role aur,
                    xdw_app.au_role_item auri where aur.au_role_ukid =
                    auri.au_role_ukid  and aur.create_user_id = '%s' and role_type in ('21','31','22','32'))''' % user_id,
                '''delete from xdw_app.au_role where create_user_id ='%s' and role_type in ('21','31','22','32')''' % user_id,
                '''delete from xdw_app.au_role where participant_ukid ='%s' and role_type in ('1') ''' % user_id,
                '''update xdw_app.cm_participant_relation set relation_status = 20 where relation_sn in (select receiver_id
                   from xdw_app.ms_card where card_name = '分配管理者和监控者') and  PARTICIPANT_UKID ='%s' ''' % user_id,
                '''delete from xdw_app.ms_card where receiver_id in (select relation_sn from xdw_app.cm_participant_relation
                    where participant_ukid = '%s') and card_name in ('发布运输供应','发布供货供应','发布仓储供应',
                    '发布仓储需求','发布劳务需求','激活商品','激活仓库','授权并新增店铺','激活实体店')''' % user_id]
        for sql in sql1:
            curs.execute(sql)
            con.commit()

        sql2 = ['''update xdw_app.ts_operation set status = 0 where pptr_ukid in (select relation_sn from
                   XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s'))
                    and card_type in ('AllotManagerAndMonitorService') ''' % user_id,
                '''delete from xdw_app.ts_operation tso where tso.pptr_ukid in (select relation_sn from
                    XDW_APP.CM_PARTICIPANT_relation  where PARTICIPANT_UKID in('%s')) and
                    tso.card_type in ('ManagerAuthorizeService','MonitorAuthorizeService','QueryNewEmployeesService')
                    ''' % user_id,
                '''update xdw_app.ms_card set status = 0 where receiver_id in (select cmpr.relation_sn from
                   xdw_app.CM_PARTICIPANT_relation  cmpr where PARTICIPANT_UKID = '%s')   and card_type =
                    'AllotManagerAndMonitorService' ''' % user_id,
                '''delete from xdw_app.ms_card where receiver_id in (select cmpr.relation_sn from
                    xdw_app.CM_PARTICIPANT_relation  cmpr where PARTICIPANT_UKID = '%s')   and card_type
                    in( 'ManagerAuthorizeService','MonitorAuthorizeService','QueryNewEmployeesService')''' % user_id]
        for sql in sql2:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原分配管理者和监控者任务')
    except Exception as e:
        print('还原分配管理者和监控者任务失败')
        print(e)


def get_operation(user_id):
    try:
        # con, curs = basic_cit()
        con, curs = basic_sit()
        sql = '''select operation_ukid from xdw_app.ts_operation where owner_bu_id='%s'
                    and card_type in ('AllotManagerAndMonitorService')''' % user_id
        curs.execute(sql)
        result = curs.fetchall()
        close_oracle(con, curs)
        return result[0][0]
    except Exception as e:
        print('还原分配管理者和监控者任务失败')
        print(e)


def reduction_d(operation_ukid):
    try:
        # con, curs = basic_cit()
        con, curs = basic_sit()
        print(operation_ukid)
        operation_ukid = str(operation_ukid)
        operation_ukid1 = operation_ukid + '%'
        print(operation_ukid1)
        sql = '''delete from xdw_app.ts_tc_relation where sn like '%s' ''' % operation_ukid1
        curs.execute(sql)
        con.commit()
        close_oracle(con, curs)
        print('还原分配管理者和监控者任务1')
    except Exception as e:
        print('还原分配管理者和监控者任务失败')
        print(e)
