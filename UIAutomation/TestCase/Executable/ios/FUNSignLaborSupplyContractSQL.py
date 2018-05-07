from UIAutomation.Utils import basic_sit, close_oracle

__author__ = 'chenyanxiu'


def reduction_labor_contract(contract_ukid=51817000000010130):
    """
    还原劳务需求契约
    """
    con, curs = basic_sit()
    try:
        sql_list = ['''update xdw_app.dd_contract set contract_status=20 where contract_ukid = '%s' ''' % contract_ukid,
                    '''update xdw_app.dd_contract_item set qty = 2 where contract_ukid = '%s' ''' % contract_ukid]
        for sql in sql_list:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原劳务需求契约成功')
    except Exception as e:
        print('还原劳务需求契约失败')
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
        print('获取创造者信息失败')
        print(e)
        close_oracle(con, curs)


# 删除劳务契约
def delete_labor_contract(user_id, participant_ukid, contract_type='LA'):
    con, curs = basic_sit()
    try:
        creator_ukid = get_creator_ukid(user_id)
        sql2 = ['''delete from xdw_app.ru_labour_log where CONTRACT_SOURCE_UKID  in (select CONTRACT_UKID
                  from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and DEMANDER_ID='%s')'''
                % (contract_type, participant_ukid),
                '''delete from xdw_app.rs_repository where owner_id in ('%s','%s')'''
                % (participant_ukid, creator_ukid),
                '''delete from xdw_app.dd_contract where CONTRACT_UKID in (select CONTRACT_UKID from
                    xdw_app.dd_contract where CONTRACT_TYPE = '%s' and DEMANDER_ID='%s'and supplier_id ='%s')'''
                % (contract_type, participant_ukid, user_id),
                '''delete from xdw_app.dd_contract_item where CONTRACT_UKID in (select CONTRACT_UKID from
                    xdw_app.dd_contract where CONTRACT_TYPE = '%s' and supplier_id ='%s' and DEMANDER_ID='%s'
                    and contract_ascription ='CONTRACT') '''% (contract_type, user_id, participant_ukid)]
        for sql in sql2:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('删除劳务契约日志成功')
    except Exception as e:
        print('删除劳务契约日志失败')
        print(e)
        close_oracle(con, curs)


# 获取劳务契约ukid
def get_labor_contract_ukid(user_id, participant_ukid, contract_type='LA'):
    con, curs = basic_sit()
    try:
        sql = '''select CONTRACT_UKID from xdw_app.dd_contract where CONTRACT_TYPE = '%s' and
                 DEMANDER_ID='%s' and supplier_id='%s' order by create_time desc ''' % (contract_type, participant_ukid,
                                                                                        user_id)
        curs.execute(sql)
        result = curs.fetchall()
        print(result)
        if len(result) >= 1:
            print(len(result))
            print('获取劳务契约ukid成功')
            contract_ukid = result[0][0]
            return contract_ukid
        else:
            return False
    except Exception as e:
        print('获取劳务契约ukid失败')
        print(e)
        close_oracle(con, curs)


# 获取劳务契约信息:状态、数量、发布人名称、开始时间、结束时间
def get_labor_contract_info(user_id, contract_ukid=51817000000010130):
    con, curs = basic_sit()
    try:
        creator_ukid = get_creator_ukid(user_id)
        print(creator_ukid)
        sql = '''select DISTINCT ddc.CONTRACT_UKID, (select SALE_PRICE from XDW_APP.dd_unit_price ddup,
    XDW_APP.dd_contract_item ddci where ddup.PRICE_UNIT='YUAN_PER_HOUR'and ddci.CONTRACT_UKID='%s'and ddup.CONTRACT_ITEM_UKID=
    (select  CONTRACT_ITEM_UKID from  XDW_APP.dd_contract_item where CONTRACT_UKID='%s'))as hour,
    (select SALE_PRICE from XDW_APP.dd_unit_price ddup,XDW_APP.dd_contract_item ddci where ddup.PRICE_UNIT='YUAN_PER_PIECE'
    and ddci.CONTRACT_UKID='%s'and ddup.CONTRACT_ITEM_UKID=(select  CONTRACT_ITEM_UKID from  XDW_APP.dd_contract_item where
    CONTRACT_UKID='%s'))as PIECE, ddc.contract_status,ddci.start_time,ddci.end_time,ddci.QTY,cma.country,cma.city,
    cma.county,cma.street,cma.address,rslp.work_type,rslp.work_shift_type from XDW_APP.dd_contract ddc,
    XDW_APP.dd_contract_item ddci,XDW_APP.cm_address cma,XDW_APP.dd_unit_price ddup,XDW_APP.dd_fee_amount ddfa,
    XDW_APP.rs_labour_publish rslp where ddc.CONTRACT_TYPE = 'LA' and ddc.CONTRACT_ASCRIPTION in('DEMAND') and
    ddci.CONTRACT_UKID =ddc.CONTRACT_UKID and ddc.CONTRACT_UKID in('%s')and ddc.demander_id='%s'and
    ddci.resource_address = cma.address_ukid and ddup.contract_item_ukid = ddci.CONTRACT_ITEM_UKID and
    rslp.labour_publish_ukid = ddci.REPOSITORY_UKID''' \
              % (contract_ukid, contract_ukid, contract_ukid, contract_ukid, contract_ukid, creator_ukid)
        curs.execute(sql)
        result = curs.fetchall()
        print(result)
        dic = {'hour': result[0][1], 'piece': result[0][2], 'status': result[0][3], 'start_time': result[0][4],
               'end_time': result[0][5], 'qty': result[0][6], 'country': result[0][7], 'street': result[0][8],
               'address': result[0][9], 'work_type': result[0][10], 'work_shift_type': result[0][11]}
        print(dic)
        return dic
    except Exception as e:
        print('获取劳务契约信息失败')
        print(e)
        close_oracle(con, curs)


# 签订劳务契约后，查看新生成的契约，记录，资源信息，通过数量来判断
def get_new_labor_contract(user_id, contract_ukid=51817000000010130):
    con, curs = basic_sit()
    try:
        dic = {}
        creator_ukid = get_creator_ukid(user_id)
        sql = '''select demander_id from xdw_app.dd_contract where CONTRACT_UKID ='%s' ''' % contract_ukid
        curs.execute(sql)
        result = curs.fetchall()
        demander_id = result[0][0]
        sql2 = '''select count(*) from xdw_app.dd_contract where  demander_id in (select demander_id from
                     xdw_app.dd_contract where CONTRACT_UKID ='%s') and supplier_id ='%s' order by
                     create_time desc''' % (contract_ukid, creator_ukid)
        curs.execute(sql2)
        result2 = curs.fetchall()
        dic['new_labor_contract_no'] = result2[0][0]

        sql3 = '''select count(*) from xdw_app.rs_repository  where owner_id in ('%s','%s')''' \
               % (demander_id, creator_ukid)
        curs.execute(sql3)
        result3 = curs.fetchall()
        dic['rs_repository_no'] = result3[0][0]

        sql4 = '''select count(*) from xdw_app.ru_labour_log where CONTRACT_SOURCE_UKID = '%s' ''' \
               % contract_ukid
        curs.execute(sql4)
        result4 = curs.fetchall()
        dic['operation_record_no'] = result4[0][0]
        print('获取劳务契约信息成功')
        return dic
    except Exception as e:
        print('获取劳务契约信息失败')
        print(e)
        close_oracle(con, curs)
# print(reduction_labor_contract())
# print(delete_labor_contract(10001465,10001465))
# print(get_new_labor_contract())
# print(get_labor_contract_info(10001465))
# print(get_new_labor_contract(10001465))
# print(2==2==2)
#
# print(get_labor_contract_ukid(10001465, 10001465))
# print(get_new_labor_contract(10001465, 51817300000012081))