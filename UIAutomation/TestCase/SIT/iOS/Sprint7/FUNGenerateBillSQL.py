# -*- coding: utf-8 -*-
from UIAutomation.Utils import basic_cit, close_oracle
__author__ = "zcw"


def resume_generate_bill(demander_id=199983, supplier_id=199833):
    """
    还原生成账单数据
    :param demander_id:需方id
    :param supplier_id:供方id
    """
    con, curs = basic_cit()
    try:
        sql_list = ['''update xdw_app.em_promotion_service_fee e set e.bill_ukid = '' where e.supplier_id='%s'
                       and e.demander_id='%s' and e.contract_type in ('WA','TR')''' % (supplier_id, demander_id),
                    '''delete from xdw_app.ms_card m where m.card_name in('支付','生成账单') and m.create_user_id
                       = '%s' ''' % demander_id,
                    '''delete from xdw_app.ts_operation m where m.operation_name in( '支付','生成账单') and
                        m.create_user_id = '%s' ''' % demander_id,
                    '''delete from xdw_app.ts_payment_bill tpb where tpb.participant_ukid='%s' and
                      tpb.receive_unit = '%s' ''' % (demander_id, supplier_id),
                    '''delete from  xdw_app.em_participant_money_record epmr where (epmr.participant_ukid =
                       '%s' and epmr.other_ppt_ukid = '%s') or (epmr.participant_ukid ='%s' and epmr.other_ppt_ukid =
                       '%s') ''' % (supplier_id, demander_id, demander_id, supplier_id)
                    ]
        for sql in sql_list:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('还原生成账单成功')
    except Exception as e:
        print('还原生成账单失败')
        print(e)
        close_oracle(con, curs)


def get_bill_info(demander_id=199983, supplier_id=199833):
    """
    获取上传账单的详细信息： 对方的名字，开始时间，结束时间，契约类型的金额，总额
    :param demander_id:需方id
    :param supplier_id:供方id
    """
    get_info = {}
    con, curs = basic_cit()
    try:
        sql1 = '''select user_name from xdw_app.ba_user where user_id = '%s' ''' % supplier_id
        curs.execute(sql1)
        result = curs.fetchall()
        get_info['name'] = result[0][0]

        sql2 = '''select trunc(min(create_time)),trunc(max(create_time)) from xdw_app.em_promotion_service_fee e
                  where e.supplier_id='%s'and e.demander_id='%s' and e.contract_type in ('WA','TR')
                  and e.bill_ukid is  null ''' % (supplier_id, demander_id)
        curs.execute(sql2)
        result = curs.fetchall()
        start_time = str(result[0][0])
        end_time = str(result[0][1])
        get_info['start_time'] = start_time[:start_time.find(' ')]
        get_info['end_time'] = end_time[:end_time.find(' ')]

        sql3 = '''select contract_type,sum(e.settlement_fee)  from xdw_app.em_promotion_service_fee e where
                  e.supplier_id='%s' and e.demander_id='%s' and e.contract_type in ('WA','TR') and
                  e.bill_ukid is null group by e.demander_id,e.contract_type''' % (supplier_id, demander_id)
        curs.execute(sql3)
        result = curs.fetchall()
        total = 0.0
        for re in result:
            get_info[re[0]] = re[1]
            total += re[1]
        get_info['total'] = '%.2f' % total
        print('获取生成账单信息成功')
        close_oracle(con, curs)
        return get_info

    except Exception as e:
        print('获取生成账单信息失败')
        print(e)
        close_oracle(con, curs)


def get_generate_bill_result(demander_id=199983, supplier_id=199833):
    """
    生成账单后，查看计费表、支付表、流水表、任务表、卡片表符合结果的条数
    :param demander_id:需方id
    :param supplier_id:供方id
    """
    con, curs = basic_cit()
    get_result = {}
    try:
        sql1 = '''select count(*) from xdw_app.em_promotion_service_fee e where e.supplier_id='%s'and
                       e.demander_id='%s' and e.contract_type in ('WA','TR') and e.bill_ukid is null ''' \
                      % (supplier_id, demander_id)
        curs.execute(sql1)
        result = curs.fetchall()
        get_result['fee_no'] = result[0][0]

        sql2 = '''select count(*) from xdw_app.ts_payment_bill tpb where tpb.participant_ukid='%s' and
                      tpb.receive_unit = '%s' ''' % (demander_id, supplier_id)
        curs.execute(sql2)
        result = curs.fetchall()
        get_result['bill_no'] = result[0][0]

        sql3 = '''select count(*) from  xdw_app.em_participant_money_record epmr where (epmr.participant_ukid =
                       '%s' and epmr.other_ppt_ukid = '%s') or (epmr.participant_ukid ='%s' and epmr.other_ppt_ukid =
                       '%s') ''' % (supplier_id, demander_id, demander_id, supplier_id)
        curs.execute(sql3)
        result = curs.fetchall()
        get_result['record_no'] = result[0][0]

        sql4 = '''select count(*) from xdw_app.ts_operation t where  t.create_user_id = '%s' and ((t.operation_name
                  in('支付') and t.status = 0) or (t.operation_name in('生成账单')and t.status = 10))''' % demander_id
        curs.execute(sql4)
        result = curs.fetchall()
        get_result['operation_no'] = result[0][0]

        sql5 = '''select count(*) from xdw_app.ms_card m where  m.create_user_id = '%s' and ((m.card_name in('支付')
                  and m.status = 0) or (m.card_name in('生成账单')and m.status = 10))''' % demander_id
        curs.execute(sql5)
        result = curs.fetchall()
        get_result['card_no'] = result[0][0]
        print('获取生成账单结果成功')
        close_oracle(con, curs)
        return get_result
    except Exception as e:
        print('获取生成账单结果失败')
        print(e)
        close_oracle(con, curs)
