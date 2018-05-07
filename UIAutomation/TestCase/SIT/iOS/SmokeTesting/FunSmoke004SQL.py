# -*- coding: utf-8 -*-
# language:zh-CN



# CY
from UIAutomation.Utils import close_oracle, cit, sit


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


def delete_supply_card(user_id=None):   # 删除仓储需求、仓储供给、运输供应卡片
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
        print ('删除供应卡片\n')
    except Exception as e:
        print (e)


def delete_commodity2(user_id=None):
    try:
        con, curs = cit()
        sql = ['''delete from xdw_app.cm_identify_item t where t.participant_ukid = '%s' and t.issue_party =
                  '商家' ''' % user_id,  # 上传的信息
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
        print ('恢复激活商品\n')
    except Exception as e:
        print (e)


def delete_entity_shop(user_id=None):
    try:
        con, curs = sit()
        sql = [  # 恢复激活实体店的输入项
            '''delete from xdw_app.ms_card t where t.card_step = '1' and t.owner_bu_id= '%s' ''' % user_id,
            '''delete from xdw_app.im_item_area t where t.building_ukid = (select t.sales_building_ukid
from basic_owner.ba_sales_building t where t.item_ukid =(select t.item_ukid from basic_owner.IM_ITEM t where
t.create_user_id = '%s'  and t.item_type = 'PHY_STORE'))''' % user_id,
            '''delete from xdw_app.IM_ITEM_ADDRESS t where t.building_ukid = (select t.sales_building_ukid
            from basic_owner.ba_sales_building t where t.item_ukid =(select t.item_ukid from basic_owner.IM_ITEM t where
            t.create_user_id = '%s'  and t.item_type = 'PHY_STORE'))''' % user_id,
            '''delete from xdw_app.IM_ITEM t where t.create_user_id = '%s'  and t.item_type = 'PHY_STORE' '''
            % user_id,
            '''delete from xdw_app.ba_shop t where t.create_user_id='%s' ''' % user_id,
            '''delete from xdw_app.ms_card t where t.owner_bu_id = '%s' and t.card_name = '激活实体店'
and t.card_step='3' ''' % user_id]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print('恢复实体店原始状态成功，不含杂质\n')
    except Exception as e:
        print(e)


def delete_warehouse_card(user_id=None):
    try:
        con, curs = cit()
        sql = [  # 恢复激活实体店的输入项
            '''update xdw_app.ts_operation t set t.status = '0' where t.operation_name = '激活仓库' and
t.owner_bu_id = '%s' ''' % user_id,
            '''update xdw_app.ms_card t set t.status = '0' where t.card_name = '激活仓库' and
t.owner_bu_id = '%s' ''' % user_id,
            '''update xdw_app.cm_participant_relation t set t.relation_status = '20'
where t.ppt_relation_ukid =(select t.receiver_id from xdw_app.ms_card t where t.owner_bu_id = '%s' and
t.card_name = '激活仓库' )''' % user_id,
            '''delete from xdw_app.im_item_area t where t.building_ukid =
(select t.warehouse_building_ukid from xdw_app.ba_warehouse_building t where t.item_ukid =
(select t.item_ukid from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  '仓库'))''' % user_id,
            '''delete from xdw_app.IM_ITEM_ADDRESS t where t.building_ukid =
(select t.warehouse_building_ukid from xdw_app.ba_warehouse_building t where t.item_ukid =
(select t.item_ukid from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  '仓库'))''' % user_id,
            '''delete from xdw_app.im_warehouse_item t where t.item_ukid =
(select t.item_ukid from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  '仓库')''' % user_id,
            '''delete from xdw_app.dd_resources_cost t where t.item_ukid =
(select t.item_ukid from xdw_app.IM_ITEM t where t.create_user_id = '%s' and t.item_type =  '仓库')''' % user_id
        ]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print ('恢复仓库原始状态成功，不含杂质\n')
    except Exception as e:
        print (e)


if __name__ == '__main__':
    delete_entity_shop(10001481)
    pass

