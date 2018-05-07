from UIAutomation.Utils import close_oracle, basic_cit, basic_sit
__author__ = 'chenyanxiu'


# 还原运输契约
def delete_transport_contract(user_id, participant_ukid, contract_type='TR'):
    # con, curs = basic_cit()
    con, curs = basic_sit()
    try:
        creator_ukid = get_creator_ukid(user_id)
        sql2 = ['''delete from xdw_app.ru_transport_supply_log where CONTRACT_SOURCE_UKID  in (select CONTRACT_UKID
                  from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s')'''
                  % (contract_type, participant_ukid),
                '''delete from xdw_app.rs_repository where owner_id in ('%s','%s')'''
                  % (participant_ukid, creator_ukid),
                '''delete from xdw_app.dd_contract_item where CONTRACT_UKID in (select CONTRACT_UKID from
                    xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s'and DEMANDER_ID='%s')'''
                  % (contract_type, participant_ukid, creator_ukid),
                '''delete from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s' and DEMANDER_ID='%s'
and contract_ascription ='CONTRACT' '''
                  % (contract_type, participant_ukid, creator_ukid)]
        for sql in sql2:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('删除运输契约成功')
    except Exception as e:
        print('删除运输契约失败')
        print(e)
        close_oracle(con, curs)


# 获取运输契约ukid
def get_transport_contract_ukid(participant_ukid, contract_type='TR'):
    # con, curs = basic_cit()
    con, curs = basic_sit()
    try:
        sql = '''select CONTRACT_UKID from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and
                 SUPPLIER_ID='%s' and CONTRACT_ASCRIPTION ='SUPPLY' order by create_time desc ''' \
              % (contract_type, participant_ukid)
        curs.execute(sql)
        result = curs.fetchall()
        print(result)
        if len(result) >= 1:
            contract_ukid = result[0][0]
            return contract_ukid
        else:
            return False
    except Exception as e:
        print('获取运输契约ukid失败')
        print(e)
        close_oracle(con, curs)


# 获取运输契约ITEM_ukid
def get_transport_contract_item_ukid(CONTRACT_UKID):
    # con, curs = basic_cit()
    con, curs = basic_sit()
    try:
        sql = '''select contract_item_ukid from xdw_app.dd_contract_item where CONTRACT_UKID =
                 '%s' order by create_time desc''' % (CONTRACT_UKID)
        curs.execute(sql)
        result = curs.fetchall()
        print(result)
        if len(result) >= 1:
            if len(result) == 1:
                contract_item_ukid = result[0][0]
                return contract_item_ukid
            else:
                contract_item_ukid = []
                for i in range(len(result)):
                    contract_item_ukid.append(result[i][0])
                return contract_item_ukid
        else:
            return False

    except Exception as e:
        print('获取运输契约item_ukid失败')
        print(e)
        close_oracle(con, curs)


# 获取运输契约信息:状态、数量、发布人名称、开始时间、结束时间
def get_transport_contract_info(user_id, contract_ukid, contract_item_ukid):
    # con, curs = basic_cit()
    con, curs = basic_sit()
    try:
        creator_ukid = get_creator_ukid(user_id)
        sql = '''select ddc.CONTRACT_UKID,ddc.SUPPLIER_ID,ddc.DEMANDER_ID,ddc.contract_status,cma.BRAND,ddci.qty,
    cma.DEPARTURE,cma.DESTINATIONS,ddci.start_time,ddci.end_time,ddup.SALE_PRICE,ddup.PRICE_UNIT,cma.RANGE_OF_WEIGHT,
    cma.RESOURCE_NAME, cma.COLLECT_AREA from xdw_app.CM_PARTICIPANT cmp,XDW_APP.dd_contract ddc,
    XDW_APP.dd_contract_item ddci,XDW_APP.RS_TRANSPORT_PUBLISH cma,XDW_APP.dd_unit_price ddup
    where cmp.participant_ukid ='%s' and ddc.CONTRACT_TYPE = 'TR'and ddc.CONTRACT_ASCRIPTION in('SUPPLY')and
    ddci.CONTRACT_UKID =ddc.CONTRACT_UKID and ddc.CONTRACT_UKID='%s' and ddci.CONTRACT_ITEM_UKID='%s' and
    ddci.REPOSITORY_UKID = cma.RESOURCE_ukid and ddup.contract_item_ukid = ddci.CONTRACT_ITEM_UKID
    Order by ddci.start_time desc''' % (creator_ukid, contract_ukid, contract_item_ukid)
        curs.execute(sql)
        result = curs.fetchall()
        print(result)
        dic= {'status': result[0][3], 'brand': result[0][4], 'qty': result[0][5], 'DEPARTURE': result[0][6],
              'DESTINATIONS': result[0][7], 'start_time': result[0][8], 'end_time': result[0][9],
              'SALE_PRICE': result[0][10], 'PRICE_UNIT': result[0][11], 'RANGE_OF_WEIGHT': result[0][12],
              'RESOURCE_NAME': result[0][13], 'COLLECT_AREA': result[0][14]}
        return dic
    except Exception as e:
        print('获取运输契约信息失败')
        print(e)
        close_oracle(con, curs)


# 签订运输契约后，查看新生成的契约，记录，资源信息，通过数量来判断
def get_new_transport_contract(user_id, contract_ukid):
    # con, curs = basic_cit()
    con, curs = basic_sit()
    try:
        dic = {}
        creator_ukid = get_creator_ukid(user_id)
        sql = '''select supplier_id from xdw_app.dd_contract where CONTRACT_UKID ='%s' ''' % contract_ukid
        curs.execute(sql)
        result = curs.fetchall()
        supplier_id = result[0][0]
        print(supplier_id)
        print(creator_ukid)
        sql2 = '''select count(*) from xdw_app.dd_contract where supplier_id ='%s' and demander_id ='%s' order by
                  create_time desc''' % (supplier_id, creator_ukid)
        curs.execute(sql2)
        result2 = curs.fetchall()
        dic['new_transport_contract_no'] = result2[0][0]

        sql3 = '''select count(*) from xdw_app.rs_repository where rs_type='TR' AND owner_id in ('%s','%s')'''\
                  % (supplier_id, creator_ukid)
        curs.execute(sql3)
        result3 = curs.fetchall()
        dic['rs_repository_no'] = result3[0][0]

        sql4 = '''select count(*) from xdw_app.ru_transport_supply_log where CONTRACT_SOURCE_UKID = '%s' AND
                  log_user_id = '%s' ''' % (contract_ukid, user_id)
        curs.execute(sql4)
        result4 = curs.fetchall()
        dic['operation_record_no'] = result4[0][0]
        return dic

    except Exception as e:
        print('获取运输契约信息失败')
        print(e)
        close_oracle(con, curs)


# 获取创造者id
def get_creator_ukid(user_id):
    # con, curs = basic_cit()
    con, curs = basic_sit()
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


def reduction_transport_contract(contract_ukid=51817000000009223):
    """
    还原运输供应契约
    """
    con, curs = basic_sit()
    try:
        sql_list = [
            '''update xdw_app.dd_contract set contract_status=20 where contract_ukid = '%s' ''' % contract_ukid,
            '''update xdw_app.dd_contract_item set qty = 3088 where contract_ukid = '%s' ''' % contract_ukid]
        for sql in sql_list:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原运输供应契约成功')
    except Exception as e:
        print('还原运输供应契约失败')
        print(e)
        close_oracle(con, curs)

