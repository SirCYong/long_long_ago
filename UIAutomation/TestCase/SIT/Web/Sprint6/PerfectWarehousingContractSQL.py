from UIAutomation.Utils import close_oracle, basic_cit

__author__ = "zcw"


def resume_perfect_warehousing_contract():
    """
    还原完善仓储契约数据
    """
    con, curs = basic_cit()
    try:
        sql_list = ['''delete from xdw_app.dd_charging_breach_detail dcbd where dcbd.delivery_requirements_ukid in
                      (select dbr.delivery_requirements_ukid from xdw_app.dd_delivery_requirements dbr where
                       dbr.charging_breach_item_ukid in (select dcbi.charging_breach_item_ukid from
                       xdw_app.dd_charging_breach_item dcbi where dcbi.contract_ukid in
                       (51784800000039000,51784000000033000,51788500000010000)))''',
                    '''delete from xdw_app.dd_delivery_requirements dbr where dbr.charging_breach_item_ukid in
                        (select dcbi.charging_breach_item_ukid from xdw_app.dd_charging_breach_item dcbi where
                        dcbi.contract_ukid in (51784800000039000,51784000000033000,51788500000010000))''',
                    '''delete from xdw_app.dd_charging_breach_item dcbi where
                        dcbi.contract_ukid in (51784800000039000,51784000000033000,51788500000010000)''',
                    '''update xdw_app.dd_contract dc set dc.contract_status = 20 where dc.contract_ukid in
                       (51784800000039000,51784000000033000,51788500000010000)'''
                    ]
        for sql in sql_list:
            curs.execute(sql)
            con.commit()
        close_oracle(con, curs)
        print('删除数据成功')
    except Exception as e:
        print('删除数据失败')
        print(e)
        close_oracle(con, curs)


def get_perfect_warehousing_contract_result():
    """
    上传excel后，获取上传的数量
    """
    con, curs = basic_cit()
    try:
        sql = '''select count(*) from xdw_app.dd_charging_breach_item dbi
                 inner join xdw_app.dd_delivery_requirements ddr on dbi.charging_breach_item_ukid = ddr.charging_breach_item_ukid
                 inner join xdw_app.dd_charging_breach_detail dbd on ddr.delivery_requirements_ukid = dbd.delivery_requirements_ukid
                 inner join xdw_app.rs_service_publish rsp on rsp.resource_ukid = (select dci.repository_ukid from
                 xdw_app.dd_contract_item dci where dci.contract_item_ukid= dbi.contract_item_ukid)
                 where dbi.contract_ukid in (51784800000039000,51784000000033000,51788500000010000) '''
        curs.execute(sql)
        result = curs.fetchall()
        close_oracle(con, curs)
        return result[0][0]
    except Exception as e:
        print('获取数据失败')
        print(e)
        close_oracle(con, curs)

