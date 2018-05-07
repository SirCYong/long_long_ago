# coding=utf-8
from UIAutomation.Utils import close_oracle, basic_cit

__author__ = "xuwangchao"

def get_bill_info(user_id = 199885):
    """
    获得钱仓页面的信息
    :param user_id:
    :return:
    """
    get_info = {}
    con, curs = basic_cit()
    try:
        sql0 = '''select count(*) from xdw_app.TS_PAYMENT_BILL tpb where (tpb.participant_ukid = '%s' or
                  tpb.receive_unit = '%s') and tpb.bill_ukid in (select bill_ukid from
                  xdw_app.em_promotion_service_fee e) and tpb.bill_status = 0
                  and tpb.payment_title = '结算账单支付信息' ''' % (user_id, user_id)
        curs.execute(sql0)
        result = curs.fetchall()
        get_info['unliquidated_counts'] = str(result[0][0])

        sql1='''select money_type,sum(money) from xdw_app.EM_PARTICIPANT_MONEY_RECORD e
                where e.money_type in ( '契约预付款','保证金') and e.status=2
                and e.participant_ukid='%s' group by money_type''' % user_id
        curs.execute(sql1)
        result = curs.fetchall()
        print('---------------------sql1------------------------------')
        print('---------------------sql1------------------------------')
        print('---------------------sql1------------------------------')
        print('---------------------sql1------------------------------')
        print('---------------------sql1------------------------------')
        print('---------------------sql1------------------------------')
        print('---------------------sql1------------------------------')
        print(result)
        print(result)
        print(result)
        print(result)
        print(result)
        print(result)
        for r in result:
            if r[0] == '契约预付款':
                get_info['wallet_left_advance'] = str(r[1])
            if r[0] == '保证金':
                get_info['wallet_left_deposit'] = str(r[1])

        sql2='''select count(*) from xdw_app.TS_PAYMENT_BILL tpb where
                (tpb.participant_ukid ='%s' or tpb.receive_unit ='%s')
                and tpb.bill_ukid in (select bill_ukid from xdw_app.em_promotion_service_fee e)
                and tpb.payment_title = u'结算账单支付信息' ''' % (user_id, user_id)
        curs.execute(sql2)
        result = curs.fetchall()
        get_info['all_counts'] = str(result[0][0])
        print(get_info)
        close_oracle(con, curs)
        return get_info
    except Exception as e:
        print('获取账单信息失败')
        print(e)
        close_oracle(con, curs)


def get_bill_list_detail_info(user_id = 199885):
    """
    获得全部账单页面的详细信息
    :param user_id:
    :return:
    """
    con, curs = basic_cit()
    all_count_list = []
    try:
        sql0 = '''select tpb.bill_money,tpb.create_time,bill_status,b.user_name
        from xdw_app.TS_PAYMENT_BILL tpb inner join xdw_app.ba_user b on b.user_id = tpb.participant_ukid
        where  tpb.receive_unit = '%s' and tpb.bill_ukid in (select bill_ukid from
        xdw_app.em_promotion_service_fee e)union all select  -tpb.bill_money,tpb.create_time,bill_status,b.user_name
        from xdw_app.TS_PAYMENT_BILL tpb inner join xdw_app.ba_user b on b.user_id = tpb.receive_unit
         where tpb.participant_ukid = '%s' and tpb.bill_ukid in (select bill_ukid from xdw_app.em_promotion_service_fee
         e)order by create_time desc''' % (user_id, user_id)
        curs.execute(sql0)
        result = curs.fetchall()
        print('get_bill_list_detail_info')
        print('get_bill_list_detail_info')
        print('get_bill_list_detail_info')
        print('get_bill_list_detail_info')
        print('get_bill_list_detail_info')
        print(result)
        print(result)
        print(result)
        print(result)
        print(result)
        for all_count in result:
            get_info = {}
            get_info['bill_money'] = '%.2f' % all_count[0]
            get_info['create_time'] = all_count[1]
            get_info['bill_status'] = all_count[2]
            get_info['user_name'] = all_count[3]
            all_count_list.append(get_info)
        print(all_count_list)
        close_oracle(con, curs)
        return all_count_list
    except Exception as e:
        print('获取账单信息失败')
        print(e)
        close_oracle(con, curs)
    pass

if __name__ == '__main__':
    # get_bill_list_detail_info()
    get_bill_info()






# def get_bill_list_info(user_id=199885):
#     """
#     得到
#     """
#     get_info = {}
#     con, curs = basic_cit()
#     try:
#         sql0 = '''select count(*) from xdw_app.TS_PAYMENT_BILL tpb where (tpb.participant_ukid ='%s' or tpb.receive_unit ='%s') and tpb.bill_ukid
# in (select bill_ukid from xdw_app.em_promotion_service_fee e) and tpb.bill_status = 0 and tpb.payment_title = u'结算账单支付信息' ''' & (user_id)
#         curs.execute(sql0)
#         result = curs.fetchall()
#         print result
#         print type(result)
#         # get_info['unliquidated_number'] = result[0][0]
#
#         sql2 = '''select trunc(min(create_time)),trunc(max(create_time)) from xdw_app.em_promotion_service_fee e
#                   where e.supplier_id='%s'and e.demander_id='%s' and e.contract_type in ('WA','TR')
#                   and e.bill_ukid is  null ''' % (supplier_id, demander_id)
#         curs.execute(sql2)
#         result = curs.fetchall()
#         start_time = str(result[0][0])
#         end_time = str(result[0][1])
#         get_info['start_time'] = start_time[:start_time.find(' ')]
#         get_info['end_time'] = end_time[:end_time.find(' ')]
#
#         sql3 = '''select contract_type,sum(e.settlement_fee)  from xdw_app.em_promotion_service_fee e where
#                   e.supplier_id='%s' and e.demander_id='%s' and e.contract_type in ('WA','TR') and
#                   e.bill_ukid is null group by e.demander_id,e.contract_type''' % (supplier_id, demander_id)
#         curs.execute(sql3)
#         result = curs.fetchall()
#         total = 0.0
#         for re in result:
#             get_info[re[0]] = re[1]
#             total += re[1]
#         get_info['total'] = '%.2f' % total
#         print('获取生成账单信息成功')
#         close_oracle(con, curs)
#         return get_info
#
#     except Exception as e:
#         print('获取生成账单信息失败')
#         print(e)
#         close_oracle(con, curs)


# def resume_generate_bill(demander_id=199983, supplier_id=199833):
#     """
#     还原账单列表数据
#     """
#     con, curs = basic_cit()
#     try:
#         sql_list = ['''update xdw_app.em_promotion_service_fee e set e.bill_ukid = '' where e.supplier_id='%s'
#                        and e.demander_id='%s' and e.contract_type in ('WA','TR')''' % (supplier_id, demander_id),
#                     '''delete from xdw_app.ms_card m where m.card_name in('支付','生成账单') and m.create_user_id
#                        = '%s' ''' % demander_id,
#                     '''delete from xdw_app.ts_operation m where m.operation_name in( '支付','生成账单') and
#                         m.create_user_id = '%s' ''' % demander_id,
#                     '''delete from xdw_app.ts_payment_bill tpb where tpb.participant_ukid='%s' and
#                       tpb.receive_unit = '%s' ''' % (demander_id, supplier_id),
#                     '''delete from  xdw_app.em_participant_money_record epmr where (epmr.participant_ukid =
#                        '%s' and epmr.other_ppt_ukid = '%s') or (epmr.participant_ukid ='%s' and epmr.other_ppt_ukid =
#                        '%s') ''' % (supplier_id, demander_id, demander_id, supplier_id)
#                     ]
#         for sql in sql_list:
#             curs.execute(sql)
#             con.commit()
#         close_oracle(con, curs)
#         print('还原账单列表成功')
#     except Exception as e:
#         print('还原账单列表失败')
#         print(e)
#         close_oracle(con, curs)



# def get_generate_bill_result(demander_id=199983, supplier_id=199833):
#     """
#     生成账单后，查看计费表、支付表、流水表、任务表、卡片表符合结果的条数
#     :param demander_id:需方id
#     :param supplier_id:供方id
#     """
#     con, curs = basic_cit()
#     get_result = {}
#     try:
#         sql1 = '''select count(*) from xdw_app.em_promotion_service_fee e where e.supplier_id='%s'and
#                        e.demander_id='%s' and e.contract_type in ('WA','TR') and e.bill_ukid is null ''' \
#                       % (supplier_id, demander_id)
#         curs.execute(sql1)
#         result = curs.fetchall()
#         get_result['fee_no'] = result[0][0]
#
#         sql2 = '''select count(*) from xdw_app.ts_payment_bill tpb where tpb.participant_ukid='%s' and
#                       tpb.receive_unit = '%s' ''' % (demander_id, supplier_id)
#         curs.execute(sql2)
#         result = curs.fetchall()
#         get_result['bill_no'] = result[0][0]
#
#         sql3 = '''select count(*) from  xdw_app.em_participant_money_record epmr where (epmr.participant_ukid =
#                        '%s' and epmr.other_ppt_ukid = '%s') or (epmr.participant_ukid ='%s' and epmr.other_ppt_ukid =
#                        '%s') ''' % (supplier_id, demander_id, demander_id, supplier_id)
#         curs.execute(sql3)
#         result = curs.fetchall()
#         get_result['record_no'] = result[0][0]
#
#         sql4 = '''select count(*) from xdw_app.ts_operation t where  t.create_user_id = '%s' and ((t.operation_name
#                   in('支付') and t.status = 0) or (t.operation_name in('生成账单')and t.status = 10))''' % demander_id
#         curs.execute(sql4)
#         result = curs.fetchall()
#         get_result['operation_no'] = result[0][0]
#
#         sql5 = '''select count(*) from xdw_app.ms_card m where  m.create_user_id = '%s' and ((m.card_name in('支付')
#                   and m.status = 0) or (m.card_name in('生成账单')and m.status = 10))''' % demander_id
#         curs.execute(sql5)
#         result = curs.fetchall()
#         get_result['card_no'] = result[0][0]
#         print('获取生成账单结果成功')
#         close_oracle(con, curs)
#         return get_result
#     except Exception as e:
#         print('获取生成账单结果失败')
#         print(e)
#         close_oracle(con, curs)
