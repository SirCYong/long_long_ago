from UIAutomation.Utils import close_oracle, cit

__author__ = 'zhongchangwei'


# 删除绑定的打印机
def delete_bound_printer(user_id=10001646):
    con, curs = cit()
    try:
        sql = '''delete from xdw_app.Dm_Binding_Device where ppt_ukid = '%s' ''' % user_id
        curs.execute(sql)
        con.commit()

    except Exception as e:
        print('删除绑定的打印机失败')
        print(e)
        close_oracle(con, curs)


# 绑定后，获取绑定的打印机消息
def get_bound_printer_info(user_id=10001646):
    con, curs = cit()
    try:
        sql = '''select identify_code from xdw_app.cm_Identify_Relation c where c.identify_relation_ukid in
                 (select t.active_device_ukid from Dm_Binding_Device t where t.PPT_UKID = '%s')''' % user_id
        curs.execute(sql)
        result = curs.fetchall()
        return result[0][0]
    except Exception as e:
        print('获取绑定的打印机信息失败')
        print(e)
        close_oracle(con, curs)


