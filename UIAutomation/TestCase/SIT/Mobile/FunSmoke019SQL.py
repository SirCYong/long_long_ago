from UIAutomation.Utils import cit, close_oracle


def delete_address(user_id=None):
    try:
        con, curs = cit()
        sql = [  # 恢复激活实体店的输入项
            '''delete from xdw_app.TM_DELIVERY_ADDRESS t
where t.address_owner_ukid='%s' and t.address_nick_name='pd' ''' % user_id]
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        close_oracle(con, curs)
        print('恢复管理收货地址原始状态成功，不含杂质\n')
    except Exception as e:
        print(e)