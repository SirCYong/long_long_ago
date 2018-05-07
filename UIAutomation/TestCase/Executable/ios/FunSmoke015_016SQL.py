from UIAutomation.Utils import close_oracle, basic_sit
__author__ = 'zhongchangwei'


# 删除仓储契约
def delete_warehouse_contract(user_id, contract_type, participant_ukid, contract_ascription='SUPPLY'):
    """

    :param user_id:
    :param contract_type:
    :param participant_ukid:
    :param contract_ascription:
    :rtype: object
    """
    con, curs = basic_sit()
    try:
        creator_ukid = get_creator_ukid(user_id)
        sql2 = []
        if contract_ascription == 'SUPPLY':
            sql2 = ['''delete from xdw_app.dd_unit_price ddup where ddup.CONTRACT_UKID in (select CONTRACT_UKID from
                       xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s')'''
                       % (contract_type, participant_ukid),
                    '''delete from xdw_app.dd_fee_amount ddfa where ddfa.CONTRACT_UKID in (select CONTRACT_UKID from
                      xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s')'''
                       % (contract_type, participant_ukid),
                    '''delete from xdw_app.DD_WAREHOUSE_EXTRA_RESOURCE ddewr where ddewr.CONTRACT_ITEM_UKID in (select
                      CONTRACT_ITEM_UKID from xdw_app.dd_contract_item ddci where ddci.CONTRACT_UKID in (select
                      CONTRACT_UKID from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s'))'''
                       % (contract_type, participant_ukid),
                    '''delete from xdw_app.ru_warehouse_supply_log where CONTRACT_SOURCE_UKID  in (select CONTRACT_UKID
                      from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s')'''
                       % (contract_type, participant_ukid),
                    '''delete from xdw_app.rs_repository where ppt_relation_ukid in ('%s','%s')'''
                       % (participant_ukid, creator_ukid),
                    '''delete from xdw_app.dd_contract_item where CONTRACT_UKID in (select CONTRACT_UKID from
                        xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s')'''
                       % (contract_type, participant_ukid),
                    '''delete from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and SUPPLIER_ID='%s' '''
                       % (contract_type, participant_ukid)]

        if contract_ascription == 'DEMAND':
            sql2 = ['''delete from xdw_app.dd_unit_price ddup where ddup.CONTRACT_UKID in (select CONTRACT_UKID from
                       xdw_app.dd_contract where CONTRACT_TYPE = '%s' and DEMANDER_ID='%s')'''
                    % (contract_type, participant_ukid),
                    '''delete from xdw_app.dd_fee_amount ddfa where ddfa.CONTRACT_UKID in (select CONTRACT_UKID from
                      xdw_app.dd_contract where CONTRACT_TYPE = '%s' and DEMANDER_ID='%s')'''
                    % (contract_type, participant_ukid),
                    '''delete from xdw_app.DD_WAREHOUSE_EXTRA_RESOURCE ddewr where ddewr.CONTRACT_ITEM_UKID in (select
                      CONTRACT_ITEM_UKID from xdw_app.dd_contract_item ddci where ddci.CONTRACT_UKID in (select
                      CONTRACT_UKID from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and DEMANDER_ID='%s'))'''
                    % (contract_type, participant_ukid),
                    '''delete from xdw_app.ru_warehouse_demand_log where CONTRACT_SOURCE_UKID in (select CONTRACT_UKID
                      from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and DEMANDER_ID='%s')'''
                    % (contract_type, participant_ukid),
                    '''delete from xdw_app.rs_repository where ppt_relation_ukid in ('%s','%s')'''
                    % (participant_ukid, creator_ukid),
                    '''delete from xdw_app.dd_contract_item where CONTRACT_UKID in (select CONTRACT_UKID from
                        xdw_app.dd_contract where CONTRACT_TYPE = '%s' and DEMANDER_ID='%s')'''
                    % (contract_type, participant_ukid),
                    '''delete from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and DEMANDER_ID='%s' '''
                    % (contract_type, participant_ukid)]

        for sql in sql2:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原仓储契约成功')
    except Exception as e:
        print('还原仓储契约失败')
        print(e)
        close_oracle(con, curs)


# 获取仓储契约ukid
def get_warehouse_contract_ukid(contract_type='RE', participant_ukid=199145, contract_ascription='SUPPLY'):
    con, curs = basic_sit()
    try:
        sql = ''
        if contract_ascription == 'SUPPLY':
            sql = '''select CONTRACT_UKID from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and
                     SUPPLIER_ID='%s' and contract_status = 20 order by create_time desc ''' \
                  % (contract_type, participant_ukid)
        if contract_ascription == 'DEMAND':
            sql = '''select CONTRACT_UKID from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and
                     DEMANDER_ID='%s' and contract_status = 20 order by create_time desc '''\
                  % (contract_type, participant_ukid)
        curs.execute(sql)
        result = curs.fetchall()
        if len(result) >= 1:
            contract_ukid = result[0][0]
            return contract_ukid
        else:
            return False

    except Exception as e:
        print('获取仓储契约ukid失败')
        print(e)
        close_oracle(con, curs)


# 获取仓储契约信息:状态、数量、发布人名称、开始时间、结束时间
def get_warehouse_contract_info(supply_user_id=199145, contract_ukid=88888002, contract_ascription='SUPPLY'):
    con, curs = basic_sit()
    try:
        creator_ukid = get_creator_ukid(supply_user_id)
        sql = ''
        if contract_ascription == 'SUPPLY':
            sql = '''select ddc.contract_status,ddci.qty,ppt_name,breach_discount,ddci.start_time,ddci.end_time
                 from xdw_app.CM_PARTICIPANT cmp,xdw_app.dd_contract ddc,xdw_app.dd_contract_item ddci,
                 xdw_app.DD_WAREHOUSE_EXTRA_RESOURCE ddwer,xdw_app.dd_breach_define ddbd where cmp.participant_ukid
                 = '%s' and ddbd.breach_item_code=to_char(ddwer.star_level) and ddwer.contract_item_ukid in
                 (select CONTRACT_ITEM_UKID from xdw_app.dd_contract_item where CONTRACT_UKID ='%s') and
                 ddc.contract_ukid = '%s' and ddci.contract_ukid =ddc.contract_ukid''' \
                 % (creator_ukid, contract_ukid, contract_ukid)
        if contract_ascription == 'DEMAND':
            sql = '''select ddc.contract_status,ddci.qty,ppt_name,breach_discount,ddci.start_time,ddci.end_time
                from xdw_app.CM_PARTICIPANT cmp,xdw_app.dd_contract ddc,xdw_app.dd_contract_item ddci,
                xdw_app.DD_WAREHOUSE_EXTRA_RESOURCE ddwer,xdw_app.dd_breach_define ddbd where cmp.participant_ukid =
                '%s' and ddbd.breach_item_code=to_char(ddwer.MARKET_PRICING) and ddwer.contract_item_ukid in
                (select CONTRACT_ITEM_UKID from xdw_app.dd_contract_item where CONTRACT_UKID ='%s') and
                ddc.contract_ukid = '%s' and ddci.contract_ukid =ddc.contract_ukid'''\
                % (creator_ukid, contract_ukid, contract_ukid)
        curs.execute(sql)
        result = curs.fetchall()
        if len(result) > 0:
            dic = {'status': result[0][0], 'qty': result[0][1], 'ppt_name': result[0][2], 'overdue_clause': result[0][3],
                   'start_time': result[0][4], 'end_time': result[0][5]}
            return dic
        else:
            print('查询无结果')
            assert False
    except Exception as e:
        print('获取仓储契约信息失败')
        print(e)
        close_oracle(con, curs)


# 签订契约后，查看新生成的契约，记录，资源信息，通过数量来判断,获取当前契约的状态和剩余数量
def get_warehouse_sign_result(contract_ukid, user_id=10001394, contract_ascription='SUPPLY', type='RE'):
    con, curs = basic_sit()
    try:
        dic = {}
        creator_ukid = get_creator_ukid(user_id)
        if contract_ascription == 'SUPPLY':
            sql = '''select supplier_id from xdw_app.dd_contract where CONTRACT_UKID = '%s'  ''' % contract_ukid
            curs.execute(sql)
            result = curs.fetchall()
            supplier_id = result[0][0]
            sql2 = '''select count(*) from xdw_app.dd_contract_item d where contract_ukid in (select contract_ukid from
                      xdw_app.dd_contract  where  supplier_id ='%s' and demander_id ='%s' and contract_type='WA') and
                     d.rs_type='%s' ''' % (supplier_id, creator_ukid, type)
            curs.execute(sql2)
            result2 = curs.fetchall()
            dic['get_new_contract_no'] = result2[0][0]

            sql3 = '''select count(*) from xdw_app.rs_repository  where owner_id in ('%s','%s') and rs_type='%s' ''' \
                   % (creator_ukid, supplier_id, type)
            curs.execute(sql3)
            result3 = curs.fetchall()
            dic['rs_repository_no'] = result3[0][0]

            sql4 = '''select count(*) from xdw_app.ru_warehouse_supply_log where CONTRACT_SOURCE_UKID = '%s'  ''' \
                      % contract_ukid
            curs.execute(sql4)
            result4 = curs.fetchall()
            dic['log_no'] = result4[0][0]

            sql5 = '''select contract_status from xdw_app.dd_contract where CONTRACT_UKID = '%s' ''' % contract_ukid
            curs.execute(sql5)
            result5 = curs.fetchall()
            dic['contract_status'] = result5[0][0]

            sql6 = '''select qty from xdw_app.dd_contract_item where CONTRACT_UKID = '%s'  and rs_type='%s'  ''' \
                     % (contract_ukid, type)
            curs.execute(sql6)
            result6 = curs.fetchall()
            dic['contract_no'] = result6[0][0]
            return dic
        if contract_ascription == 'DEMAND':
            sql = '''select demander_id from xdw_app.dd_contract where CONTRACT_UKID =  '%s' ''' % contract_ukid
            curs.execute(sql)
            result = curs.fetchall()
            demander_id = result[0][0]

            sql2 = '''select count(*) from xdw_app.dd_contract_item d where contract_ukid in (select contract_ukid from
                      xdw_app.dd_contract  where  supplier_id ='%s' and demander_id ='%s' and contract_type='WA') and
                     d.rs_type='%s' ''' % (creator_ukid, demander_id, type)
            curs.execute(sql2)
            result2 = curs.fetchall()
            dic['get_new_contract_no'] = result2[0][0]

            sql3 = '''select count(*) from xdw_app.rs_repository  where owner_id in ('%s','%s') and
                    rs_type='%s' ''' % (creator_ukid, demander_id, type)
            curs.execute(sql3)
            result3 = curs.fetchall()
            dic['rs_repository_no'] = result3[0][0]

            sql4 = '''select count(*) from xdw_app.ru_warehouse_demand_log where CONTRACT_SOURCE_UKID = '%s' ''' \
                   % contract_ukid
            curs.execute(sql4)
            result4 = curs.fetchall()
            dic['log_no'] = result4[0][0]

            sql5 = '''select contract_status from xdw_app.dd_contract where CONTRACT_UKID = '%s'  ''' % contract_ukid
            curs.execute(sql5)
            result5 = curs.fetchall()
            dic['contract_status'] = result5[0][0]

            sql6 = '''select qty from xdw_app.dd_contract_item where CONTRACT_UKID = '%s'  and rs_type='%s'  '''\
                       % (contract_ukid, type)
            curs.execute(sql6)
            result6 = curs.fetchall()
            dic['contract_no'] = result6[0][0]
            return dic
    except Exception as e:
        print('获取仓储契约信息失败')
        print(e)
        close_oracle(con, curs)


# 获取创造者id
def get_creator_ukid(user_id):
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
        print('获取仓储契约信息失败')
        print(e)
        close_oracle(con, curs)


def reduction_warehouse_supply_contract():
    """
    还原仓储供应契约
    """
    con, curs = basic_sit()
    try:
        sql_list = ['''update xdw_app.dd_contract set contract_status=20 where contract_ukid in (51817100000010009)''',
                    '''update xdw_app.dd_contract_item set qty = 500 where contract_ukid in (51817100000010009)
                       and rs_type = 'WA' ''',
                    '''update xdw_app.dd_contract_item set qty = 1000 where contract_ukid in (51817100000010009)
                        and rs_type = 'RE' ''',
                    '''delete from xdw_app.ru_warehouse_supply_log where CONTRACT_SOURCE_UKID in (51817100000010009)''',
                    '''delete from xdw_app.rs_repository where owner_id in (10001437,10001392)''',
                    '''delete from xdw_app.dd_contract where  SUPPLIER_ID=10001437 and demander_id = 10001392 '''
                    ]
        for sql in sql_list:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原仓储供应契约成功')
    except Exception as e:
        print('还原仓储供应契约失败')
        print(e)
        close_oracle(con, curs)


def reduction_warehouse_demand_contract():
    """
    还原仓储需求契约
    """
    con, curs = basic_sit()
    try:
        sql_list = ['''update xdw_app.dd_contract set contract_status = 20 where contract_ukid = 51817200000010012''',
                    '''update xdw_app.dd_contract_item set qty = 500 where contract_ukid in (51817200000010012)
                       and rs_type = 'WA' ''',
                    '''update xdw_app.dd_contract_item set qty = 1000 where contract_ukid in (51817200000010012)
                       and rs_type = 'RE' ''',
                    '''delete from xdw_app.ru_warehouse_demand_log where CONTRACT_SOURCE_UKID in (51817200000010012)''',
                    '''delete from xdw_app.rs_repository where owner_id in (10001392,10001437)''',
                    '''delete from xdw_app.dd_contract where SUPPLIER_ID=10001392 and demander_id =10001437 ''']
        for sql in sql_list:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原仓储需求契约成功')
    except Exception as e:
        print('还原仓储需求契约失败')
        print(e)
        close_oracle(con, curs)
