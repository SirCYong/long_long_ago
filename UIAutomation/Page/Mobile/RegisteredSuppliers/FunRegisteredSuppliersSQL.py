from UIAutomation.Utils import close_oracle, sit


def register_suppliers_sql(user_id):
    try:
        con, curs = sit()
        sql = ['''delete from  XDW_APP.ts_registered_supplier t
where t.create_user_id='%s'  ''' % user_id]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print('数据删除成功')
    except Exception as e:
        print(e)


